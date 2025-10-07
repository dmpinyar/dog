"""
Script Name: apache_push_helper.py

Description:
    Helps push files from a permanent, simple-to-navigate location in the file tree
    to where Apache serves them. Also provides several auxiliary parameters for
    managing the server environment.

    aliased by appu='python3 /home/devin/projects/dog/com/apache_push_helper.py'

Parameters:
    g : Build the Grok server within the same terminal window.
    b : Build the Grok server within a separate screen session.
    c : Attach to the screen session.
    n : Skip pushing files.

Notes:
    - By default the script kills all relevant screens sessions.
    - Parameters b and c do not work well with g.
"""

import subprocess
import sys
import os
import re

# for screen parameters this is the default name for the screen
screen_name = "ngrok"

def needs_dos2unix(path):
    """
    Determine whether a .pl file needs to be converted to Unix line endings.

    Useful for checking if a .pl file needs to be converted to unix formatting 
    so that we can still read # actual error logs in the instance we just 
    automatically convert every file and have to pipe stderr, unfortunately where 
    dos2unix prints conversions, into /dev/null or whatever it is on ubuntu server

    Parameters:
        path (str): The path to the .pl file to check.

    Returns:
        bool: True if the file contains Windows-style line endings and should
        be converted with 'dos2unix'; False otherwise.
    """

    with open(path, "rb") as file:
        shebang = file.readline()
        if b'\r' in shebang:
            return True
    return False

def attempt_screen_close():
    """
    Attempts to close any screens currently running the ngrok server
    """

    result = subprocess.run(['screen', '-ls'], capture_output=True, text=True)

    for line in result.stdout.splitlines():
        match = re.match(rf"\s*(\d+)\.{re.escape(screen_name)}", line)
        if match:
            pid = match.group(1)
            subprocess.run(['screen', '-X', '-S', pid, 'quit'])
            print(f"closing ngrok on screen: {pid}...")
    

def push_changes():
    """
    Turned into a method because the parameters I was passing in started getting really weird

    The primary function of the script
    """

    # generate backups from previous version
    # create backup directories
    subprocess.run(['mkdir', '-p', '/home/devin/projects/dog/prev_ver'])
    subprocess.run(['rm', '-rf', '/home/devin/projects/dog/prev_ver/src'])
    subprocess.run(['rm', '-rf', '/home/devin/projects/dog/prev_ver/cgi-bin'])
    subprocess.run(['mkdir', '/home/devin/projects/dog/prev_ver/src'])
    subprocess.run(['mkdir', '/home/devin/projects/dog/prev_ver/cgi-bin'])
    # copy over the files
    subprocess.run(['cp', '-r', '/var/www/html/.', '/home/devin/projects/dog/prev_ver/src/'])
    subprocess.run(['cp', '-r', '/usr/lib/cgi-bin/.', '/home/devin/projects/dog/prev_ver/cgi-bin'])

    # remove previous version
    subprocess.run(['find', '/var/www/html', '-mindepth', '1', '-delete'])
    subprocess.run(['find', '/usr/lib/cgi-bin', '-mindepth', '1', '-delete'])

    # push current version
    print("compiling typescript files...")
    subprocess.run(['tsc'])
    print("pushing changes from permanent location to apache filetree...")
    subprocess.run(['cp', '-r', '/home/devin/projects/dog/src/.', '/var/www/html/'])

    # deal with perl file permissions and potential windows to unix conversion
    with os.scandir('/home/devin/projects/dog/cgi-bin') as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".pl"):
                if (needs_dos2unix(entry.path)):
                    subprocess.run(['dos2unix', entry.path])
                subprocess.run(['chmod', '755', entry.path])

    subprocess.run(['cp', '-r', '/home/devin/projects/dog/cgi-bin/.', '/usr/lib/cgi-bin/'])

if __name__ == "__main__":
    # address all call parameters
    attempt_screen_close()
    
    if (len(sys.argv) > 1 and sys.argv[1][0] == '-'):
        if (sys.argv[1].find('n') < 0):
            push_changes()
        if (sys.argv[1][1] == 'g'):
            # port 80 is defaulted with apache server
            subprocess.run(['ngrok', 'http', '80'])
        else:
            if (sys.argv[1].find('b') >= 0):
                command = "ngrok http 80"
                subprocess.run([
                    "screen",
                    "-dmS", screen_name,
                    "bash", "-c", command
                ])
                    
                print(f"forwarding apache server in the background on screen: {screen_name}...")
            if (sys.argv[1].find('c') >= 0):
                subprocess.run(["screen", "-r", screen_name])
    else:
        push_changes()
        
"""
Script Name: apache_push_helper.py

Description:
    Helps push files from a permanent, simple-to-navigate location in the file tree
    to where Apache serves them. Also provides several auxiliary parameters for
    managing the server environment.

    aliased by appu='python3 /home/devin/projects/dog/com/apache_push_helper.py'

Parameters:
    c : Attach to the frontend screen session.
    a : Attach to the backend screen session.

Notes:
    - The script kills all relevant screens sessions.
    - Could be more optimized for target rebooting, but on this scale it shouldn't matter
"""

import subprocess
import sys
import os
import re

FRONTEND_SCREEN_NAME = "NGROK"
BACKEND_SCREEN_NAME = "UVICORN"
API_PORT = "8000"
APACHE_PORT = "80"
FRONTEND_RUN_COMMAND = "ngrok http 80"
BACKEND_RUN_COMMAND = f"uvicorn app:app --host 127.0.0.1 --port {API_PORT}"

def needs_dos2unix(path):
    """
    Determine whether a .pl file needs to be converted to Unix line endings.

    Useful for checking if a .pl file needs to be converted to unix formatting 
    so that we can still read # actual error logs in the instance we just 
    automatically convert every file and have to pipe stderr, unfortunately where 
    dos2unix prints conversions, into /dev/null or whatever it is on ubuntu server

    I recently learned I can do all of this with a .sh file, but I personally love my 
    legacy code, so we're just gonna keep it.

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

def attempt_screen_close_helper(screen_name, line):
    match = re.match(rf"\s*(\d+)\.{re.escape(screen_name)}", line)
    if match:
        pid = match.group(1)
        subprocess.run(['screen', '-X', '-S', pid, 'quit'])
        print(f"closing {screen_name} on screen: {pid}...")
        return True
    return False


def attempt_screen_close():
    """
    Attempts to close any screens currently running the ngrok server or local api
    """

    result = subprocess.run(['screen', '-ls'], capture_output=True, text=True)

    for line in result.stdout.splitlines():
        if not attempt_screen_close_helper(BACKEND_SCREEN_NAME, line):
            attempt_screen_close_helper(FRONTEND_SCREEN_NAME, line)

def screen_init_helper(name, command, path):
    subprocess.run([
        "screen",
        "-dmS", name,
        "bash", "-c", command
    ], cwd=path)


    print(f"running process in the background on screen: {name}...")

def screen_initialization():
    """
    Creates the instances of relevant screens in one method
    """

    screen_init_helper(BACKEND_SCREEN_NAME, BACKEND_RUN_COMMAND, "/home/devin/projects/dog/backend")
    screen_init_helper(FRONTEND_SCREEN_NAME, FRONTEND_RUN_COMMAND, "/home/devin/projects/dog/frontend")

def push_changes():
    """
    Turned into a method because the parameters I was passing in started getting really weird

    The primary function of the script
    """

    # generate backups from previous version
    subprocess.run(['mkdir', '-p', '/home/devin/projects/dog/prev_ver'])
    subprocess.run(['rm', '-rf', '/home/devin/projects/dog/prev_ver/src'])
    subprocess.run(['rm', '-rf', '/home/devin/projects/dog/prev_ver/cgi-bin'])
    subprocess.run(['mkdir', '/home/devin/projects/dog/prev_ver/src'])
    subprocess.run(['mkdir', '/home/devin/projects/dog/prev_ver/cgi-bin'])
    subprocess.run(['cp', '-r', '/var/www/html/.', '/home/devin/projects/dog/prev_ver/src/'])
    subprocess.run(['cp', '-r', '/usr/lib/cgi-bin/.', '/home/devin/projects/dog/prev_ver/cgi-bin'])

    # remove previous version
    subprocess.run(['find', '/usr/lib/cgi-bin', '-mindepth', '1', '-delete'])

    print("pushing changes from permanent location to apache filetree...")
    subprocess.run(['npx', 'vite', 'build'], cwd="/home/devin/projects/dog/frontend")

    # deal with perl file permissions and potential windows to unix conversion
    with os.scandir('/home/devin/projects/dog/cgi-bin') as entries:
        for entry in entries:
            if entry.is_file() and entry.name.endswith(".pl"):
                if (needs_dos2unix(entry.path)):
                    subprocess.run(['dos2unix', entry.path])
                subprocess.run(['chmod', '755', entry.path])

    subprocess.run(['cp', '-r', '/home/devin/projects/dog/cgi-bin/.', '/usr/lib/cgi-bin/'])

    # rebuild 
    attempt_screen_close()
    screen_initialization()

if __name__ == "__main__":
    # address all call parameters
    if (len(sys.argv) > 1 and sys.argv[1][0] == '-'):   
        if (sys.argv[1].find('c') >= 0):
            subprocess.run(["screen", "-r", FRONTEND_SCREEN_NAME])
        elif (sys.argv[1].find('a') >= 0):
            subprocess.run(["screen", "-r", BACKEND_SCREEN_NAME])
    else:
        attempt_screen_close()
        push_changes()
        
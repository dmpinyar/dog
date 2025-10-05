import subprocess
import sys
import os

# aliased by appu='python3 /home/devin/projects/dog/com/apache_push_helper.py'

### SCRIPT INFO ###
# desc:
# helps push files from a permanent, simple to navigate location in the filetree to where
# apache deals with them. Has a bunch of side parameters for running the server as well
# parameters:
# g to build grok server within the same terminal window
# b to build grok server within a different screen session
# r to terminate any active screen sessions related to this script
# c to load into the screen
# n to opt out of pushing the files

# b, r, and c don't play well with g
# n just doesn't do anything if no other parameters are selected

# for screen parameters this is the default name for the screen
screen_name = "ngrok"

# useful for checking if a .pl file needs to be converted to unix formatting so that we can still read
# actual error logs in the instance we just automatically convert every file and have to pipe stderr,
# unfortunately where dos2unix prints conversions, into /dev/null or whatever it is on ubuntu server
def needs_dos2unix(path):
    with open(path, "rb") as file:
        shebang = file.readline()
        if b'\r' in shebang:
            return True
    return False

# turned into a method because the parameters I was passing in started getting really weird
def push_changes():
    print("pushing changes from permanent location to apache filetree...")

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
    if (len(sys.argv) > 1 and sys.argv[1][0] == '-'):
        if (sys.argv[1].find('n') < 0):
            push_changes()
        if (sys.argv[1][1] == 'g'):
            # port 80 is defaulted with apache server
            subprocess.run(['ngrok', 'http', '80'])
        else:
            if (sys.argv[1].find('r') >= 0):
                process = subprocess.run(['screen', '-X', '-S', 'ngrok', 'quit'], 
                            capture_output=True, 
                            text=True)
                if (not process.stdout):
                    print(f"closing ngrok on screen: {screen_name}...")
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
        
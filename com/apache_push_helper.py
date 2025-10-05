import subprocess
import sys
import os

# aliased by appu='python3 /home/devin/projects/dog/com/apache_push_helper.py'
# use -g to build grok server after

# useful for checking if a .pl file needs to be converted to unix formatting so that we can still read
# actual error logs in the instance we just automatically convert every file and have to pipe stderr,
# unfortunately where dos2unix prints conversions, into /dev/null or whatever it is on ubuntu server
def needs_dos2unix(path):
    with open(path, "rb") as file:
        shebang = file.readline()
        if b'\r' in shebang:
            return True
    return False

# just to be safe
if __name__ == "__main__":
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

    if (len(sys.argv) > 1 and sys.argv[1][0] == '-'):
        if (sys.argv[1][1] == 'g'):
            # port 80 is defaulted with apache server
            subprocess.run(['ngrok', 'http', '80'])
        elif (sys.argv[1][1:3] == 'bg'):
            screen_name = "ngrok"
            command = "ngrok http 80"

            subprocess.run([
                "screen",
                "-dmS", screen_name,
                "bash", "-c", command
            ])
            
            print("running ngrok in the background on in screen ngrok on port 80")
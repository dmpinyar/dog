import subprocess
import sys

# aliased by appu='python3 /home/devin/projects/dog/com/apache_push_helper.py'
# use -g to build grok server after

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
subprocess.run(['cp', '-r', '/home/devin/projects/dog/cgi-bin/.', '/usr/lib/cgi-bin/'])

if (len(sys.argv) > 1 and sys.argv[1] == '-g'):
    # port 80 is defaulted with apache server
    subprocess.run(['ngrok', 'http', '80'])
import subprocess
import sys
def run_command(command):
    p = subprocess.Popen(command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    return p.communicate()

print 'Commiting changes'
msg = 'update'
command = 'git commit -a -m \''+msg+'\''
result = run_command(command)
ret = result[0]
print "Commit DONE"

if 'git add' in ret:
    print 'Untracked files found, adding...'
    run_command('git add *.py')
    print 'Untracked files added DONE'
    print "Committing changes..."
    result = run_command('git commit -a -m \'update\'')
    print "Commit DONE"
    ret = result[0]
    
print "RESULT:"
print ret


input_read = raw_input("Do you want to upload your changes to website?(y/n)")
if 'y' in input_read:
    print 'Updating website...'
    ret = run_command('git push origin master')[0]
    print ret
    raw_input("PRESS ENTER TO EXIT")

print 'Bye'


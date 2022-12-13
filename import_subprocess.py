import subprocess
val = subprocess.check_output('git remote -v',shell=True)
print(val.decode('utf-8').split()[1])
import subprocess

cmd = ["ls"]
proc = subprocess.run(cmd)


print(proc.stdout)

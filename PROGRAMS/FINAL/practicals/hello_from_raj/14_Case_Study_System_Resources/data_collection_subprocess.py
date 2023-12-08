import subprocess

p = subprocess.Popen(["python", "data_collection.py"])
p.kill()
p.terminate()
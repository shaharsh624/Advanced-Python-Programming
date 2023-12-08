import subprocess
import sys

subprocess.run(["python", "test.py"])
subprocess.run(["python", "-c", "print('This is a subprocess')"])
result = subprocess.run([sys.executable, "-c", "print('this is second subprocess')"])
print(result)

result2 = subprocess.run(
    ["python", "-c", "print('This is third subprocess')"], capture_output=True
)
print("output: ", result2.stdout)
print("erorr: ", result2.stderr)

result3 = subprocess.run(
    ["python", "-c", "print('This is fourth subprocess')"],
    capture_output=True,
    text=True,
    check=True,
)
print("output: ", result3.stdout)
print("error: ", result3.stderr)

# subprocess.run(["python","-c","import time; time.sleep(5)"], capture_output=True, text=True)

# subprocess.run(["python","-c","import time; time.sleep(5)"], capture_output=True, text=True, timeout=2)

result4 = subprocess.run(
    ["python", "-c", "import sys;my_input=sys.stdin.read();print(my_input)"],
    capture_output=True,
    text=True,
    input="my_text",
)

print(result4.stdout)

result5 = subprocess.run(
    ["python", "subprocessprob2.py", "2", "4"], capture_output=True, text=True
)
print("output: ", result5.stdout)


result6 = subprocess.run(
    ["python", "subprocessprob3.py", "6", "7"], capture_output=True, text=True
)
print("output: ", result6.stdout)

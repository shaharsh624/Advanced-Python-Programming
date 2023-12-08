import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            print("Command executed successfully:")
            print(result.stdout)
        else:
            print("Command failed:")
            print(result.stderr)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    command = input("Enter a command to run: ")
    run_command(command)


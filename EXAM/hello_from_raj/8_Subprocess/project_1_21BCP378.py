import logging
import subprocess

logging.basicConfig(filename="output.log", level=logging.INFO)

first_command = subprocess.Popen(
    "echo 'Raj:21BCP378'", shell=True, stdout=subprocess.PIPE, text=True
)

second_command = subprocess.Popen(
    "ipconfig | findstr IPv4",
    shell=True,
    stdin=first_command.stdout,
    stdout=subprocess.PIPE,
    text=True,
)

first_command.stdout.close()
output, error = second_command.communicate()

if output:
    logging.info(output)

if error:
    logging.error(error)

second_command.wait()

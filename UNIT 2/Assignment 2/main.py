import subprocess

name_rollno_echo = "echo Name: Harsh Shah, Roll No.: 21BCP359" # Echo name and roll no

ip_add_command = "curl ifconfig.me" # Configure IP Address

log_file = "output.log" # Log the data

name_rollno_process = subprocess.Popen(

    name_rollno_echo,

    shell=True,

    stdout=subprocess.PIPE,

    stderr=subprocess.PIPE

)

name_rollno_output, name_rollno_error = name_rollno_process.communicate()

ip_add_process = subprocess.Popen(

    ip_add_command,

    shell=True,

    stdin=subprocess.PIPE,

    stdout=subprocess.PIPE,

    stderr=subprocess.PIPE

)

ip_add_output, ip_add_error = ip_add_process.communicate(input=name_rollno_output)

log_data = name_rollno_output.decode() + ip_add_output.decode()

log_file_handle = open(log_file, "w")

log_file_handle.write(log_data)

log_file_handle.close()

print("Data logged to", log_file)
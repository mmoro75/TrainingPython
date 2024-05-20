############################################ PARAMIKO MODULE #####################################################


# paramiko python module is usefully to work with linux remote server ( to use this module on your local machine you should have ssh2 )
# paramiko module establish an SSH2 connection wil remote server and by then you are allowed to execute command, upload/download files and so on
# in order to use Paramiko module you should have SSH2v2 on your local machine


import paramiko   # paramiko is not default module it has to be installed with "pip.exe install paramiko"

"""
paramiko module use two ways to establish connection with remote server 
   - username and password
   - user name and cryptographic keys
   
we can connect Linux/Windows  <-> Windows/Linux <-> Windows/windows <-> Lunix/Linux
"""

########### Linux to Linux ###################################

# check if you have ssh by running ssh on your command line ( if not yum install ssh)

ssh=paramiko.SSHClient() # create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # to authenticate automatically without asking yes or no permission when you connect to new server
ssh.connect(hostname="ipaddress/hostname",username="root",password="",port=22)  # connect with username and password
# now to run commands we use the blow syntax in order to have variable for= stdout=output, stderr=error and stdin=for additional input
stdin, stdout, stderr = ssh.exec_command("your_command")  # exec command will execute the command
"""
stderr == contains error message if command fails 
stdout == contains command output message if command is succesfulls
stdin == this variable is needed only if an additional imput has to be provided to remote server 
"""

print("the output is: ", stdout.read())  # the variable are files, so you need read to see the content by using read ( or readline/readlines functions)
print("The errors is: " ,stderr.read())

ssh.close() # close connection

# syntax to connect with you private key
# ssh.connect(host="ip/hostname",username="username",key_filename="your_private_key_file",port=22)

################################# Windows to Linux ##################################################################

ssh=paramiko.SSHClient() # create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="ipaddress/hostname",username="root",password="",port=22,)
stdin, stdout, stderr = ssh.exec_command("your_command")

print("the output is: ", stdout.read())  # the variable are files, so you need read to see the content
print("The error is: " ,stderr.read())

ssh.close() # close connection

########################################## transfer or download file from to remote server #############################

ssh=paramiko.SSHClient() # create ssh client
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="ipaddress/hostname",username="root",password="",port=22)

sftp_client=ssh.open_sftp() # open sftp connection to deal with files
sftp_client.get("path/filename","destination_Path/filename") # to download the file
# if you do not want to specify the path you can use the command sftp_client.chdir("location") to move to desired location
# print(sftp_client.getcwd()) it will print location where you are in remote server

sftp_client.put("location/filename", "destination_Location/filename") # to upload file

sftp_client.close() # close ftp client
ssh.close() # close connection



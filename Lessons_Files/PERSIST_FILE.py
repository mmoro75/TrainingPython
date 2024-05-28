"""
This script allows the user to download the PMAT file from a desired venue and check if the given RIC is persisted
"""
import paramiko


def main():
    hostname=input("provide server Ip: ")
    username=input("provide username: ")
    password=input("provide password: ")
    
    Lh_name=input("provide LH name :")
    venue_name=input("provide venue name :")
    file_path = "/data/Venues/"+ venue_name +"/config/"
    persist_file = "PERSIST_" + Lh_name +".DAT"
    download_Persist(hostname,username,password,file_path,persist_file)


#/data/Venues/OMXINET/config/
#
# PERSIST_OMXINET01.DAT
"""
hostname = "10.167.119.86"
username = "root"
password = "Reuters1"
file_path="/data/Venues/OMXINET/config/"
persist_file="PERSIST_OMXINET01.DAT"
"""

# this function is to dowload the PMAT file to your local machine#

def download_Persist(hostname,username,password,file_path,persist_file):

    try:

        ssh=paramiko.SSHClient() # create ssh client
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname,username=username,password=password,port=22,)

        print("I am connected")

        sftp_client = ssh.open_sftp()
        print("file is downloading")
        sftp_client.get(file_path + persist_file, "C:\\PMAT\\" + persist_file)
        print("download completed")
        ssh.close

    except socket.gaierror:
        print("Connection Error make sure server ip provided is correct and you are connected to the LSEG VPN")
        quit()
    except TimeoutError:
        print("Host file not found make sure the server ip and local path provided are correct")
        quit()
    except FileNotFoundError:
        print("Host file not found make sure the server ip and local path provided are correct")
        quit()
    except ConnectionError:
        print("Connection Error make sure server ip provided is correct and you are connected to the LSEG VPN")
        quit()
    except ConnectionRefusedError:
        print("connection is refused make sure password for the server is correct")
        quit()
    except AuthenticationException:
        print(f"The password '{password}' provided is not correct for the selected server, try again with correct password")
        quit()
    except Exception as e:
        print(e)
        quit()




# download_Persist(hostname,username,password)

main()
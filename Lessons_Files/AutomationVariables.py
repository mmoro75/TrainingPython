import datetime

today=print(datetime.datetime.now().strftime("%Y%m%d"))

hostname = input("provide server Ip: ")
username = input("provide username: ")
password = input("provide password: ")

Lh_name = input("provide LH name :")
venue_name = input("provide venue name :")
file_path = "/data/Venues/" + venue_name + "/config/"
persist_file = "PERSIST_" + Lh_name + ".DAT"
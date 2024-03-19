######################################## DAY-TIME MODULE  ##########################################

# Datetime is a builtin python module designed it to work with date and time

import datetime
print(dir(datetime))  # for available operations in date time main module
print(dir(datetime.datetime)) # for documentation about the submodule we are going to be using for next operations

## below operations will give you as output time based on your timezone, as set in your host
print(datetime.datetime.now())  # get time now
print(datetime.datetime.today()) # today datetime

# however with "now" operation you can get time for any desired timezone in order to do this you need to import another module as follow

import pytz # by importing this submodule now you can get time for any zone not just your host ( import with pip )
# print(dir(pytz)) # for available operations
ist=pytz.timezone("Europe/Rome")  # create the object for the time zone needed
print(datetime.datetime.now(ist)) # by passing this object you can get time for the configured timezone

# find all the timezones available at : https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

# we can also get only the info we need like day.hours , minute, month, year  ( see options below)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().month)   # we can store this information in variables if needed

# with the help of "string format time" operation we can build the info we need about dates and time see examples below

print(datetime.datetime.now().strftime("%y-%m-%d")) #  print year month
print(datetime.datetime.now().strftime("%Y-%M-%D")) # with capital letter the filter will give 4 digits output

# please refer to "https://strftime.org/" website to find out meaning about each letter in oder to compile the desired data ant time

# with option from-timestamp you can convert from number seconds into dates
print(datetime.datetime.fromtimestamp(150000))

print(datetime.datetime.max)  # gives the max allowed date
print(datetime.datetime.min)  # gives the min allowed date

'''
remember to use directly datetime submodule you can import this way 

from datetime import datetime # access directly submodule

print(datetime.now())  # instead of print(datetime.datetime.now())

'''




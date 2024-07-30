################################ Python on Linux #######################

# to get version installed - most of linux operating system already have python installed by default
# python --version

## if for some reason you required a new version of python do not disturb your default version os yum command depends on it

# to install new version log in as root

"""
1) go to python.org and download the linux version needed
2) copy the link location from python.org
3) see if wget is installed if not run "sudo yum install wget"
4) go to desired location on linux and dowload pytong using wget example "wget https://www.python.org/ftp/python/3.7.0/python-3.7.0.tgz"
5) extract the package "tar -xvzf Python-3.7.0.tgz
6) now package is extracted you need some dependencies
   --- yum install gcc openssl-devel bzip2-devel libiffi-devel
7) now navigate into you extracted package python and run "./configure --prefix=/usr//bin" command to decide location ( by default location is /usr/local/bin/)
8) after installation to compile run the command "make" on your python location
9) now run command "make altinstall" to not disturb existing vesrion (if you do not have any previous version you can simply run "make install")
10) now your python is installed in the location specified with configure and new version of python has to be run from there
11) now you can verify your new version like "./python3.7 --version"
12) using command "which python3.7" to get location
13) echo $path to check environment path is the location of your new python is specified
13) now create softlink to refer to new version lie " ln -s python3.7 python3"
14) now you can run from anywhere simply "python3 --version"
15  you can create also sof link for pip like "ln -s pip3.7 pip3" to manage external packages installation



"""

####################### Running python scrip on Linux system ###########################

"""
1) you can go to script location and specify which python version you want ot use 
   example "python3 helloworld.py"  or "python helloworld.py" for the standard version 

2) extra option on linux to run your scripts is to check where the desired version location is 
   "which python3" then copy the location open the script you want to run and first line add
   " #! python path" example for default location is "#!/usr/local/bin/python3"  ---> shebank line ( purpose is to specify which interpreter to use for your script)
    after that provide execution permission for your file "chmod +x helloworld.py"
    now you can run the script this way "./helloworld.py because the python info is already included in the script


"""



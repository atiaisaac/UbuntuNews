# UbuntuNews
Get news about your favourite Linux distro-ubuntu and it's flavours from omgubuntu.co.uk   
Python3.5 is suppoerted but it's not supported for python2.7.
Here is a screenshot of the result produced on ubuntu 17.10 running gnome on xorg.  
![screenshot1](https://user-images.githubusercontent.com/29587987/33105603-d90800ae-cf25-11e7-974e-091c094d5376.png)  

# Installation
Just run
`sudo python3 setup.py install`  
This will add the script to your environment path  

# Running
Type `ubuntunews`  
This will run the script. Note that you will need an active internet connection to see the expected output.
A cronjob can also be set to run the code at desired intervals

# Uninstallation
`pip3 uninstall ubuntunews` will uninstall the script. Remember to disable the cronjob (if any).


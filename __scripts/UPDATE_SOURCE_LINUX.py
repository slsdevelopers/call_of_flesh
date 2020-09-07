import os
import shutil
import time
import sys

##if you're a noob in python the hash tag is for comments
## this script is mainly for ubuntu linux

t1 = time.time()
##config
## if you want to change the installation directories, edit the mdir and cdir variables. mdir is the folder to install path, cdir is the civ13 game path to create.
mdir = os.path.dirname(os.path.abspath(__file__))
cdir = "cof13"  ## directory for overwritten files aka the original dir
byond_version_major = sys.argv[1]
byond_version_minor = sys.argv[2]
####
####

print("Installing dependencies...") ## this is pretty much pythons echo command
os.system("sudo apt install make git unzip python3 python3-pip lib32z1 lib32ncurses5 libc6-i386 lib32stdc++6") ## install requirements for BYOND
os.system("sudo apt autoremove") ## more reqs
os.system("sudo apt autoclean") ## oooooo a clean one
print("Getting and Installing Recent BYOND...")
exists = os.path.isfile(os.path.join(mdir,cdir,byond_version_major,".",byond_version_minor,"_byond_linux.zip"))
if not exists:
	os.system("sudo wget http://www.byond.com/download/build/{}/{}.{}_byond_linux.zip".format(byond_version_major,byond_version_major,byond_version_minor))
    ##make sure above grabs newest BYOND for major and minor version (should be newest one)
os.system("unzip {}.{}_byond_linux.zip".format(byond_version_major,byond_version_minor))
os.system("sudo mkdir /usr/share/man/man6")
os.system("make install -C byond")
print("Cloning the github...")
os.system("sudo git clone https://github.com/DojoDetroit/call_of_flesh cof13-git")  ## civ13-git is the new temp directory
##make sure above github url is whatever game github you want
print("Building binaries...")

os.system("DreamMaker cof13-git/*.dme")
os.system("sudo pip3 install psutil")
print("Copying files and folders...")
os.system("mkdir {}".format(cdir))
dmb = os.path.join(mdir,'cof13-git/*.dmb')
rsc = os.path.join(mdir,'cof13-git/*.rsc')

shutil.copy(dmb, os.path.join(mdir,cdir))
shutil.copy(rsc, os.path.join(mdir,cdir))
uip = os.path.join(mdir,cdir,'UI')
scriptsp = os.path.join(mdir,cdir,'__scripts')
configp = os.path.join(mdir,cdir,'config')

shutil.copytree('cof13-git/UI', uip)
shutil.copytree('cof13-git/__scripts', scriptsp)
shutil.copytree('cof13-git/config', configp)

print("Updating the config...")
with open(os.path.join(mdir,cdir,"__scripts/paths.txt"), 'r') as file :
  filedata = file.read()

filedata = filedata.replace("/home/1713", mdir)

with open(os.path.join(mdir,cdir,"__scripts/paths.txt"), 'w') as file:
  file.write(filedata)
t2 = time.time() - t1

print("Finished creating everything in {} seconds".format(t2))
print("Run sudo python3 {}/scripts/launch.py to start the server!".format(cdir))
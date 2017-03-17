#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import httplib
import time 
import os.path

# edit the save_directory to where you want the files. Below is Windows format.
save_directory="D:\\SecurityNow\\"
# or for Mac or Linux use this format:
#save_directory =  '/home/x/Music/Security-Now/'

# last episode you want to download (check https://www.grc.com/securitynow.htm)
last_episode=603

# base url for downloading podcasts. probably don't need to change this.
base_url='http://twit.cachefly.net/audio/sn/'

def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
ensure_dir(save_directory)

while os.path.isfile('sn_dwnldr.log') == False:
	print
	print 'Creating Log'
	f = open("sn_dwnldr.log", 'w') 
	f.write('1')
	f = open("sn_dwnldr.log", 'r')
	log = f.read()
	f.close()
	print #'--------------------------------------------------------------------------------'

f = open("sn_dwnldr.log", 'r+')
log = f.read()
i=  int(log)
f.close()
number=str(i)
print

#---------------------#!--------------------------------------------------------
print
print '-------------------FAIR-WARNING-------------------------------------------------'
print
print 'As it progresses the episodes get longer and therefore longer to download.'
print 'Depending internet speed, this could take hours if not days to download them all!'
print 'This script is aware of this fact and is meant to be stopped and started at your convenience.'
print 'The script will log what episode you last downloaded in a file called sn_dwnldr.log'
print 'in the same directory that the script is located'
print
print 'The episodes will be downloaded to:' + save_directory
print
print '-------------------BEGIN-DOWNLOAD-----------------------------------------------'
print
print 'Will start downloading at Episode ' + number

while 10>i:
	number=str(i)
	episode_number = '000' + number
	name = 'sn' + episode_number 
	file_name= name + '.mp3'
	full_url= base_url + name + '/' + file_name
	urllib.urlretrieve(full_url, save_directory + file_name )
	i=i+1
	f = open('sn_dwnldr.log', 'w') #creates or overwrites log file
	f.write(episode_number) #logs the next episode that needs to be downloaded
	f.close()
	print file_name + ' was downloaded'
	time.sleep(15) #slows it down so that CacheFly doesn't disconnect you, you can try less time 
	print '-------------------------'

while i<100:
	number=str(i)
	episode_number = '00' + number
	name = 'sn' + episode_number 
	file_name= name + '.mp3'
	full_url= base_url + name + '/' + file_name
	urllib.urlretrieve(full_url, save_directory + file_name )
	i=i+1
	f = open('sn_dwnldr.log', 'w') #creates or overwrites log file
	f.write(episode_number) #logs the next episode that needs to be downloaded
	f.close()
	print file_name + ' was downloaded'
	time.sleep(15)
	print '-------------------------'

while i<=557: #this is the most current episode number, where it stops
	number=str(i)
	episode_number = '0' + number 
	name = 'sn' + episode_number 
	file_name= name + '.mp3'
	full_url= base_url + name + '/' + file_name
	urllib.urlretrieve(full_url, save_directory + file_name )
	i=i+1
	f = open('sn_dwnldr.log', 'w') #creates or overwrites log file
	f.write(episode_number) #logs the next episode that needs to be downloaded
	f.close()
	print file_name + ' was downloaded'
	time.sleep(15)
	print '-------------------------'

print 'Finished downloading all Security Now episodes'	
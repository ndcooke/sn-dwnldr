# sn-dwnldr.py
# https://github.com/ndcooke/sn-dwnldr
# forked from https://github.com/thepunkgeek/sn-dwnldr a while back
# A downloader for security now podcast. could probably do others.


import http.client
import os.path
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ElTree

save_directory = "D:\\SecurityNow\\"
last_episode = 751

base_url = 'http://twit.cachefly.net/audio/sn/'

# now we can get the latest episode straight from the rss feed
url = 'http://www.leoville.tv/podcasts/sn.xml'
tree = ElTree.parse(urllib.request.urlopen(url))
doc = tree.getroot()

# declare namespaces that exist in the feed (as of 2019-06-03)
namespaces = dict(atom='http://www.w3.org/2005/Atom', media='http://search.yahoo.com/mrss/',
                  itunes='http://www.itunes.com/dtds/podcast-1.0.dtd',
                  creativeCommons='http://backend.userland.com/creativeCommonsRssModule',
                  content='http://purl.org/rss/1.0/modules/content/',
                  sy='http://purl.org/rss/1.0/modules/syndication/')

# get the largest episode number
results = tree.findall('.//itunes:episode', namespaces)
for result in results:
    if int(result.text) > last_episode:
        last_episode = int(result.text)


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


ensure_dir(save_directory)

while os.path.isfile('sn_dwnldr.log') == False:
    print()
    print('Creating Log')
    f = open("sn_dwnldr.log", 'w')
    f.write('1')
    f = open("sn_dwnldr.log", 'r')
    log = f.read()
    f.close()
    print()  # '--------------------------------------------------------------------------------'

f = open("sn_dwnldr.log", 'r+')
log = f.read()
i = int(log)
f.close()
number = str(i)
print()

print('-------------------FAIR-WARNING-------------------------------------------------')
print()
print('As it progresses the episodes get longer and therefore longer to download.')
print('Depending internet speed, this could take hours if not days to download them all!')
print('This script is aware of this fact and is meant to be stopped and started at your convenience.')
print('The script will log what episode you last downloaded in a file called sn_dwnldr.log')
print('in the same directory that the script is located')
print()
print('The episodes will be downloaded to:' + save_directory)
print()
print('-------------------BEGIN-DOWNLOAD-----------------------------------------------')
print()

print('Will start downloading at: Episode ' + number)
print('Will finish downloading at: Episode ' + str(last_episode))

while 10 > i:
    number = str(i)
    episode_number = '000' + number
    name = 'sn' + episode_number
    file_name = name + '.mp3'
    full_url = base_url + name + '/' + file_name
    urllib.request.urlretrieve(full_url, save_directory + file_name)
    i = i + 1
    f = open('sn_dwnldr.log', 'w')  # creates or overwrites log file
    f.write(episode_number)  # logs the next episode that needs to be downloaded
    f.close()
    print(file_name + ' was downloaded')
    time.sleep(15)  # slows it down so that CacheFly doesn't disconnect you, you can try less time
    print('--------------------------------------------------------------------------------')

while i < 100:
    number = str(i)
    episode_number = '00' + number
    name = 'sn' + episode_number
    file_name = name + '.mp3'
    full_url = base_url + name + '/' + file_name
    urllib.request.urlretrieve(full_url, save_directory + file_name)
    i = i + 1
    f = open('sn_dwnldr.log', 'w')  # creates or overwrites log file
    f.write(episode_number)  # logs the next episode that needs to be downloaded
    f.close()
    print(file_name + ' was downloaded')
    time.sleep(15)
    print('--------------------------------------------------------------------------------')

while i <= int(last_episode):  # this is the most current episode number, where it stops
    number = str(i)
    episode_number = '0' + number
    name = 'sn' + episode_number
    file_name = name + '.mp3'
    full_url = base_url + name + '/' + file_name
    urllib.request.urlretrieve(full_url, save_directory + file_name)
    i = i + 1
    f = open('sn_dwnldr.log', 'w')  # creates or overwrites log file
    f.write(episode_number)  # logs the next episode that needs to be downloaded
    f.close()
    print(file_name + ' was downloaded')
    time.sleep(15)
    print('--------------------------------------------------------------------------------')

print('Finished downloading all Security Now episodes')

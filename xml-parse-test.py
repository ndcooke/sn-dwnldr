# xml_
# test for the xml parsing

import urllib.request, urllib.parse, urllib.error
import http.client
import os

import xml.etree.ElementTree as ET

xml_url='http://www.leoville.tv/podcasts/sn.xml'

#urllib.request.urlretrieve(xml_url, os.getcwd()) 
#urllib.request.urlretrieve(xml_url)

xmltree = ET.parse(urllib.request.urlopen(xml_url))
xmldoc = xmltree.getroot()

#for child in root:
#    print(child.tag, child.attrib)

title1 = xmldoc.find('title')

# this returns "channel", which is the first element.
for node in xmldoc:
    print(node)

for parent in xmldoc.getiterator():
    for child in parent:
        print(str(parent)+":"+str(child))



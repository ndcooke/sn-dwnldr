## THE SECURITY NOW PODCAST DOWNLOADER aka sn-dwnldr  

#### Original Author: THEPUNKGEEK aka Radio || [thepunkgeek/sn-dwnldr](https://github.com/thepunkgeek/sn-dwnldr)  
#### Fork Author: ndcooke

### Updates:  
* Now reads the latest episode from the RSS feed.  
* Changed from Python 2.x to 3.x (mainly just changing print commands).  
  * Python 2 is also available as `sn-dwnldr-py2.py` now. (This version still uses
  `last_episode` and does not get the latest episode number from the RSS feed.)  
* Changed to Windows file system by default.  
* ~~Added a variable for the maximum podcast number to download (see `last_episode`).~~  
 
### Usage:  
* Adjust `save_directory` variable to where you want the files downloaded.
* ~~Adjust `last_episode` to coincide with the last episode of Security Now you
want downloaded.  If you don't know and want them all, look [here](https://www.grc.com/securitynow.htm) 
and check what episode number the topmost episode is.~~  
 
### Roadmap:  
* Eventually we're going to get into 4-digit episode numbers and it will require
an update.
* ~~It'd be nice to be able to automatically know what the latest podcast is and
only use the `last_episode` variable when you want to specifically hardcode 
the last episode you want downloaded.~~  

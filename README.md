## THE SECURITY NOW PODCAST DOWNLOADER aka sn-dwnldr  

#### Original Author: THEPUNKGEEK aka Radio  
#### Original GitHub: [thepunkgeek/sn-dwnldr](https://github.com/thepunkgeek/sn-dwnldr)  
#### Forked Author: ndcooke aka ndcooke  
#### Forked GitHub: [ndcooke/sn-dwnldr](https://github.com/ndcooke/sn-dwnldr)  

### Forked Updates:  
* Changed from Python 2.x to 3.x (mainly just changing print commands).
  * Python 2 is also available as `sn-dwnldr-py2.py` now.
* Changed to Windows file system by default.
* Added a variable for the maximum podcast number to download (see `last_episode`).
 
### Usage:  
* Adjust `save_directory` variable to where you want the files downloaded.
* Adjust `last_episode` to coincide with the last episode of Security Now you
want downloaded.  If you don't know and want them all, look [here](https://www.grc.com/securitynow.htm) 
and check what episode number the topmost episode is.  
 
### Looking Forward:  
* It'd be nice to be able to automatically know what the latest podcast is and
only use the `last_episode` variable when you want to specifically hardcode 
the last episode you want downloaded.
 
 
* * *  
 
Original Author: THEPUNKGEEK aka Radio  
Original Message:  
  
I wanted to download all the security now episodes because I love this podcast!
This script attempts to do just that...
It's not the most amazing piece of code, but it's better than doing so manually lol
The main problem with doing this is that the files get big, 
and therefore this script will take hours to complete... 
To compensate I've added a log, and made the script able to pick up where it left off.

You must adjust save_directory to where you want it download to.

You're welcome to use and distribute as you wish. I'd love it if you gave me credit.

Enjoy! 

### ChucK waves  

this repository will host a python based server application that 

- takes an incoming full gist link
- downloads the tar.gz into a temporary directory
- looks for a compatible tar.gz (must contain a dir and initialize.ck)
- if it's found gold, it extracts the content to it's own directory
- will record a .wav of given (length|name|volume) to disk
- the wave is moved to the output directory
- the tar and folder are deleted.

#### future plans   
- offer a flac/mp3 encoder

### How?  
- The Chuck-plugin for SublimeText3 can upload multi-file gist of the current project (or you can do it manually, like a sap) 
- with this gist point a browser at:  
    http://127.0.0.1:5000/encode/url=https://gist.github.com/zeffii/8021115&name=newname&time=30&gain=90

http://packages.debian.org/squeeze/flac


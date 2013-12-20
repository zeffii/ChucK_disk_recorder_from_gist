### ChucK Encoder Server App. 

this repository hosts a python based server application that 

- takes an incoming full gist link with parameters for length, name and gain
- downloads the tar.gz into a temporary directory
- looks for a compatible tar.gz (must contain a dir and initialize.ck)
- if it's found gold, it extracts the content to its own directory
- will record a .wav of given (length|name|volume) to disk
- the wave is moved to the output directory
- the tar and folder are deleted.

### How?  
- The Chuck-plugin for SublimeText3 can upload multi-file gist of the current project  
- with this gist point a browser at:  
    (gist_url) = https://gist.github.com/zeffii/8021115   
    - `http://127.0.0.1:5000/encode/url=(gist_url)&name=newname&time=30&gain=90`  
    - `http://the-host.ext:5000/encode/url=(gist_url)&name=newname&time=30&gain=90`  

### future plans   
- offer a flac/mp3 encoder ( http://packages.debian.org/squeeze/flac )


### ChucK waves
this repository will host a python based server application that 

- takes an incoming gist link (either the number or the full url)  
- and parses the associated json and downloads the tar.gz  
- and extracts that into a temporary directory.  
- then will record record a .wav of given length to disk  
- the wav will be converted to mp3 or flac and a link will be presented.  

### How?

- The Chuck-plugin for SublimeText3 can upload multi-file gist of the current project (or you can do it manually, like a sap) 
- with this gist point a browser at   your_server/CW&gist_id&length(ms)

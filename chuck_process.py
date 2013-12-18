# incoming 
"""
https://gist.github.com/zeffii/8021115/download
https://gist.github.com/zeffii/8021115
gist8021115-7d121fb45ec5486debdbd673dba4017247701aa5.tar.gz
"""
import os
import json
from urllib.request import urlopen
from urllib.request import urlretrieve
import tarfile

def download_tar(gist_url):
    dl_url = "https://gist.github.com/zeffii/8021115"
    gist_id = dl_url.split("/")[-1]

    cwd = os.getcwd()
    tarname = gist_id + ".tar.gz"
    destination_temp = os.path.join(cwd, "tmp", tarname)
    urlretrieve(dl_url + "/download", destination_temp)
    #os.chdir("..")
    # print
    
    #tar = tarfile.open(destination_temp)
    #tar.extractall()
    #tar.close()

    with tarfile.open(destination_temp, "r:gz") as tar:
        for tarinfo in tar:
            if tarinfo.isreg():
                print(os.path.split(tarinfo.name)[-1])
            elif tarinfo.isdir():
                print("a directory:", tarinfo.name)
            else:
                print("something else.")

download_tar("https://gist.github.com/zeffii/8021115")

# def get_raw_url_from_gist_id(gist_id):
    
#     gist_id = str(gist_id)
#     url = 'https://api.github.com/gists/' + gist_id
    
#     found_json = urlopen(url).readall().decode()

#     wfile = json.JSONDecoder()
#     wjson = wfile.decode(found_json)

#     # 'files' may contain several - this will mess up gist name.
#     files_flag = 'files'
#     file_names = list(wjson[files_flag].keys())
#     #file_name = file_names[0]
#     #return wjson[files_flag][file_name]['raw_url']
#     print(file_names)

# get_raw_url_from_gist_id(8021115) 


#def get_file(gist_id):
#    url = get_raw_url_from_gist_id(gist_id)
#    conn = urlopen(url).readall().decode()
#    return conn
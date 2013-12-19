# incoming 
"""
takes input like: https://gist.github.com/zeffii/8021115
obtains: gist8021115-7d121fb45ec5486debdbd673dba4017247701aa5.tar.gz
gists can't have sub-directories, Just go flat, or write your own.

"""
import os
import json
from urllib.request import urlopen
from urllib.request import urlretrieve
import tarfile
import subprocess
import threading
import shutil

#wav_writer_ck_path = "wav_writer_wgain.ck"
# this would be the absolute path on the server, and must use forward slashes (this is passed into chuck)
# chuck expects forward slashes.. (don't ask...)
#wav_writer_ck_path = "C:/Users/dealga/Documents/GitHub/ChucK_disk_recorder_from_gist/wav_writer_wgain.ck"
#destination_directory = "C:/Users/dealga/Documents/GitHub/ChucK_disk_recorder_from_gist/output/"
wav_writer_ck_path = 'wav_writer_wgain.ck'

def take_input2(dir_name, wav_name, length, max_amp):
    # chuck somefile.ck wav_writer_wgain.ck:20:new_wavename:1.0
    cc = [wav_writer_ck_path, str(length), wav_name, str(max_amp)]
    record_commands = ':'.join(cc)
    chuck_init_wav = ['chuck', 'initialize.ck', record_commands, '-s']

    cwd = os.getcwd()
    print("> " +  " ".join(chuck_init_wav) + "\n")
    print("os.getcwd():", cwd)
    # os.chdir(os.path.join(cwd, dir_name))
    print("now os.getcwd():", os.getcwd())

    p = subprocess.Popen(chuck_init_wav, 
                    cwd=os.getcwd(),
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT, 
                    shell=True).communicate()

    print(p)
    print("complete! ")
    print("doing clean up.")
    # self.perform_cleanup()


take_input2("gist8021115-7d121fb45ec5486debdbd673dba4017247701aa5", "demo_output", 20, 1.0)

# EOF



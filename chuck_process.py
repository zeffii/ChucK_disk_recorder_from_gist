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

wav_writer_ck_path = "../wav_writer_wgain.ck"
destination_directory = "/home/zeffii/public_html/output"

def get_dir_name(destination_tmpfile):
    found_dir_name = None
    has_initialize_file = None
    found_files = []
    take = found_files.append

    with tarfile.open(destination_tmpfile, "r:gz") as tar:
        # check every item in the tar
        for tarinfo in tar:
            if tarinfo.isreg():
                # strip off the directory info
                file_found = os.path.split(tarinfo.name)[-1]
                take(file_found)

                if file_found == "initialize.ck":
                    has_initialize_file = True

            elif tarinfo.isdir():
                found_dir_name = tarinfo.name

    if found_dir_name and has_initialize_file:
        print("found:", found_files)
        return found_dir_name
    else:
        print("Didn't find a directory or initialize.ck")

    return

def download_tar(dl_url):
    dl_url = "https://gist.github.com/zeffii/8021115"
    gist_id = dl_url.split("/")[-1]
    # user_id = dl_url.split("/")[-2] 
    cwd = os.getcwd()
    tarname = gist_id + ".tar.gz"
    destination_tmpfile = os.path.join(cwd, "tmp", tarname)

    try:
        urlretrieve(dl_url + "/download", destination_tmpfile)
    except:
        print("unable to get file")
        return 

    dir_name = get_dir_name(destination_tmpfile)
    if dir_name:
        print("found:", dir_name)
        return dir_name, destination_tmpfile
    else:
        print("nothing to work with..")

    return


def perform_cleanup(cwd, wav_name, destination_tmpfile):    
    wav_file_full_path = os.path.join(cwd, wav_name + ".wav")

    print("copying:", wav_file_full_path )
    shutil.copy(wav_file_full_path, destination_directory)

    try:
        print("removing /tmp file:", destination_tmpfile)
        os.remove(destination_tmpfile)
        print("deleting directory:", cwd)
        shutil.rmtree(cwd)
    except:
        print("unable to remove tmp content")


def take_input(dl_url, wav_name, length, max_amp):
    success = download_tar(dl_url)
    if not success:
        print("ending..")
        return

    dir_name, destination_tmpfile = success
    print(dir_name)
    
    # extract!
    tar = tarfile.open(destination_tmpfile)
    tar.extractall()
    tar.close()

    old_dir = os.getcwd()
    tar_directory = os.path.join(old_dir, dir_name)
    os.chdir(tar_directory)

    # chuck somefile.ck wav_writer_wgain.ck:20:new_wavename:1.0
    cc = [wav_writer_ck_path, str(length), wav_name, str(max_amp)]
    record_commands = ":".join(cc)
    chuck_init = ["chuck", "initialize.ck", record_commands, "-s"]
    full_command = " ".join(chuck_init)

    print("> " +  full_command)

    try:
        sts = subprocess.Popen(full_command, shell=True).wait()
    except:
        print("--- error while writing to disk. ---")
        os.chdir(old_dir)
        return

    try:
        perform_cleanup(tar_directory, wav_name, destination_tmpfile)
    except:
        print("--- error while performing cleaunp ---")
    finally:
        print("restoring original directory")
        os.chdir(old_dir)




# take_input("https://gist.github.com/zeffii/8021115", "demo_output", 5, 1.0)

# EOF



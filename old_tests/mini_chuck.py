import os
import subprocess

def take_input2():

    record_commands = '../wav_writer_wgain.ck:20:demo_track:1.0'
    chuck_init_wav = ['chuck', 'initialize.ck', record_commands, '-s']

    print("os.getcwd():", os.getcwd())
    full_command = " ".join(chuck_init_wav)
    print("sending > " +  full_command)

    print("processing, attempt:")
    sts = subprocess.Popen(full_command, shell=True).wait()

    print("complete! ")
    print("doing clean up.")

take_input2()

# EOF



# file_size_tester.py
import os
import time
import sys
import json
from json_writer import write_full_json

def print_names(cwd):
    a = list(os.walk(cwd))
    print(a)

def get_finished_value(full_path_to_file):
    with open(full_path_to_file) as fp:
        read_file = json.load(fp)
        return read_file.get("finished", -1)

def test_size(full_path_to_file, predicted_size, wav_name):

    status_src = "/home/zeffii/public_html/static/status.json"

    while(not get_finished_value(status_src) == 1):

        try:
            stats = os.stat(full_path_to_file)
            found_size = stats.st_size

            # print(found_size, " vs predicted: ", predicted_size)
            if found_size >= 0:
                percent = float(found_size) / float(predicted_size)
                write_full_json(0, wav_name, "wav", str(percent*100))

        except:
            # print("not found yet")
            time.sleep(1.0)
            continue

        finally:

            time.sleep(2.0)

    write_full_json(1, wav_name, "wav", str(100))
    print("done!!")

if __name__ == "__main__":
    # print("starting script")
    test_size(*sys.argv[1:])
    # print("ending script")


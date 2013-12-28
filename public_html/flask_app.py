from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import copy_current_request_context

import threading
import subprocess

#from chuck_process import take_input
from json_writer import write_full_json

app = Flask(__name__)

link_str = "http://www.thegibson.net/~zeffii/output/{0}.wav"

@app.route('/encode/<path:path>', methods=['GET', 'POST'])
def encoder(path):

    try:
        commands = path.split("&")
        params = {key: value for key, value in [c.split("=") for c in commands]}

        url = params.get('url', "https://gist.github.com/zeffii/8021115")
        name = params.get('name', "demo_name")
        _time = int(params.get('time', 30))
        gain = float(params.get('gain', 100.0))/100.0

        # initial write to the json to state it is not finished yet.
        write_full_json(0, name, "wav", 0)

        # # start event thread, for concurrency.
        commands = ["python3", "process_input.py",  url, name, str(_time), str(gain)]
        print("commands:", commands)

        print("starting thread")
        th = Ck_Thread(commands)
        th.start()

        # tell browser to render the progress indicator.
        # javascript will update the page according to status.json
        print("redirecting")
        return redirect(url_for('static', filename='rendering_animation.html'))

    except:
        return "try that again!"


class Ck_Thread(threading.Thread):
    def __init__(self, commands):
        self.commands = commands
        threading.Thread.__init__(self)

    def run(self):
        print("doing script")
        subprocess.Popen(self.commands)
        print("ended scripts")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


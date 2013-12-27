from flask import Flask
from flask import render_template
from flask import url_for, redirect
import threading
import subprocess
import time
import os

app = Flask(__name__)

@app.route('/debug/<path:path>', methods=['GET', 'POST'])
def dencoder(path):

    try:
        commands = ["python3", "semi_process.py",  "18"]
        th = Ck_Thread(commands)
        th.start()
        print("process started, returning flow")

        #return redirect(url_for('static', filename='rendering_animation.html'))
        return "seems to work! " + str(time.time())

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
    # app.run(host='0.0.0.0')
    # app.run() # host='0.0.0.0')
    # app.run()
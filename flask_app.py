from multiprocessing import Process
from flask import Flask
from flask import render_template
from flask import url_for, redirect
from flask import copy_current_request_context

from chuck_process import take_input
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
        time = int(params.get('time', 30))
        gain = float(params.get('gain', 100.0))/100.0

        # # write status json, to say things are being processed.
        write_full_json(0, name, "wav")

        # # start event thread, for concurrency.
        #p = Process(target=take_input, args=(url, name, time, gain))
        #p.start()
        #p.join()
        take_input(url, name, time, gain)

        # we are done, send it off and javascript will update the page
        # when the status.json is is modified to finished = 1
        #return redirect(url_for('static', filename='rendering_animation.html'))
        return render_template('complete.html', link=link_str.format(name), name=name)

    except:
        return "try that again!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


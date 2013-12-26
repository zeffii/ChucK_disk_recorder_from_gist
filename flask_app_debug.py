from flask import Flask
from flask import render_template
from flask import url_for, redirect
from multiprocessing import Process
import time

app = Flask(__name__)

def do_things(num_secs):
    print("entered here")
    time.sleep(num_secs)
    print("leaving here")

@app.route('/debug/<path:path>', methods=['GET', 'POST'])
def dencoder(path):

    try:
        # return render_template('rendering_animation.html')
        #return "harrrrr"
        print("starting process")
        p = Process(target=do_things, args=(10,))
        p.start()
        p.join()

        #return redirect(url_for('static', filename='rendering_animation.html'))
        return "stuff happened good!"

    except:
        return "try that again!"




if __name__ == '__main__':
    app.run() # host='0.0.0.0')
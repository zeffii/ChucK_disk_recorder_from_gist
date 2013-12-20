from chuck_process import take_input
from flask import Flask
from flask import render_template

app = Flask(__name__)

link_str = "http://www.thegibson.net/~zeffii/output/{0}.wav"


@app.route('/encode/<path:path>', methods=['GET', 'POST'])
def encoder(path):

    try:
        commands = path.split("&")
        params = {key: value for key, value in [c.split("=") for c in commands]}

        url = params.get('url', "https://gist.github.com/zeffii/8021115")
        name = params.get('name', "demo_name")
        time = params.get('time', 30)
        gain = params.get('gain', 1.0)

        # show this anyway
        render_template('rendering.html', thecontent=name)

        take_input(url, name, int(time), (int(gain)/100))
        return render_template('complete.html', link=link_str.format(name), name=name)
        #return render_template('complete.html', link=name)
    except:
        return "try that again!"


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
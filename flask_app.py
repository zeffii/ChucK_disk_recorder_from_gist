from chuck_process import take_input
from flask import Flask
app = Flask(__name__)

link_str = """\n\nIf it worked, the output is here: http://www.thegibson.net/~zeffii/public_html/output/{0}.wav"""


@app.route('/encode/<path:path>', methods=['GET', 'POST'])
def encoder(path):

    try:
        commands = path.split("&")
        params = {key: value for key, value in [c.split("=") for c in commands]}

        url = params.get('url', "https://gist.github.com/zeffii/8021115")
        name = params.get('name', "demo_name")
        time = params.get('time', 30)
        gain = params.get('gain', 1.0)

        take_input(url, name, int(time), (int(gain)/100))
        return "yes! " + str(params) + link_str.format(name)
    except:
        return "try that again!"


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0')
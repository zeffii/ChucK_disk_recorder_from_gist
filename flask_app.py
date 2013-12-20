from flask import Flask
app = Flask(__name__)

@app.route('/encode/<path:path>', methods=['GET', 'POST'])
def encoder(path):

    try:
        commands = path.split("&")
        params = {key: value for key, value in [c.split("=") for c in commands]}
    except:
        return "try that again!"



    return "yes! " + str(params)

if __name__ == '__main__':
    app.run(debug=True)
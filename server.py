from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/alert', methods=['GET', 'POST'])
def alert():
    if request.method == 'POST':
        watchcoin = request.form['watchcoin']
        paircoin = request.form['paircoin']
        alertlevel = request.form['alertlevel']
        subprocess.Popen(['python', 'alert.py', watchcoin, paircoin, alertlevel])
        return 'Alert activated.'
    else:
        return '''
            <form method="post">
                <label for="watchcoin">Watchcoin:</label>
                <input type="text" name="watchcoin"><br><br>
                <label for="paircoin">Paircoin:</label>
                <input type="text" name="paircoin"><br><br>
                <label for="alertlevel">Alert level:</label>
                <input type="text" name="alertlevel"><br><br>
                <input type="submit" value="Activate alert">
            </form>
        '''

if __name__ == '__main__':
    app.run(port=8089)

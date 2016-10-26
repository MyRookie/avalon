from flask import Flask
from flask import render_template
from flask import request
from Gamedb import database
from Game import Player, Room, OnlinePlayer

app = Flask(__name__)
db = database()
players = OnlinePlayer()

@app.route("/",  methods=['POST', 'GET'])
def main():
    return render_template('main.html')

@app.route('/login_or_regist',  methods=['POST', 'GET'])
def login_or_regist():
    ctx = {}
    ctx['error'] = None
    if 'redirect' not in request.form:
        ctx['redirect'] = 'login'
        ctx['error'] = request.args['error']
    else:
        ctx['redirect'] = request.form['redirect']
    return render_template('login_or_regist.html',ctx=ctx)

@app.route('/game_hall',  methods=['POST', 'GET'])
def game_hall():
    if request.form['submit'] == 'login':
        success, p = db.find_user(request.form)
        print success
        pass
    elif request.form['submit'] == 'regist':
        success, p = db.insert_user(request.form)
        if not success:
            return redirect(url_for('/login_or_regist',error='User already exists'))
    else:
        return redirect(url_for('/login_or_regist',error='Server error'))
    players.add_player(p[0])
    return render_template('game_hall.html')

if __name__ == "__main__":

    app.run(debug=True)

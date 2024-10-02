from flask import Flask, render_template, request, redirect, url_for
from backend.blockchain import join_game, make_move

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join', methods=['POST'])
def join():
    account = request.form['account']
    private_key = request.form['private_key']
    tx_hash = join_game(account, private_key)
    return redirect(url_for('game', tx_hash=tx_hash))

@app.route('/game/<tx_hash>')
def game(tx_hash):
    # Fetch game state based on tx_hash
    return render_template('game.html', tx_hash=tx_hash)

@app.route('/move', methods=['POST'])
def move():
    account = request.form['account']
    private_key = request.form['private_key']
    from_x = request.form['from_x']
    from_y = request.form['from_y']
    to_x = request.form['to_x']
    to_y = request.form['to_y']
    tx_hash = make_move(account, private_key, from_x, from_y, to_x, to_y)
    return redirect(url_for('game', tx_hash=tx_hash))

if __name__ == '__main__':
    app.run(debug=True)

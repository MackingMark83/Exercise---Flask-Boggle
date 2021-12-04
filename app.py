from flask import Flask, request, render_template, jsonify, session
from boggle import Boggle
app.config["SECRET_KEY"] = "mycode"

app = Flask(__name__)


boogle_game = Boggle()


@app.route("/")
def homepage():
    """Show board."""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("base.html", board=board,
                           highscore=highscore,
                           nplays=nplays)

from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NFLRankingTable.db'


db = SQLAlchemy(app)

class NFLRankingTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.String(255), nullable=False)
    team = db.Column(db.String(255), nullable=False)
    proj_win = db.Column(db.String(255), nullable=False)
    proj_loss = db.Column(db.String(255), nullable=False)
    play_off = db.Column(db.String(255), nullable=False)
    sb_win = db.Column(db.String(255), nullable=False)


@app.route("/", methods=["GET"])
def home():

    table = NFLRankingTable.query.all()

    d=[]

    

    for row in table:

        row_as_dict = {

            "rank": row.rank,

            "rating": row.rating,

            "team": row.team,

            "proj_win": row.proj_win,

            "proj_loss": row.proj_loss,

            "play_off": row.play_off,

            "sb_win": row.sb_win

        }

        d.append(row_as_dict)

    return render_template("index.html", data=d)


@app.route("/api", methods=["GET"])
def api_route():

    table = NFLRankingTable.query.all()

    d=[]

    for row in table:

        row_as_dict = {

            "rank": row.rank,

            "rating": row.rating,

            "team": row.team,

            "proj_win": row.proj_win,

            "proj_loss": row.proj_loss,

            "play_off": row.play_off,

            "sb_win": row.sb_win


        }

        d.append(row_as_dict)

    return jsonify(d)


if __name__ == "__main__":

    app.run(debug=True)
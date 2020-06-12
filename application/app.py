from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.nba_demo
population = db.nba_players


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    players = list(population.find())
    #print(players)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", players=players)

@app.route("/tableau")
def tableu():
    return render_template("tableau.html")

if __name__ == "__main__":
    app.run(debug=True)

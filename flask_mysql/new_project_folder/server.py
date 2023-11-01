from flask import Flask, render_template
# import the class from friend.py
from friend import friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = friends.get_all()
    print(friends)
    return render_template("index.html")

if __name__ == "__main__":
      app.run(debug=True, host="localhost", port=8000)


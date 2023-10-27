from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
      student_info = [
      {"first_name": "Michael", "last_name": "Choi"},
      {"first_name": "John", "last_name": "Supsupin"},
      {"first_name": "Mark", "last_name": "Guillen"},
      {"first_name": "KB", "last_name": "Tonel"},
      ]
      for eachDictionary in student_info:
            first_name = eachDictionary.get("first_name", "")
            last_name = eachDictionary.get("last_name", "")
            full_name = f'{first_name} {last_name}'
            eachDictionary["full_name"] = full_name
      return render_template("index.html", student_info=student_info)


app.run(debug=True, host="localhost", port=8000)

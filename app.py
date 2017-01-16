from flask import Flask, render_template, redirect, url_for

app=Flask(__name__)

reminders=[]
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", todos=reminders)

@app.route("/add/<message>")
def add(message):
    reminders.append(message)
    return redirect("/")

@app.route("/remove/<int:index>")
def remove(index):
    try:
        del reminders[index]
        return redirect("/")
    except Exception as e:
        return render_template("error.html", message="List index out of bounds")


if __name__ == '__main__':
    app.run(debug=True)

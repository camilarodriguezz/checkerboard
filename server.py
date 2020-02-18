from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_checkerboard():
    return render_template("index8_8.html")

@app.route('/<x>/<y>')
def display_x_y(x,y):
    return render_template("index_x_y.html",rows=int(x), columns=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def display_own_color(x,y,color1,color2):
    return render_template("index_x_y.html",rows=int(x), columns=int(y), col1 = color1, col2 = color2)

@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
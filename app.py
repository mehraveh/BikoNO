from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.get("/")
def index():
    # main page to choose games
    return render_template("index.html")

@app.get("/games/bikono")
def bikono():
    return render_template("BicoNo.html")

@app.get("/games/bicochin")
def bicochin():
    return render_template("BicoChin.html")

@app.get("/games/choobico")
def choobico():
    return render_template("Choobico.html")
  

# --- PWA files (keep as you had) ---
@app.get("/sw.js")
def sw():
    return send_from_directory("static", "sw.js")

@app.get("/manifest.json")
def manifest():
    return send_from_directory("static", "manifest.json")

@app.get("/icon-192.png")
def icon192():
    return send_from_directory("static/icons", "icon-192.png")

@app.get("/icon-512.png")
def icon512():
    return send_from_directory("static/icons", "icon-512.png")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
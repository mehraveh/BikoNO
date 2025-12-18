from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

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
    print("Starting Bikono...")
    app.run(host="127.0.0.1", port=5000, debug=True)
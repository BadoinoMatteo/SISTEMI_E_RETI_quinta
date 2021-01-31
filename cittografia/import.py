from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "pagina iniziale"

@app.route("/pagina2/")
def index2():
    return "pagina secondaria"

if __name__ == '__main__':
    app.run(host="127.0.0.1")
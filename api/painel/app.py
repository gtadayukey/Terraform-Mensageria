from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # A mensagem está "hard-coded", mas você pode futuramente puxar do Kafka
    return render_template("index.html")

if __name__ == "__main__":
    # só usado se rodar python painel/app.py diretamente
    app.run(host="0.0.0.0", port=80)


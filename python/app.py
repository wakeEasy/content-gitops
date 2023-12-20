from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Azure DevOps! Today we are going to learn 1 lesson for GitOps!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

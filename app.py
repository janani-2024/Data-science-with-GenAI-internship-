from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    name=request.args.get('name')
    if not name:
        return "please enter a name"
    name_upper=name.upper() 
    return f"<i>Hello, <span style='color:blue;'>{name_upper}</span></i> 😊👋"

if __name__ == "__main__":
    app.run(debug=True)

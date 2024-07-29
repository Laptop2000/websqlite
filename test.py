from flask import Flask, render_template 

app=Flask(__name__)

@app.route("/abc")
def index():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)



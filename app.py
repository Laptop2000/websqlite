from flask import Flask, render_template,request
import connect as c
app=Flask(__name__)

@app.route("/abc")
def index():
    return render_template('home.html')


@app.route("/talk")
def select():
    name=request.args.get("t1")
    t=c.showweb(name)
    id,name,price=t
    return f"<h1>my product id is {id} name is {name} and price is {price}</h1>" 




if __name__=='__main__':
    app.run(debug=True)



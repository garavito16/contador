from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'para guardar visitas'

@app.route('/',methods=['GET'])
def panel_initial():
    if(len(session) == 0):
        session["visit"] = 1
        session["contador"] = 0
    else:
        session["visit"] = int(session["visit"]) + 1
    print(session["visit"])
    return render_template("index.html")

@app.route('/sumar',methods=['POST'])
def sum():
    return redirect("/")

@app.route('/destroy_session',methods=['GET'])
def destroy_session():
    session.clear()
    return redirect("/")

@app.route('/reset',methods=['POST'])
def reset_session():
    # session["visit"] = 0
    session.clear()
    return redirect("/")

@app.route('/add_two',methods=['POST'])
def add_two():
    session["visit"] = int(session["visit"]) + 1
    return redirect("/")

@app.route('/add_amount',methods=['POST'])
def add_amount():
    if request.form["cantidad"] == "":
        print("cantidad esta vacia")
    else:
        if(request.form["cantidad"].isdigit()):
            print("Solo se acepta numeros")
        else:
            session["contador"] = int(session["contador"]) + int(request.form["cantidad"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
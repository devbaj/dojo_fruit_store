from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():

    strawS = request.form["strawberry"]
    raspS = request.form["raspberry"]
    appleS = request.form["apple"]
    first_nameS = request.form["first_name"]
    last_nameS = request.form["last_name"]
    idS = request.form["student_id"]
    fruit_count = int(strawS) + int(raspS) + int(appleS)
    print("*"*30)
    print(f"Charging {first_nameS} {last_nameS} for {fruit_count} fruits")
    print("*"*30)
    return render_template("checkout.html", strawT=strawS, raspT=raspS, appleT=appleS, first_nameT=first_nameS, last_nameT=last_nameS, idT=idS)

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
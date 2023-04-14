from flask import Flask , request,render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template("home.html")

@app.route('/result',methods=['POST',"GET"])
def add_two_nuber():
    if request.method =='POST':
        num1 = request.form.get('fnumber')
        num2 = request.form.get('snumber')
        res = float(num1)+float(num2)
        return render_template('result.html',output=res)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
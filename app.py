from flask import Flask, request,render_template
from flask_cors import cross_origin
import pickle
import sklearn

app = Flask(__name__)
model = pickle.load(open('final_model.pkl','rb'))

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        rate_marriage = int(request.form['marriage'])
        age = int(request.form['age'])
        yrs_married = float(request.form['yrs_married'])
        children = float(request.form['children'])
        religious = int(request.form['religious'])
        education = int(request.form['education'])
        occupation = int(request.form['occupation'])
        husband_occ = int(request.form['husband_occ'])
        affair = float(request.form['affair'])
        prediction = model.predict([[rate_marriage,age,yrs_married,children,religious,education,occupation,husband_occ,affair]])
        print("Prediction: {}".format(prediction))
        if prediction[0] == 0:
            return render_template("home.html", prediction_text="Women is not having an Affair!!")
        else:
            return render_template("home.html", prediction_text="Women is having an Affair!!")

        # # return render_template("home.html", prediction_text="House Price is: ${:.2f}".format(100.45))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False,port=8080)
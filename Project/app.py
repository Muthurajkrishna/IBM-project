from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("water_quality.joblib")

@app.route("/")
def f():
    return render_template("index.html")

@app.route("/inspect")
def inspect():
    return render_template("inspect.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        var1 = float(request.form["pH_Value"])
        var2 = float(request.form["Hardness"])
        var3 = float(request.form["Solids"])
        var4 = float(request.form["Chloramines"])
        var5 = float(request.form["Sulfate"])
        var6 = float(request.form["Conductivity"])
        var7 = float(request.form["Organic_carbon"])
        var8 = float(request.form["Trihalomethanes"])
        var9 = float(request.form["Turbidity"])
        
        # Prepare input data
        input_data = np.array([[var1, var2, var3, var4, var5, var6, var7, var8, var9]])
        
        # Make predictions
        prediction = model.predict(input_data)
        
        if prediction == 0:
            return render_template('output.html', predict="Portable")
        else:
            return render_template('output.html', predict="Not Portable")
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

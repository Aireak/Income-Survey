from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["survey"]
collection = db["responses"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        age = request.form['age']
        gender = request.form['gender']
        income = request.form['income']
        expenses = {
            'utilities': request.form.get('utilities', 0),
            'entertainment': request.form.get('entertainment', 0),
            'school_fees': request.form.get('school_fees', 0),
            'shopping': request.form.get('shopping', 0),
            'healthcare': request.form.get('healthcare', 0),
        }
                    
         # Insert data into MongoDB
        collection.insert_one({'age': age, 'gender': gender, 'income': income, 'expenses': expenses})
        return redirect(url_for('index'))
# Retrieve data from MongoDB to display
    data = collection.find()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)




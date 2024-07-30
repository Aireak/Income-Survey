# Income-Survey
This project involves the development of a survey tool to collect participant data to analyze their income spending in preparation for a new product launch in the healthcare industry. 
# The project consists of the following components:

  ## 1. Web Development with Flask:
A simple webpage using Flask to collect user data.
  ## 2. Data Storage with MongoDB: 
Storing user details in MongoDB, including age, gender, total income, and expenses across various categories.
  ## 3. Data Processing with Python: 
Creating a Python class to loop through collected data, store it in a CSV file, and load it into a Jupyter notebook for analysis.
  ## 4. Data Visualization: 
Performing visualizations to show the ages with the highest income and gender distribution across spending categories. Exporting the charts for use in a PowerPoint presentation.

# FILE
├── app.py
├── templates
│   └── index.html
├── user.py
├── survey.response.csv
├── expense visuals.ipynb
├── README.md

# STEPS
1. Clone the repository

2. Install the required Python packages 

3. Install and configure MongoDB:
     - Start the MongoDB server.

## Running the Flask Application

1. Navigate to the project directory and run the Flask application:
   export FLASK_APP=app.py
   flask run
   
2. Open your web browser and go to http://127.0.0.1:5000/ to access the survey form.
3. Exported collected data from mongodb as csv
4. Load the CSV file into a Jupyter notebook for analysis
   - Open Expense visuals.ipynb in Jupyter notebook.
   - Run the cells to load data and generate visualizations.

## Data Visualization

The Jupyter notebook Expense visuals.ipynb includes the following visualizations:
1. Ages with the Highest Income
2. Gender Distribution across Spending Categories

The generated charts are saved as PNG files and can be used in a PowerPoint presentation.




import csv
import pandas as pd
class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses
   

    @staticmethod
    def save_to_csv(data, filename='user_data.csv'):
        keys = data[0].keys()
        with open(filename, 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

    @staticmethod
    def load_from_csv(filename='user_data.csv'):
        return pd.read_csv(filename) 


    # Retrieve data from MongoDB to display
users = list(collection.find())
user.save_to_csv(users)
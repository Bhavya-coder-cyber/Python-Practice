import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = 'weather.csv'

def graph():
    dates = []
    temp = []
    conditions = defaultdict(int)
    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dates.append(row['Date'])
            temp.append(float(row['Temperature']))
            conditions[row['Condition']] += 1

        if not dates or not temp:
            print("No data available to plot.")
            return

        plt.figure(figsize=(10, 7))
        plt.plot(dates, temp, marker='^') #To create a scatter plot
        plt.title('Temperature Over Time')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.tight_layout()
        plt.grid(True)
        plt.show() #Necessary to show the plot not required in jupyter notebook

        plt.figure(figsize=(7, 5))
        plt.bar(conditions.keys(), conditions.values(), color='green') #To create a bar chart
        plt.title('Weather Conditions')
        plt.xlabel('Conditions')
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

graph()

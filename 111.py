import pymongo
import csv
import matplotlib.pyplot as plt
import numpy as np

# create a MongoClient object and connect to the running MongoDB instance
client = pymongo.MongoClient()

# select a database
db = client['datas']

# select a collection
collection = db['train1']
data = collection.find({}, {'_id': 0, 'Weatherconditions': 1, 'Time_taken(min)': 1})

    # create lists for x and y axis data
x_data = []
y_data = []
for item in data:
    x_data.append(item['Weatherconditions'])
    y_data.append(item['Time_taken(min)'])

x = x_data.count("Snack ")
y = x_data.count("Meal ")
z = x_data.count("Buffet ")
a = x_data.count("Drinks ")
z1 = np.array([x, y, z, a])
x1 = ["Snack", "Meal", "Buffet", "Drinks"]
y1=[.2,.2,.2,.2]
plt.subplot(1,2,1)
plt.pie(z1, labels=x1, autopct='%.2f%%')
plt.subplot(1,2,2)
plt.pie(z1, labels=x1, autopct='%.2f%%')
#plt.axis('equal')
#plt.legend(title='Type of Order')
plt.show()



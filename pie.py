import pymongo
import matplotlib.pyplot as plt
import numpy as np


# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.datas
collection = db.train

# retrieve data from collection
data = collection.find({}, {'_id': 0,  'Type_of_order': 1})

# create lists for x and y axis data
x_data = []
for item in data:
    x_data.append(item['Type_of_order'])

# create bar chart
x=x_data.count("Snack ")
y=x_data.count("Meal ")
z=x_data.count("Buffet ")
a=x_data.count("Drinks ")

z1=np.array([x/1.5,y,z,a])
x1 = ["Snack", "Meal", "Buffet", "Drinks"]
plt.pie(z1, labels = x1,autopct='%.2f%%')
plt.axis('equal')
plt.legend()
plt.show()


import pymongo
import matplotlib.pyplot as plt


# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.datas
collection = db.train1

# retrieve data from collection
#data = collection.find({}, {'_id': 0, 'Weatherconditions': 1, 'Time_taken(min)': 1})

# create lists for x and y axis data
x_data = []
y_data = []
for item in data:
    x_data.append(item['Weatherconditions'])
    y_data.append(item['Time_taken(min)'])

# create bar chart
plt.bar(x_data, y_data, color='r')
plt.xlabel("Weatherconditions")
plt.ylabel("Time_taken(min)")
plt.show()


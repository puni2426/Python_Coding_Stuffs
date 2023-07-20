from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.aggregate([    { "$group": { "_id": "$Weatherconditions", "count": { "$sum": 1 } } }])

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(doc["_id"])
    y_axis.append(float(doc["count"]))

plt.bar(x_axis, y_axis)
plt.xlabel("Weatherconditions")
plt.ylabel("Number of Orders Delivered")
plt.title("Number of Orders Delivered with respect to Weatherconditions")
plt.show()



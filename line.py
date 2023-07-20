from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.aggregate([    { "$group": { "_id": "$Order_Date", "count": { "$sum": 1 } } },    { "$sort": { "_id": 1 } }])

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(doc["_id"])
    y_axis.append(doc["count"])

plt.plot(x_axis, y_axis)
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Orders by Date")
plt.show()


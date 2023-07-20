from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.aggregate([    { "$group": { "_id": "$Time_taken", "count": { "$sum": 1 } } }])

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(int(doc["_id"]))
    y_axis.append(float(doc["count"]))

plt.bar(x_axis, y_axis,width=1)
plt.xlabel("Time_taken")
plt.ylabel("Number of Orders Delivered")
plt.title("Number of Orders Delivered with respect to Time_taken")
plt.show()



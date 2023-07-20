from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.aggregate([    { "$group": { "_id": "$Delivery_person_Age", "count": { "$sum": 1 } } }])

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(float(doc["_id"]))
    y_axis.append(float(doc["count"]))

plt.bar(x_axis, y_axis,width=1)
plt.xlabel("Delivery_person_Age")
plt.ylabel("Count")
plt.title("Count by Delivery Person Age")
plt.show()



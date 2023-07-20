from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.train_123

result = orders.aggregate([    { "$group": { "_id": "$Delivery_person_Ratings", "avg_time": { "$avg": "$Time_taken(min)" } } }])

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(float(doc["_id"]))
    y_axis.append(float(doc["avg_time"]))

plt.bar(x_axis, y_axis)
plt.xlabel("Delivery Person Rating")
plt.ylabel("Average Time (min)")
plt.title("Average Delivery Time by Rating")
plt.show()


from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.train_123

result = orders.aggregate([    { "$group": { "_id": "$Type_of_order", "count": { "$sum": 1 } } }])

labels = []
sizes = []

for doc in result:
    labels.append(doc["_id"])
    sizes.append(doc["count"])

plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Orders by Type")
plt.axis("equal")
plt.legend()
plt.show()


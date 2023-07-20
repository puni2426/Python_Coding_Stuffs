from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.aggregate([    { "$group": { "_id": "$Time_taken", "count": { "$sum": 1 } } }])

labels = []
sizes = []

for doc in result:
    labels.append(doc["_id"])
    sizes.append(doc["count"])

plt.pie(sizes, labels=labels, autopct="%.1f%%", startangle=90)
plt.title("Road_traffic_density")
plt.axis("equal")
plt.show()


from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.train_123

result = orders.aggregate([    { "$group": { "_id": { "weather": "$Weatherconditions", "traffic": "$Road_traffic_density" }, "count": { "$sum": 1 } } }])

x_axis = []
y_axis = []
sizes = []

for doc in result:
    x_axis.append(doc["_id"]["traffic"])
    y_axis.append(doc["_id"]["weather"])
    sizes.append(doc["count"])

plt.scatter(x_axis, y_axis, s=sizes)
plt.ylabel("Weather Conditions")
plt.title("Orders by Weather and Traffic")
plt.show()


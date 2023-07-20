from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.find({}, { "_id": 0, "Delivery_location_longitude": 1, "Delivery_location_latitude": 1 })

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(float(doc["Delivery_location_longitude"]))
    y_axis.append(float(doc["Delivery_location_latitude"]))

plt.scatter(x_axis, y_axis)
plt.xlabel("Delivery Location Longitude")
plt.ylabel("Delivery Location Latitude")
plt.title("Order Locations")
plt.show()


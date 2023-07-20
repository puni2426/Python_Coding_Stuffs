from pymongo import MongoClient
import matplotlib.pyplot as plt

client = MongoClient()
db = client.datas
orders = db.trail1

result = orders.find({}, { "Time_taken(min)": 1, "Restaurant_latitude": 1, "Restaurant_longitude": 1 })

x_axis = []
y_axis = []

for doc in result:
    x_axis.append(doc["Restaurant_longitude"])
    y_axis.append(doc["Restaurant_latitude"])

plt.scatter(x_axis, y_axis, c=[t for t in doc["Time_taken(min)"]])
#plt.colorbar()
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Order Time by Restaurant Location")
plt.show()


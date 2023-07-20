import pymongo
import matplotlib.pyplot as plt

# Connect to the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["datas"]
collection = db["trail1"]

# Retrieve the data for the graphs
data = collection.find()

# Count the number of orders for each type
order_types = {}
for order in data:
    order_type = order["Type_of_order"]
    if order_type in order_types:
        order_types[order_type] += 1
    else:
        order_types[order_type] = 1

# Count the number of orders for each vehicle type
vehicle_types = {}
for order in data:
    vehicle_type = order["Type_of_vehicle"]
    if vehicle_type in vehicle_types:
        vehicle_types[vehicle_type] += 1
    else:
        vehicle_types[vehicle_type] = 1

# Count the time taken for each order in minutes
time_taken = []
for order in data:
    time_taken.append(order["Time_taken"])

# Create the plots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Create the pie chart for order types
axs[0].pie(order_types.values(), labels=order_types.keys())
axs[0].set_title("Order Types")

# Create the bar graph for vehicle types
axs[1].bar(vehicle_types.keys(), vehicle_types.values())
axs[1].set_title("Vehicle Types")

# Create the histogram for time taken
axs[2].hist(time_taken)
axs[2].set_title("Time Taken")

# Display the plots
plt.show()


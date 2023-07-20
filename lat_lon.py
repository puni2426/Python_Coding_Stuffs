import matplotlib.pyplot as plt
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["datas"]
orders = db["trail1"]

# Query the data
cursor = orders.find()

# Initialize empty lists
x_values = []
y_values = []
colors = []

# Iterate through each document in the cursor
for doc in cursor:
    # Check if the order is a snack
    if doc["Type_of_order"] == "Snack":
        # Iterate through each delivery person in the order
        for delivery_person in doc["Delivery_persons"]:
            # Check if the delivery person has a rating greater than 4.5
            if float(delivery_person["Delivery_person_Ratings"]) > 4.5:
                # Append the latitude and longitude values to the x and y value lists
                x_values.append(float(doc["Restaurant_longitude"]))
                y_values.append(float(doc["Restaurant_latitude"]))
                # Append a color value based on the delivery person's rating
                colors.append(float(delivery_person["Delivery_person_Ratings"]))

# Create the scatter plot
plt.scatter(x_values, y_values, c=colors)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Snack Orders by Restaurant Location and Delivery Person Rating")
plt.show()


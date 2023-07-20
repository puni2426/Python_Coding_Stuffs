# City with respect to traffic density
import pandas as pd
import matplotlib.pyplot as plt
import csv
import pymongo
import numpy as np

# create a MongoClient object and connect to the running MongoDB instance
client = pymongo.MongoClient()
# select a database
db = client['datas']
# select a collection
collection = db['train1']
with open('/home/ee212821/Downloads/Dataset1.csv') as f:
    # create a CSV reader object
    reader = csv.DictReader(f)
    # read the data from the file into a list of dictionaries
    data = [dict(row) for row in reader]
# insert the data into the collection
result = collection.insert_many(data)

# perform aggregation operation to calculate the average delivery person rating for each city and road traffic density
df = collection.aggregate([
    {"$group": {"_id": {"City": "$City", "Road_traffic_density": "$Road_traffic_density"}, "Delivery_person_Ratings":{'$avg':
     "$Delivery_person_Ratings"}}},
    {"$project": {"City": "$_id.City", "Road_traffic_density": "$_id.Road_traffic_density", "Delivery_person_Ratings": 1, "_id": 0}}
])
df = pd.DataFrame(list(df))

# print out data to check if aggregation operation returned results
print(df)

# create bar graph
df.pivot(index='City', columns='Road_traffic_density', values='Delivery_person_Ratings').plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Delivery person Ratings')
plt.title('Traffic Density with respect to City and Delivery Rating Achieved')
plt.legend(loc='upper right')
plt.savefig('BarG1.png')
plt.show()


# df = pd.read_csv('/home/ee212824/Downloads/train.csv')
'''df = pd.read_csv('Dataset1.csv')

df = df.groupby(['City', 'Road_traffic_density'])['Delivery_person_Ratings'].mean().reset_index()

df.pivot(index='City', columns='Road_traffic_density', values='Delivery_person_Ratings').plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Delivery person Ratings')
plt.title('Traffic Density with respect to City and Delivery Rating Achieved')
plt.legend(loc='upper right')
plt.savefig('Bar1.png')
plt.show()
'''

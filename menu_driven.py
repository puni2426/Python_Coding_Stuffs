import pymongo
import csv
import matplotlib.pyplot as plt
import numpy as np

# create a MongoClient object and connect to the running MongoDB instance
client = pymongo.MongoClient()

# select a database
db = client['datas']

# select a collection
collection = db['train_123']

# open the CSV file
def push_data():
    with open('/home/ee212821/Downloads/Dataset1.csv') as f:
        # create a CSV reader object
        reader = csv.DictReader(f)
        # read the data from the file into a list of dictionaries
        data = [dict(row) for row in reader]

    # insert the data into the collection
    result = collection.insert_many(data)
    # print(collection.count())

# print the object IDs of the inserted documents
# print(result.inserted_ids)
def bar_graph():
    data = collection.find({}, {'_id': 0, 'Delivery_person_Ratings': 1, 'City': 1,'Road_traffic_density':1})

    # create lists for x and y axis data
    x_data = []
    y_data = []
    for item in data:
        y_data.append(item['Delivery_person_Ratings'])
        x_data.append(item['Road_traffic_density'])
    City=["Urban ","Rural ","Semi-Urban",]
   df = pd.DataFrame({'Road_traffic_density': Road_traffic_density,
...                    'Delivery_person_Ratings': Delivery_person_Ratings}, City=City)
    plt.title("Road traffic density in different city")
    plt.xlabel("Road_traffic_density")
    plt.ylabel("Delivery_person_Ratings")
    #plt.savefig("bar_graph.png")
    ax = df.plot.bar(rot=0)
    ax.show()
    
def pie_chart():
    # retrieve data from collection
    data = collection.find({}, {'_id': 0, 'Type_of_order': 1})
    # create lists for x and y axis data
    x_data = []
    for item in data:
        x_data.append(item['Type_of_order'])
    # create bar chart
    x = x_data.count("Snack ")
    y = x_data.count("Meal ")
    z = x_data.count("Buffet ")
    a = x_data.count("Drinks ")
    z1 = np.array([x / 1.5, y, z, a])
    x1 = ["Snack", "Meal", "Buffet", "Drinks"]
    y1=[.2,.2,.2,.2]
    plt.pie(z1, labels=x1, autopct='%.2f%%')
    plt.axis('equal')
    plt.legend(title='Type of Order')
    #plt.savefig("pie_chart.png")
    plt.show()
def histogram():
    data = collection.find({}, {'_id': 0, 'Delivery_person_Ratings': 1})
    # create lists for x and y axis data
    x_data = []
    for item in data:
        x_data.append(item['Delivery_person_Ratings'])
    plt.hist(x_data)
    plt.title("Delivery_person_Ratings")
    #plt.savefig("hist.png")
    plt.show()

print("-------------------------Welcome to Geo Coding------------------------")
while(1):
    print("1.Push Data\n2.Bar Graph\n3.Pie Chart\n4.Histogram\n0.Exit")
    ch=int(input("Enter your choice\n"))
    if ch==1:
        push_data()
    elif ch==2:
        bar_graph()
    elif ch==3:
        pie_chart()
    elif ch==4:
        histogram()
    elif ch==0:
        exit("Thank You!!!")

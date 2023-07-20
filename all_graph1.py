import pymongo
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Connect to MongoDB server and retrieve data
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['datas']
collection = db['trail1']
data = pd.DataFrame(list(collection.find()))

# Create a pie chart of delivery person ratings
ratings_count = data['Delivery_person_Ratings'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(ratings_count.values, labels=ratings_count.index, autopct='%1.1f%%')
ax1.set_title('Delivery Person Ratings')

# Create a bar chart of delivery person age
age_count = data['Delivery_person_Age'].value_counts()
fig2, ax2 = plt.subplots()
ax2.bar(age_count.index, age_count.values)
ax2.set_title('Delivery Person Age')

# Create a histogram of time taken for delivery
fig3, ax3 = plt.subplots()
ax3.hist(data['Time_taken'], bins=10)
ax3.set_title('Time Taken for Delivery')

# Display the graphs in Streamlit
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)


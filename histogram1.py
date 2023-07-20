# group the data based on the "Time_taken" field and count the occurrences
pipeline = [
    {"$group": {"_id": "$Time_taken", "count": {"$sum": 1}}}
]
result = list(collection.aggregate(pipeline))

# create a list of counts and a list of corresponding values
counts = [r["count"] for r in result]
values = [r["_id"] for r in result]

# plot the histogram using matplotlib
plt.hist(values, weights=counts, bins=20)
plt.xlabel("Time Taken")
plt.ylabel("Count")
plt.title("Delivery Time Histogram")
plt.show()

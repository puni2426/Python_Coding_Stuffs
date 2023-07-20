data = collection.find({}, {'_id': 0, 'Weatherconditions': 1, 'Road_traffic_density': 1})

    # create lists for x and y axis data
    x_data = []
    y_data = []
    for item in data:
        x_data.append(item['Weatherconditions'])
        y_data.append(item['Road_traffic_density'])
    # create bar chart
    plt.bar(y_data, x_data)
    plt.title("Road traffic density in different weather condition")
    plt.ylabel("Weatherconditions")
    plt.xlabel("Road_traffic_density")
    #plt.savefig("bar_graph.png")
    plt.show()

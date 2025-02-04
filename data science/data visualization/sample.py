import matplotlib.pyplot as plt

# #Basic Plot
# x = [1,2,3,4]   
# y = [10,20,25,100]

# plt.plot(x,y)
# plt.show()

#Line Plot
plt.plot([1,2,3], [10,20,30], label="Trend", color="brown", linestyle="--", marker="x")
plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

# # Bar Chart
# categories = ["A", "B", "C"]
# values = [10,15,100]
# plt.bar(categories,values, color="blue")
# plt.title("Bar Chart")
# plt.show()

# # Histogram
# data = [1,2,3,5,6,5,4,4,3,3]
# plt.hist(data, bins=4, color="green", edgecolor="black")
# plt.title("histogram")
# plt.show()

# Scatter Plot
# x = [1,2,3,4,5]
# y = [10,20,25,30,45]
# plt.scatter(x,y, color="red")
# plt.title("Scatter")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.legend(["Dataaset 1 "])
# plt.show()
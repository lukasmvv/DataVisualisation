import matplotlib.pyplot as plt

max = 100

input_values = list(range(1, 100 + 1))
squares = [x**2 for x in input_values]

# This scatter plot uses a color map to color each individual point according to value
# c="red" will make all points red
# c=(0, 0, 0.8) will be light blue; rg values between 0 and 1
plt.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues,  edgecolor="none", s=4)

# Set chart title and label axes
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis="both", which="major", labelsize="14")

# Set the range for each axis
plt.axis([0, 1.1*max, 0, (1.1*max)**2])

# Save image
plt.savefig("squares_scatter_plot.png", bbox_inches="tight")
plt.show()
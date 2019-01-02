import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Adjust output window
    plt.figure(figsize=(10, 6))  # tuple dimension in inches

    # List for color map
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="None", s=15)

    # Emphasize first and last
    plt.scatter(0, 0, c="green", edgecolor="None", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="None", s=100)

    # Remove axes
    ax = plt.axes()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    msg = input("Do you want to quit? (y/n): ")
    if msg == "y":
        break
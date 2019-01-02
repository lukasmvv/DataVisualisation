import pygal
from die import Die

rolls = 10000

# Create dice
die_1 = Die()
die_2 = Die()

# Make some rolls and add to results
results = []
for roll_num in range(rolls):
    results.append(die_1.roll() + die_2.roll())

max_result = die_1.num_sides + die_2.num_sides

# Analyze results
frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize results

# Bar chart
hist = pygal.Bar()

# Chart properties
hist.title = "Results of rolling two D6 " + str(rolls) + " times"
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist_x_title = "Result"
hist._y_title = "Frequency of Result"

# Adding data to histogram
hist.add("D6 + D6", frequencies)

# Render file as svg vector file
hist.render_to_file("die_visual.svg")


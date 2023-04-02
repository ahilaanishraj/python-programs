import matplotlib.pyplot as plt
# Define some data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the data on the axis
ax.plot(x, y)

# Add labels to the chart
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_title('My Chart')

# Display the chart
plt.show()

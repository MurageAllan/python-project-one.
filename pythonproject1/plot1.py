import matplotlib.pyplot as plt
activities = ['Eat', 'Sleep', 'Work', 'Play', 'Leisure']

# portion covered by each label
slices = [3, 7, 8, 6, 8]

# color for each label
colors = ['r', 'y', 'g', 'b', 'c']

# Plotting the pie chart
plt.pie(slices, labels = activities, colors = colors, startangle=90, shadow=False, explode=(0, 0, 0, 0, 0), radius=1.2,
       autopct='%1.1f%%' )
plt.title("Matplotlib charts")
plt.legend()
plt.show()
#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Library Problems

# In[4]:


pip install matplotlib


# In[38]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# 1. Write a Python program to draw a line with suitable label in the x axis, y axis and a title

# In[6]:


X = range(1, 50)
Y = [value * 3 for value in X]
print("Values of X:")
print(*range(1,50)) 
print("Values of Y (thrice of X):")
print(Y)
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
# Display the figure.
plt.show()


# 2. Write a Python program to draw a line using given axis values with suitable label in the x axis
# , y axis and a title

# In[7]:


x = [1,2,3]
y = [2,4,1]

plt.plot(x, y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Sample graph!')

plt.show()


# 3. Write a Python program to draw a line using given axis values taken from a text file, with
# suitable label in the x axis, y axis and a title.
# Test Data:
# test.txt
# 1 2
# 2 4
# 3 1

# In[102]:


import matplotlib.pyplot as plt
with open("data.txt") as f:
    data = f.read()
data = data.split('\n')
x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Sample graph!')

plt.show()


# 4. Write a Python program to draw line charts of the financial data of Alphabet Inc. between
# October 3, 2016 to October 7, 2016.
# Sample Financial data (fdata.csv):
# Date,Open,High,Low,Close
# 03-10-16,774.25,776.065002,769.5,772.559998
# 04-10-16,776.030029,778.710022,772.890015,776.429993
# 05-10-16,779.309998,782.070007,775.650024,776.469971
# 06-10-16,779,780.47998,775.539978,776.859985
# 07-10-16,779.659973,779.659973,770.75,775.080017
# 

# In[42]:


import pandas as pd
df = pd.read_csv('fdata.csv', sep=',', parse_dates=True, index_col=0)
df.plot()
plt.show()


# 5. Write a Python program to plot two or more lines on same plot with suitable legends of each
# line.

# In[46]:


x1 = [10,20,30]
y1 = [20,40,10]
# plotting the line 1 points 
plt.plot(x1, y1, label = "line 1")
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]
# plotting the line 2 points 
plt.plot(x2, y2, label = "line 2")
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends ')
# show a legend on the plot
plt.legend()
plt.show()


# 6. Write a Python program to plot two or more lines with legends, different widths and colors.

# In[49]:


# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Two or more lines with different widths and colors with suitable legends ')
# Display the figure.
plt.plot(x1,y1, color='yellow', linewidth = 3,  label = 'line1-width-3')
plt.plot(x2,y2, color='pink', linewidth = 5,  label = 'line2-width-5')
# show a legend on the plot
plt.legend()
plt.show()


# 7. Write a Python program to plot two or more lines with different styles

# In[52]:


# line 1 points
x1 = [10,20,30]
y1 = [20,40,10]
# line 2 points
x2 = [10,20,30]
y2 = [40,10,30]

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.plot(x1,y1, color='blue', linewidth = 3,  label = 'line1-dotted',linestyle='dotted')
plt.plot(x2,y2, color='green', linewidth = 4,  label = 'line2-dashed', linestyle='dashed')

plt.title("Plot with two or more lines with different styles")

plt.legend()

plt.show()


# 8. Write a Python program to plot two or more lines and set the line markers.

# In[57]:


x = [1,4,5,6,7]

y = [2,6,3,6,3]

# plotting the points 
plt.plot(x, y, color='yellow', linestyle='dashdot', linewidth = 3,
         marker='>', markerfacecolor='blue', markersize=12)

#Set the y-limits of the current axes.
plt.ylim(1,8)

#Set the x-limits of the current axes.
plt.xlim(1,8)

plt.xlabel('x - axis')

plt.ylabel('y - axis')

plt.title('Display marker')

plt.show()


# 9. Write a Python program to display the current axis limits values and set new axis values

# In[58]:


X = range(1, 50)
Y = [value * 3 for value in X]
plt.plot(X, Y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Draw a line.')
# shows the current axis limits values
print(plt.axis()) 

# set new axes limits
# Limit of x axis 0 to 100 & Limit of y axis 0 to 200
plt.axis([0, 100, 0, 200]) 
# Display the figure.
plt.show()


# 10. Write a Python program to plot quantities which have an x and y position.

# In[59]:


import pylab as pl

# Make an array of x values
x1 = [2, 3, 5, 6, 8]
# Make an array of y values for each x value
y1 = [1, 5, 10, 18, 20]

# Make an array of x values
x2 = [3, 4, 6, 7, 9]
# Make an array of y values for each x value
y2 = [2, 6, 11, 20, 22]

# set new axes limits
pl.axis([0, 10, 0, 30]) 

# use pylab to plot x and y as red circles
pl.plot(x1, y1,'b*', x2, y2, 'ro')
# show the plot on the screen
pl.show()


# 11. Write a Python program to plot several lines with different format styles in one command
# using arrays.

# In[61]:


# Sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# green dashes, blue squares and red triangles
plt.plot(t, t, 'g--', t, t**2, 'ys', t, t**3, 'r^')
plt.show()


# 12. Write a Python program to create multiple types of charts

# In[63]:


import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)

# Plot the data as a red line with round markers
graph.plot(x,y,'g-o')

# Set the xtick locations
graph.set_xticks(x)

# Set the xtick labels
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )
plt.show()


# 13. Write a Python program to display the grid and draw line charts of the closing value of
# Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with
# linestyle -, width .5. and color blue.
# Date,Close
# 03-10-16,772.559998
# 04-10-16,776.429993
# 05-10-16,776.469971
# 06-10-16,776.859985
# 07-10-16,775.080017

# In[64]:


import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)

# Plot the data as a red line with round markers
graph.plot(x,y,'r-o')

# Set the xtick locations
graph.set_xticks(x)

# Set the xtick labels
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Closing Value')
 # giving a title  
plt.title('Closing stock value of Alphabet Inc.') 
# Customize the grid
plt.grid(linestyle='-', linewidth='0.5', color='blue')
plt.show()


# 14. Write a Python program to display the grid and draw line charts of the closing value of
# Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with
# rendering with a larger grid (major grid) and a smaller grid (minor grid).Turn on the grid but turn
# off ticks.

# In[65]:


import datetime as DT
from matplotlib import pyplot as plt
from matplotlib.dates import date2num

data = [(DT.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (DT.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (DT.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (DT.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (DT.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017 )]

x = [date2num(date) for (date, value) in data]
y = [value for (date, value) in data]

fig = plt.figure()

graph = fig.add_subplot(111)

# Plot the data as a red line with round markers
graph.plot(x,y,'r-o')

# Set the xtick locations
graph.set_xticks(x)

# Set the xtick labels
graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
        )

# naming the x axis
plt.xlabel('Date')
# naming the y axis
plt.ylabel('Closing Value')
# giving a title  
plt.title('Closing stock value of Alphabet Inc.') 
# Turn on the minor TICKS, which are required for the minor GRID
plt.minorticks_on()

# Customize the major grid
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

# Turn off the display of all ticks.
plt.tick_params(which='both', # Options for both major and minor ticks
                top='off', # turn off top ticks
                left='off', # turn off left ticks
                right='off',  # turn off right ticks
                bottom='off') # turn off bottom ticks
plt.show()


# 15. Write a Python program to create multiple plots.

# In[66]:


import matplotlib.pyplot as plt
fig = plt.figure()
fig.subplots_adjust(bottom=0.020, left=0.020, top = 0.900, right=0.800)

plt.subplot(2, 1, 1)
plt.xticks(()), plt.yticks(())

plt.subplot(2, 3, 4)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 5)
plt.xticks(())
plt.yticks(())

plt.subplot(2, 3, 6)
plt.xticks(())
plt.yticks(())

plt.show()


# # Matplotlib Barchart

# 1. Write a Python programming to display a bar chart of the popularity of programming
# Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# In[67]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 2. Write a Python programming to display a horizontal bar chart of the popularity of
# programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# In[68]:


x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.barh(x_pos, popularity, color='green')
plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.yticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 3. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Use uniform color.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# 

# In[69]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 4. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Use different color for each bar.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# 

# In[71]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=['red', 'yellow', 'green', 'blue', 'black', 'cyan'])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 5. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Attach a text label above each bar displaying its popularity (float value).
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# In[74]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

fig, ax = plt.subplots()
rects1 = ax.bar(x_pos, popularity, color='c')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%f' % float(height),
        ha='center', va='bottom')
autolabel(rects1)

plt.show()


# 6. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Make blue border to each bar
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# 

# In[78]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0), edgecolor='blue')

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 7. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Specify the position of each bar plot.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# In[81]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Select the position of each barplots on the x-axis (space=1,3,3,2,1)
y_pos = [0,1,3,5,7,9]
# Create bars
plt.bar(y_pos, popularity)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 8. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Select the width of each bar and their positions.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# In[82]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
plt.xticks(x_pos, x)
# Select the width of each bar and their positions
width = [0.1,0.2,0.5,1.1,0.2,0.3]
y_pos = [0,.8,1.5,3,5,6]

# Create bars
plt.bar(y_pos, popularity, width=width)
plt.xticks(y_pos, x)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 9. Write a Python programming to display a bar chart of the popularity of programming
# Languages. Increase bottom margin.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

# In[83]:


x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color=(0.4, 0.6, 0.8, 1.0))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
# Rotation of the bars names
plt.xticks(x_pos, x, rotation=90)
# Custom the subplot layout
plt.subplots_adjust(bottom=0.4, top=.8)
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
# Customize the minor grid
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 10. Write a Python program to create bar plot of scores by group and gender. Use multiple X
# values on the same chart for men and women.
# Sample Data:
# Means (men) = (22, 30, 35, 35, 26)
# Means (women) = (25, 32, 30, 35, 29)

# In[90]:


# data to plot
n_groups = 5
men_means = (22, 30, 33, 30, 26)
women_means = (25, 32, 30, 35, 29)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, men_means, bar_width,
alpha=opacity,
color='b',
label='Men')

rects2 = plt.bar(index + bar_width, women_means, bar_width,
alpha=opacity,
color='y',
label='Women')

plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()


# 11. Write a Python program to create bar plot from a DataFrame.
# Sample Data Frame:
# a b c d e
# 2 4,8,5,7,6
# 4 2,3,4,2,6
# 6 4,7,4,7,8
# 8 2,6,4,8,6
# 10 2,4,3,3,2

# In[92]:


from pandas import DataFrame

a=np.array([[4,8,5,7,6],[2,3,4,2,6],[4,7,4,7,8],[2,6,4,8,6],[2,4,3,3,2]])
df=DataFrame(a, columns=['a','b','c','d','e'], index=[2,4,6,8,10])

df.plot(kind='bar')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()


# 12. Write a Python program to create bar plots with error bars on the same figure. Sample Date
# Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
# Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645

# In[93]:


N = 5
menMeans = (54.74, 42.35, 67.37, 58.24, 30.25)
menStd = (4, 3, 4, 1, 5)
# the x locations for the groups
ind = np.arange(N)    
# the width of the bars
width = 0.35   
plt.bar(ind, menMeans, width, yerr=menStd, color='red')
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')
# Turn on the grid
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()


# 13. Write a Python program to create bar plots with errorbars on the same figure. Attach a text
# label above each bar displaying men means (integer value).
# Sample Data
# Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
# Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
# 

# In[95]:


import matplotlib.patches as mpatches

N = 5
men_means = (54.74, 42.35, 67.37, 58.24, 30.25)
men_std= (4, 3, 4, 1, 5)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)

# add some text for labels, title and axes ticks
plt.ylabel('Scores')
plt.xlabel('Velocity')
plt.title('Scores by Velocity')

red_patch = mpatches.Patch(color='red', label='Men')
plt.legend(handles=[red_patch])


def autolabel(rects):
    
    #Attach a text label above each bar displaying its height
    
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
       ha='center', va='bottom')
autolabel(rects1)
plt.show()


# # Matplotlib Piechart

# 1. Write a Python programming to create a pie chart of the popularity of programming
# Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# 

# In[96]:


languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# 2. Write a Python programming to create a pie chart with a title of the popularity of programming
# Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
# 

# In[98]:


# Plot data
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
#colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0, 0, 0)  
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
plt.show()


# 3. Write a Python programming to create a pie chart of gold medal achievements of five most
# successful countries in 2016 Summer Olympics. Read the data from a csv file.
# Sample data:
# medal.csv
# country,gold_medal
# United States,46
# Great Britain,27
# China,26
# Russia,19
# Germany,17

# In[101]:


df =  pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold_medal"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = (0.1, 0, 0, 0, 0)  
plt.pie(medal_data, labels=country_data, explode=explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()


# # Matplotlib Scatterplot

# 1. Write a Python program to draw a scatter graph taking a random distribution in X and Y and
# plotted against each other.

# In[111]:


from pylab import randn
X = randn(200)
Y = randn(200)
plt.scatter(X,Y, color='r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# 2. Write a Python program to draw a scatter plot with empty circles taking a random distribution
# in X and Y and plotted against each other.

# In[112]:


x = np.random.randn(50) 
y = np.random.randn(50)
plt.scatter(x, y, s=70, facecolors='none', edgecolors='g')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# 3. Write a Python program to draw a scatter plot using random distributions to generate balls of
# different sizes.

# In[113]:


import math
import random

# create random data
no_of_balls = 25
x = [random.triangular() for i in range(no_of_balls)]
y = [random.gauss(0.5, 0.25) for i in range(no_of_balls)]
colors = [random.randint(1, 4) for i in range(no_of_balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range(no_of_balls)]
# draw the plot
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# 4. Write a Python program to draw a scatter plot comparing two subject marks of Mathematics
# and Science. Use marks of 10 students.
# Test Data:
# math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
# science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
# marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# In[114]:


math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label='Math marks', color='r')
plt.scatter(marks_range, science_marks, label='Science marks', color='g')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()


# 5. Write a Python program to draw a scatter plot for three different groups camparing weights
# and heights.

# In[122]:


weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9] 

weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1] 

weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]

weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))

plt.scatter(weight, height, marker='*', color=['red','green','blue'])
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('Group wise Weight vs Height scatter plot',fontsize=20)
plt.show()


# In[ ]:





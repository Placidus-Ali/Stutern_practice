#import matplotlib and pyplot
from turtle import color
import matplotlib
from matplotlib import pyplot as plt

# plot a base line graph

# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# plt.plot(x,y)
# plt.show()

#plot the following point in a graph (1,2),(4,6),(3,2),(5,1)
# get x and y values from the coordinates

# x = [1,4,3,5]
# y = [2,6,2,1]

# plt.plot(x,y)
# plt.show()

#ploting multiple lines on the same axes
days = [0,1,2,3,4,5,6]
mariam_allowance = [25,30,40,50,60,70,80]
Chinenye_allowance = [5,10,15,20,25,30,35]
# plt.plot(days, mariam_allowance)
# plt.plot(days, Chinenye_allowance)
# plt.show()

# let's customize the lines
plt.plot(days, mariam_allowance, linestyle = ':', color = 'red', marker = 'o' )
plt.plot(days, Chinenye_allowance, linestyle = '--', color = 'black', marker = '.' )
# plt.show()

# labelling the axes
plt.xlabel('Days of the week')
plt.ylabel('Allowance(in dollars)')
plt.title('Daily Allowance Graph')
plt.show()


#importing items
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

#loading the file and reading the list
df=pd.read_csv("data.csv")
data=df["Math_score"].tolist()

#finding mean of 100 data points 1000 times
#function to get mean ofgiven data samples
#pass the no.of data points u want as a counter
def random_set_of_mean(counter):
  dataSet=[]
  for i in range(0,counter):
    random_index=random.randint(0,len(data)-1)
    value=data[random_index]
    dataSet.append(value)

  mean=statistics.mean(dataSet)
  return mean

#pass no.of time u want mean of the data points as a parameter in range function in for loop
mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

#finding mean and std_dev
mean=statistics.mean(mean_list)
std_dev=statistics.stdev(mean_list)

#finding 1 std deviation start and end values, 2 std deviation start and end values
first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)

#printing the findings
print("mean of sampling dis -> ",mean)
print("std_dev of sampling dis -> ",std_dev)
print("std_dev 1 -> ",first_std_dev_start, first_std_dev_end)
print("std_dev 2 -> ",second_std_dev_start, second_std_dev_end)
print("std_dev 3 -> ",third_std_dev_start, third_std_dev_end)

#ploting the graph
fig=ff.create_distplot([data],["math scores"],show_hist=False)
fig.show()

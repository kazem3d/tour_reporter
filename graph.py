import matplotlib.pyplot as plt 
import csv
from gurd import similar

name=''
date=''
left=[]
height=[]

with open('report/report_duration_tour.csv',encoding="utf_8") as f:
    csv_reader = csv.reader(f, delimiter=',')

    line_count = 0
    

    for row in csv_reader:
        if line_count > 0 and line_count%2 == 0:
            
            name=row[0]
            print(name)
            name=similar(name)
            print(name)

            name=name[::-1]
            data=float(row[1])
            left.append(name)
            height.append(data)
        line_count+=1
print(left)
print(height)



# # x-coordinates of left sides of bars 
# left = ['ee1', 'w2', '3', '4', '5'] 

# # heights of bars 
# height = [10, 24, 36, 40, 5] 

# labels for bars 
# tick_label = ['one', 'two', 'three', 'four', 'five'] 
tick_label=left

# plotting a bar chart 
plt.bar(left, height,tick_label=tick_label,width = 0.8, color = ['green']) 

# naming the x-axis 
plt.xlabel('name') 
# naming the y-axis 
plt.ylabel('minute') 
# plot title 
plt.title('Tour report') 



# function to show the plot 
plt.show() 

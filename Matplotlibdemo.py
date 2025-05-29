import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
y = [2,3,8,5,1]
x = ["p1","p2","p3","p4","p5"]
colors = ["green","black","red","orange","blue"]
#plt.bar(x,y,color = colors)
#plt.show()

plt.plot(y,x,marker="*")
y = np.random.randint(1,100,24)
x = np.random.randint(10,100,24)
#plt.scatter(x,y)
#plt.show()

brands = ["oneplus","nokia","apple","redmi","samsung"]
X = [30,20,10,35,45]
c = ["green","red","yellow","blue","orange"]
ex = [0,0,0,0,0.1]
#plt.pie(X,labels=brands,colors=c,explode=ex,shadow=True)
#plt.boxplot(X)
#plt.show()

days = [1,2,3,4,5,6,7]
#plt.hist(x, bins = 20)
#plt.stem(x)
#plt.show()

NOP1 =[8,10,12,13,14,15,18]
NOP2 =[9,11,13,14,15,16,19]
NOP3 =[10,12,14,15,17,19,21]

#The stackplot function in Matplotlib is used to create a stacked area plot,
# which visualizes how multiple datasets contribute to a cumulative total over a shared axis, typically time.
# It is useful for showing how different components change over time and their total sum.

#plt.stackplot(days,NOP1,NOP2,NOP3)
#plt.step(days,NOP1)
#plt.figure(figsize=[5,3])
#plt.plot(days,NOP1,label = "Test1")
#plt.plot(days,NOP2,label = "Test2")
#plt.legend(loc = 2)
#plt.show()
#plt.subplot(1,2,1)
#plt.title("Days")
#plt.plot(days,NOP1)

days = [1,2,3,4,5,6,7]
NOP2 =[9,11,13,14,15,16,19]
#plt.subplot(1,2,2)
#plt.title("Days1")
#plt.plot(days,NOP2)
#plt.suptitle("Data")
#plt.show()
#plt.savefig("Data.png")

#The sns.lineplot function in Seaborn is used to create line charts,
# which are helpful for visualizing trends over time or across continuous variables. It can show the relationship between two or more variables,
# including the possibility of adding semantic groupings using parameters such as hue, size, and style.
#data = {
    #"Days" : [1,3,5,7,9],
    #"NOP" : [10,9,14,44,30],
    #"Gender" : ["Girl","Boy","Girl","Boy","Girl"]
#}
#df = pd.DataFrame(data)
#color = sns.color_palette("pastel")
#sns.lineplot(data = data , x = "Days", y = "NOP", hue = "Gender",palette = color)
#plt.show()

data = sns.load_dataset("tips")
#print(data)
#sns.barplot(data = data, x = "day", y = "tip", hue = "sex", palette = "pastel")
#plt.show()
#data = sns.load_dataset("titanic")
#sns.histplot(data = data, x = "age", hue = "sex" , palette="pastel" , kde = True)
#plt.show()
#sns.scatterplot(data = data, x = "total_bill", y = "tip", hue="time")
#plt.show()
#data = sns.load_dataset("flights")
#gp = data.groupby("month").agg({"passengers" : "max"})
#sns.heatmap(gp)
#plt.show()
#data = sns.load_dataset("tips")
#sns.countplot(data = data, x = "day")
#plt.show()
#sns.violinplot(data = data, x = "day")
#sns.pairplot(data,hue="day")

#sns.set_style(style="whitegrid")
#sns.barplot(x="day", y = "tip", data = data)

#a = sns.FacetGrid(data, col="smoker", height=2)
#a.map(sns.scatterplot, "day","tip")
#a.map(sns.barplot, "day","tip")
#sns.relplot is a figure-level function in the Seaborn
# library used for visualizing statistical relationships
#sns.relplot(data= data, x = "tip", y = "total_bill", hue = "sex", col = "day")
#plt.show()
#kdeplot provides a way to visualize the distribution of data,
#similar to a histogram, but with a smoothed curve instead of bars.
#sns.kdeplot(data= data, x = "total_bill", hue = "day", multiple="stack")
iris = sns.load_dataset("iris")
sns.kdeplot(data=iris)
plt.show()



import pandas as pd
import matplotlib.pyplot as mp

data={"No_of_People":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],
      "Age":[23,34,54,45,65,77,53,21,33,67,87,55,57,32,46,35,66,31,41,34,18,29,62,53,64,44,54,56,68,88],
      "Gender":["Male","Male","Female","Male","Female","Female","Male","Male","Female","Female","Female","Male","Male","Male","Female","Male","Male","Male","Male","Male","Female","Female","Female","Male","Male","Male","Female","Male","Male","Male"]}

Dic=pd.DataFrame(data)


Totel_Gender=Dic["Gender"].value_counts()
mp.bar(Totel_Gender.index,Totel_Gender.values, color=["blue","y"],width=0.3)
mp.xlabel("Gender")
mp.ylabel("No of People")
mp.title("Gender Distribution in Population")
mp.show()


mp.hist(Dic["Age"],bins=5,color="red",edgecolor="black")
mp.xlabel("Age")
mp.ylabel("Number of People")
mp.title("Age Distribution in Population")
mp.show()
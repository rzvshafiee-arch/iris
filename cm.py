import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
import seaborn as sns
import  matplotlib.pyplot  as plt 
from sklearn.metrics import accuracy_score
from sklearn.metrics import  precision_score




data=pd.read_excel("test.xlsx")

predictions=data["prediction"].values
truth=data["Species"].values

cm=confusion_matrix(truth,predictions,labels=["versicolor","virginica","setosa"])

plt.figure(figsize=(5,5))
sns.heatmap(cm,annot=True,xticklabels=["versicolor","virginica","setosa"],yticklabels=["versicolor","virginica","setosa"],fmt="d")


print( accuracy_score(truth,predictions))

print(precision_score(truth, predictions, average=None,
                      labels=["versicolor", "virginica", "setosa"]))

#print(classification_report(truth,predictions))

plt.show()
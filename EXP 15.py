from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.metrics import accuracy_score

data = pd.read_csv("iris_15.csv")

X = data.iloc[:,0:4]
y = data.iloc[:,4]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

model = GaussianNB()
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("Predictions:",pred)
print("Accuracy:",accuracy_score(y_test,pred))

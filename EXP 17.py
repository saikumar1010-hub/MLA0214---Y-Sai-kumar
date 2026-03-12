import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("mobile_price_17.csv")

X = data[['RAM','Storage','Battery']]
y = data['Price']

model = LinearRegression()
model.fit(X,y)

ram=int(input("RAM: "))
storage=int(input("Storage: "))
battery=int(input("Battery: "))

pred=model.predict([[ram,storage,battery]])

print("Predicted Mobile Price:",pred[0])

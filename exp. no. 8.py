import csv

X = []
Y = []

# paste your CSV file path here
file_path = "C:/Users/ymala/OneDrive/Desktop/MLA0214/linear regression.csv"

with open(file_path, 'r') as file:
    data = csv.reader(file)
    next(data)   # skip header
    
    for row in data:
        X.append(float(row[0]))
        Y.append(float(row[1]))

n = len(X)

sum_x = sum(X)
sum_y = sum(Y)
sum_xy = sum(X[i]*Y[i] for i in range(n))
sum_x2 = sum(x*x for x in X)

# slope and intercept
m = (n*sum_xy - sum_x*sum_y) / (n*sum_x2 - sum_x**2)
b = (sum_y - m*sum_x) / n

print("Slope:", m)
print("Intercept:", b)

# prediction
x = 6
y = m*x + b
print("Predicted value:", y)

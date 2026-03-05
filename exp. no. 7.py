import math

# sigmoid function
def sigmoid(x):
    return 1/(1+math.exp(-x))

# simple dataset
X = [1,2,3,4,5]
y = [0,0,0,1,1]

w = 0
b = 0
lr = 0.1

# training
for i in range(1000):
    for j in range(len(X)):
        z = w*X[j] + b
        pred = sigmoid(z)
        error = y[j] - pred
        
        w = w + lr * error * X[j]
        b = b + lr * error

# prediction
x_test = 6
result = sigmoid(w*x_test + b)

print("Probability:", result)

if result > 0.5:
    print("Class: 1")
else:
    print("Class: 0")

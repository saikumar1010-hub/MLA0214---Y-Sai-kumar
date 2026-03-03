import csv
import math
from collections import Counter

def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data

def entropy(data):
    labels = [row[-1] for row in data]
    total = len(labels)
    counts = Counter(labels)
    ent = 0
    for count in counts.values():
        p = count / total
        ent -= p * math.log2(p)
    return ent

def info_gain(data, attr_index):
    total_entropy = entropy(data)
    values = set(row[attr_index] for row in data)
    weighted_entropy = 0
    
    for value in values:
        subset = [row for row in data if row[attr_index] == value]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    
    return total_entropy - weighted_entropy

def id3(data, attrs):
    labels = [row[-1] for row in data]
    
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    
    if not attrs:
        return Counter(labels).most_common(1)[0][0]
    
    gains = [info_gain(data, i) for i in range(len(attrs))]
    best_index = gains.index(max(gains))
    best_attr = attrs[best_index]
    
    tree = {best_attr: {}}
    values = set(row[best_index] for row in data)
    
    for value in values:
        subset = [row[:best_index] + row[best_index+1:] 
                  for row in data if row[best_index] == value]
        
        new_attrs = attrs[:best_index] + attrs[best_index+1:]
        tree[best_attr][value] = id3(subset, new_attrs)
    
    return tree


data = load_data(r"C:\Users\WELCOME\Downloads\id3_data.csv")

attributes = data[0][:-1]
training_data = data[1:]

tree = id3(training_data, attributes)

print("Decision Tree:")
print(tree)


# Classify New Sample
new_sample = ['Sunny','Cool','High','Strong']

def classify(tree, sample, attrs):
    if type(tree) != dict:
        return tree
    
    root = next(iter(tree))
    index = attrs.index(root)
    value = sample[index]
    
    subtree = tree[root][value]
    
    new_attrs = attrs[:index] + attrs[index+1:]
    new_sample = sample[:index] + sample[index+1:]
    
    return classify(subtree, new_sample, new_attrs)

result = classify(tree, new_sample, attributes)

print("\nNew Sample:", new_sample)
print("Classification:", result)

import csv

def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data

def candidate_elimination(data):

    num_attr = len(data[0]) - 1
    S = None   # Initialize safely
    G = [['?'] * num_attr]

    # Find first positive example
    for row in data[1:]:
        if row[-1].strip() == "Yes":
            S = row[:-1]
            break

    if S is None:
        print("ERROR: No positive example found in dataset.")
        return None, None

    for row in data[1:]:

        if row[-1].strip() == "Yes":

            for i in range(num_attr):
                if S[i] != row[i]:
                    S[i] = '?'

            G = [g for g in G if all(
                g[i] == '?' or g[i] == S[i]
                for i in range(num_attr)
            )]

        else:

            new_G = []

            for g in G:
                for i in range(num_attr):

                    if g[i] == '?':
                        if row[i] != S[i]:
                            new_h = g.copy()
                            new_h[i] = S[i]
                            new_G.append(new_h)

            G = new_G

    return S, G


data = load_data(r"C:\Users\WELCOME\Downloads\enjoysport.csv")

S, G = candidate_elimination(data)

if S:
    print("Final Specific Hypothesis (S):")
    print(S)

    print("\nFinal General Hypothesis (G):")
    for g in G:
        print(g)

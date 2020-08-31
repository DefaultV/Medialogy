import numpy as np
import csv


gender = [] #0
race = [] #1
parental = [] #2
lunch = [] #3
test_prep = [] #4
math_score = [] #5
read_score = [] #6
write_score = [] #7

gender_dict = ["female", "male"]
test_prep_dict = ["none", "completed"]

with open('StudentsPerformance.csv') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        gender.append(row[0])
        if not row[0] in gender_dict:
            gender_dict.append(row[0])
        race.append(row[1])
        parental.append(row[2])
        lunch.append(row[3])
        test_prep.append(row[4])
        if not row[4] in test_prep_dict:
            test_prep_dict.append(row[4])
        math_score.append(row[5])
        read_score.append(row[6])
        write_score.append(row[7])

def parent_dec(arg):
    return (
            arg == "bachelor's degree"
            or arg == "master's degree"
            or arg == "associate's degree")

def gender_dec(arg):
    return arg=="female"

def score_dec(arg):
    return int(arg) > 65

def lunch_dec(arg):
    return arg == "standard"

train_set = np.zeros((1000, 4), dtype=int)
train_result = np.zeros((1000, 1), dtype=int)

for i in range(0, 1000):
    train_set[i][0] = int(gender_dict.index(gender[i]))
    train_set[i][1] = test_prep_dict.index(test_prep[i])
    train_set[i][2] = parent_dec(parental[i])
    train_set[i][3] = lunch_dec(lunch[i])
    train_result[i] = score_dec(math_score[i])

#DATA HANDLING DONE


# PERCEPTRON LEARNING
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x) * (1 - sigmoid(x))

weights = np.random.rand(4,1)
bias = np.random.rand(1)
learnrate = 0.0005

for epoch in range(2500):
    inputs = train_set

    # feed
    sum = np.dot(train_set, weights) + bias
    print(sum,":sum")
    sig_sum = sigmoid(sum)

    # backprop
    err_marg = sig_sum - train_result
    if (epoch % 500 == 1):
        print(err_marg.sum())

    sigged = err_marg * sigmoid_der(sig_sum)
    weights -= learnrate * np.dot(train_set.T, sigged)
    print(,(sigged))
    print(sigged[0])
    for x in sigged:
        bias -= learnrate * x

# TESTING


while(1):
    userinput = np.array([0,0,0,0])
    userinput[0] = input("Gender: 1 = Female\n")
    userinput[1] = input("Did the student prepare? 1 = Yes\n")
    userinput[2] = input("Does the students parents have educational degree? 1 = Yes\n")
    userinput[3] = input("Did the student eat lunch? 1 = Yes\n")

    result = sigmoid(np.dot(userinput, weights) + bias)
    print("\nStudent probability of passing: ", result[0]*100, "%\n\n")

import tensorflow as tf
import keras as ks
import numpy as np

import csv

#"gender","race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"

gender = [] #0
race = [] #1
parental = [] #2
lunch = [] #3
test_prep = [] #4
math_score = [] #5
read_score = [] #6
write_score = [] #7

gender_dict = []
race_dict = []
test_prep_dict = []
parental_dict = []

with open('StudentsPerformance.csv') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        gender.append(row[0])
        if not row[0] in gender_dict:
            gender_dict.append(row[0])
        race.append(row[1])
        if not row[1] in race_dict:
            race_dict.append(row[1])
        parental.append(row[2])
        if not row[2] in parental_dict:
            parental_dict.append(row[2])
        lunch.append(row[3])
        test_prep.append(row[4])
        if not row[4] in test_prep_dict:
            test_prep_dict.append(row[4])
        math_score.append(row[5])
        read_score.append(row[6])
        write_score.append(row[7])

print(gender_dict)
print(race_dict)
print(test_prep_dict)
print(parental_dict)



train_label = np.zeros(len(gender), dtype=float)

train_data = np.zeros((len(gender), 4), dtype=int)

for i in range(0, len(gender)):
    train_label[i] = int(math_score[i])/100 - 0.001
    train_data[i] = i
    train_data[i][0] = gender_dict.index(gender[i])
    train_data[i][1] = race_dict.index(race[i])
    train_data[i][2] = test_prep_dict.index(test_prep[i])
    train_data[i][3] = parental_dict.index(parental[i])
#    train_data[i] = rank[i]
#    train_data[i][0] = len(name[i])
#    if (not year[i] == 'N/A'):
#        train_data[i][1] = int(year[i])
#    else:
#        train_data[i][1] = 0
#    train_data[i][2] = decode_genre(genre[i])
#    train_data[i][3] = decode_pub(publisher[i])


model = tf.keras.models.Sequential([
    #tf.keras.layers.Flatten(input_shape=(3)),
    tf.keras.layers.Dense(8, input_shape=(4,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
    ])

#predictions = model(x_train[:1]).numpy()
#tf.nn.softmax(predictions).numpy()
#loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#loss_fn(y_train[:1], predictions).numpy()

train_data_t = train_data[:500]
train_label_t = train_label[:500]
train_data_e = train_data[500:]
train_label_e = train_label[500:]

print(train_data)
print(train_label)

model.compile(optimizer='adam',
        loss="sparse_categorical_crossentropy",
        metrics=['accuracy'])
model.fit(train_data_t, train_label_t, epochs=20, verbose=1)



result = model.evaluate(train_data_e, train_label_e)
print(result)
#userinput = np.zeros((1, 4), dtype=int)
#userinput[0][0] = gender_dict.index(input("Enter gender (male, female): "))
#userinput[0][1] = race_dict.index(input("Enter race (group A ... E): "))
#userinput[0][2] = test_prep_dict.index(input("Enter test prep (none, completed): "))
#userinput[0][3] = parental_dict.index(input("Enter parental education (DEBUG): "))

#probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
#predictions_single = probability_model.predict(userinput)

#print(predictions_single)
#print(np.argmax(predictions_single[0]))

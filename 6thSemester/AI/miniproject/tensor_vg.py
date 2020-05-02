import tensorflow as tf
import keras as ks
import numpy as np

#Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
import csv

rank = [] #0
name = [] #1
platform = [] #2
year = [] #3
genre = [] #4
publisher = [] #5
sales_na = [] #6
sales_eu = [] #7
sales_jp = [] #8
sales_other = [] #9
sales_go = [] #10

genre_dictionary = []
pub_dictionary = []

with open('vgsales.csv') as csvfile:
    csvread = csv.reader(csvfile)
    for row in csvread:
        rank.append(row[0])
        name.append(row[1])
        platform.append(row[2])
        year.append(row[3])
        genre.append(row[4])
        if not row[4] in genre_dictionary:
            genre_dictionary.append(row[4])
        publisher.append(row[5])
        if not row[5] in pub_dictionary:
            pub_dictionary.append(row[5])
        sales_na.append(row[6])
        sales_eu.append(row[7])
        sales_jp.append(row[8])
        sales_other.append(row[9])
        sales_go.append(row[10])

def morph_data(array):
    len(array[0])
    if(len(array[0]) > 20):
        array[0] = array[0][0:20]
    while(len(array[0]) < 20):
        array[0] = array[0]+ " "
    return array

def decode_genre(genre):
    return genre_dictionary.index(genre)

def decode_pub(pub):
    return pub_dictionary.index(pub)

def flatten(input):
    val = (input - 0.01)/(82.74 - 0.01)
    if val >= 0.999:
        val -= 0.001
    if val <= 0:
        val= 0
    return val

train_label = np.zeros(len(rank), dtype=float)
#train_label[0] = int(float(sales_go[idx]))

train_data = np.zeros((len(rank), 4), dtype=int)

for i in range(0, len(rank)):
    train_label[i] = flatten(float(sales_go[i]))
    train_data[i] = rank[i]
    train_data[i][0] = len(name[i])
    if (not year[i] == 'N/A'):
        train_data[i][1] = int(year[i])
    else:
        train_data[i][1] = 0
    train_data[i][2] = decode_genre(genre[i])
    train_data[i][3] = decode_pub(publisher[i])


#print("MODDED: ", train_data, " ", train_label)
print(np.shape(train_data))
print(np.shape(train_label))
### CNN TENSORFLOW
print(train_data[len(rank)-1000][1])
print(train_label)
#mnist = tf.keras.datasets.mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data()
#x_train, x_test = x_train / 255.0, x_test / 255.0
#print(x_train)
#print(y_train)
#print(np.shape(x_train))
#print(np.shape(y_train))
#print(y_train[0],"helll: ", y_train)

model = tf.keras.models.Sequential([
    #tf.keras.layers.Flatten(input_shape=(3)),
    tf.keras.layers.Dense(4, input_shape=(4,)),
    tf.keras.layers.Dense(12, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='relu')
    ])

#predictions = model(x_train[:1]).numpy()
#tf.nn.softmax(predictions).numpy()
#loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
#loss_fn(y_train[:1], predictions).numpy()
model.compile(optimizer='adam',
        loss="mean_squared_error")
model.fit(train_data, train_label, epochs=3)

userinput = np.zeros((1, 4), dtype=int)
userinput[0][0] = len(input("Enter name: "))
userinput[0][1] = int(input("Enter year: "))
userinput[0][2] = decode_genre(input("Enter genre: "))
userinput[0][3] = decode_pub(input("Enter publisher: "))

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions_single = probability_model.predict(userinput)

print(predictions_single)
print(np.argmax(predictions_single[0]))

import numpy
import tensorflow
from keras.layers import Dense
from keras.models import Sequential
from matplotlib import pyplot
from dataset import get_dataset

SELECTED_IDS = [6, 7, 21, 24, 25, 26, 27, 32, 33, 57, 59, 99]
SELECTED_COUNT = len(SELECTED_IDS)
PREDICT_ID = 54
DATASET_SPLIT = 50


dataset = get_dataset()


result = [user for user in dataset if user[PREDICT_ID] is not None]
result = [[-1 if i == None else i for i in user] for user in result]


selected_set = [numpy.asfarray([user[id - 1] for user in result]) for id in SELECTED_IDS]
selected_set.append(numpy.asfarray([user[PREDICT_ID] for user in result]))

dataset = numpy.array(selected_set).T
x = dataset[:-DATASET_SPLIT, 0:SELECTED_COUNT]
y = dataset[:-DATASET_SPLIT, SELECTED_COUNT]

model = Sequential()
model.add(Dense(25, input_dim=len(selected_set) - 1, kernel_initializer='normal', activation='relu'))
model.add(Dense(55, activation='relu'))
model.add(Dense(125, activation='relu'))
model.add(Dense(70, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(40, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', metrics=['accuracy'], optimizer='adam')

history = model.fit(x, y, epochs=50, batch_size=5)

model.save('predictormodelComplete.h5')

pyplot.plot(history.history['accuracy'])
pyplot.title('Model accuracy')
pyplot.ylabel('Accuracy')
pyplot.xlabel('Epoch')
pyplot.legend(['Train', 'Test'], loc='upper left')
pyplot.show()

a = dataset[-DATASET_SPLIT:, 0:variables]
b = dataset[-DATASET_SPLIT:, variables]

predictions = model.predict(a)
error = 0
for i in range(len(predictions)):
    print((predictions[i] * 2).round() / 2, dataset[-(DATASET_SPLIT-i), variables])
    error += abs(predictions[i].round() - dataset[-(DATASET_SPLIT-i), variables])


error = error / DATASET_SPLIT

_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

_, accuracy = model.evaluate(a, b)

print('Pinpoint Accuracy: %.2f' % (accuracy*DATASET_SPLIT), '/', DATASET_SPLIT)
print('Percentage accuracy: %.2f' % (accuracy*100))
print("Average error %.2f" % error)

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3    # classify our test items based on the classes of 3 nearest neighbors

    # process each of the test data points
    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]

        # add your code here
        nearest = np.argmin(distances)       # this just finds the nearest neighbour (so k=1)
        print("nearest: ", nearest)
        nearest_array = np.argsort(distances)[:k]     # this finds the k nearest neighbours
        print("nearest_array: ", nearest_array)
        print("y_train[nearest_array]: ", y_train[nearest_array])
        print("np.bincount(y_train[nearest_array]): ", np.bincount(y_train[nearest_array]))
        y_predict[i] = np.argmax(np.bincount(y_train[nearest_array]))     # this finds the most common class of the k nearest neighbours
        print("y_predict[i]: ", y_predict[i])

        # create a line connecting the points for the chart
        # you may change this to do the same for all the k nearest neigbhors if you like
        # but it will not be checked in the tests
        lines.append(np.stack((test_item, X_train[nearest_array[0]])))
        lines.append(np.stack((test_item, X_train[nearest_array[1]])))
        print("lines: ", lines)
    
    print(y_predict)

main(X_train, X_test, y_train, y_test)
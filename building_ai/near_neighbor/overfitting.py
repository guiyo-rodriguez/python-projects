from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score

# do not edit this
# create fake data
x, y = make_moons(
    n_samples=500,  # the number of observations
    random_state=42,
    noise=0.3
)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

K_values = np.arange(1, 260, 1)

for k in K_values:
    # Create a classifier and fit it to our data
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)

    # Get the accuracy of our model on the training data
    train_prediction = knn.predict(x_train)
    ac_t = accuracy_score(y_train, train_prediction)

    # Get the accuracy of our model on the testing data
    test_prediction = knn.predict(x_test)
    ac_v = accuracy_score(y_test, test_prediction)

    # Plot the data
    # plt.scatter(x[:, 0], x[:, 1], c=y, cmap='winter')
    # plt.title("KNN classification with K=%d" % k)
    # plt.show()

    # print("training accuracy: %f" % ac_t)
    # print("testing accuracy: %f" % ac_v)
    print("%d, %f, %f" % (k, ac_t, ac_v))

""" # Create a classifier and fit it to our data
knn = KNeighborsClassifier(n_neighbors=42)
knn.fit(x_train, y_train)

#print("training accuracy: %f" % ac_t)
test_prediction = knn.predict(x_test)
acc_test = accuracy_score(y_test, test_prediction)

train_prediction = knn.predict(x_train)
acc_train = accuracy_score(y_train, train_prediction)

print("training accuracy: %f" % acc_train)
print("testing accuracy: %f" % acc_test) """
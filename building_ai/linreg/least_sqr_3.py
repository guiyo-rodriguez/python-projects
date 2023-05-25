import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    np.set_printoptions(precision=1)    # this just changes the output settings for easier reading

    input_train_file = StringIO(train_string)
    input_test_file = StringIO(test_string)

    aux_train_mat = np.genfromtxt(input_train_file, delimiter=' ')
    aux_test_mat = np.genfromtxt(input_test_file, delimiter=' ')

    x_train = aux_train_mat[:, :-1]
    y_train = aux_train_mat[:, -1]

    x_test = aux_test_mat[:, :-1]

    c = np.linalg.lstsq(x_train, y_train, rcond=None)[0]
    
    print(x_train)
    print(y_train)
    print(x_test)
    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)


main()
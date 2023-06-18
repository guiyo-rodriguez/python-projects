import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def dist_manhattan(a, b):
    return np.sum(np.abs(np.array(a) - np.array(b)))

def find_nearest_pair(data):
    N = len(data)
    #print("N: ", N)
    dist = np.empty((N, N), dtype=float)
    dist.fill(np.inf)
    
    for x in range(N):
        for y in range(N):
            if x == y:
                continue
            dist[x, y] = dist_manhattan(data[x], data[y])
            #print("x: ", x, "y: ", y, "dist: ", dist[x, y])

    #print("dist: \n", dist)
    #print("np.argmin(dist): ", np.argmin(dist))
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
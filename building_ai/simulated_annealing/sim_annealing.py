import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import cm


N = 100     # size of the problem is N x N                                      
steps = 3000    # total number of iterations                                        
tracks = 50
plateau_time = 180
initial_temperature = 1

# generate a landscape with multiple local optima                                          
def generator(x, y, x0=0.0, y0=0.0):
    return np.sin((x/N-x0)*np.pi)+np.sin((y/N-y0)*np.pi)+\
        .07*np.cos(12*(x/N-x0)*np.pi)+.07*np.cos(12*(y/N-y0)*np.pi)

x0 = np.random.random() - 0.5
y0 = np.random.random() - 0.5
h = np.fromfunction(np.vectorize(generator), (N, N), x0=x0, y0=y0, dtype=int)
peak_x, peak_y = np.unravel_index(np.argmax(h), h.shape)

# starting points                                                               
x = np.random.randint(0, N, tracks)
y = np.random.randint(0, N, tracks)

def accept_prob(S_old, S_new, T):
    if S_new > S_old:
        return 1.0
    elif T > 0:
        return np.exp(-(S_old - S_new)/T)
    else:
        return 0.0

def accept(S_old, S_new, T):
    r = random.random()
    if r < accept_prob(S_old, S_new, T):
        return True
    else:
        return False

def formatXY(x, y, dim):
    secuence = ""
    for i in range(dim):
        secuence = secuence + "(" + str(x[i]) + "," + str(y[i]) + ")"
    return secuence

def main():
    global x
    global y

    contador = 1
    plateau_value = plateau_time
    T = initial_temperature
    for step in range(steps):
        # add a temperature schedule here
        #print(x)
        #print(y)
        # update solutions on each search track                                     
        for i in range(tracks):
            # try a new solution near the current one                               
            x_new = np.random.randint(max(0, x[i]-2), min(N, x[i]+2+1))
            y_new = np.random.randint(max(0, y[i]-2), min(N, y[i]+2+1))
            S_old = h[x[i], y[i]]
            S_new = h[x_new, y_new]

            # change this to use simulated annealing
            if S_new > S_old:
                x[i], y[i] = x_new, y_new   # new solution is better, go there
                #print("Enfriado: " + str(x[i]) + ", " + str(y[i]) + ", " + str(S_new))       
            elif accept(S_old, S_new, T):
                x[i], y[i] = x_new, y_new
                #print("Recocido: " + str(x[i]) + ", " + str(y[i]) + ", " + str(S_new))
            else:
                #print("Descartar: " + str(x[i]) + ", " + str(y[i]) + ", " + str(S_new))
                pass                        # if the new solution is worse, do nothing
        res = sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)])
        if res >= 0:
            print("T= " + str(T) + " contador= " + str(contador) + ", res= " + str(res) + ", path= " + formatXY(x, y, tracks))
            contador = contador + 1
        plateau_value = plateau_value - 1
        if plateau_value == 0:      
            T = T/2
            plateau_value = plateau_time

    # Number of tracks found the peak
    print(str(peak_x) + ", " + str(peak_y))
    print(sum([x[j] == peak_x and y[j] == peak_y for j in range(tracks)]))
     
    plt.xlim(0, N-1)
    plt.ylim(0, N-1)
    plt.imshow(h, cmap=cm.get_cmap())
    plt.scatter([peak_y], [peak_x], color='red', marker='+', s=100)

    for j in range(tracks):
        #c = cm.colors(j/tracks)    # use different colors for different tracks 
        plt.scatter([y[j]], [x[j]], s=40)
    plt.show()

main()
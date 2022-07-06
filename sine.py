import math

dirac = [0 for i in range(1000)]
dirac[100] = 1  # needs a Dirac impulse to start swinging

amp = 0.995     # exponentially increasing amplitude
#amp = 1        # constant amplitude
#amp = 1.005    # exponentially decreasing amplitude
freq = 137      # a lovely frequency for a 1000 long array

sine = [0,0]    # initialized to ease indexing

for i in range(1,len(dirac)):
    sine.append((amp*math.sin(2*3.14159*freq)*dirac[i] - sine[i-1] + 2*amp*math.cos(2*3.14159*freq)*sine[i]) / amp**2)


import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.title("Sine with Z-transform")
plt.plot(sine, color="blue")

plt.show()

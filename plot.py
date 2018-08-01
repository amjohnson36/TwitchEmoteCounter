import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

"""
# Generate fake data
import random
test1 = []
test2 = []
test3 = []

for i in range(60):
    test1.append(random.randint(0, 100))
    test2.append(random.randint(0, 100))
    test3.append(random.randint(0, 100))
"""

with open('data.json', 'r') as f:
    d = json.loads(f.read())

emotes = [l for l in d]
names = ['PogChamp', 'LUL', 'Kappa', 'ResidentSleeper', 'BibleThump', 'WutFace']

# Data for plotting
df = pd.DataFrame({'x': range(0, len(emotes[0])), names[0]: np.array(emotes[0]),
        names[1]: np.array(emotes[1]), names[2]: np.array(emotes[2]),
        names[3]: np.array(emotes[3]), names[4]: np.array(emotes[4]),
        names[5]: np.array(emotes[5])})

# Create and save plots
fig, ax = plt.subplots()
ax.plot('x', names[0], data = df, color = 'tan')
ax.plot('x', names[1], data = df, color = 'green')
ax.plot('x', names[2], data = df, color = 'gray')
ax.plot('x', names[3], data = df, color = 'black')
ax.plot('x', names[4], data = df, color = 'blue')
ax.plot('x', names[5], data = df, color = 'red')

ax.legend()
ax.grid()

ax.set(xlabel='time (min)', ylabel= 'number of emotes',
    title='Use of Twitch emotes over time')

fig.savefig("/home/Alex/twitch/graphs/test.png", bbox_inches='tight')

plt.show()
plt.close()

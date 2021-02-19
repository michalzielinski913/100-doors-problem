import numpy as np
isDoorOpened=np.full((100), False)

for x in range(100):
    for y in range(x, 100, x+1):
        isDoorOpened[y]=not isDoorOpened[y]

for x in range(isDoorOpened.size):
    print("Door %d:" % (x + 1), 'open' if isDoorOpened[x] else 'close')


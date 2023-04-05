import time
import matplotlib.pyplot as plt

x_val = []
y_val = []

startTime: float = time.time()

for i in range(15):
    print(f"Processing {i}")
    x = i
    step = 0
    while x != 1:
        step = step + 1
        x_val.append(step)
        if (x % 2) == 0:
            x = x / 2
            y_val.append(x / 2)
        else:
            x = (x * 3) + 1
            y_val.append((x * 3) + 1)
    plt.plot(x_val, y_val, label=f"{i}")
    x_val.clear()
    y_val.clear()

print(f"Took {int(time.time()) - int(startTime)} seconds to process")
plt.legend()
plt.show()

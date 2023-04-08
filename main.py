import time
import matplotlib.pyplot as plt

x_val = []  # Get a list ready to store the x values before plotting
y_val = []  # Get a list ready to store the y values before plotting

if __name__ == "__main__":
    startTime: float = time.time()  # Get the time before the application starts - Used to measure how long the calculations took.

    for i in range(1, 5):
        x = i
        step = 0
        while x != 1:  # If x == 1, then the number has completed its journey.
            print(x)
            step = step + 1
            x_val.append(step)
            if (x % 2) == 0:
                x = x / 2
                y_val.append(x / 2)
            else:
                x = (x * 3) + 1
                y_val.append((x * 3) + 1)

        print(f"Finished {i}")
        plt.plot(x_val, y_val, label=f"{i}")
        x_val.clear()
        y_val.clear()

    print(f"Took {int(time.time()) - int(startTime)} seconds to process")
    plt.legend(loc="upper right")
    plt.show()

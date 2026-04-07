import subprocess
import time
import matplotlib.pyplot as plt

input_files = [
    "data/file1.in",
    "data/file2.in",
    "data/file3.in",
    "data/file4.in",
    "data/file5.in",
    "data/file6.in",
    "data/file7.in",
    "data/file8.in",
    "data/file9.in",
    "data/file10.in"
]

x_values = []  # n * m
y_values = []  # runtime (ms)

for file_name in input_files:
    total_time = 0

    # run 3 times and average
    for _ in range(3):
        start = time.perf_counter()
        subprocess.run(
            ["py", "src/main.py", file_name],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        end = time.perf_counter()
        total_time += (end - start)

    avg_time_ms = (total_time / 3) * 1000

    # read input to get sizes
    with open(file_name, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    k = int(lines[0])
    A = lines[k + 1]
    B = lines[k + 2]

    n = len(A)
    m = len(B)

    x_values.append(n * m)
    y_values.append(avg_time_ms)

# sort points for cleaner graph
points = sorted(zip(x_values, y_values))
x_values, y_values = zip(*points)

# plot
plt.figure(figsize=(8, 5))
plt.scatter(x_values, y_values)
plt.xlabel("Input Size (n * m)")
plt.ylabel("Average Runtime (ms)")
plt.title("HVLCS Runtime on 10 Input Files")
plt.grid(True)

# save image
plt.savefig("data/runtime_graph.png")

# optional: show it
plt.show()

print("Graph saved as runtime_graph.png")
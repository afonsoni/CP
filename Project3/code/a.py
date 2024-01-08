import matplotlib.pyplot as plt

# Example data, replace with your actual data
num_threads = [4, 8, 12, 14, 18, 22, 24, 26, 30, 34, 36, 40]
time_elapsed = [12.222, 6.215, 4.205, 3.630, 2.859, 2.635, 2.613, 2.626, 2.558, 2.545, 2.534, 2.469]


# Plot the speedup analysis
plt.subplot(2, 1, 1)  # 3 rows, 1 column, this is the second plot
# Calculate speedup
speedup = [time_elapsed[0] / t for t in time_elapsed]
# Plotting
plt.plot(num_threads, speedup, marker='o')
plt.xlabel('Number of Threads')
plt.ylabel('Speedup')
plt.title('Scalability Analysis')
plt.grid(True)

# Plot the efficiency analysis
plt.subplot(2, 1, 2)  # 3 rows, 1 column, this is the third plot
# Calculate efficiency
efficiency = [s / t for s, t in zip(speedup, num_threads)]
# Plotting
plt.plot(num_threads, efficiency, marker='o')
plt.xlabel('Number of Threads')
plt.ylabel('Efficiency')
plt.title('Efficiency Analysis')
plt.grid(True)

plt.tight_layout()  # Adjust layout to prevent overlapping
plt.show()

# Print speedup values for each thread
print("Speedup values:")
for thread, s in zip(num_threads, speedup):
    print(f"Thread {thread}: {s:.4f}")
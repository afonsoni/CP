import matplotlib.pyplot as plt
import numpy as np

# Data
sizes = [2500, 5000, 10000, 20000]
num_threads = [8, 16, 32, 64]

config_1_times = [5.662, 10.579, 26.779, 101.518]
config_2_times = [6.152, 8.614, 20.606, 66.406]
config_3_times = [6.979, 10.387, 18.166, 58.984]
config_4_times = [7.149, 10.494, 19.629, 55.422]

# Set up positions for bars on X axis
bar_width = 0.2
bar_positions = np.arange(len(sizes))

# Plotting the bar chart
plt.figure(figsize=(12, 8))

for i, config_times in enumerate([config_1_times, config_2_times, config_3_times, config_4_times]):
    plt.bar(bar_positions + i*bar_width, config_times, width=bar_width, label=f'Threads: {num_threads[i]}')

plt.title('Execution Time for Different Thread Configurations')
plt.xlabel('Number of Particles (N)')
plt.ylabel('Execution Time (s)')
plt.xticks(bar_positions + 1.5*bar_width, sizes)

# Set legend font size
plt.legend(title='Number of Threads per Block', fontsize='xx-large')

plt.grid(True)
plt.show()

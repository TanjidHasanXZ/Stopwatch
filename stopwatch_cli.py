import time

print("Press ENTER to start the stopwatch. Press ENTER again to record lap times. Press Ctrl+C to stop.")
input()  # Wait for the user to press ENTER
print("Stopwatch started.")
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f"Lap {lap_num}: {lap_time} seconds (Total: {total_time} seconds)")
        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print("\nStopwatch stopped.")

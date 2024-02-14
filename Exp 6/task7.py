# Write a Python program to print current hour, minute, second and microsecond using in-built datetime module

from datetime import datetime

current_time = datetime.now()

print(f"Current time: {current_time}")
print(f"Current hour: {current_time.hour}")
print(f"Current minute: {current_time.minute}")
print(f"Current second: {current_time.second}")
print(f"Current microsecond: {current_time.microsecond}")
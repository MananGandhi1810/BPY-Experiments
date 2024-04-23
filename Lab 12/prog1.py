import time

with open("test.txt", "a+") as f:
    f.write(f"{time.time()}\n")
    f.seek(1)
    print(f.read())
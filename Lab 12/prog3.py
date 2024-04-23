with open("file.txt", "w+") as f:
    f.write("Hello!")
    f.seek(0)
    print(f.read())
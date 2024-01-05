languages = ["Python", "C", "C++", "Java"]
print(languages[0])
print(languages[-1])
print(languages[::-1])
print(languages[1:3])
print(len(languages))
print(languages[-4:-1])
if "Python" in languages:
    print("Python is in the list")
languages.append("JavaScript")
print(languages)
languages[3] = "Dart"
languages[1:3] = ["C#", "Go"]
print(languages)
languages.insert(1, "C")
print(languages)
languages.clear()
print(languages)
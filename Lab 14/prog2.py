import re

regex = r"https?://[a-zA-Z]+\.[a-zA-Z]{2,}"

test_str = "Manan <https://manangandhi.tech>"

print(re.findall(regex, test_str))
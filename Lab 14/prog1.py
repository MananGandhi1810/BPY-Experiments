import re

regex = r"[a-zA-Z_%-.0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}"

test_str = "Manan <manan.gandhi@manangandhi.tech>"
print(re.findall(regex, test_str))
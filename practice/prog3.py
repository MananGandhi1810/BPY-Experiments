import re

email_regex = r"[a-z0-9A-Z_%-.]+@[a-zA-Z]+.[a-zA-Z]{2,}"

s = "Manan <manan@manangandhi.tech>, Manan<ardumanan@gmail.com>"
print(re.findall(email_regex, s))
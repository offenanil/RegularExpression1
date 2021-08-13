# regex pattern
# r"(\d\d\d)-\d\d\d-\d\d\d\d" for phone number like (555)-555-5555
# or r"(\d{3})-\d{3}-\d{4}"


text = "the agent's phone number is 408-444-1234.call soon"

print("phone" in text)

import re
pattern = "phone"
print(re.search(pattern,text))

pattern = "NOT IN TEXT"
print(re.search(pattern,text))
pattern = "phone"
match = re.search(pattern,text)
print(match)

print(match.span())
print(match.end())
matches = re.findall("phone", text)
print(matches)
print(len(matches))




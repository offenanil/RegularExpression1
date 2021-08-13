# \d- a digit
# \w alphanumeric
# \s - white space (eg a\sb\sc = a b c)
# \D - a non digit  (eg \D\D\D = ABC)
# \W - non alphanumeric (eg \w\w\w\w\w = *_+=)
# \S - non white apace ( eg \S\S\S\S = YOYO

# look quantifiers
# + occurs one or more times
# {3} occurs exactly 3 times
# {2, 4} occurs 2 to 4 times
# {3,} occurs 3 or more times
# * occurs zero or more times
# ? once or none




import re
text = "my phone number is 408-555-1234"
# phone = re.search("408-555-1234", text)
phone = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)  # r escapes new line etc and line 13 n 14 code is same but line 14 is universal and line 13 is only for that phone number
print(phone)
print(phone.group())  # here i can get phone number 408-555-1234



# now above example by using quantifiers

phone = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())  # 408-555-1234
print(results.group(1))  # 408 if group(2 ) then 555 so easy to find area code

print(re.search(r'cat', 'the cat is here')) #print(re.search(r'cat', 'the dog is here')) result is not match to cat so for this we put or operator|

print(re.search(r'cat|dog', 'the dog is here'))

print(re.findall(r'at', 'the cat in the hat sat here'))  #finadall wildcard operator matches for all:['at', 'at', 'at']
print(re.findall(r'.at', 'the cat in the hat sat here'))  #['cat', 'hat', 'sat']
print(re.findall(r'...at', 'the cat in the hat sat here')) #['e cat', 'e hat'] (count from three space before at so e space c and at ok

print(re.findall(r'^\d', '1 is a number')) #searching for entire text start with a number :['1']
print(re.findall(r'^\d', ' the 2 is a number')) # []
print(re.findall(r'\d$', ' the number is 2')) # searching for entire text end with a number :['2']


phrase = 'there are 3 numbers 34 inside 5 this sentence'
# so i want all the numbers inside this Phrase
pattern = r'[^\d]' #means excludes  digits
print(re.findall(pattern, phrase))
pattern = r'[^\d]+' # + is quantifiers have a look
print(re.findall(pattern, phrase))
punct = 'hi! i am anil.how are yoy?' # if i want to remove all the punctation
print(re.findall(r'[^!.?]+', punct))


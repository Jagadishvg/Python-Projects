import pprint
message = "hello I am fine!" #if you want to use multiple lines of text then use triple quotes(''')
count = {}
for char in message.upper(): #if you dont want uppercased version of the characters then remove .upper()
    count.setdefault(char, 0)
    count[char] = count[char]+1
pprint.pprint(count)

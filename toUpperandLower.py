string1 = "stringone"
string2 = "STRINGTWO"
string3 = "STRINGthree"
print(string1.upper())
print(string2.lower())
string4 = []
for i in string3:
    if i.isupper():
        i = i.lower()
        string4.append(i)
    elif i.islower():
        i = i.upper()
        string4.append(i)
string5 = ''.join(string4)     
print(string5)

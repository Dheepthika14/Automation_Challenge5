import re

Str1 = input("Enter the String 1 : ")
Str2 = input("Enter the String 2 : ")

FinalStr1 = re.findall(r'\w+', Str1)
FinalStr2 = re.findall(r'\w+', Str2)
MaxLength = 0
Match = []
for x in FinalStr1:
    if x in FinalStr2 and len(x) > MaxLength:
        MaxLength = len(x)

for x in FinalStr1:
    if len(x) == MaxLength and x in FinalStr2:
        Match.append(x)

if (len(Match)) > 0:
    print("The longest shared substring : ", Match)
else:
    print("We dont have any matching substring")

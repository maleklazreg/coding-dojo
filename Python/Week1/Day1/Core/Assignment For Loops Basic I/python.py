for interger in range(151):
    print(interger)

for multiple in range(5, 1001, 5):
    print(multiple)

for dojo in range(1, 101):
    if dojo % 10 == 0:
        print("Coding Dojo")
    elif dojo % 5==0:
        print("Coding")
    else:
        print(dojo)

summer = sum(summer for summer in range(1, 500001, 2))
print(summer)

for era in range(2018, 0, -4):
    print(era)

lowNum = 2
highNum = 9
mult = 3
for three in range(lowNum, highNum +1):
    if three % mult == 0:
        print(three)
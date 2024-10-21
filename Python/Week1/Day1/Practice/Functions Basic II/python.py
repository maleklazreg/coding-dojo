def contdown(num):
    return[x for x in range(num, -1,-1)]
print(contdown(5))

def printandreturn(numbers):
    print(numbers[0])
    return numbers[1]
print(printandreturn([1,2]))

def firstpluslength(first):
    return first[0] + len(first)
print(firstpluslength([1,2,3,4,5]))

def valuesgreaterthansecond(my_list):
    if len(my_list) < 2:
        return False
    second = my_list[1]
    new_list = [x for x in my_list if x > second]
    print(len(new_list))
    return new_list
print(valuesgreaterthansecond([5, 2, 3, 2, 1, 4]))

def lengthandvaluer(size, value):
    return [value]* size
print(lengthandvaluer(6, 2))
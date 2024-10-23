
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print("this is Z ", z)

x[1][0] = 15
print (x)

students[0]["last_name"]= "Bryant"
print (students)

sports_directory["soccer"][0] = "Andres"
print (sports_directory)



students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(a):
    for dictionary in a:
        for key in dictionary:
            print(f"{key} - {dictionary[key]}")
iterateDictionary(students)

def iterateDictionary(a):
    for dictionary in a:
        print(f"first_name - {dictionary['first_name']}, last_name - {dictionary['last_name']}")
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):
    if (key_name=="first_name"):
        for dictionary in some_list:
            print (dictionary['first_name'])
    else:
        for dictionary in some_list:
            print (dictionary['last_name'])
iterateDictionary2('last_name',students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(a):
    print (len(a['locations']),"LOCATIONS")
    for value in range(len(a['locations'])):
        print (a['locations'][value])
    print("")
    print(len(a['instructors']), "INSTRUCTORS")
    for value in range(len(a['instructors'])):
        print (a['instructors'][value])

printInfo(dojo)
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

# Problem 1
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30
print(x, students, sports_directory, z)

# Problem 2


def iterateDictionary(myStudents):
    for i in range(len(myStudents)):
        print(myStudents[i].items())


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)

# Problem 3


def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('first_name', students)

# Problem 4
def printInfo(myDict):
    result = []
    for i in myDict.keys():
        result.append(len(myDict[i]))
        result.append(i)
        result.append(myDict[i])
    print(result)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

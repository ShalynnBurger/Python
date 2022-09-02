print("sanity check")
print("=================================")

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


x[1][0] = 15 
print(x)

print("=================================")

students[0]['last_name'] = 'Bryant'
print(students[0])

print("=================================")

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

print("=================================")

z[0]['y'] = 30
print(z)

print("=================================")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# for name in students:
#     print("first_name - " +name['first_name'], "last_name - " + name['last_name'])


def iterateDictionary(students):
    for i in range(len(students)):
        output = ""
        if len(students)-1==i-1:
            for key, value in students[i].items():
                output+=f"{key} - {value}"
                break
        for key, value in students[i].items():
            output+=f"{key} - {value}, "
       
        print(output) 

iterateDictionary(students)
print("=================================")

# for name in students:
#     print(name['first_name'])
#     print(name['last_name'])

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
 

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)




print("=================================")

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    # print(f'{len(dojo)}')
    # for i in range(0,len(arr[])):
        
    #     print(arr[i])
    for key,value in dojo.items():
        print(len(value), key.upper())
        for i in range(0, len(value)):
            print(value[i])

printInfo(dojo)

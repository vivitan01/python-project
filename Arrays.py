
courses =["MIT","Python","Android"]
print(courses)


#Accessing an element
print(courses[0])

#Looping through an array
for x in courses:
    print(x)

# Adding a new element
courses.append("java")
print(courses)

#Removing an element
courses.remove("Android")
print(courses)
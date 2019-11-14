

#----------------Dictionary---------------#

#A dictionary is a collection which is unordered, changeable and indexed. In Python
# dictionaries are written with curly  brackets, and they have keys and values.

# thisdict = {
#     'name': 'kamran',
#     'age': 24,
#     'Qualification': 'Btech'
# }
# print(thisdict)

#Output - {'name': 'kamran', 'age': 24, 'Qualification': 'Btech'}


#----------------->Accessing Items<------------------

#if you want to accessing only the name from the  dictionary so you can use the Bracket

# print(thisdict['name'])
#Output - kamran

#you can also use GET method for accessing the specific details from the dictionary

# print(thisdict.get('name'))

#Output - kamran


#-------------------CHANGE VALUE-----------------

#You can change the value of a specific item  by referring  to its key name:

# thisdict = {
#     'name': 'kamran',
#     'age': 24,
#     'date': 1995
# }
#
# thisdict['age'] = 23
# print(thisdict)


#-----------------Loop Through a Dictionary---------------

#You can loop through a dictionary by using a for loop.When looping through a dictionary,
# the return value are the keys of the dictionary, but there are methods to return the values as well.

#Print all key names in the dictionary, one by one:

# for i in thisdict:
#     print(i)

#output - name
# age
# Qualification


#Print all values in the dictionary, one by one:

# for i in thisdict:
#     print(thisdict[i])

#Output - kamran
# 24
# Btech

#You can also use the values() function to return values of a dictionary:

# for i in thisdict.values():
#     print(i)

#Output- kamran
# 24
# Btech


#Loop through both keys and values, by using the items() function:

# for i,j in thisdict.items():
#     print(i,j)

#Output - name kamran
# age 24
# Qualification Btech


#-------------------Check if Key Exists------------------

#Check if 'model' exist in dictionary:

# thisdict = {
#     'brand': 'ford',
#     'model': 'khan',
#     'year': 2016
# }
#
# if 'model' in thisdict:
#     print('yes model is one of the key in the thisdict dictionary')
# else:
#     print('model is not key of thisdict')

#Output - yes model is one of the key in the thisdict dictionary


#-------------Dictionary Length----------------------

# print(len(thisdict))

#Output - 3


#-----------------ADD Items---------------------

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# thisdict['color'] = 'red'
# print(thisdict)

#Output - {'brand': 'ford', 'model': 'khan', 'year': 2016, 'color': 'red'}


#-------------------Removing Items-------------------

#There are several methods to remove items from a dictionary:

# thisdict.pop('model')
# print(thisdict)


#The popitem() method removes the last inserted item
# (in versions before 3.7, a random item is removed instead):

# thisdict.popitem()
# print(thisdict)

#Output - {'brand': 'ford', 'model': 'khan'}


#The del keyword removes the item with the specified key name:

# del thisdict['model']
# print(thisdict)

#Output - {'brand': 'ford', 'year': 2016}


#-----------------------Clear method--------------------

#The clear() keyword empties the dictionary:

# thisdict.clear()
# print(thisdict)


#-------------------Copy method------------------

#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be
# a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
#There are ways to make a copy, one way is to use the built-in Dictionary method copy().


#Make a copy of a dictionary with the copy() method:

# mydict = thisdict.copy()
# print(mydict)


#Another way to make a copy is to use the built-in method dict().

# mydict = dict(thisdict)
# print(mydict)

#Output - {'brand': 'ford', 'model': 'khan', 'year': 2016}


#---------------------Nested Dictionaries-----------------------

#A dictionary can also contain many dictionaries, this is called nested dictionaries.

#Create a dictionary that contain three dictionaries

# myFamily = {
#     'child1':{'name': 'kamran','age': 24},
#     'child2':{'name':'aisha','age': 23},
#     'child3':{'name': 'ruhi','age': 26}
# }
#
# print(myFamily)


#-----------------------The dict() Constructor-----------------------

#It is also possible to use the dict() constructor to make a new dictionary:

# thisdi = dict(brand = 'ford',model = 'khan',year = 2016)
# print(thisdi)

#Output - {'brand': 'ford', 'model': 'khan', 'year': 2016}


#----------------------Update method--------------------------

# car = {
#     'brand': 'ford',
#     'model': 'Mustang',
#     'year': 1964
# }
#
# car.update({'color': 'White'})
# print(car)



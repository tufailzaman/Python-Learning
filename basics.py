# # python data Types
 
# a = [1,8,3,2,5,3,5,9,0]
# print(a[2])
# age = 36
# #text = "My name is Khan And i am " + age
# #print (text.format(age))
# print(len(a))
# print(type(a))
# a[2] = "Tufail"
# print(a)
# a.insert(1,"Zaman")
# a.insert(0,"Tufail Zaman")
# print(a)
# a.append("Khan")
# print(a)

# list = ["Tufail","Awais","Amjad","Anas","Habib"]
# list1 = [1,2,3,4,5,6]
# print(len(list))
# print(list[3])
# list[1] = "Html" 
# list.insert(0,"python")
# list.append("JavaScript")
# print(list)
# list.extend(list1)
# print(list)
# list.append(list1)
# print(list)
# list.remove("Amjad")
# print(list)
# list.pop(0)
# print(list) 
# list.reverse()
# print(list)
# #list.clear()
# #print(list)

# ### Python Indentation  == we will use in program otherwise  python will gave error
# ### it refers to spaces in the begening

# if 5 > 2:
#     print("Five is greater than two")

# #### Variables
# #Assign Multiple values

# x,y,z = "orange","Apple","Banana"
# print(x)
# print(y)
# print(z)

# x=y=z = "Mango"
# print(x)
# print(y)
# print(z)

# ## Unpack a Collection

# fruits =[ "apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# ##Output Variables

# x = "Python is Awesome"
# print (x) ## Here "x" is output variable because used is print() function

# x="python"
# y="is"
# z="Awesome"
# print (x,y,z)

# x = 5
# y = 8
# print(x+y)

# a = "Tufail Zamna"
# b=5
# c="2"
# print(a,b)
# print(a+c)

# ## Global Variables

# x = "python is fantastic"
# def myfunc ():
#     print(x)
#     myfunc()
    
#     ## Global KeyWord
#     def zams():
#         global x
#         x = "Awesome"
#         zams()
#         print("python is "+x)
        
#         ## End of Variables
        
# def myfunc ():
#        x = 10
#        y = 878
#        global z
#        z = x+y        
# myfunc ()        
# print(z)

# def my_function (fname):
#     print (fname + "Zaman")
            
# my_function("Tufail")
# my_function("Amjad")
# my_function("Taif")

# def name (fname,lname):
#     print (fname + "  " +lname)
# name("Tufail","Zaman")    
# name("Amjad","Khan")    

# def arbitrary (*kids):
#     print ( " The Youngest Child is "  + kids[2])
# arbitrary("Tufail","Amjad","Rashid","Habib")    

# def arbitvalue (child1,child2,child3):
#       print ("The Stupid Person in the world is "+child3)
        
# arbitvalue(child1 = "tufail", child2 ="amjad", child3 ="rashid")      

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

## Default Parameter Value
# def deafultvalue (country = "Pskistan"):
#     print ("I am from "+country)
# deafultvalue()    
# deafultvalue("india")

## passing a list througth as Argunment
# def list(food):
#     for x in food:
        
#         print(x)

# fruits = ["apple","banan","Mango"]
# list(fruits)        

### Return Value
def return_value(x):
    return 5 * x
print(return_value(3))
print(return_value(5))
print(return_value(19))
print(return_value(20))
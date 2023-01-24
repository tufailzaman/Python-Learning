# python data Types
 
a = [1,8,3,2,5,3,5,9,0]
print(a[2])
age = 36
#text = "My name is Khan And i am " + age
#print (text.format(age))
print(len(a))
print(type(a))
a[2] = "Tufail"
print(a)
a.insert(1,"Zaman")
a.insert(0,"Tufail Zaman")
print(a)
a.append("Khan")
print(a)

list = ["Tufail","Awais","Amjad","Anas","Habib"]
list1 = [1,2,3,4,5,6]
print(len(list))
print(list[3])
list[1] = "Html" 
list.insert(0,"python")
list.append("JavaScript")
print(list)
list.extend(list1)
print(list)
list.append(list1)
print(list)
list.remove("Amjad")
print(list)
list.pop(0)
print(list) 
list.reverse()
print(list)
#list.clear()
#print(list)

### Python Indentation  == we will use in program otherwise  python will gave error
### it refers to spaces in the begening

if 5 > 2:
    print("Five is greater than two")

#### Variables
#Assign Multiple values

x,y,z = "orange","Apple","Banana"
print(x)
print(y)
print(z)

x=y=z = "Mango"
print(x)
print(y)
print(z)

## Unpack a Collection

fruits =[ "apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

##Output Variables

x = "Python is Awesome"
print (x) ## Here "x" is output variable because used is print() function

x="python"
y="is"
z="Awesome"
print (x,y,z)

x = 5
y = 8
print(x+y)

a = "Tufail Zamna"
b=5
c="2"
print(a,b)
print(a+c)
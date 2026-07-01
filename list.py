Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a = [2,5.7,"python",6+9j,True,False]
a
[2, 5.7, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b = [5]
typ(b)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    typ(b)
NameError: name 'typ' is not defined. Did you mean: 'type'?
type(b)
<class 'list'>
c = 5
type[c]
type[5]
type(c)
<class 'int'>
# append()
a = ["python","c","c++","java"]
a.append("dsa")
# append is used for to add only one string or a datatype to the list
a
['python', 'c', 'c++', 'java', 'dsa']
a.append("ai","ml")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a.append("ai","ml")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ai","ml"])
a
['python', 'c', 'c++', 'java', 'dsa', ['ai', 'ml']]
# extend() -> to addd some string or a datatype to the list
a = ["python","c","java"]
a.extend(["c++","dsa"])
a
['python', 'c', 'java', 'c++', 'dsa']
# insert() -> to insert a string(or) a data type in a particular location
b = ["vij","hyd"]
b.insert(1,"vzg")
b
['vij', 'vzg', 'hyd']
# indexposition of a string & also it helps to copy the data
a = ["black","white","pink", "red"]
a.index("white")
1
a.copy()
['black', 'white', 'pink', 'red']
b = a.copy()
b
['black', 'white', 'pink', 'red']
# count()-> number of time it reapeated
b.count("red")
1
b.count("white")
1
# sort()
a =["grapes","mango","apple","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b = [8,9,5,7,3,5,2,5,6,3,1]
b.sort()
b
[1, 2, 3, 3, 5, 5, 5, 6, 7, 8, 9]
# reverse()
a = [7,234,45,6,658,689,87]
a.reverse()
a
[87, 689, 658, 6, 45, 234, 7]
b = ["java","c","html","c++","css","python"]
b.reverse()
b
['python', 'css', 'c++', 'html', 'c', 'java']
# pop()-> last datatype will be delete
>>> a = ["java","c","html","c++","css","python"]
>>> a.pop()
'python'
>>> a
['java', 'c', 'html', 'c++', 'css']
>>> a.pop("html")
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a.pop("html")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(2)
'html'
>>> a
['java', 'c', 'c++', 'css']
>>> # remove() -> removing something at any postion in the list
>>> a.remove("c")
>>> a
['java', 'c++', 'css']
>>> 
>>> # length()
>>> a = ["yashu","viji","suri","suni"]
>>> len(a)
4
>>> b="viji"
>>> len(b)
4
>>> c = ["viji"]
>>> len(c)
1
>>> a.clear()
>>> a
[]
>>> b = []
>>> b.append("hi")
>>> b
['hi']

Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# dict{}
a = {"name":"vijitha","city":"vja"}
print(a)
{'name': 'vijitha', 'city': 'vja'}
type(a)
<class 'dict'>
b = {1,2,3,4,5,6,78,"viji"}
type(b)
<class 'set'>
a = {"name":"vijitha","city":"vja","mailid":"garikapativijithachowdary2004@gmail.com","mobile_number":"1234567890"}
print(a)
{'name': 'vijitha', 'city': 'vja', 'mailid': 'garikapativijithachowdary2004@gmail.com', 'mobile_number': '1234567890'}
a.keys()
dict_keys(['name', 'city', 'mailid', 'mobile_number'])
a.values()
dict_values(['vijitha', 'vja', 'garikapativijithachowdary2004@gmail.com', '1234567890'])
a.items()
dict_items([('name', 'vijitha'), ('city', 'vja'), ('mailid', 'garikapativijithachowdary2004@gmail.com'), ('mobile_number', '1234567890')])
a{"course":"python","instute":"codegnan"}
SyntaxError: invalid syntax
a = {"course":"python","instute":"codegnan"}
a.update({"year":"2026"})
a
{'course': 'python', 'instute': 'codegnan', 'year': '2026'}
a.update({"year":2026},{"month":7})
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.update({"year":2026},{"month":7})
TypeError: update expected at most 1 argument, got 2
a.update({"year":2026,"month":7})
a
{'course': 'python', 'instute': 'codegnan', 'year': 2026, 'month': 7}
a.update({"name":"vijitha"})
a
{'course': 'python', 'instute': 'codegnan', 'year': 2026, 'month': 7, 'name': 'vijitha'}
# default()-> it doesnot follow the dictionary rules
a = {"year":2026,"month":7}
a.setdefault("date",2)            
2
a         
{'year': 2026, 'month': 7, 'date': 2}
a = {'year': 2026, 'month': 7, 'date': 2}            
a.pop()             
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("year")            
2026
a             
{'month': 7, 'date': 2}
a.popitem()            
('date', 2)
a           
{'month': 7}
# get() ->read            
a = {"university":"kl","branch":"it"}             
a.get("university")            
'kl'
a             
{'university': 'kl', 'branch': 'it'}
a.get("cse")            
a 
{'university': 'kl', 'branch': 'it'}
a["cse"]            
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a["cse"]
KeyError: 'cse'
a = {"hour":12,"min":1,"sec":46}
a.copy()
{'hour': 12, 'min': 1, 'sec': 46}
a     
{'hour': 12, 'min': 1, 'sec': 46}
a.clear()
             
a
             
{}
b = {}
             
b.update({"name":"vijitha"})
             
b
             
{'name': 'vijitha'}
a = {'course': 'python', 'instute': 'codegnan', 'year': 2026, 'month': 7, 'name': 'vijitha'}
             
len(a)
             
5
>>> a.count("name")
...              
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.count("name")
AttributeError: 'dict' object has no attribute 'count'
>>> 
>>> a = {"name":"vijitha","city":"vij","name":"shobha"}
...              
>>> a
...              
{'name': 'shobha', 'city': 'vij'}
>>> # it will print the update value
...              
>>> a = {"name":"vijitha","city":"vij","name":"vijitha"}
...              
>>> a
...              
{'name': 'vijitha', 'city': 'vij'}
>>> a = {"name1":"vijitha","city":"vij","name2":"shobha"}
...              
>>> a
...              
{'name1': 'vijitha', 'city': 'vij', 'name2': 'shobha'}
>>> a = {"idnos":[10,20,30],"name":["vijitha","jeenith","hari"],"marks":[60,70,80]}
...              
>>> a
...              
{'idnos': [10, 20, 30], 'name': ['vijitha', 'jeenith', 'hari'], 'marks': [60, 70, 80]}
>>> type(a)
...              
<class 'dict'>
>>> a.keys()
...              
dict_keys(['idnos', 'name', 'marks'])
>>> a.values()
...              
dict_values([[10, 20, 30], ['vijitha', 'jeenith', 'hari'], [60, 70, 80]])
>>> a.items()
...              
dict_items([('idnos', [10, 20, 30]), ('name', ['vijitha', 'jeenith', 'hari']), ('marks', [60, 70, 80])])

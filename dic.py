#1.create a dictionary from two lists:
#    keys = ['name', 'age']
#    values = ['101', 'john',25]

keys = ['id', 'name', 'age']
values = ['101', 'john', 25]
res=dict(zip(keys, values))
print(res)
output:
# {'id': '101', 'name': 'john', 'age': 25}

#2.create a dictionary to store name age.
res = [{"name": "sindhu", "age": "23"},{"name": "pandu", "age": "23"}]
print(res)
# output:
# [{'name': 'sindhu', 'age': '23'}, {'name': 'pandu', 'age': '23'}]

#3.create an empty dictionary and add key value pairs one by one:
res=dict()
spc["name"]=input("Enter name: ")
spc["pin"]=input("Enter pin: ")
spc["city"]=input("Enter city: ")
res.append(spc)
print(res)
   output:
enter name: sindhu
# enter pin: 502034
# enter city: hyderabad

#4.get the value of key "salary"from this dictionary:
#                    ex:employee={"name": "john", "salary": 5000, "age": 25}
employee = {"name": "pandu", "salary": 5000, "age": 25}
print(employee['salary'])
# output:
# 5000

#5.remove the last inserted key-value pair from the dictionary usingan appropriate method
res = {"name": "pandu", "salary": 5000, "age": 25}
res.popitem()
print(res)
# output:
# {'name': 'pandu', 'salary': 5000}

#7.define packing and unpacking in python. also,provide an example for both packing and unpacking

packing:
  packing refers to the process of putting multiple values into a single variable (usually a tuple or list). 
example:
data=("pandu", 25, "hyderabad")
print(data)
# output:
# ('pandu', 25, 'hyderabad')
 
 unpacking:
data=("pandu", 25, "hyderabad")
data=name, age, city
print(name)
print(age)
print(city)
# output:
# pandu
# 25
# hyderabad



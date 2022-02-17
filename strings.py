#Multiline strings
a = "A glass plate is taken.A fine powder of the micro particle is sprayed on the glass "
print(a)
#Looping in strings 
a  =  ['banana','apple','orange']
for x in a:
  print(a)
#String length
a  = "Hello world"
print(len(a))
#check string
a  = "A glass plate is taken and used in the table"
print("glass" in a)
#check if 
a  = "I printed a large number of lines"
if 'large' in a :
  print("Yes,free is present")
#check if not  
a  = "Things present in the world are free"
print('expensive ' not in a)
b  = "we should allow animals to live their life"
if 'expensive' not in b:
  print("yes,it is not in b")
#slicing the string
a  = "hello world"
print(a[2:5])
#slice to the start
a = "hello world"
print(a[:5])
#slice to the end
a = "hello world"
print(a[2:])
#negative slicing
a = "hello world"
print(a[-5:-2])
#Modifying the strings
a  = "Hello world"
print(a.upper())
#Lower case
a  = "hello world"
print(a.lower())
#replacing
a = "hello world"
print(a.replace('o','oo'))
#split
a = "hello,world"
print(a.split(','))
#strip
a = "hello,world   "
print(a.strip())
#string concatenation
a = "hello"
b = "world"
print(a+b)
#string concatenation with space
a = "hello "
b = "world"
print(a + ''+b)
#string format
age  = 36
a = "my name is john, my age is {}"
print (a.format(age))
#format using Indexing
quantity = 5
itemno = 234
price = 24324.342
print("The {} pieces of the item {} costs {} rupeees".format(quantity,itemno,price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#Escape characters 
print("The colombus is a great person, who invented \"America\"")


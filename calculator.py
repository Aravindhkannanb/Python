x = float(input("Enter the Number a : "))
z = float(input("Enter the Number b : "))
print("1.addition\n2.Subtraction\n3.Multiplication\n4.division " )
y  = int(input('Enter any option :'))
if (y ==1 ):
  print(x+z)
elif(y==2):
  print(x-z)
elif(y==3):
  print(x*z)
elif(y==4):
  print(x/z)

else:
  print("Enter a valid number ")

'''
Exercise 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
number_1 = int(input('Please provide a number between 1 and 100:>>> '))
number_2 = int(input('Please provide a second number between 1 and 100:>>> '))

while number_1 < 0 or number_2 < 0 or number_1 > 100 or number_2 > 100 or number_1 == number_2:
     print('Numbers must be different values between 1 and 100, try again')
     number_1 = int(input('Please enter a number between 1-100:> '))
     number_2 = int(input('Please enter a number between 1-100:> '))
     else: 
           print('Numbers must be written in numerical form, try again')
          number_1 = int(input('Please enter a number between 1-100:> '))
          number_2 = int(input('Please enter a number between 1-100:> '))
          

if number_1 < number_2:
     for i in range (number_1, number_2+1):
       print(i, end=" ")

else:
    for i in range(number_2,number_1+1):
      print(i,end=' ')

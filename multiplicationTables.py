'''
Create a file that prints the times tables between 1-12
'''

for i in range (1,13):
   print('=============================')
   print()
   print(f'This is the {i} times table')
   print()
   for j in range (1,13):
      print(f'{j} x {i} = {j*i}')    

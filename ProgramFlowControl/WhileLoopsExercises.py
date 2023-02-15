# We're testing this one just to demonstrate how while loops work
for i in range(18, -4, -5):
    if i == 13:
        continue
    print(i, end=' ')
# Another one like Dj Khalid
for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
else:
    print('Else block of code')

print('\nAfter the for Loop')

# Check out this while loop
for letter in 'word':
    i = 3
    while i > 0:
        i -= 1
        print(letter, end='')
    print('')
# From the quiz
x = 5
while x > 0:
    x -= 1
else:
    print('Bye!')

#Coding Exercise
# Solution 1
my_sum = 0
x = 100
while x:
    if x % 2 != 0:
        my_sum += x
    x -= 1

print(my_sum)


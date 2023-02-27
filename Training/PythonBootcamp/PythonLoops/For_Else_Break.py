for letter in "Python":
    if letter == "o":
        print("letter is o and I\'m breaking out of the loop....")
        break
        print(letter)

# Also check what this code does
for letter in 'pythoooon!!!':
    if letter == 'o':
        break
    print(letter, end='')
else:
    print('Go!')

# Check this one out
nums = [1, 2, 4, 7, 8]
s = 0
for n in nums:
    s += n
    if s >= 4:
        break
print(f's={s}')

# Check this for
for x in range(7):
    if x == 3 or x == 6:
        continue
    print(x, end='#')

# Eish this for lops,they require attention like an insecure girlfriend
for i in range(18, -4, -5):
    if i == 13:
        continue
    print(i, end=' ')
# Another one like DJ Khaled
for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
else:
    print('Else block of code')
print('\nAfter the for Loop')
# On and on and on
for i in range(10):
    print(i, end=' ')
    if i == 5:
        break
    else:
        print('Else block of code')
print('\nAfter the for Loop')

# Exercise 12 Using a for loop and the range() function, calculate the sum and the product of the numbers between 1
# and 25  (both included). Store the calculated values in two variables called my_sum and my_product. Print the
# values of my_sum and my_product variables
my_sum = 0
my_product = 1

for no in range(1, 26):
    my_sum = my_sum + no  # add each no. in the range to my_sum
    my_product = my_product * no  # multiply each no. in the range by my_product

# Printing the variables
print(my_sum)
print(my_product)

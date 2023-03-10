import random
import matplotlib.pyplot as plt
#You import random module to generate random numbers
#Then import matplotlib.pylot module to draw

#We define our function here and give it NumOfBars as parameter
def DrawBars(NumOfBars):
    heights = []
    for i in range(NumOfBars):
        heights.append(random.randint(1, 10))
    plt.bar(range(NumOfBars), heights)
    plt.show()

#You prompt the user for number of bars to generate
#Then you assign that value to
NumOfBars = int(input("Enter the number of bars to generate: "))
DrawBars(NumOfBars)

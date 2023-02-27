msg ="Hey ,lets see what age category you are in !"
print(msg)

#prompting the user for an input
name =input("What is your name ? : ")
surname =input("What is your surname ? : ")

age =input("How old are you ? : ")
age =int(age)
print("")

category = " "

#print('Hellow '+ name + ' aged ' + str(age) + ' years old.' )

#Playing with if statements
if age < 18 :
 category ="Junior"
elif age >= 18 and age <40 :
 category ="Open"
else:
    category="Veteran"

#For loop
print("Here is the a list of age categories :")
print("======================================")
CategoryDesc =["Junior","Open","Veteran"]
for CatDesc in CategoryDesc:
    print(CatDesc)

print("======================================")
#Print their name,age and category
print('Hellow '+ name + ' aged ' + str(age) + ' years old. Your are in ' + str(category) + " category !" )


#Function to display the same output
def MyFunction(name :str , age:int ,category:str) -> str :
   OutPutMessage = "Hellow " + name + ' aged ' + str(age) + ' years old. Your are in ' + str(category) + " category !"
   return OutPutMessage

print(MyFunction(name,age,category))




#2023.12.17 
#Author:Ceyda Disli
#Purpose: I aim to learn Python, GitHub 

variable_name= "hello THIS is My Name CEYDA disli"
#print(variable_name.title())
#print(variable_name.lower())
#print(variable_name.upper())

first_name = "uraz"
last_name = "disli"
full_name = first_name + " " + last_name
message = "Hello," + full_name.title()  + "!"
#print(message)
fruits = "Fruit List of the Day:\n\tOrange\n\tBanana\n\tApple"
#print(fruits)
fruits = "           Fruits List:\n\tLemon\n\tOrange      "
#print(fruits)
fruits = (fruits.rstrip())
#print(fruits)
fruits = fruits.lstrip() 
#print(fruits)
fruits= fruits.strip()
#print(fruits)

new_line = "Python has a varied List's of Code"
#print(new_line)


calculate = int(1+8*3/2**3)
#print(calculate)

#Adding calculations

n1 = 1+4
n2 = 5**2+2
n3 = 5+2
n4=  9+4

#print(n1) 
#print(n2)
#print(n3)
#print(n4)

new_word = "My favorite number is " + str(n4) +"!" + " Congrats!"
#print(new_word)

#import this

list = ['flower','table','cabinet','shoes']
print(list)
print(list[0])
print(list[0].title())
print(list[-1])
print(list[-2].lower())


customers = ['Ceyda Disli','Berk Disli','Uraz Disli']

print(customers[0])
print(customers[-1])

print("Dear " + (customers[-1]).title() + "," + 
                   " You have received a gift. Follow the steps to log in:\n\t*Open your account\n\t*Login your password" )
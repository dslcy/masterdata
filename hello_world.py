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
#print(list)
#print(list[0])
#print(list[0].title())
#print(list[-1])
#print(list[-2].lower())


customers = ['Ceyda Disli','Berk Disli','Uraz Disli']

#print(customers[0])
#print(customers[-1])

#print("Dear " + (customers[-1]).title() + "," + 
 #                  " You have received a gift. Follow the steps to log in:\n\t*Open your account\n\t*Login your password" )

#Changing an element's name on the list 

customers[-1]= 'U Disli'
#print(customers)


#append adds values to the end of a list 

mylist = []
mylist.append('domates')
mylist.append('peynir')
mylist.append('yumurta') 
mylist.append('yumurta') 

#insert adds values to a position you want and move the other elements one by one. 

mylist.insert(0,'zeytin')

#print(mylist)

del mylist[0]
#print(mylist)


last = mylist.pop(1)
#print(last)

#print('Kahvaltida en cok sevdigim sey ' + last.title() + "'" +"dir.")


#remove() only removed the first appearence on the list. To remove the others you need to run a loop


removed_item = 'yumurta'

mylist.remove(removed_item)

#print(mylist)


#Inviting people to dinner

guest_list = []

guest_list.append('Zuhal Ugur')
guest_list.append('Berk Disli')
guest_list.append('Sadi Ugur')

#print(guest_list)

#print("Dear " + guest_list[0] + ' I invite you to a dinner')
#print("Dear " + guest_list[1] + ' I invite you to a dinner')
#print("Dear " + guest_list[2] + ' I invite you to a dinner')

guest_list.remove('Zuhal Ugur')
guest_list.append('Hande Ugur')


#print("Dear " + guest_list[0] + ' I invite you to a dinner')
#print("Dear " + guest_list[1] + ' I invite you to a dinner')
#print("Dear " + guest_list[2] + ' I invite you to a dinner')

guest_list.insert(2,'Meral')
guest_list.insert(0,'Arda')
guest_list.append('Sare')

#print(guest_list)
#print("Dear " + guest_list[0].title() + ' We have more space now!')
#print("Dear " + guest_list[1].title() + ' We have more space now!')
#print("Dear " + guest_list[2].title() + ' We have more space now!')
#print("Dear " + guest_list[3].title() + ' We have more space now!')
#print("Dear " + guest_list[4].title() + ' We have more space now!')
#print("Dear " + guest_list[5].title() + ' We have more space now!')

#print(guest_list)


removed = guest_list.pop(0)

#print('Dear ' + removed + ' Sorry, the table did not arrive on time')

#print(guest_list)



removed_=guest_list.pop(0)

#print('Dear ' + removed_ + ' Sorry, the table did not arrive on time')

#print(guest_list)

removed__=guest_list.pop(0)

#print('Dear ' + removed__ + ' Sorry, the table did not arrive on time')

#print(guest_list)

removed___=guest_list.pop(0)

#print('Dear ' + removed___ + ' Sorry, the table did not arrive on time')

#print(guest_list)

#print("Dear " + guest_list[0].title() + ' You are still invited!')
#print("Dear " + guest_list[1].title() + ' You are still invited!')


del guest_list[0:2]

#print(guest_list)



###### New List

cars = []

cars.append('mitsubishi')
cars.append('honda')
cars.append('toyota')
cars.append('volkswagen')

#print(cars)
cars.sort()
#print(cars)
cars.sort(reverse= 'TRUE')
#print(cars)

#print(sorted(cars))
#print("Here is the original list again:")



# Places i want to see
cities = ['Madrid','Barcelona','Holland','Istanbul']
print(sorted(cities))
print(sorted(cities, reverse='TRUE'))
print(cities)

cities.reverse()
print(cities)

cities.sort(reverse='TRUE')
print(cities)

print('I will be travelling ' + str(len(cities))+ ' new places')
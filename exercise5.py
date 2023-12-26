available_toppings = ('mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese')
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']


for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(requested_topping + ' is added to your pizza')
    else:
        print(requested_topping + ' is not available at the moment')
print('your pizza is ready!')


users = ['Ceyda','Berk','Admin','Uraz','Maymun']

for user in users:
    if user == 'Admin':
        print('Hello ' + user + ' Would you like to see a status report?')
    else:
        print('Welcome '+ user )





users = []

if users: 
    for user in users:
        if user =='Admin':
            print('Hello' + user + 'Would you like to have a status report?')
        else: 
            print('Welcome' + user)

else: 
    print('We need to find')



current_usernames = ['John','Adele', 'CELINE', 'JACK'] 
new_usernames = ['JOHN','Clara','Adele','celine','Mahmut']

current_usernames_title = [user.title() for user in current_usernames]
new_usernames_title = [user.title() for user in new_usernames]

print(current_usernames_title)
print(new_usernames_title)


for users in new_usernames:
    if users in current_usernames_title:
        print('You need to find another name')
    else:
        print('The ' + users + ' is available')
        


numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers: 
    if number == 1:
        print(str(number)+'th')
    elif number == 2: 
        print(str(number)+'nd')
    elif number == 3:
        print(str(number)+'rd')
    else:
        print(str(number)+'th')

        
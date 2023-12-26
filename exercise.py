age = 17

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")





favorite_fruits = ['blueberries','apple','banana']

if 'apple' in favorite_fruits:
    print('you are chosen apple')
if 'grapes' in favorite_fruits:
    print('you are chosen grapes')




requested_toppings = ['olives','mushrooms','egg','salami']


for requested_topping in requested_toppings:
    if requested_topping == 'olives':
        print('sorry we are out of' + requested_topping)
    else:
        print('adding the ' + requested_topping)


toppings= []

if toppings:
    for topping in toppings:
        print('adding' + topping)
    else:
        print('are you sure you want a plain pizza')


requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")




    
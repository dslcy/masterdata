

magicians = ['Harry Potter', 'Berk Disli', 'Uraz Disli']

for magician in magicians:
    print('That was a great trick, Welldone ' + (magician).lower() + '.\n')

print("Thank you, everyone. That was a great magic show!")


animals = ['dog','bird','fish','parrot']

for animal in animals:
    print("I love " + animal.title() + '.They are very cute' + '.\n\t' )
print('I love animals.')



for number in range(1,6):
    print(number)

list_numbers = list(range(1,7))    
print(list_numbers)


#Square

squares = [] 

for value in range(1,11):
    square= value**2
    squares.append(square)
print(squares)

#Square second way 
new_square=[]

for value in range(1,11):
    new_square.append(value**2)

print(new_square)


#Digits
digits = [1,2,3,4,5,6,7,8,9]

print(max(digits))
print(min(digits))
print(sum(digits))


#list comprehensions

squarex = [value**2 for value in range(1,11)]
print(squarex)


#Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive

values = []

for value in range(1,21):
    values.append(value)
print(values)


millions = []

for million in range(1,1000001):
    millions.append(million)
print(millions)

print(max(millions))
print(min(millions))
print(sum(millions))


odd_numbers = [] 

for odd in range(1,21,2):
    odd_numbers.append(odd)

print(odd_numbers)


multiples = []

for multiple in range(3,31,3):
    multiples.append(multiple)

print(multiples)


cubes=[cube**3 for cube in range(1,11)]
print(cubes)


cubex = []

for cube in range(1,11):
    cubex.append(cube)

print(cubex)
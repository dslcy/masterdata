dictionaries = {'user':'ceyda','age':5}

(dictionaries['user']) = 'berk'

(dictionaries['eye']) = 'blue'

del dictionaries['eye']
print(dictionaries)



print('The username is now\n'+ dictionaries['user'])

alien={'xposition':0, 'yposition':25, 'speed':'medium'}

alien['speed'] = 'fast'

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien['speed'] == 'slow':
    move = 1 
elif alien['speed'] =='medium':
    move=2 
else:
    move = 3


alien['xposition'] = alien['xposition'] + move

print('This is the alien new speed:' + str(alien['xposition']))





people = {'name': 'Berk',
           'last_name':'Disli',
           'age':31, 
           'city':'Berlin',
           }

print(people['name'])
print(people['last_name'])
print(people['age'])
print(people['city'])


favorite_numbers = {'ceyda':7,
                    'berk':8,
                    'uraz':2,
                    'deniz':5,
                    'enes':4}

print('Deniz fav num is ' + str(favorite_numbers['deniz']))


codes = {'remove':'it is used to remove values', 
         'del':'it is used to delete values',
         'append':'it is used to add new stuff',
         'title': 'it is used to capitalize the first letter'}

print ('Remove is a line and\n' +codes['remove'].upper())









favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name)

    if name in friends:
        print('Hi '+ name.title() + ' I see your favorite language is:' +'\n' + favorite_languages[name])


if 'berk' not in favorite_languages.keys():
    print('Berk please join us')



days =  {'Wednesday':'boring', 
         'Purple':'fun',
         'Monday':'funnier',
           'Monday':'funnier',
             'Monday':'funnier',
               'Monday':'funnier'
               }

for day,mood in sorted(days.items()):
    print('My mood today is '+ mood+ ' on '+ day )




for key,value in codes.items():
    print(key + ' is a python code' + value )



country_river = {'germany':'bro', ' france':'kro', 'turkey':'hirzo', 'egypt':'nil','germany':'llo','germany':'bdo' }

for country , river in country_river.items():
    print(country + 'has the river called' + river) 

for country  in country_river.keys():
    print(country)     

for river  in country_river.values():
    print(river)     



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }


for language in set(favorite_languages.values()):
    print(language)


poll = ['sarah','kenan','edward','berk']

for name in set(favorite_languages.keys()):
    if name in poll:
        print('Well done ' + name)
    else:
        print(name + ' you need to join the survey')












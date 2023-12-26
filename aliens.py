aliens = []


for alien in range(30):
    new_alien = {'color':'yellow', 'speed':'medium', 'point':5}
    aliens.append(new_alien)

   # print(aliens)

#print(aliens)
#print(len(aliens))



for alien in aliens[0:3]:
    if alien['color'] == 'yellow':
     alien['color'] = 'green'
     alien['speed'] = 'medium'
     alien['points'] = 10

print(aliens[0:5])



favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }


for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print('\n' + name + ' has more than one language:\n')
        for language in languages:
            if len(language)>1:
                print(language)
    else:
        print('\n' + name + ' has only one language:\n')
        print(language)




                         
## 
        
users_usa = {'cey':{'firstname':'Ceyda',
                'last_name':'disli' , 
                'location':'Disney', 
                'age':56}, 
         'ber':{'firstname':'Berk',
                'last_name':'disli',
                'location':'Canakkale',
                'age':45}}


users_uk = {'mel':{'firstname':'Melis',
                'last_name':'Yuksel' , 
                'location':'Mugla', 
                'age':23}, 
         'den':{'firstname':'Deniz',
                'last_name':'Artan',
                'location':'Bursa',
                'age':22}}

users_tr = {'han':{'firstname':'Hande',
                'last_name':'coskun' , 
                'location':'Cizre', 
                'age':33}, 
         'eb':{'firstname':'Ebru',
                'last_name':'Danaci',
                'location':'Istanbul',
                'age':35}}





list_of_dic = [users_tr,users_uk,users_usa]

for user, user_info in  (list_of_dic[0]).items():
        print((user_info['firstname'].title() +' '+ (user_info['last_name'].title())) + 
              ' is from ' +
                user_info['location'].title() + 
                ' and ' + str(user_info['age']) + 
                ' is years old. ')
        

#for user, user_info in user.items():
 #   print('\nUsername:' + user +'\n')
  #  full_name = user_info['firstname'] + ' ' + user_info['last_name']
   # print(full_name)
   # print('Fullname: ' + full_name.title() + ' is from ' +user_info['location']) 

                           


favorite_places = {'ceyda':['istanbul','mugla'], 'uraz':['geyikli','sariyer'], 'hande':['cizre'],'ebru':['umraniye']}

for name,place in favorite_places.items():
    print(name + 's favorite place is' )

    for place_name in place:
        print(place_name)


favorite_numbers = {'ceyda':{'age':[25] , 
                             'place': ['istanbul','mugla'],
                             'hair' : ['purple', 'curly']}, 

                           'uraz':{'age':[1] , 
                             'place': ['canakkale','berlin'],
                             'hair' : ['brown', 'straight']} , 


                           'berk':{'age':[21] , 
                             'place': ['luleburgaz','paris'],
                             'hair' : ['black', 'straight']} } 

favorite_numbers['melis'] =  {'age':[25] , 
                             'place': ['istanbul','mugla'],
                             'hair' : ['purple', 'curly']}

print(favorite_numbers)

del favorite_numbers['melis']
print(favorite_numbers)


favorite_numbers['berk']['age'] = [43]
print(favorite_numbers)



for key , value in favorite_numbers.items():
    print(key + 's data is like this:') 
    for user, user_info in value.items():
        for data in user_info:
            if user == 'age':
                print('User Age: ' + str(data) )
            elif user == 'place':
                print('User Location: ' + str(data) )
            elif user == 'hair':
                print('User Hair: ' + str(data) )
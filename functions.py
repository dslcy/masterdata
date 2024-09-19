#def display_message():
 #   print('I am learning functions in python')

#display_message()

#def favorite_books(title):
 #   print('This is my fav book: ' + title.title())

#favorite_books('Alice in Wonderland')


#def make_shirt(size = 'MEDIUM',writing = 'I LOVE PYTHON'):
 #   print('\nThe size of the shirt is ' + size + '\nIt says' + writing +' Ha ha')
#make_shirt()
#make_shirt(writing='BOO')

#make_shirt('34','No need to be here')   
#make_shirt(size='34', writing='No need to be here')


#def countries(city,country='Germany'):
 #   print(city.title() + ' is in ' + country)


#countries(city='Berlin')
#countries(city='Dusselforf')
#countries(city='Ghent',country='Belgium')


#def make_album(artist_name, album_title, records = ''):
 #   dictionary = {'artist' : artist_name, 'album': album_title}
  #  if records != '':
   #     dictionary['records'] = records

   # return dictionary


#album = make_album('Tarkan', 'Kis Gunesi','393')

#print(album)



#Defining a Function 


#def make_album(artist, title, tracks=''):
 #   album_info = {'artist':artist, 'title':title}

  #  if tracks!= '':
   #      album_info['tracks'] = tracks

   # return album_info

#user_albums = []

#while True:    
 #   artist = input('\n What is your favorite album?')
  #  artist += input('\n Q id you do not want to answer')

   # if artist == 'q':
   #      break
    

   # title = input('\n What is your producer?')
   # title += input('\n Q id you do not want to answer')

    #if title == 'q':
     #    break
    
    #tracks = input('\n How many times have you seen that movie?')
   # tracks += input('\n Q id you do not want to answer')

 #   if tracks == 'q':
#         break        

  #  album_info = make_album(artist,title,tracks)

   # user_albums.append(album_info)

#print("\nUser Albums:")
#for album in user_albums:
 #   print(album)







def make_album(artist_name,album_title,tracks=''):

      dictionary = {'artist_name':artist_name, 'album_title':album_title}
      if tracks !='':
           tracks=int(tracks)
           dictionary['tracks'] =tracks
      return dictionary
user_albums=[]

while True:
    artist_name = input("\nType 'Q' if you want to quit\nWhat is the name of the artist?")
           
           
    if artist_name.lower() =='q':
        break

    album_title = input("\nType 'Q' if you want to quit\nWhat is the name of the album? ")

    if album_title.lower() =='q':
        break
      
    tracks = input("\nType 'Q' if you want to quit\nHow many times have you listened? ")

    if tracks.lower() =='q':
        break

    dictionary = make_album(artist_name, album_title, tracks)
    print(dictionary)

    user_albums.append(dictionary)

print("\nUser Albums:")
for album in user_albums:
    print(album)






import json, urllib.request
import spotipy 
import webbrowser 

username = '31c3wysbw735b237nkwwi5xzsnla'
clientID = '2704fff2eda84dcfb8924cf6f61541ba'
clientSecret = 'a4de74be2cf0415d9a576b6cb9758b94'
redirect_uri = 'http://google.com/callback/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri) 
token_dict = oauth_object.get_access_token() 
token = token_dict['access_token'] 
print("-----------------------------------")
print(token_dict)
spotifyObject = spotipy.Spotify(auth=token) 
user_name = spotifyObject.current_user() 

# To print the JSON response from 
# browser in a readable format. 
# optional can be removed 
print(json.dumps(user_name, sort_keys=True, indent=4)) 

while True: 
	print("Welcome to the project, " + user_name['display_name']) 
	print("0 - Exit the console") 
	print("1 - Select Playlist") 
	user_input = int(input("Enter Your Choice: ")) 
	if user_input == 1: 
		playlist_list = ['7H6gu7y5AkuZPxd3bPM3N6', '7H6gu7y5AkuZPxd3bPM3N6']
		search_Playlist = int(input("Select playlist: ")) 
		print(type(search_Playlist))
		playlist_id = playlist_list[search_Playlist] 
		webbrowser.open("https://open.spotify.com/playlist/"+playlist_id)
		
		# track_uris = []
		# for track in spotifyObject.playlist_tracks(playlist_id)['items']:
		# 	# print(track['external_urls']['spotify'])
		# 	# print(type(track['track']['uri']))
		# 	# song_id = track['track']['uri'].split("spotify:track:")
		# 	song_id = track['track']['name']
		# 	# song = "https://open.spotify.com/album/"+str(song_id[1])
		# 	print(song_id)
			# with urllib.request.urlopen(song) as url:
			# 	data = json.load(url)
			# 	print(data)
        
             
			# track_uris.append(track_uri)
			# print(track['track']['name'])
		# results = spotifyObject.search(search_song, 1, 0, "track") 
		# songs_dict = results['tracks'] 
		# song_items = songs_dict['items'] 
		# song = song_items[0]['external_urls']['spotify'] 
		# webbrowser.open(song) 
		# print('Song has opened in your browser.') 
	elif user_input == 0: 
		print("Good Bye, Have a great day!") 
		break
	else: 
		print("Please enter valid user-input.") 



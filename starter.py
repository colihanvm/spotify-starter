#	Vanessa Colihan 2020
#	pulls all of current users playlists in
#	creates directory of files with Spotify song IDs
#	each file represents a playlist

import sys, os

import spotipy
import spotipy.util as util

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        # print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
        #     track['name']))
        print(track['id'])

if __name__ == '__main__':        
	if len(sys.argv) > 1:
	    username = sys.argv[1]
	else:
	    print("Usage: %s username" % (sys.argv[0],))
	    sys.exit()

	scope = 'playlist-read-private'
	token = util.prompt_for_user_token(username, scope)

	if token:
	    sp = spotipy.Spotify(auth=token)
	    sp.trace = False
	    playlists = sp.user_playlists(username)
	    for playlist in playlists['items']:
		    if playlist['owner']['id'] == username:
		        print()
		        print(playlist['name'])

		        if not os.path.exists('songs'):
		        	os.mkdir('songs')

		        filename = 'songs/' + playlist['name'] + '.txt'
		        
		        f = open(filename, "w")

		        results = sp.playlist(playlist['id'],
		            fields="tracks,next")
		        
		        tracks = results['tracks']
		        
		        # show_tracks(tracks)

		        for item in tracks['items']:
		        	f.write(item['track']['id'] + '\n')

		        f.close()

		        while tracks['next']:
		            tracks = sp.next(tracks)
		            #show_tracks(tracks)
	   
	else:
	    print("Can't get token for", username)

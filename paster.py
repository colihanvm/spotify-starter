#	Vanessa Colihan 2020
#	reads files created by starter.py
#	creates playlists for current user

import sys, os

import spotipy
import spotipy.util as util


if __name__ == '__main__':        
	if len(sys.argv) > 1:
	    username = sys.argv[1]
	else:
	    print("Usage: %s username" % (sys.argv[0],))
	    sys.exit()

	scope = 'playlist-modify-private'
	token = util.prompt_for_user_token(username, scope)

	if token:
	    sp = spotipy.Spotify(auth=token)
	    sp.trace = False
	    
	    playlists = os.listdir('songs/')

	    for playlist in playlists:
	    	name = playlist[:playlist.find('.')]

	    	f = open('songs/' + playlist, "r")

	    	pid = sp.user_playlist_create(username, name, public=False, description="automatically generated from blah blah blah")['id']
	    	print(pid)
	    	tracks = f.readlines()
	    	for i in range(0, len(tracks)):
	    		tracks[i] = tracks[i][:-1]
	    	#print(tracks)

	    	sp.user_playlist_add_tracks(username, pid, tracks)
	    	f.close()
	    
	   
	else:
	    print("Can't get token for", username)

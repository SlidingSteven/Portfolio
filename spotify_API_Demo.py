# more info on spotipy- https://github.com/plamere/spotipy
import spotipy
import spotipy.util as util
import json
from pprint import pprint
import config #this file has my clientID, secret and username

client_id = getattr(config, 'client_id', 'default value if not found')
client_secret = getattr(config, 'client_secret', 'default value if not found')
username = getattr(config, 'username', 'default value if not found')
token = util.prompt_for_user_token(username,
                                   scope = 'user-read-currently-playing',
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri='http://127.0.0.1:5000/spotify')
spotify = spotipy.Spotify(auth=token)

# if the account is currently playing a song, retun the song name, artist name, cover art
    # this is done in HTML so it can be served easier to a widget page I worked on a while back
# else return not playing
def get_current_song():
    res = spotify.current_user_playing_track()
    s1 = json.dumps(res)
    parsed = json.loads(s1)
    #pprint(parsed)
    if res is not None and res["is_playing"]:
        currBest = None
        for image in res['item']['album']['images']:
            if image['height']==300:
                currMax = image['height']
                currBest = image
        image_html = '<img src="' + currBest['url'] + '" alt="Current-Cover-Art" >'
        return [res['item']['name'] + ", by " + res["item"]["artists"][0]["name"] + "<br>" + image_html, currBest['url']]
    else:
        print("not playing")
        return ["Not Playing", "Not Playing"]

print(get_current_song())
# --- example output ---
# ['Blue Eyes Crying In the Rain, by Willie Nelson<br><img src="https://i.scdn.co/image/ab67616d00001e020e5489389aa853f454a4b1e8" alt="Current-Cover-Art" >', 'https://i.scdn.co/image/ab67616d00001e020e5489389aa853f454a4b1e8']
# ['Not Playing', 'Not Playing']

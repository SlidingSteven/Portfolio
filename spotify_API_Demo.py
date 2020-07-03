# more info on spotipy- https://github.com/plamere/spotipy
import spotipy
import spotipy.util as util
import json
from pprint import pprint
import config 

client_id = getattr(config, 'client_id', 'default value if not found')
client_secret = getattr(config, 'client_secret', 'default value if not found')
username = getattr(config, 'username', 'default value if not found')
token = util.prompt_for_user_token(username,
                                   scope = 'user-read-currently-playing',
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri='http://127.0.0.1:5000/spotify')
spotify = spotipy.Spotify(auth=token)

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


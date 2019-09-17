from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
API = tweepy.API(auth)

Tweet = namedtuple('Tweet', 'id_str created_at text')

class UserTweets(object):
    """TODOs:
    - save tweets to csv file in data/ subdirectory
    - implement len() an getitem() magic (dunder) methods"""

    def __init__(self, handle, max_id=None):
        self.handle = handle
        self.max_id = max_id
        self.output_file = f"{os.path.join(DEST_DIR, handle)}.{EXT}"
        self.tweets = list(self._get_tweets())
        self._save_tweets = self.save_tweets()

    def _get_tweets(self):
        tweets = API.user_timeline(screen_name=self.handle, count=NUM_TWEETS, max_id=self.max_id)
        return (Tweet(s.id_str, s.created_at, s.text.replace('\n', '')) for s in tweets)

    def save_tweets(self):
        with open(self.output_file, 'w') as f:
            write = csv.writer(f)
            write.writerow(Tweet._fields)
            write.writerows(self.tweets)

    def __len__(self):
        return len(self.tweets)

    def __getitem__(self, position):
        return self.tweets[position]
   
if __name__ == "__main__":
  for handle in ('pybites', '_juliansequeira', 'bbelderbos'):
      print('--- {} ---'.format(handle))
      user = UserTweets(handle)
      for tw in user[:5]:
          print(tw)
      print()

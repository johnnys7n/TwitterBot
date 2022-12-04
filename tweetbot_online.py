import tweepy
import time

auth = tweepy.OAuthHandler('',
                           '')
auth.set_access_token('',
                      '')

api = tweepy.API(auth)
user = api.me()

# Project 1: gets the home time line
public_tweets = api.home_timeline()


def get_timeline():
    for tweet in public_tweets:
        print(tweet.text)

# function to curb api overload


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep()
    except StopIteration:
        break

# Project 2: follow bot for given criteria


def follow_bot():
    try:
        for follower in limit_handler(tweepy.Cursor(api.followers).items()):
            if follower.follower_count >= 100:
                print(f'I just followed {follower.name}')
                follower.follow():
            else:
                print(f'follower {follower.name} was not followed')
    except StopIteration as err:
        print(err.reason)
    except tweepy.TweepError as err:
        print(err.reason)


# Project 3: Likes twitter post based on certain keyword
search_string = 'keyword'
numberOfTweets = 2


def twitter_liker(keyword):
    for tweet in tweepy.Cursor(api.search, keyword).items(numberOfTweets):
        try:
            tweet.favorite()
            print('I liked that tweet')
        except tweepy.TweepError as err:
            print(err.reason)
        except StopIteration:
            break

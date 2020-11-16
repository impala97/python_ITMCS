"""
Clootrack Assignment
Find most tweeted users
"""

__author__ = "Smit R. Mehta"
__author_email__ = "mehtasmit44@gmail.com"
__data__ = "21st Oct'20 20:36"


def main():

    def _prepare_user_tweet_data():
        """
        1. Get input from user
        2. appends a tweet_id in user's key value in user_tweet
        Required Data Form :: {'a': ['t1', 't3', 't4'], 'b': ['t2']}
        :return: {'a': ['t1', 't3', 't4'], 'b': ['t2']}
        """
        user_tweet = dict()
        # print("nos of input :: {}".format(nos_of_input))

        for i in range(nos_of_input):
            user, tweet_id = str(input()).split()
            _(user_tweet, user, tweet_id)
        # print("Required Data Form :: {}".format(user_tweet))
        return user_tweet

    def get_most_tweeted_users():
        """
        1. Prepares user tweets data dictionary by the number of times user has tweeted.
        e.g, {3: ['a'], 1: ['b']}
        2. Finds the max. tweeted count and it's users
        3. Join all users and nos. of tweet count e.g, "['a 3', 'b 1']"
        :return: ['a 3', 'b 1']
        """
        tweet_count_by_users = dict()
        for user, tweet in user_tweet_data.items():
            nos_of_tweet = len(tweet)
            _(tweet_count_by_users, nos_of_tweet, user)
        # print("Tweet Count of Users :: {}".format(tweet_count_by_users))

        most_tweeted_count = max(tweet_count_by_users)  # Finds Max. number of tweet
        # print("Most Tweeted Users :: {}".format(tweet_count_by_users[most_tweeted_count]))

        return [" ".join([users, str(most_tweeted_count)]) for users in sorted(tweet_count_by_users[most_tweeted_count])]

    def _(dictionary, key, value):
        """
        if key presents in the dictionary then value will be append to the list,
        otherwise new key & list of value will be created in dictionary.
        :param dictionary: type dict
        :param key: type str
        :param value: type any
        :return: Nothing
        """
        if key in dictionary:
            dictionary[key].append(value)
        else:
            dictionary[key] = [value]

    nos_of_input = int(input())
    user_tweet_data = _prepare_user_tweet_data()
    return get_most_tweeted_users()


if __name__ == "__main__":
    nos_of_tests = int(input())
    results = []
    for i in range(nos_of_tests):
        [results.append(i) for i in main()]

    [print(result) for result in results]  # Prints the output of all test cases.
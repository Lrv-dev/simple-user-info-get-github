from requests import get
from json import loads

user = input('type the name of the user you want to search\n: ')

request = get(f'https://api.github.com/users/{user}')
json_response = loads(request.text)


print("""
Username: {}
Bio: {}
Location: {}
Avatar-url: {}
Mail: {}
Twitter: {}
Number of public repos: {}
Number of public gists: {}
Following: {}
Followers: {}
""".format(json_response['login'], json_response['bio'], json_response['location'],json_response['avatar_url'],json_response['email'],json_response['twitter_username'],json_response['public_repos'],json_response['email'],json_response['following'],json_response['followers']))

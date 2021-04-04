from requests import get
from json import loads

user = input('type the name of the user you want to search\n: ')

request = get(f'https://api.github.com/users/{user}')
json_response = loads(request.text)


print("""
Username: {0[login]}
Bio: {0[bio]}
Location: {0[location]}
Avatar-url: {0[avatar_url]}
Mail: {0[email]}
Twitter: {0[twitter_username]}
Followers: {0[followers]}
Number of public repos: {0[public_repos]}
Number of public gists: {0[public_gists]}
Following: {0[following]}
""".format(json_response))

import requests


def repos_with_most_stars():
    gh = "https://api.github.com/search/repositories"
    params = {"q": "stars:>50000"}
    response = requests.get(gh, params=params)
    response_json = response.json()["items"]
    return response_json


if __name__ == "__main__":
    # have a main method here
    results = repos_with_most_stars()

    for result in results:
        language = result['language']
        stars = result["stargazers_count"]
        name = result["name"]

        print(f"=> {name} is a {language} repo with {stars} stars")

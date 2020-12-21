import requests


def repos_with_most_stars():
    gh = "https://api.github.com/search/repositories"
    params = {"q": "stars:>50000"}
    response = requests.get(gh, params=params)
    response_json = response.json()
    print(response_json.keys())


if __name__ == "__main__":
    # have a main method here
    repos_with_most_stars()

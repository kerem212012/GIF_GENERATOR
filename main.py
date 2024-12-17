import requests
from environs import Env

def get_url(name):
    env = Env()
    env.read_env()
    api_key = env.str("API_KEY")
    params = {"api_key": api_key, "q": name, "limit": 1}
    response = requests.get(env.str("DB_URL"), params=params)
    response.raise_for_status()
    return response.json()["data"][0]["images"]["original"]["url"]


def get_gif(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content


if __name__ == '__main__':
    try:
        gif_name =input("Имя GIF:")
        with open(f"Downloads/{gif_name}.gif", "wb") as file:
            file.write(get_gif(get_url(gif_name)))


    except ConnectionError:
        print("Check your internet")
    except IndexError:
        print("Try something other")

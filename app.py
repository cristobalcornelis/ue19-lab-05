import requests

JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    try:
        response = requests.get(JOKE_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        setup = data.get("setup")
        punchline = data.get("punchline")

        if setup and punchline:
            print("Petite blague aléatoire:")
            print(setup)
            print(punchline)
        else:
            print("Le format de l'API n'est pas correcte")
            print(data)

    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'appel à l'API:")
        print(e)

if __name__ == "__main__":
    get_joke()

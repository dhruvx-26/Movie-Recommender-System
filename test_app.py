import requests

url = "https://api.themoviedb.org/3/movie/440"

params = {
    "api_key": "8265bd1679663a7ea12ac168da84d2e8",
    "language": "en-US"
}

try:
    response = requests.get(url, params=params, timeout=20)
    print("Status:", response.status_code)
    print(response.json())

except requests.exceptions.Timeout:
    print("TMDB connection timed out")

except requests.exceptions.RequestException as e:
    print("Error:", e)
import requests
from bs4 import BeautifulSoup

def get_top_scorers():
    url = "https://www.premierleague.com/stats/top/players/goals?se=-1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeatifulSoup(response.content, "html.praser")
        players = soup.find_all("tr", {"class": "top-player"})
        top_players = []
        for player in players:
            player_name = player.find("a", {"class": "playerName"}).text.strip()
            goals = player.find("span", {"class": "allStatContainer statgoals"}).text.strip()
        return top_scorers
    else:
        print("Failed to fetch data.")
        return None

def display_top_scorers(top_scorers):
    if top_scorers:
        print("Top Scorers in Premier League:")
        for idx, player in enumerate(top_scorers, start=1):
            print(f"{idx}, {player['Player']} - {player['Goals']} goals")
    else:
        print("No data available.")

if __name__ == "__main__":
    top_scorers = get_top_scorers()
    display_top_scorers(top_scorers)

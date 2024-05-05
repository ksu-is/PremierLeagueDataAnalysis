import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def get_top_scorers():
    url = "https://native-stats.org/competition/PL"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.content, "html.parser")
        players = soup.find_all("tr", {"class": "js-row"})
        top_scorers = []
        for player in players:
            player_name = player.find("a", {"class": "js-link"}).text.strip()
            goals = player.find("td", {"class": "jsx-3306694010 stats-value"}).text.strip()
            top_scorers.append(f"{player_name} - {goals} goals")
        return top_scorers
    except requests.RequestException as e:
        print("Failed to fetch data:", e)
        return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def show_top_scorers():
    top_scorers = get_top_scorers()
    if top_scorers is not None:
        # Create a new window
        window = tk.Tk()
        window.title("Premier League Top Scorers")
        
        # Create a listbox to display top scorers
        listbox = tk.Listbox(window, width=50, height=15)
        for idx, player in enumerate(top_scorers, start=1):
            listbox.insert(tk.END, f"{idx}. {player}")
        listbox.pack(padx=10, pady=10)
        
        window.mainloop()
    else:
        print("Failed to retrieve top scorers data.")

if __name__ == "__main__":
    show_top_scorers()

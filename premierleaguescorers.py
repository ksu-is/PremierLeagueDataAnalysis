import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def fetch_top_scorers():
    
    url = "https://fbref.com/en/stathead/player_comparison.cgi?request=1&sum=0&comp_type=spec&dom_lg=1&spec_comps=9&player_id1=1f44ac21&p1yrfrom=2023-2024&player_id2=dc7f8a28&p2yrfrom=2023-2024&player_id3=8e92be30&p3yrfrom=2023-2024&player_id4=aed3a70f&p4yrfrom=2023-2024&player_id5=e342ad68&p5yrfrom=2023-2024&player_id6=e77dc3b2&p6yrfrom=2023-2024&player_id7=92e7e919&p7yrfrom=2023-2024"
    response = requests.get(url)

 
    if response.status_code == 200:
       
        soup = BeautifulSoup(response.content, "html.parser")

        
        table = soup.find("table", {"class": "stats_table"})

        
        if table:
            
            rows = table.find_all("tr")

           
            top_scorers_window = tk.Toplevel(root)
            top_scorers_window.title("Top Scorers")

           
            tree = ttk.Treeview(top_scorers_window, columns=("Player", "Goals"), show="headings")
            tree.heading("Player", text="Player")
            tree.heading("Goals", text="Goals")
            tree.pack(fill="both", expand=True)

            
            for row in rows:
                
                player_cell = row.find("td", class_="left")
                if player_cell:
                    player_name = player_cell.get_text(strip=True)

                    
                    goals_cell = row.find("td", class_="right group_start")
                    if goals_cell:
                        goals = goals_cell.get_text(strip=True)

                        
                        tree.insert("", "end", values=(player_name, goals,))
        else:
            error_label.config(text="Table not found on the page.")
    else:
        error_label.config(text="Failed to retrieve the webpage.")


root = tk.Tk()
root.title("Premier Leage Top Scorers 2023/2024")


fetch_button = tk.Button(root, text="Fetch Top Scorers for 2023/2024", command=fetch_top_scorers)
fetch_button.pack(pady=10)


error_label = tk.Label(root, fg="red")
error_label.pack()

root.mainloop()

#Eli Baker
#Video Game Catalog Manager

import pandas as pd

#Have program read data in the CSV
games = pd.read_csv("video_games_raw.csv")

#Ask for row and display game
while True:
    row_text = input(f"Enter a row number (1–{len(games)}): ").strip()

    if row_text.isdecimal() and 1 <= int(row_text) <= len(games):
        position = int(row_text) - 1
        break

    print("Please enter a whole number in the range shown.")

print("Selected game:")
print(games.iloc[position])

#Change game status based on user input
new_status = input(
    "Enter a new status (Backlog, Playing, Completed, or Dropped): "
).strip().title()

row_label = games.index[position]
games.at[row_label, "Status"] = new_status

#Recommend games with the above eight ratings and under 40 bucks
games["Recommended"] = "No"

qualifies = (games["Rating"] >= 8) & (games["Price"] <= 40)
games.loc[qualifies, "Recommended"] = "Yes"

#Display them games that are recommended
recommended_games = games.query("Recommended == 'Yes'")

print("Recommended games:")
print(recommended_games[["Title", "Rating", "Price"]].to_string(index=False))

#Update the csv with the new data and games recommended
games.to_csv("video_games_cleaned.csv", index=False)
print("Saved the updated catalog to video_games_cleaned.csv.")
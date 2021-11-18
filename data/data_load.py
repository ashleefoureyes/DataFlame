import pandas as pd

# create panda dataframe from csv
df = pd.read_csv("data/olympic_womens_dataset.csv")

# Retrieve values filtered vales from generated dataframe
teams = df["Home Team"].unique()
players = df["Player"].unique()

# Create dataframe mapping team to players
mapped_players_df = pd.DataFrame({"Team": df["Team"].unique()})
mapped_players_df["Players"] = [list(set(df['Player'].loc[df['Team'] == x['Team']])) for _, x in mapped_players_df.iterrows()]


# show list of players based on team
def dynamic_players(team):
    players_df = (mapped_players_df.loc[mapped_players_df['Team'] == team])
    players_list = players_df["Players"]
    return players_list

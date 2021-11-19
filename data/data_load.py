import pandas as pd

# create panda dataframe from csv
df = pd.read_csv("data/olympic_womens_dataset.csv")

# unique team and player dataframes
teams = df["Home Team"].unique()
players = df["Player"].unique()
player_team = df[["Player", "Team"]].drop_duplicates()
player_event_details = df[["Player", "Team", "Event"]]
shot_event_details = df[["Player", "Event", "Detail 1", "Detail 2"]]
shot_event_details_loc = df[["Player", "Event", "Detail 1", "Detail 2", "X Coordinate", "Y Coordinate"]]

'''
DATAFRAME GENERATION
'''
# show list of players based on team
def dynamic_players(team):
    players_df = player_team[player_team.Team == team]
    return players_df


# Retrieve dynamic player detail data
def player_details(player):
    players_det_df = player_event_details[player_event_details.Player == player]
    return players_det_df


# shot details
def shot_details(player):
    shot_det_df = shot_event_details[(shot_event_details.Player == player) & (
                (shot_event_details.Event == "Shot") | (shot_event_details.Event == "Goal"))]
    shot_det_df.rename(columns={"Detail 1": "Shot Type", "Detail 2": "Shot Detail"}, inplace=True)
    shot_det_df.drop('Player', axis=1, inplace=True)
    return shot_det_df


# shot details for plotting on arena
def shot_details_for_plot(player):
    shot_det_df = shot_event_details_loc[(shot_event_details.Player == player) & (
                (shot_event_details.Event == "Shot") | (shot_event_details.Event == "Goal"))]
    shot_det_df.rename(columns={"Detail 1": "Shot Type", "Detail 2": "Shot Detail"}, inplace=True)
    return shot_det_df

# invert x and y values, scale to figure
#TODO - FIX SCALING TO ARENA FIGURE
def load_shooting_df(shot_dataframe):
    shot_dataframe = shot_dataframe.assign(
        X=shot_dataframe["Y Coordinate"].apply(lambda x: (((x - 42.5) * 500) / 85)).values)
    shot_dataframe = shot_dataframe.assign(
        Y=shot_dataframe["X Coordinate"].apply(lambda x: (((x - 100) * 500) / 85)).values)
    return shot_dataframe

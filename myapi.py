from fastapi import FastAPI, HTTPException
import json
import random
from enums.positions import PositionEnum
from enums.teams import TeamEnum
from models.player import Player

app = FastAPI()

with open("data/all_time_players.json") as f:
    players = json.load(f)

with open("data/draft.json") as f:
    draft_data = json.load(f)

def save_players_data(players):
    with open("data/all_time_players.json", "w") as f:
        json.dump(players, f, indent=4)

def save_draft_data(draft_data):
    with open("data/draft.json", "w") as f:
        json.dump(draft_data, f, indent=4)

@app.get("/players")
def get_players():
    return players


@app.get("/players/{player_id}")
def get_player_by_id(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player
    return {"error": "Player not found"}



@app.get("/players/position/{position}")
def get_players_by_position(position: PositionEnum):
    filtered_players = [player for player in players if player["position"] == position]
    if not filtered_players:
        return {"error": "No players found for this position"}
    return filtered_players


@app.get("/players/top-scorers/{top_n}")
def get_top_scorers(top_n: int):
    sorted_by_ppg = sorted(players, key=lambda x: x["ppg"], reverse=True)
    top_players = sorted_by_ppg[:top_n]
    return {"top_scorers" : top_players}


@app.get("/players/top-assisters/{top_n}")
def get_top_assisters(top_n: int):
    sorted_by_apg = sorted(players, key=lambda x: x["apg"], reverse=True)
    top_players = sorted_by_apg[:top_n]
    return {"top_assisters" : top_players}


@app.get("/players/top-rebounders/{top_n}")
def get_top_rebounders(top_n: int):
    sorted_by_rpg = sorted(players, key=lambda x: x["rpg"], reverse=True)
    top_players = sorted_by_rpg[:top_n]
    return {"top_rebounders" : top_players}


@app.get("/players/championships/{min_championships}")
def get_players_by_championships(min_championships: int):
    filtered_players = [player for player in players if player["championships"] >= min_championships]
    return {f"players with at least {min_championships} championships" : filtered_players}


@app.get("/players/team/{team_name}")
def get_players_by_team(team_name: TeamEnum):  
    filtered_players = [player for player in players if team_name in player["team"]]
    return {f"players who played at {team_name}" : filtered_players}


@app.get("/players/no-championships/")
def get_players_without_championship():
    filtered_players = [player for player in players if player["championships"] == 0]
    return {"players_with_0_championships" : filtered_players}


@app.get("/players/hall-of-fame/")
def get_hall_of_fame_candidates():
    #! CUSTOM CRITERIA FOR CHOOSING HOF CANDIDATES
    hof_threshold = 25
    hof_candidates = []
    for player in players:
        player_score = (player["ppg"] * 0.4) + (player["apg"] * 0.3) + (player["rpg"] * 0.2) + (player["championships"] * 10)
        if player_score >= hof_threshold:
            hof_candidates.append(player)
    return {"hall_of_fame_candidates": hof_candidates}


@app.get("/players/all-stars/{min_all_star_appearances}")
def get_all_star_players(min_all_start_appearances: int):
    filtered_players = [player for player in players if player["all_star_appearances"] >= min_all_start_appearances]
    return {f"players with at least {min_all_start_appearances} all-start appearances" : filtered_players}


@app.get("/drafts/")
def get_drafts():
    return draft_data

@app.put("/players/championships/add-championship/{player_id}")
def add_championship(player_id : int):
    player = get_player_by_id(player_id)
    player["championships"] += 1
    save_players_data(players)
    return {f"{player['name']} now has {player['championships']} championship(s)"}


@app.put("/players/all-star/add-allstar/{player_id}")
def add_allstar(player_id: int):
    player = get_player_by_id(player_id)
    player["all_star_appearances"] += 1
    save_players_data(players)
    return {f"{player['name']} now has {player['all_star_appearances']} all-star appearances"}


@app.put("/players/change-team/{player_id}")
def change_team(player_id: int, new_team: TeamEnum):
    player = get_player_by_id(player_id)
    player["team"] = new_team
    save_players_data(players)
    return {f"{player['name']}'s team updated successfully to {new_team}."} 
    

@app.put("/players/change-position/{player_id}")
def change_team(player_id: int, new_position: PositionEnum):
    player = get_player_by_id(player_id)
    player["position"] = new_position
    save_players_data(players)
    return {f"{player['name']}'s position updated successfully to {new_position}."} 


@app.post("/players/add-player/")
def add_player(player: Player):
    new_player = player.model_dump()
    new_player_with_id_first = {"id": len(players) + 1}
    new_player_with_id_first.update(new_player)
    players.append(new_player_with_id_first)
    save_players_data(players)
    return {"message": f"Player {player.name} added successfully!", "player": new_player_with_id_first}

@app.post("/team/random-draft/")
def draft_team():
    draft = {}
    for position in PositionEnum:
        players_at_position = [player for player in players if player["position"] == position.value]
        if players_at_position:
            draft[position.value] = random.choice(players_at_position)["name"]
        else:
            draft[position.value] = None  # If no players for that position
    
    id = len(draft_data) + 1
    draft_data.append({"id": id, "draft": draft})
    save_draft_data(draft_data) 

    return {"Random created draft": draft}


@app.delete("/players/delete/{player_id}")
def delete_player(player_id: int):
    if player_id > len(players):
        raise HTTPException(status_code=404, detail="Player not found")
    my_players = [player for player in players if player["id"] != player_id]
    save_players_data(my_players)
    
    return {"message": f"Player with ID {player_id} has been successfully deleted!"}

        
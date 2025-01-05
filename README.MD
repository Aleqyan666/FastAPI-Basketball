# FastAPI Basketball API

## Description
This project is a FastAPI application that allows you to manage and interact with basketball players. It supports functionalities like adding players, updating stats, retrieving top players based on different stats, and generating random drafts.

## Structure
```
FastAPI
├── data
│   ├── drafts
│   └── all_time_players.py
├── enums
│   ├── positions.py
│   └── teams.py
├── models
│   └── player.py
├── .gitignore
├── myapi.py
├── README.MD
└── requirements.txt
```

## Technologies Used
- **FastAPI**: Fast web framework for building APIs.
- **Python 3.8+**: Programming language used to implement the backend logic.
- **JSON**: Data format for persisting player and draft data.
- **Uvicorn**: ASGI server to run the FastAPI application.
- **Pydantic**: Data validation and settings management using Python data models.

## Requirements
- Python 3.8+
- **Create a Virtual Environment**
 ```bash
  python3 -m venv venv
  ```
- **Activate the Virtual Environment**
 ```bash
  .\venv\Scripts\activate  
  ```

- **Install Dependencies:** 
 ```bash
  pip install -r requirements.txt
  ``` 

- **Launch FastAPI App with *Auto-reloading* Activated**
```bash
  uvicorn myapi:app --reload
  ``` 
  
## Features
- **Player Management**:
  - Add, update, and retrieve player details.
  - Retrieve players by position, team, or statistical achievements.
  - Top scorers, rebounders, and assist leaders.
  - Track player championships and all-star appearances.
  - Hall of Fame candidate identification based on custom criteria.

- **Draft Functionality**:
  - Generate random drafts for basketball teams.
  - Position-based player selection.

- **Data Persistence**:
  - Store and retrieve player data and draft results in JSON format.

## API Endpoints

### Player Endpoints
- `GET /players`: Retrieves all players.
- `GET /players/{player_id}`: Retrieve details of a specific player by ID.
- `GET /players/position/{position}`: Retrieve players by their position.
- `GET /players/top-scorers/{top_n}`: Retrieves top N scorers based on PPG (Points Per Game).
- `GET /players/top-assisters/{top_n}`: Retrieves top N assisters based on APG (Assists Per Game).
- `GET /players/top-rebounders/{top_n}`: Retrieves top N rebounders based on RPG (Rebounds Per Game).
- `GET /players/championships/{min_championships}`: Get players with a minimum number of championships.
- `GET /players/team/{team_name}`: Get players who have played for a given team.
- `GET /players/no-championships`: Get players with no championships.
- `GET /players/hall-of-fame`: Get Hall of Fame candidates based on a custom formula & criteria.
- `GET /players/all-stars/{min_all_star_appearances}`: Get players with a minimum number of all-star appearances.

### Player Management Endpoints
- `PUT /players/championships/add-championship/{player_id}`: Add one championship to the specified player.
- `PUT /players/all-star/add-allstar/{player_id}`: Add one all-star appearance to the specified player.
- `PUT /players/change-team/{player_id}`: Change the team of a specified player.
- `PUT /players/change-position/{player_id}`: Change the position of a specified player.
- `POST /players/add-player/`: Add a new player to the dataset.
- `DELETE /players/delete/{player_id}/`: Delete a player from the dataset based on their unique player_id.

### Draft Endpoints
- `POST /team/random-draft/`: Generate a random draft based on player positions.


## Data Models

### Player Model
A `Player` consists of the following attributes:
- `id`: The unique identifier for the player.
- `name`: The name of the player.
- `position`: The player's playing position.
- `team`: The team(s) the player has played for.
- `ppg`: Points per game.
- `apg`: Assists per game.
- `rpg`: Rebounds per game.
- `championships`: Number of championships won.
- `all_star_appearances`: Number of all-star appearances.

### TeamEnum
A list of NBA teams:
- `Los Angeles Lakers`
- `Boston Celtics`
- `Chicago Bulls`
- `Dallas Mavericks`
- ...

### PositionEnum
A list of basketball positions:
- `PG` `SG` `SF` `PF` `C`

## Contacts
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/Aleqyan666)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/hayk-alekyan-900797204/)



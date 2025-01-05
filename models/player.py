from pydantic import BaseModel
from enums.teams import TeamEnum
from enums.positions import PositionEnum

# ydantic model for request data validation
class Player(BaseModel):
    name: str
    position: PositionEnum
    age: int
    team: TeamEnum
    ppg: float
    apg: float
    rpg: float
    championships: int
    all_star_appearances: int
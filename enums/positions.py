from enum import Enum

# Positions list as an Enum
class PositionEnum(str, Enum):
    Point_Guard = "PG"
    Shooting_Guard = "SG"
    Small_Forward = "SF"
    Power_Forward = "PF"
    Center = "C"

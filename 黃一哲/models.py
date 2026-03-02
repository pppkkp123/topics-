from dataclasses import dataclass

@dataclass
class SpeedInfo:
    current_speed: float
    historical_speed: float

@dataclass
class Event:
    type: str          # accident / construction / jam
    distance: float    # meters
    minutes_ago: int
    bearing: float     # 方向角（0~360）

@dataclass
class UserReport:
    user_id: str
    distance: float
    minutes_ago: int
    confidence: float = 0  # 預設0，之後算

from dataclasses import dataclass
from typing import List

@dataclass
class Team:
    title: str
    name: str
    info: str
    members: List[str]

TEAMS = [ Team("management", "Management", "The management team oversees the chores done at Base Camp and ensures everyone is on task and on time.", ["Daelan", "Michelle", "Logan C.", "Will", "Dylan G.", "Rylee"]), Team("documentation", "Documentation", "The documentation team photographs all events, follows up with guest speakers, and manages Base Camp's social medias.", ["Ryan", "Randy", "Isaac", "Ma'kyla", "Ben"]), Team("procurement", "Procurement", "The procurement team orders all supplies needed at Base Camp and sets out and cleans up lunch.", ["Richard", "Gary", "Marian", "Dylan S.", "Ethan", "Quinton"]), Team("community", "Community", "The community team plans all community events for students, as well as hosts parties for birthdays and holidays.", ["Jacen", "Ariyana", "Justin", "RJay", "Logan W."])
]
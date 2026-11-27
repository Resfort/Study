from dataclasses import dataclass, field
from enum import StrEnum

@dataclass
class ItemType(StrEnum):
    """A class representing an item in a game."""
    # Define the possible values for the item type
    WEAPON = 'weapon'
    ARMOR = 'armor'
    POTION = 'potion'

@dataclass(slots=True, frozen=True)
class Item:
    """A class representing an item in a game."""
    id: str 
    name: str
    item_type: ItemType
    power: int
    description: str = ""

class Character:
    name: str
    max_hp: int
    hp: int
    base_attack: int
    base_defense: int
    level: int
    xp: int
    gold: int
    inventory: list[Item] = field(default_factory=list)
    equipped_weapon: Item | None = None
    equipped_armor: Item | None = None

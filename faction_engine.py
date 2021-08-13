from typing import *
from dataclasses import dataclass
import typing
import dice
import json



class MapKnowledge:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


@dataclass
class Faction:
    FactionName: str
    LeaderSKill: int
    Commanders: dict
    SupplyRating: int
    EquipmentRating: int
    Status: int
    MapKnowledge: MapKnowledge
    CurrentLocation : dict
    LastTurnLocation : dict
    Units: dict
    Items: list
    StealthRating: int


@dataclass
class SimpleFaction:
    Name: str
    LeaderSkill: int
    RangedSkill: int
    MeleeSkill: int
    Status: int
    MapKnowledge: list
    CurrentLocation: dict
    LastTurnLocation: dict





def LoadPlayer(filepath: str) -> SimpleFaction:
    with  open(filepath, 'r') as f:
        faction = SimpleFaction(**json.load(f))
    return faction
    






def run_combat(attacker: SimpleFaction, defender: SimpleFaction) -> SimpleFaction :
    print(f"Entering combat Attacker: {attacker.Name} Defender: {defender.Name}")
    combatRound = 1
    while (attacker.Status > 0) & (defender.Status > 0):
        print(f"Combat Round: {combatRound}")
        print(f"Starting {attacker.Name} status: {attacker.Status}")
        print(f"Starting {defender.Name} status: {defender.Status}")
        attackerResult = attacker.LeaderSkill + attacker.RangedSkill + attacker.MeleeSkill + int(dice.roll('1d6'))
        defenderResult = defender.LeaderSkill + defender.RangedSkill + defender.MeleeSkill + int(dice.roll('1d6'))
        
        print(f"Attacker Result {attackerResult} --- Defender Result {defenderResult}")
        if attackerResult > defenderResult:
            defender.Status -= 1
        elif defenderResult > attackerResult:
            attacker.Status -= 1
        else:
            defender.Status -= 1
            attacker.Status -= 1
        
        combatRound += 1
        print(f"{attacker.Name} status: {attacker.Status}")
        print(f"{defender.Name} status: {defender.Status}")
    
    if attacker.Status <= 0:
        print(f"Attacking faction {attacker.Name} routed!!")
    if defender.Status <= 0:
        print(f"Defending faction {defender.Name} routed!!")



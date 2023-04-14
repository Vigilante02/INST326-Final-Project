import json
import random
import argparse

"""A turn-based fighting game"""

class Player:
    """
    The base class for all players in the game.

    Attributes:
    - name (str): The name of the player
    - attack_power (int): The player's attack power
   
    """
    def __init__(self, name, level, attack_power, defense_power):
        self.name = name
        self.level = level
        self.attack_power = attack_power if level < 10 else attack_power * 2
        self.defense_power = defense_power
        self.hp = 50 + (level * 10) if level <= 10 else 150
        self.max_hp = self.hp
    
    def attack(self, other_player):
        """
        Attacks the other player, deducting damage from their HP.

        Args:
        - other_player (Player): The player being attacked
        """
        if other_player.defense_power >= self.attack_power:
            print(f"{self.name}'s attack was ineffective against {other_player.name}!")
            return
        damage = damage(self.attack_power, other_player.defense_power).calculate()
        print(f"{self.name} attacks {other_player.name} for {damage} damage!")
        other_player.take_damage(damage)
    
    def take_damage(self, damage):
        """
        Takes damage from an attack.

        Args:
        - damage (int): The amount of damage to take
        """
        self.hp = max(self.hp - damage, 0)
        print(f"{self.name} takes {damage} damage! {self.name}'s HP is now {self.hp}.")
    
class ComputerPlayer(Player):
    """
    A computer-controlled player in the game.

    Attributes:
    - name (str): The name of the player (default: "CPU")
    - level (int): The player's level (default: 1)
    - attack_power (int): The player's attack power (default: 10)
    - defense_power (int): The player's defense power (default: 5)
    """
    def __init__(self, name="CPU", level=1, attack_power=10, defense_power=5):
        super().__init__(name, level, attack_power, defense_power)
    
    def choose_action(self):
        """
        Chooses an action for the computer player to take.
        
        Returns:
        - A string representing the action to take ("attack")
        """
        return "attack"
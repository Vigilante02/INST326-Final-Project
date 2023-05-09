"""A turn-based fighter game called Showup, Showout, Showdown where the user fights against a cpu fighter"""
import random
import re

class QuitInCase(Exception):
    """Creates the QuitInCase class.

    Args:
        Exception (class): The class for the Exception object.
        
    Main Author: Ryan Borak
    """
    pass

def quitinput(prompt):
    """Function for inputs where the user wants to quit. 

    Args:
        prompt (str): Represents the input of the user. 

    Raises:
        QuitInCase: An exception that allows for a user to back out of the game.

    Returns:
        str: The input of the user.
        
    Main Author: Ryan Borak
    """
    userinput = input(prompt)
    if userinput.strip().lower() == "quit":
        raise QuitInCase
    else: 
        return userinput

    
class ShowupShowoutShowdown:
    def __init__(self, player_name, player_hp=100, computer_hp=100):
        """Initializes the attributes for the ShowupShowoutShowdown class.

        Args:
            player_name (str): Represents the name of the player.
            player_hp (int, optional): Represents the health points of the player. Defaults to 100.
            computer_hp (int, optional): Represents the health points of the computer. Defaults to 100.
        
        Side Effects:
            - Initializes the instance variables for the class, including the player's name and health points,
              the computer's health points, the dictionary of fighters, the selected fighter, the computer's
              selected fighter, the dictionary of computer powers, the player's turn status, the computer's
              turn status, the play more flag, and the winner variable.
        
        Main Author: Noah Kandel
        """
        self.player_name = player_name
        self.player_hp = player_hp
        self.computer_hp = computer_hp
        self.fighters = {}
        self.selected_fighter = ""
        self.cpu_fighter = ""
        self.cpu_powers = {}
        self.player_turn = False
        self.computer_turn = False
        self.play_more = True
        self.winner = None
    
    
    def __eq__(self, other):
        """Check if this instance of ShowupShowoutShowdown is equal to another instance.

        Args:
            other (ShowupShowoutShowdown): The other instance to compare.

        Returns:
            bool: True if the instances are equal, False otherwise.
            
        Main Author: Ross Zaslavsky
        
        Technique(s) Demonstrated: magic methods other than __init__()
        """
        return (isinstance(other, ShowupShowoutShowdown)
                and self.player_name == other.player_name
                and self.player_hp == other.player_hp
                and self.computer_hp == other.computer_hp
                and self.fighters == other.fighters
                and self.selected_fighter == other.selected_fighter
                and self.cpu_fighter == other.cpu_fighter
                and self.cpu_powers == other.cpu_powers
                and self.player_turn == other.player_turn
                and self.computer_turn == other.computer_turn
                and self.play_more == other.play_more
                and self.winner == other.winner)
    
    def __str__(self):
        """Returns an informal string representation of this instance of the class.

        Returns:
            str: An informal string representation of the instance, including the player's name and HP, and the computer's HP.
        
        Main Author: Ross Zaslavsky

        Technique(s) Demonstrated: magic methods other than __init__()
        """
        return f"Player: {self.player_name} | Player HP: {self.player_hp} | Computer HP: {self.computer_hp}"
    
    def __repr__(self):
        """Returns a formal string representation of this instance of the class.

        Returns:
            str: A formal string representation of the instance that can be used to recreate it.
            
        Main Author: Ross Zaslavsky
    
        Technique(s) Demonstrated: magic methods other than __init__()
        """
        return f"ShowupShowoutShowdown(player_name='{self.player_name}', player_hp={self.player_hp}, computer_hp={self.computer_hp})"
    
    def __contains__(self, item):
        """Checks if the given item is present in the fighters dictionary.

        Args:
        item (str): The name of the fighter to check.

        Returns:
            str: A string representation of the fighter if present in the fighters dictionary, otherwise a string indicating that the fighter is not in the list.
        
        Main Author: Ross Zaslavsky
    
        Technique(s) Demonstrated: magic methods other than __init__()
        """
        if item in self.fighters:
            return str(self.fighters[item])
        else:
            return f"{item} is not in the fighters list."
    
    def welcome(self):
        """Prints out a welcome message for the player and explains the rules of the game.

        Returns: None
        
        Main Author: Ryan Borak
        
        Technique(s) Demonstrated: f-strings containing expressions
        """
        print(f"Thank you for showing up, {self.player_name}! Welcome to Showup, Showout, Showdown!")
        print("\nThis is a turn-based battle game where you either attack your opponent or heal yourself until there is only one fighter left standing!")

        print("\nHow to play.\n\nPlayers take turns choosing a move. Moves can either be heal or attack, with a 10% chance of landing a critical.")
        print("Fighters differ in heal and attack power.\nEach player starts with 100 health, and the first to get their opponent to 0 wins!\n")
        print(f"Please select your fighter, {self.player_name}!\n")

    def load_fighters(self):
        """Loads the fighters' data from a file and populates the 'fighters' dictionary.
        The file should be in the format: 'fighter,attack_power,heal_power'. Each line in the file represents a different fighter.

        Returns:
            None
            
        Main Authors: Noah Kandel
        
        Technique(s) Demonstrated: with statements, sequence unpacking
        """
        with open('fighters.txt', mode='r', encoding='utf-8') as fighter_file:
            for line in fighter_file.readlines():
                fighter, attack_power, heal_power = line.strip().split(',')
                self.fighters[fighter] = {"attack_power": int(attack_power), "heal_power": int(heal_power)}
                print(fighter)
                print(f"Attack Power: {attack_power}")
                print(f"Heal Power: {heal_power}")
                print()
        fighter_file.close()

    def select_fighter(self):
        """Allows the player to select their fighter, validates the selection and sets the selected fighter and CPU fighter.
        
        Returns: None
        
        Main Author: Ross Zaslavsky
        
        Technique(s) Demonstrated: set operations on sets 
        """
        self.selected_fighter = quitinput("Please enter the name of your fighter: ")
        while self.selected_fighter not in self.fighters:
            print("Invalid fighter name.")
            self.selected_fighter = quitinput("Please enter the name of your fighter: ")
        print(f"{self.selected_fighter}")
        remaining_fighters = set(self.fighters.keys()) - {self.selected_fighter}
        self.cpu_fighter = random.choice(list(remaining_fighters))
        print(f"The computer has selected {self.cpu_fighter}!")
        self.cpu_powers = self.fighters[self.cpu_fighter]
        if self.selected_fighter in self:
            print(f"{self.selected_fighter}: Attack Power: {self.fighters[self.selected_fighter]['attack_power']}, Heal Power: {self.fighters[self.selected_fighter]['heal_power']}")
    
    def computer_move(self):
        """
        Makes a move for the computer player.

        Chooses between attacking or healing. 
        - If attacking, calculate damage based on the computer player's attack power and the critical hit chance. 
        - If healing, calculate the amount of health regained based on the computer 
        player's heal power and the critical heal chance.
        
        Main Author: Ross Zaslavsky
        """
        self.computer_turn = True
        cpu_move = random.choice(["attack", "heal"])
        if cpu_move == "attack":
            attack_power = self.cpu_powers['attack_power']
            damage = int(attack_power * (1.5 if random.random() < 0.1 else 1))
            critical_hit = damage > attack_power
            print(f"\n{self.cpu_fighter} {'lands a critical hit on' if critical_hit else 'attacks'} {self.player_name} for {damage} damage!")
            self.player_hp -= damage
        elif cpu_move == "heal":
            heal_power = self.cpu_powers['heal_power']
            heal_amount = int(heal_power * (1.5 if random.random() < 0.1 else 1))
            critical_heal = heal_amount > heal_power
            print(f"\n{self.cpu_fighter} {'critically heals' if critical_heal else 'heals'} for {heal_amount} health!")
            self.computer_hp += heal_amount
        self.computer_turn = False
        print(f"\nPlayer health: {self.player_hp}, Computer health: {self.computer_hp}")

    def player_move(self):
        """Prompt the user to select a move and execute it.

        Asks the user to select a move until a valid move is provided.
        - If the user selects 'attack', calculate the damage dealt to the computer and prints a message. 
        - If the user selects 'heal', the method calculates the amount of health
        restored to the player and prints a message. 
        - If the damage heal amount is critical, the message indicates that. 
        - Finally, it updates the player and computer health points and prints them.
        
        Main Author: Ross Zaslavsky
        
        Technique(s) Demonstrated: regular expressions
        """
        self.player_turn = True
        valid_moves = ["attack", "heal"]
        while True:
            player_move = quitinput(f"\n{self.selected_fighter}, select your move: Attack, Heal: ").lower()
            if re.match(r"^\b(attack|heal)\b$", player_move):
                if player_move in valid_moves:
                    break
        print("Invalid move. Please select either attack or heal.")
        if player_move == "attack":
            attack_power = self.fighters[self.selected_fighter]['attack_power']
            damage = int(attack_power * (1.5 if random.random() < 0.1 else 1))
            critical_hit = damage > attack_power
            print(f"\n{self.selected_fighter} {'lands a critical hit on' if critical_hit else 'attacks'} {self.cpu_fighter} for {damage} damage!")
            self.computer_hp -= damage
        elif player_move == "heal":
            heal_power = self.fighters[self.selected_fighter]['heal_power']
            heal_amount = int(heal_power * (1.5 if random.random() < 0.1 else 1))
            critical_heal = heal_amount > heal_power
            print(f"\n{self.selected_fighter} {'critically heals' if critical_heal else 'heals'} for {heal_amount} health!")
            self.player_hp += heal_amount
        self.player_turn = False
        print(f"\nPlayer health: {self.player_hp}, Computer health: {self.computer_hp}")

    def determine_winner(self):
        """Determines the winner of the game.

        - If the player's health points are less than or equal to 0, the computer is declared as the winner.
        - If the computer's health points are less than or equal to 0, the player is declared as the winner.
        - If neither condition is met, the winner remains None.
        
        Returns: str or None: The winner of the game, as determined by the method. Returns "Computer" if the computer wins,
        the player's name if the player wins, and None if neither wins.
        
        Main Author: Ryan Borak
        
        Technique(s) Demonstrated: Conditional expressions
        """
        self.winner = "Computer" if self.player_hp <= 0 else self.player_name if self.computer_hp <= 0 else None

    def play_again(self):
        """Prompts the player to choose whether or not to play again.

        - If the player chooses 'no', the game state variable `play_more` is set to False, indicating that the player
        does not want to play again. 
        - If the player chooses 'yes', `play_more` is set to True, indicating that the player
        wants to play again.
        
        Main Authors: Ryan Borak, Ross Zaslavsky
        
        Technique(s) Demonstrated: Conditional expressions, regular expressions
        """
        while True:
            play_again = quitinput("Would you like to play again? (yes/no): ")
            if not re.match(r'(?i)^(yes|no)$', play_again):
                print("Invalid choice. Please enter either yes or no.")
            else: 
                break
        self.play_more = False if play_again.strip().lower() == "no" else True

    def play_game(self):
        """Starts a new game of Fighters.

        Returns:
            None
            
        Main Author: Ryan Borak
        
        Technique(s) Demonstrated: f-strings containing expressions
        """
        self.welcome()
        self.load_fighters()
        
        while self.play_more:
            self.selected_fighter = ""
            self.player_hp = 100
            self.computer_hp = 100
            self.winner = None
            self.select_fighter()                
            
            while self.winner is None:
                self.player_turn = True
                self.player_move()
                self.determine_winner()
                
                if self.winner is not None:
                    break
                
                self.computer_turn = True
                self.computer_move()
                self.determine_winner()
            
            print(f"\nThe winner is {self.winner}!")
            self.play_again()
        print(f"Thanks for playing, {self.player_name}! Show up and show out again soon!")
            
def main():
    """
    The entry point of the game. This prompts the player to enter their name and creates a new instance
    of the ShowupShowoutShowdown class. The game is played until the player chooses to quit.
    
    Parameters:
        None

    Returns:
        None
        
    Main Author: Ross Zaslavsky
    
    Technique(s) Demonstrated: Regular expressions
    """
    try: 
        while True:
            player_name = quitinput("Enter your name: ")
            if re.match(r"^[A-Za-z]+$", player_name):
                break
            print("Invalid name. Please enter a name containing only letters.")

        game = ShowupShowoutShowdown(player_name)
        game.play_game()
    except QuitInCase:
        print("We hope you show up and show out another time!")
    

if __name__ == '__main__':
    main()
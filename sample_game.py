import random

class Final:
    def __init__(self, player_name, player_hp=100, computer_hp=100):
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
        return (isinstance(other, Final)
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
        return f"Player: {self.player_name} | Player HP: {self.player_hp} | Computer HP: {self.computer_hp}"
    
    def __repr__(self):
        return f"Final(player_name='{self.player_name}', player_hp={self.player_hp}, computer_hp={self.computer_hp})"
    
    def welcome(self):
        "Function that welcomes player and explains rules"
        print("\tWelcome to Showup, Showout, Showdown! This is a turn based battle game where")
        print("\tthere can only be one winner!")

        print("\nHow to play.\n\nPlayers take turns choosing a move. Moves can either be heal or attack.")
        print("\nEach player starts with 100 health, and the first to get their opponent to 0 wins!")

    def load_fighters(self):
        with open('fighters.txt', 'r', encoding='utf-8') as fighter_file:
            for line in fighter_file.readlines():
                fighter, attack_power, heal_power = line.strip().split(',')
                self.fighters[fighter] = {"attack_power": int(attack_power), "heal_power": int(heal_power)}

        fighter_file.close()

    def select_fighter(self):
        print(self.fighters)
        while self.selected_fighter not in self.fighters:
            self.selected_fighter = input("Please enter the name of your fighter: ")
            if self.selected_fighter not in self.fighters:
                print("Invalid fighter name.")
        print(f"{self.fighters[self.selected_fighter]}")
        self.cpu_fighter = random.choice(list(self.fighters.keys()))
        print(f"The computer has selected {self.cpu_fighter}.")
        self.cpu_powers = self.fighters[self.cpu_fighter]
    def Match(self):
        if self.player_hp <= 0:
            self.winner = self.computer_fighter
            print("You lost game over")
            self.play_more = False
        elif self.computer_hp <= 0:
            self.winner = self.selected_fighter
            print("You won congrats!!!")
            self.play_more = False    
#Test from Ross        
def main():
        gametest = Final()
        

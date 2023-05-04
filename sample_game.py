import random
import re

class ShowupShowoutShowdown:
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
        return f"Player: {self.player_name} | Player HP: {self.player_hp} | Computer HP: {self.computer_hp}"
    
    def __repr__(self):
        return f"ShowupShowoutShowdown(player_name='{self.player_name}', player_hp={self.player_hp}, computer_hp={self.computer_hp})"
    
    def __contains__(self, item):
        if item in self.fighters:
            return str(self.fighters[item])
        else:
            return f"{item} is not in the fighters list."
    
    def welcome(self):
        """Function that welcomes player and explains rules"""
        print(f"Thank you for showing up, {self.player_name}! Welcome to Showup, Showout, Showdown!")
        print("\nThis is a turn-based battle game where you either attack your opponent or heal yourself until there is only one fighter left standing!")

        print("\nHow to play.\n\nPlayers take turns choosing a move. Moves can either be heal or attack, with a 10% chance of landing a critical.")
        print("Fighters differ in heal and attack power.\nEach player starts with 100 health, and the first to get their opponent to 0 wins!\n")
        print(f"Please select your fighter, {self.player_name}!\n")

    def load_fighters(self):
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
        self.selected_fighter = input("Please enter the name of your fighter: ")
        while self.selected_fighter not in self.fighters:
            print("Invalid fighter name.")
            self.selected_fighter = input("Please enter the name of your fighter: ")
        print(f"{self.selected_fighter}")
        remaining_fighters = set(self.fighters.keys()) - {self.selected_fighter}
        self.cpu_fighter = random.choice(list(remaining_fighters))
        print(f"The computer has selected {self.cpu_fighter}.")
        self.cpu_powers = self.fighters[self.cpu_fighter]
        if self.selected_fighter in self:
            print(f"{self.selected_fighter}: Attack Power: {self.fighters[self.selected_fighter]['attack_power']}, Heal Power: {self.fighters[self.selected_fighter]['heal_power']}")
    
    def computer_move(self):
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
        self.player_turn = True
        valid_moves = ["attack", "heal"]
        while True:
            player_move = input(f"\n{self.selected_fighter}, select your move: Attack, Heal: ").lower()
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
        self.winner = "Computer" if self.player_hp <= 0 else self.player_name if self.computer_hp <= 0 else None

    def play_again(self):
        play_again = ""
        while not re.match(r'^(yes|no)$', play_again):
            play_again = input("Would you like to play again? (yes/no): ")
            print("Invalid choice. Please enter either yes or no.") if not re.match(r'^(yes|no)$', play_again) else None
            self.play_more = False if play_again == "no" else True

    def play_game(self):
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
    while True:
        player_name = input("Enter your name: ")
        if re.match(r"^[A-Za-z]+$", player_name):
            break
        print("Invalid name. Please enter a name containing only letters.")

    game = ShowupShowoutShowdown(player_name)
    game.play_game()
    

if __name__ == '__main__':
    main()
        

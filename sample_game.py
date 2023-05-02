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
        print("\nEach player starts with 100 health, and the first to get their opponent to 0 wins!\n")

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
        print(self.fighters)
        self.selected_fighter = input("Please enter the name of your fighter: ")
        while self.selected_fighter not in self.fighters:
            print("Invalid fighter name.")
            self.selected_fighter = input("Please enter the name of your fighter: ")
        print(f"{self.selected_fighter}")
        turn_choice = random.choice(['up', 'down'])
        self.player_turn = True if turn_choice == 'up' else False
        print(f"{self.player_name} shows up first!" if self.player_turn else "Computer shows up first!")
        self.cpu_fighter = random.choice(list(self.fighters.keys()))
        print(f"The computer has selected {self.cpu_fighter}.")
        self.cpu_powers = self.fighters[self.cpu_fighter]
    
    def computer_move(self):
        self.computer_turn = True
        cpu_move = random.choice(["attack", "heal"])
        if cpu_move == "attack":
            attack_power = self.cpu_powers['attack_power']
            if random.random() < 0.15:
                damage = int(attack_power) * 2
                print(f"\n{self.cpu_fighter} lands a critical hit on {self.player_name} for {damage} damage!")
            else:
                damage = int(attack_power)
                print(f"\n{self.cpu_fighter} attacks {self.player_name} for {damage} damage!")
            self.player_hp -= damage

        elif cpu_move == "heal":
            heal_power = self.cpu_powers['heal_power']
            save = int(heal_power)
            self.computer_hp += save
            print(f"\n{self.cpu_fighter} heals themselves for {save} health!")

        self.computer_turn = False
        print(f"\nPlayer health: {self.player_hp}, Computer health: {self.computer_hp}")


    def player_move(self):
        self.player_turn = True
        player_move = ""
        while player_move not in ["attack", "heal"]:
            player_move = input(f"\n{self.player_name}, select your move: Attack ({self.fighters[self.selected_fighter]['attack_power']} attack power), Heal ({self.fighters[self.selected_fighter]['heal_power']} heal power): ")
            if player_move not in ["attack", "heal"]:
                print("Invalid move. Please select either attack or heal.")

        if player_move == "attack":
            attack_power = self.fighters[self.selected_fighter]['attack_power']

            if random.random() < 0.15:
                damage = int(attack_power) * 2
                print(f"\n{self.selected_fighter} lands a critical hit on {self.cpu_fighter} for {damage} damage!")
            else:
                damage = int(attack_power)
                print(f"\n{self.selected_fighter} attacks {self.cpu_fighter} for {damage} damage!")

            self.computer_hp -= damage
        elif player_move == "heal":
            heal_power = self.fighters[self.selected_fighter]['heal_power']
            save = int(heal_power)
            self.player_hp = min(self.player_hp + save, 100)
            print(f"\n{self.selected_fighter} heals themselves for {save} health!")

        self.player_turn = False
        print(f"\nPlayer health: {self.player_hp}, Computer health: {self.computer_hp}")

    def determine_winner(self):
        if self.player_hp <= 0:
            self.winner = "Computer"
        elif self.computer_hp <= 0:
            self.winner = self.player_name

    def play_again(self):
        play_again = ""
        while play_again not in ["yes", "no"]:
            play_again = input("Would you like to play again? (yes/no): ")
            print("Invalid choice. Please enter either yes or no.") if play_again not in ["yes", "no"] else None
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
    player_name = input("Enter your name: ")
    game = Final(player_name)
    game.play_game()
    

if __name__ == '__main__':
    main()
        

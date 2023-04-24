import json
import random

class Final:
    def __init__(self):
        self.main()
        self.roster()
        self.begin()
        self.you_begin()
        self.Match()
        

    def main(self):
        "Function that welcomes player and explains rules"
        print("\tWelcome to our Fighter Game by Ross, Ryan and Noah! This is a turn based battle game where")
        print("\tthere can only be one winner!")

        print("\nHow to play.\n\nPlayers take turns choosing a move. Moves can either be heal or attack")
        print("\nEach player starts with 100 health, and the first to get their opponent to 0 wins!")
        play_more = True

        while play_more:
            winner = None
            self.player_hp = 100
            self.computer_hp = 100
            
            turn = random.randint(1,2)
            if turn == 1:
                self.player_turn = True
                self.computer_turn = False
                print("\nYou will go first.")
            else:
                self.player_turn = False
                self.computer_turn = True
                print("\nComputer will go first.")
            
            print("\nPlayer health: ", self.player_hp, "Computer health: ", self.computer_hp)
            print("\nBut first PICK YOUR CHARACTER!!!!")
        
            play_more = False
        
    def roster(self):   
        fighter_file = open('fighters.txt', 'r')
        self.fighters = {}
        for line in fighter_file.readlines():
            fighter, attack_power, heal_power = line.strip().split(',')
            self.fighters[fighter] = {'attack_power': int(attack_power), 'heal_power': int(heal_power)}

        fighter_file.close()
        
        print(self.fighters)
        self.selected_fighter = input("Please enter the name of your fighter: ")
        if self.selected_fighter in self.fighters:
            print(self.fighters[self.selected_fighter])
        else:
            print("Invalid fighter name.")
        self.computer_fighter = random.choice(list(self.fighters.keys()))
        print(f"The computer has selected {self.computer_fighter}.")
        self.cpu_powers = self.fighters[self.computer_fighter]
        attack_cpu = self.cpu_powers['attack_power']
        heal_cpu = self.cpu_powers['heal_power']
    def begin(self):
        cpu_move = random.choice(["attack", "heal"])
        if self.computer_turn == True and cpu_move == "attack":
            attack_power = self.cpu_powers['attack_power']
            damage =int(attack_power)
            self.player_hp -= damage
            print(f"\n{self.computer_fighter} attacks the player for {damage} damage!")
        
        elif self.computer_turn == True and cpu_move == "heal":
            heal_power = self.fighters[self.computer_fighter]['heal_power']
            save = self.cpu_powers[heal_power]
            self.computer_hp += save
            print(f"\n{self.computer_fighter} heals themself for {save} health!")
            
        print(f"\nPlayer health: {self.player_hp}, Computer health: {self.computer_hp}")
    
    def you_begin(self):
        player_move = input("\nSelect your move: Attack, deal {attack_power} to the opponent, \nHeal, add to your health by {heal_power}")
        if self.player_turn == True and player_move == "attack":
            attack_power = self.fighters[self.selected_fighter]['attack_power']
            damage =int(attack_power)
            self.computer_hp -= damage
            print(f"\n{self.selected_fighter} attacks the computer for {damage} damage!")
        
        elif self.player_turn == True and player_move == "heal":
            heal_power = self.fighters[self.selected_fighter]['heal_power']
            save = self.selected_fighter[heal_power]
            self.player_hp += save
            print(f"\n{self.selected_fighter} heals themself for {save} health!")
            
        print(f"\nPlayer health: {self.player_hp}, Computer health: {self.computer_hp}")
    def Match(self):
        if self.player_hp <= 0:
            self.winner = self.computer_fighter
            print("You lost game over")
            self.play_more = False
        elif self.computer_hp <= 0:
            self.winner = self.selected_fighter
            print("You won congrats!!!")
            self.play_more = False    
        
        
        
test = Final()
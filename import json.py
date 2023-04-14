import json
import random
import argparse


class Final:
    def __init__(self,fighters,computer_turn,player_turn, computer_fighter, player_hp, computer_hp, selected_fighter):
        self.fighters = fighters
        self.computer_turn = computer_turn
        self.player_turn = player_turn
        self.computer_fighter = computer_fighter
        self.player_hp = player_hp
        self.computer_hp = computer_hp
        self.selected_fighter = selected_fighter
        

    def main():
        "Function that welcomes player and explains rules"
    print("\tWelcome to our Fighter Game by Ross, Ryan and Noah! This is a turn based battle game where")
    print("\tthere can only be one winner!")

    print("\nHow to play.\n\nPlayers take turns choosing a move. Moves can either be heal or attack")
    print("\nEach player starts with 100 health, and the first to get their oppenent to 0 wins!")
    play_more = True

    while play_more:
        winner = None
        player_hp = 100
        computer_hp = 100
        
        turn = random.randint(1,2)
        if turn == 1:
            player_turn = True
            computer_turn = False
            print("\nYou will go first.")
        else:
            player_turn = False
            computer_turn = True
            print("\nComputer will go first.")
        
        print("\nPlayer health: ", player_hp, "Computer health: ", computer_hp)
        print("\nBut first PICK YOUR CHARACTER!!!!")
        play_more = False
    
    def roster():   
        fighter_file = open('fighters.txt', 'r')
        fighters = {}
        for line in fighter_file.readlines():
            fighter, attack_power, heal_power = line.strip().split(',')
            fighters[fighter] = {'attack_power': int(attack_power), 'heal_power': int(heal_power)}

        fighter_file.close()
        
        print(fighters)
        selected_fighter = input("Please enter the name of your fighter: ")
        if selected_fighter in fighters:
            print(fighters[selected_fighter])
        else:
            print("Invalid fighter name.")
        computer_fighter = random.choice(list(fighters.keys()))
        print(f"The computer has selected {computer_fighter}.")
        
        
    def begin(computer_turn,fighters, computer_fighter, computer_hp, player_hp):
        cpu_move = random.choice(["attack", "heal"])
        if computer_turn == True & cpu_move == "attack":
            attack_power = fighters[computer_fighter]['attack_power']
            damage =int(attack_power)
            player_hp -= damage
            print(f"\n{computer_fighter} attacks the player for {damage} damage!")
        
        elif computer_turn == True & cpu_move == "heal":
            heal_power = fighters[computer_fighter]['heal_power']
            save = computer_fighter[heal_power]
            computer_hp += save
            print(f"\n{computer_fighter} heals themself for {save} health!")
            
    print(f"\nPlayer health: {player_hp}, Computer health: {computer_hp}")
    
    def you_begin(player_turn, fighters, computer_fighter, selected_fighter,computer_hp):
        selected_move = input("\nSelect your move: Attack, deal {attack_power} to the opponent, \nHeal, add to your health by {heal_power}")
        if player_turn == True & selected_move == "attack":
            attack_power = fighters[selected_fighter]['attack_power']
            damage = int(attack_power)
            computer_hp -= damage
            print(f"n{selected_fighter} attacks the computer player for {damage} damage!")
            
        
        





    main()
    roster()
    begin()

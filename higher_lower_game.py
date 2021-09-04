# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:48:38 2021

@author: wajee
"""

import random
from instagram_data import data
from higher_lower_logo_insta import logo


def get_random():
    
    value=random.randint(0,48)
    return(value)

def comparision(A,B,choice,player_score,ans):
    
    A_follower_count=A['follower_count']
    B_follower_count=B['follower_count']
    
    if(A_follower_count < B_follower_count and choice=='H'):
        
        print(f" You Selected {choice}")
        print("You got it correct")
        print(f"{B['name']} has a follower count of {B_follower_count}")
        player_score+=1
        print(player_score)
        ans=True
        A=B
        return(A,player_score,ans)
    
    if(A_follower_count > B_follower_count and choice=='L'):
        
        print(f" You Selected {choice}")
        print("You got it correct")
        print(f"{B['name']} has a follower count of {B_follower_count}")
        player_score+=1
        print(player_score)
        ans=True
        A=B
        return(A,player_score,ans)
    
    if(A_follower_count > B_follower_count and choice=='H'):
        
        print(f" You Selected {choice}")
        print("You Guessed it wrong")
        print(f"{B['name']} has a follower count of {B_follower_count}")
        print(f"Your Final Score is {player_score}")
        ans=False  
        return(A,player_score,ans)
    
    if(A_follower_count < B_follower_count and choice=='L'):
        
        print(f" You Selected {choice}")
        print("You Guessed it wrong")
        print(f"{B['name']} has a follower count of {B_follower_count}")
        print(f"Your Final Score is {player_score}")
        ans=False    
        return(A,player_score,ans)
        
        
    
def main():
    
    print(logo)
    print("Welcome to the Higher and Lower Game")
    
    play='Y'
    player_score=0
    ans=True
    
    while play=='Y' or play=='y':
        
        
        randA=get_random()
        A=data[randA]
        
        while (ans==True):
             
            randB=get_random()
            B=data[randB]
            
            print(f" {A['name']} has a follower count of {A['follower_count']}")
            print(f"Does {B['name']} have a higher or lower follower count then {A['name']}")
            choice=input("Choose H for Higher or L for Lower:")
            choice=choice.upper()
            A,player_score,ans=comparision(A,B,choice,player_score,ans)
        
        print("Do you want to continue playing")
        play=input("Type Y for Yes or N for No: ")

            

if __name__=='__main__':
    main()
        

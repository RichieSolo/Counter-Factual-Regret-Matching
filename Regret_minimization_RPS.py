import numpy as np
import matplotlib.pyplot as plt
import random


'''
initilization of game variables 
rock paper scissors
'''

#cumilitve regret for each player
cumulative_regret_hero = [1,1,1]

#Player actions
actions = ["rock","paper","scissors"]

#opponent strategy profile
opponent_strategy_profile = [1/4,1/6,7/12]

#payoff matrix
payoff_matrix = {"rockpaper":-1, "rockscissors":1, "rockrock":0,
                 "paperrock":1, "paperscissors":-1, "paperpaper":0,
                 "scissorsrock":-1, "scissorspaper":1, "scissorsscissors":0}


hero_strategy_profile_sums = [1/3,1/3,1/3]

# this function normalizies our strategy profile
def normalize(strategy):
    normalizing_sum = sum(strategy)
    if normalizing_sum <= 0:
        return [1/3,1/3,1/3]
    return [a/normalizing_sum for a in strategy]
    
def get_hero_regrets(vil_action, her_action,  payoff_matrix):
    
    reward =  payoff_matrix[her_action + vil_action]
    print("reward", reward)
    
    if reward <= 0:
        if her_action == "rock":
            actions_regrets = ['paper'  + vil_action, 'scissors' + vil_action]
            print ("get_hero_regrets_function: actions_regrets", actions_regrets)
            regrets = [0,payoff_matrix[actions_regrets[0]] - reward , payoff_matrix[actions_regrets[1]] - reward]
            print("get_hero_regrets_function: regrets", regrets)
            print("get_hero_regrets_function:payoff_matrix[actions_regrets[0]]", payoff_matrix[actions_regrets[0]])
        elif  her_action == "paper":
            actions_regrets = ['rock'  + vil_action, 'scissors' + vil_action]
            print ("get_hero_regrets_function: actions_regrets", actions_regrets)
            regrets =  [payoff_matrix[actions_regrets[0]] - reward, 0, payoff_matrix[actions_regrets[1]] - reward]
            print("get_hero_regrets_function: regrets", regrets)
            print("get_hero_regrets_function:payoff_matrix[actions_regrets[0]]", payoff_matrix[actions_regrets[0]])
        elif her_action == "scissors":
            actions_regrets = ['rock'  + vil_action, 'paper' + vil_action]
            print ("get_hero_regrets_function: actions_regrets", actions_regrets)
            regrets =  [payoff_matrix[actions_regrets[0]] - reward, payoff_matrix[actions_regrets[1]] - reward, 0]
            print("get_hero_regrets_function: regrets", regrets)
            print("get_hero_regrets_function:payoff_matrix[actions_regrets[0]]", payoff_matrix[actions_regrets[0]])
                
        return regrets
    else:
        return [0,0,0]

for i in range(1000000):
    
    hero_strategy = normalize(cumulative_regret_hero)
    
    print("hero_strategy", hero_strategy)
    
    hero_strategy_profile_sums = [a+b for a,b in zip(hero_strategy_profile_sums, hero_strategy)]
    print("hero_strategy_profile_sums", hero_strategy_profile_sums)
    
    
    # hero chooses an action
    hero_action = np.random.choice(actions, p=hero_strategy)
    print("hero_action", hero_action)
    
    #villian chooses an action
    villian_action = np.random.choice(actions, p=opponent_strategy_profile)
    print("villian_action", villian_action)
    
    cumulative_regret_hero =  [a+b for a,b in zip(get_hero_regrets(villian_action, hero_action, payoff_matrix), cumulative_regret_hero)]
    
    
    
    
average_strategy_profile = [a/1000000 for a in hero_strategy_profile_sums]

print("cum_regret_hero", cumulative_regret_hero)
    
print("average_strategy_profile", average_strategy_profile)
    











    
    
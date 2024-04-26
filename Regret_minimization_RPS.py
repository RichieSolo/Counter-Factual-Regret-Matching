import numpy as np
import matplotlib.pyplot as plt
import random

''' initialization of game variables rock paper scissors '''
# Cumulative regret for each player
cumulative_regret_hero = [1, 1, 1]

# Player actions
actions = ["rock", "paper", "scissors"]

# Opponent strategy profile
opponent_strategy_profile = [1/3, 1/3, 1/3]

# Payoff matrix
payoff_matrix = {
    "rockpaper": -1, "rockscissors": 1, "rockrock": 0,
    "paperrock": 1, "paperscissors": -1, "paperpaper": 0,
    "scissorsrock": -1, "scissorspaper": 1, "scissorsscissors": 0
}

hero_strategy_profile_sums = [.4, .3, .2]
cum_reward = 0
cumulative_rewards = []

# Initialize lists to store average strategy profiles and cumulative regrets over time
average_strategy_profiles = []
cumulative_regrets = []

# This function normalizes our strategy profile
def normalize(strategy):
    normalizing_sum = sum(strategy)
    return [a / normalizing_sum for a in strategy]

def get_hero_regrets(vil_action, her_action, payoff_matrix):
    reward = payoff_matrix[her_action + vil_action]
    print("reward", reward)

    if reward < 0:
        if her_action == "rock":
            actions_regrets = ['paper' + vil_action, 'scissors' + vil_action]
            print("get_hero_regrets_function: actions_regrets", actions_regrets)
            regrets = [0, payoff_matrix[actions_regrets[0]] - reward, payoff_matrix[actions_regrets[1]] - reward]
            print("get_hero_regrets_function: regrets", regrets)
            print("get_hero_regrets_function:payoff_matrix[actions_regrets[0]]", payoff_matrix[actions_regrets[0]])
        elif her_action == "paper":
            actions_regrets = ['rock' + vil_action, 'scissors' + vil_action]
            print("get_hero_regrets_function: actions_regrets", actions_regrets)
            regrets = [payoff_matrix[actions_regrets[0]] - reward, 0, payoff_matrix[actions_regrets[1]] - reward]
            print("get_hero_regrets_function: regrets", regrets)
            print("get_hero_regrets_function:payoff_matrix[actions_regrets[0]]", payoff_matrix[actions_regrets[0]])
        elif her_action == "scissors":
            actions_regrets = ['rock' + vil_action, 'paper' + vil_action]
            print("get_hero_regrets_function: actions_regrets", actions_regrets)
            regrets = [payoff_matrix[actions_regrets[0]] - reward, payoff_matrix[actions_regrets[1]] - reward, 0]
            print("get_hero_regrets_function: regrets", regrets)
            print("get_hero_regrets_function:payoff_matrix[actions_regrets[0]]", payoff_matrix[actions_regrets[0]])
        return regrets
    else:
        return [0, 0, 0]

for i in range(1500):
    hero_strategy = normalize(cumulative_regret_hero)
    print("hero_strategy", hero_strategy)
    hero_strategy_profile_sums = [a + b for a, b in zip(hero_strategy_profile_sums, hero_strategy)]
    print("hero_strategy_profile_sums", hero_strategy_profile_sums)

    # Hero chooses an action
    hero_action = np.random.choice(actions, p=hero_strategy)
    print("hero_action", hero_action)

    # Villain chooses an action
    villain_action = np.random.choice(actions, p=opponent_strategy_profile)
    print("villain_action", villain_action)

    cumulative_regret_hero = [a + b for a, b in zip(get_hero_regrets(villain_action, hero_action, payoff_matrix), cumulative_regret_hero)]
    cum_reward += payoff_matrix[hero_action + villain_action]
    cumulative_rewards.append(cum_reward)

    # Calculate the average strategy profile for the current step
    average_strategy_profile = [a / (i + 1) for a in hero_strategy_profile_sums]
    average_strategy_profiles.append(average_strategy_profile)

    # Store the current cumulative regret for each action
    cumulative_regrets.append(cumulative_regret_hero)




# Plot the average strategy profile over time
plt.figure(figsize=(10, 6))
for i in range(3):
    plt.plot([profile[i] for profile in average_strategy_profiles], label=actions[i])
plt.axhline(y=1/3, color='black', linestyle='--', label='Nash Equilibrium')
plt.xlabel('Step')
plt.ylabel('Average Strategy Profile')
plt.title('Average Strategy Profile over Time')
plt.legend()
plt.show()

# Plot the cumulative regret for each action over time
plt.figure(figsize=(10, 6))
for i in range(3):
    plt.plot([regret[i] for regret in cumulative_regrets], label=actions[i])
plt.xlabel('Step')
plt.ylabel('Cumulative Regret')
plt.title('Cumulative Regret for Each Action over Time')
plt.legend()
plt.show()

# Plot the cumulative rewards
plt.figure(figsize=(10, 6))
plt.plot(cumulative_rewards)
plt.xlabel('Step')
plt.ylabel('Cumulative Reward')
plt.title('Cumulative Rewards per Step')
plt.show()

print("cum_regret_hero", cumulative_regret_hero)
average_strategy_profile = [a / 1500 for a in hero_strategy_profile_sums]
print("average_strategy_profile", average_strategy_profile)
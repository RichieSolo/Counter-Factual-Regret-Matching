#payoff matrix
payoff_matrix = {"rockpaper":-1, "rockscissors":1, "rockrock":0,
                 "paperrock":1, "paperscissors":-1, "paperpaper":0,
                 "scissorsrock":-1, "scissorspaper":1, "scissorsscissors":0}



# Python
def get_related_outcomes(selection, payoff_matrix):
    first, second = selection[:-5], selection[-5:]
    related_outcomes = [action + second for action in ["rock", "paper", "scissors"] if action + second != selection]
    return {k: v for k, v in payoff_matrix.items() if k in related_outcomes}

# Example usage:
selection = "paperrock"
related_outcomes = get_related_outcomes(selection, payoff_matrix)
print(related_outcomes)

regret_1 =  related_outcomes.keys()
print(regret_1)
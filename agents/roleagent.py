import numpy as np

class RoleAgent:
    def __init__(self, number_of_players: int, number_of_roles: int) -> None:
        if number_of_players <= 1:
            return
        
        # what this agent thinks every other player's role is
        ## [number_of_roles * number_of_players]
        self.probability_distribution = np.full((number_of_players, number_of_roles), float(1)/float(number_of_players - 1), dtype=float)
    


import numpy as np
from scipy.sparse import csr_matrix

class Oracle:
    def __init__(self, roles_available: int) -> None:
        ## [number_of_roles * 1]
        self.roles = csr_matrix(([1]*roles_available, (np.random.permutation(np.arange(roles_available)), list(range(roles_available)) ))).toarray()

    def reward_for_role(self, player_probability_distribution) -> int:
        return np.sum(self.roles * player_probability_distribution)
    
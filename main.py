#!/usr/bin/env python3

from oracle.oracle import Oracle
from agents.roleagent import RoleAgent

def main():
    print("starting oracle")
    roles_available = 10
    oracle = Oracle(roles_available)
    agent = RoleAgent(roles_available, roles_available)
    print(oracle.roles * agent.probability_distribution)
    print(oracle.reward_for_role(agent.probability_distribution))

if __name__ == '__main__':
    main()
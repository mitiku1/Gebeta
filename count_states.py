import envs
import gym
from collections import defaultdict
import numpy as np

def main():
    env = gym.make("Gebeta-v0")
    states_count = defaultdict(int)

    max_iteration = 100000

    for i in range(max_iteration):
        state = env.reset()
        done = False
        player = np.random.choice(2)
        
        game_iteration = 0
        while not done:
            action = np.random.choice(6)
            start, reward, done, info = env.step(action, player)
            player = (player+1)%2
            states_count[tuple(state)] += 1
            game_iteration += 1
        if (i+1) %100==0:
            print("Iteration: {} Number of states: {}".format(i+1, len(states_count)))
            


if __name__=='__main__':
    main()
import envs
import gym
from collections import defaultdict
import numpy as np

def main():
    env = gym.make("Gebeta-v0")
    states_count = set()

    max_iteration = 10000
    num_moves = []
    for i in range(max_iteration):
        state = env.reset()
        done = False
        player = np.random.choice(2)
        
        game_iteration = 0
        while not done:
            action = np.random.choice(6)
            start, reward, done, info = env.step(action, player)
            player = (player+1)%2
            states_count.add(tuple(state))
            game_iteration += 1
        num_moves.append(game_iteration)
        if (i+1) %1000==0:
            print("Iteration: {} Number of states: {}".format(i+1, len(states_count)))
    print("Avg moves:",sum(num_moves)/len(num_moves))


if __name__=='__main__':
    main()
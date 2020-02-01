import gym
import numpy as np
np.random.seed(1)
class GebetaEnv(gym.Env):
    def __init__(self, *args, **kwargs):
        super(GebetaEnv, self).__init__(*args, **kwargs)
        self.board = np.zeros((12, ), dtype=int) + 4 

    def reset(self):
        self.board = np.zeros((12, ), dtype=int) + 4 
        return self.board
    def render(self, mode="human", close=False):
        print()
        print("------------------------")
        for i in range(2):
            for j in range(6):
                print("{:2d}".format(self.board[i * 6+j]), end=" ")
            print()
        print("------------------------")
    def step(self, action, player):
        assert type(action) == int, "Action should integer type, but found '{}'".format(type(action))
        assert player == 0 or player == 1, "Player should be either 0 or 1, but found: {}".format(player)
        start_pos = action
        start_cell = self.get_cell(start_pos, player)
        if self.board[start_cell] == 0:
            
            if player == 0:
                done = (self.board[:6]==0).all()
            else:
                done = (self.board[6:]==0).all()
            if done:
                reward = -100
            else:
                reward = -5 # Reward of -5 for selecting empty 

        else:
            reward, done = self.play_one_round(start_pos, player)

        return self.board, reward, done, {}
    def get_cell(self, position, player):
        current_cell = position
        if position < 6:
            if player == 0:
                current_cell = 5 - position
            else:
                current_cell = 11 - position
        elif position>=6 and player == 1:
            current_cell = position - 6
        return current_cell

    def play_one_round(self, start_pos, player):
        reward = 0
        turn_over = False
        current_pos = start_pos
        turn_states = set(tuple(self.board))
        while not turn_over:
            current_cell = self.get_cell(current_pos, player)            
            num_seeds = self.board[current_cell]
            # print("current cell : {}, num_seeds: {}, player: {}, board: {},  iteration: {}".format(current_cell, num_seeds, player, self.board.sum(), iteration))
            self.board[current_cell] = 0
            
            while num_seeds>0:
                current_pos += 1
                current_pos = current_pos%12
                current_cell = self.get_cell(current_pos, player)
        
            
                if self.board[current_cell] == 0 and num_seeds == 1:
                    turn_over = True
                self.board[current_cell]+=1
                num_seeds -= 1
                if self.board[current_cell]==4:
                    reward += 4
                    self.board[current_cell] = 0
                    if num_seeds == 0:
                        turn_over = True
                if self.board.sum()==0:
                    turn_over = True
                if tuple(self.board) in turn_states:
                    turn_over = True
                    break
                turn_states.add(tuple(self.board))
                    
           
            
        if (self.board==0).all():
            done = True
        elif (self.board[6:]==0).all(): # The oponent doesnot have anything to play
            done = True
            reward += 100
        else:
            done = False
        return reward, done


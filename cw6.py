import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
from draw_plots import *

env = gym.make('FrozenLake-v1', desc=None, map_name="8x8", is_slippery = False, render_mode = "rgb_array")
state_size = env.observation_space.n
action_size = env.action_space.n
env.reset()

'''map "8x8": [
        "SFFFFFFF",
        "FFFFFFFF",
        "FFFHFFFF",
        "FFFFFHFF",
        "FFFHFFFF",
        "FHHFFFHF",
        "FHFFHFHF",
        "FFFHFFFG",
    ]
'''

end_states = [
    19, # Hole
    29, # Hole
    35, # Hole
    41, # Hole
    42, # Hole
    46, # Hole
    49, # Hole
    52, # Hole
    54, # Hole
    59, # Hole
    63, # Goal
    ]

def is_in_states(x, states):
    return x in states

def choose_action(state, qtable, epsilon):
    draw_num = np.random.uniform(0, 1)
    if draw_num < epsilon:
        action = np.random.randint(action_size)
    else:
        max_q_value = np.max(qtable[state, :])
        max_indices = np.where(qtable[state, :] == max_q_value)[0]
        action = np.random.choice(max_indices)
    return action

def state_to_coordinates(state):
    if state < 0 or state > 63:
        raise ValueError("State value should be between 0 and 63.")

    row = state // 8
    col = state % 8

    return row, col

def make_action(state, action):
    # move left
    if action == 0:
        if state in [0, 8, 16, 24, 32, 40, 48, 56]:
            new_state = state
        else:
            new_state = state - 1
    # move down
    elif action == 1:
        if state in [56, 57, 58, 59, 60, 61, 62, 63]:
            new_state = state
        else:
            new_state = state + 8
    # move right
    elif action == 2:
        if state in [7, 15, 23, 31, 39, 47, 55, 63]:
            new_state = state
        else:
            new_state = state + 1
    # move up
    elif action == 3:
        if state in [0, 1, 2, 3, 4, 5, 6, 7]:
            new_state = state
        else:
            new_state = state - 8

    return new_state

def get_standard_reward(state, new_state):
    if new_state == 63:
        reward = 1
    else:
        reward = 0
    return reward

# "Avoid holes"
def get_reward(state, new_state):
    if new_state in end_states:
        if new_state == 63:
            reward = 1
        else:
            reward = - 1
    else:
        reward = 0
    return reward

# "closer and faster to goal equals better"
def get_reward_v2(state, new_state):
    if state == new_state:
        row, col = state_to_coordinates(new_state)
        reward = ((row + col)/21)
    else:
        if new_state not in end_states:
            row, col = state_to_coordinates(new_state)
            reward = ((row + col)/14)
        elif new_state == 63:
            reward = 100
        else:
            reward = 0
    return reward


num_of_ind_runs = 25
num_episodes = 1000
t_max = 200


def q_learning(reward_function, learning_rate, gamma, epsilon):
    averaged_reward = np.zeros(num_episodes)
    for run in range(num_of_ind_runs):
        qtable = np.zeros((state_size, action_size))
        for episode in range(num_episodes):
            state = 0
            t = 0
            goal_reached = 0
            while t < t_max and not (is_in_states(state, end_states)):
                action = choose_action(state, qtable, epsilon)

                new_state, _, _, _, _ = env.step(action)

                # new_state = make_action(state, action)

                reward = reward_function(state, new_state)

                delta = reward + gamma * np.max(qtable[new_state, :]) \
                - qtable[state, action]

                qtable[state, action] = qtable[state, action] + learning_rate * delta

                t += 1
                state = new_state
                if state == 63:
                    goal_reached = 1
                
            averaged_reward[episode] = averaged_reward[episode] + goal_reached
            env.reset()
            
    averaged_reward = averaged_reward/(num_of_ind_runs)
    return averaged_reward

learning_rate1 = 0.05
gamma1 = 0.8
epsilon1 = 0.1

learning_rate2 = 0.9
gamma2 = 0.8
epsilon2 = 0.1

averaged_reward_base = q_learning(get_standard_reward, learning_rate1, gamma1, epsilon1)
# averaged_reward = q_learning(get_reward, learning_rate1, gamma1, epsilon1)
# averaged_reward_v2 = q_learning(get_reward_v2, learning_rate1, gamma1, epsilon1)

# draw_three_plots(averaged_reward_base, averaged_reward, averaged_reward_v2, learning_rate1, gamma1, epsilon1)

averaged_reward_base2 = q_learning(get_standard_reward, learning_rate2, gamma2, epsilon2)
draw_two_plots(averaged_reward_base, averaged_reward_base2, learning_rate1, gamma1, epsilon1, learning_rate2, gamma2, epsilon2)

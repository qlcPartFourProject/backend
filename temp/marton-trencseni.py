# source: https://bytepawn.com/solving-the-cartpole-reinforcement-learning-problem-with-pytorch.html

import argparse
import gym
import numpy as np
from itertools import count
from random import random

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

# (1)
env = gym.make('CartPole-v1')
print(env._max_episode_steps)

# (2)
def select_action_random(state):
    if random() < 0.5:
        return 0
    else:
        return 1

def goodness_score(select_action, num_episodes=100):
    num_steps = 500
    ts = []
    for episode in range(num_episodes):
        state = env.reset()
        for t in range(1, num_steps+1):
            action = select_action(state)
            state, _, done, _, _ = env.step(action)
            if done:
                break
        ts.append(t)
    score = sum(ts) / (len(ts)*num_steps)
    return score

print(goodness_score(select_action_random))

# (3)
def select_action_simple(state):
    if state[2] < 0:
        return 0
    else:
        return 1

goodness_score(select_action_simple)

# (4)
def select_action_good(state):
    if state[2]+state[3] < 0:
        return 0
    else:
        return 1

goodness_score(select_action_good)

# (5)
class PolicyNN(nn.Module):
    def __init__(self):
        super(PolicyNN, self).__init__()
        self.fc = nn.Linear(4, 2)

    def forward(self, x):
        x = self.fc(x)
        return F.softmax(x, dim=1)

def select_action_from_policy(model, state):
    state = torch.from_numpy(state).float().unsqueeze(0)
    probs = model(state)
    m = Categorical(probs)
    action = m.sample()
    return action.item(), m.log_prob(action)

def select_action_from_policy_best(model, state):
    state = torch.from_numpy(state).float().unsqueeze(0)
    probs = model(state)
    if probs[0][0] > probs[0][1]:
        return 0
    else:
        return 1
    
# (6)
model_untrained = PolicyNN()

print(
    goodness_score(lambda state: select_action_from_policy(model_untrained, state)[0]),
    goodness_score(lambda state: select_action_from_policy_best(model_untrained, state))
)

# (7)
model = PolicyNN()
optimizer = optim.Adam(model.parameters(), lr=0.01)

def train_wont_work(num_episodes=100):
    num_steps = 500
    for episode in range(num_episodes):
        state = env.reset()
        for t in range(1, num_steps+1):
            action = select_action(state)
            state, _, done, _ = env.step(action)
            if done:
                break
        loss = 1.0 - t / num_steps
        # this doesn't actually work, because
        # the loss function is not an explicit
        # function of the model's output; it's
        # a function of book keeping variables
        optimizer.zero_grad()
        loss.backward() # AttributeError: 'float' object has no attribute 'backward'
        optimizer.step()

def train_simple(num_episodes=10*1000):
    num_steps = 500
    ts = []
    for episode in range(num_episodes):
        state = env.reset()
        probs = []
        for t in range(1, num_steps+1):
            action, prob = select_action_from_policy(model, state)
            probs.append(prob)
            state, _, done, _ = env.step(action)
            if done:
                break
        loss = 0
        for i, prob in enumerate(probs):
            loss += -1 * (t - i) * prob
        print(episode, t, loss.item())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        ts.append(t)
        if len(ts) > 10 and sum(ts[-10:])/10.0 >= num_steps * 0.95:
            print('Stopping training, looks good...')
            return

train_simple()
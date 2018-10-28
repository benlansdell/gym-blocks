# gym-blocks

[![Build Status](https://travis-ci.org/benlansdell/gym-blocks.svg?branch=master)](https://travis-ci.org/benlansdell/gym-blocks)

A simple environment for OpenAI gym to test learning from observation. A number of blocks and other agents inhabit a gridworld. When some blocks are pushed to unlabled reward locations, rewards are given. The environment has three modes, used to train and then test an agent's observational learning abilities.

Possible actions are:
* 0: do nothing
* [wasd]: move up, left, down, right

There are three phases/environments defined:

1. Familiarization phase: no rewards are given, the agent can push blocks around.
2. Observation phase: rewards are given, the agent cannot move blocks around. Actions do nothing -- blocks are pushed by some either a ghost, or by other agents out of the agent's control. 
3. Test phase: rewards are given, the agent can push blocks. 

The episode terminates after a given number of steps have been taken (by
default 1000). 

## Installation

`pip install --user git+https://github.com/benlansdell/gym-blocks`

## Usage

```
import gym_blocks

env = gym.make("Blocks")

#Number of other agents
env.n_agents = 2
#Number of other blocks
env.n_blocks = 5
# Adjust number of steps before termination
env.max_steps = 2000
env.max_test_steps = 10
# Adjust random start location
env.random_start = False
```

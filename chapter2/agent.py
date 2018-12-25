import random

class Agent(object):
    def __init__(self, env):
        """set up the agent"""
        self.env = env

    def go(self, n):
        """acts for n time steps"""
        raise NotImplementedError("go")  # abstract method
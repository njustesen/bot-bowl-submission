#!/usr/bin/env python3

import ffai
import numpy as np


class MyRandomBot(ffai.Agent):

    def __init__(self, name, seed=None):
        super().__init__(name)
        self.my_team = None
        self.rnd = np.random.RandomState(seed)

    def new_game(self, game, team):
        self.my_team = team

    def act(self, game):
        # Select a random action type
        while True:
            action_choice = self.rnd.choice(game.state.available_actions)
            # Ignore PLACE_PLAYER actions
            if action_choice.action_type != ffai.ActionType.PLACE_PLAYER:
                break

        # Select a random position and/or player
        position = self.rnd.choice(action_choice.positions) if len(action_choice.positions) > 0 else None
        player = self.rnd.choice(action_choice.players) if len(action_choice.players) > 0 else None

        # Make action object
        action = ffai.Action(action_choice.action_type, position=position, player=player)

        # Return action to the framework
        return action

    def end_game(self, game):
        pass


# Register the bot to the framework
ffai.register_bot('my-random-bot', MyRandomBot)
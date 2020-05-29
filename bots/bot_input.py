class Bot:
    def __init__(self, username):
        self.username = username

    
    def get_response(self, game_state):
        # get action
        usernames = [i[0] for i in game_state['action']]
        action = game_state['action'][usernames.index(self.username)][1]

        return input(f"{ action } action: ")

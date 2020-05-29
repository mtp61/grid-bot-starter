import socketio
import json
import copy
from bots.bot_input import Bot


# constants
USERNAME = "bot"
GAMENAME = "test"

# setup the bot
bot = Bot(USERNAME)

# make game_state variable
game_state = {}
game_state_dump = json.dumps(game_state)
action = []
action_dump = ""

# create the client
sio = socketio.Client()

# connect to the server
sio.connect("http://localhost:3331/" + GAMENAME)

# send connection message
sio.emit('game_connection', {"gameName": GAMENAME, 
                             "username": USERNAME})

# ready up
sio.emit('chat-message', {"gameName": GAMENAME,
                          "username": USERNAME,
                          "message": "!ready"})


@sio.on('game_state')
def new_game_state(data):
    global game_state
    global game_state_dump
    global action
    global action_dump

    # check for new game state
    if json.dumps(data) != game_state_dump:
        # deep copy
        game_state = copy.deepcopy(data)
        game_state_dump = json.dumps(game_state)

        # update action
        # filters out game state updates with just messages
        if json.dumps(game_state['action']) != action_dump and 'action' in game_state.keys():
            # deep copy
            action = copy.deepcopy(game_state['action'])
            action_dump = json.dumps(action)
        
            # check if there is an action for me
            if USERNAME in [i[0] for i in action]:
                # get a response from the bot
                message = bot.get_response(game_state)

                # send the response
                sio.emit('chat-message', {"gameName": GAMENAME,
                                            "username": USERNAME,
                                            "message": message})

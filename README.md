# Grid Bot Starter

## How To Use a Bot

- Run the develop branch (updates not in master as of writing) of the server on your computer https://github.com/mtp61/powergrid-online
- Open the url of your server in browser (localhost:3331 by default) and make a new game for your bot to connect to
- Run client.py
- Play against your bot from the browser

## How To Make a bot

- Bots are classes called Bot in files in the directory bots
- You can rewrite the input bot or create a totally new one, but you may need to make changes to client.py

## What I'm Thinking For Bots

- Powergrid is perfect information so the bot shouldn't need to store any info throughout the game, the game state is the only thing needed to make decisions
  - You should enable showing money (in the server) since it would be easy to add tracking money
- You can play against your bot or play bot vs bot
- For playing many matches bot vs bot, you may want to make changes to your server (more updates in the works to make this easier)
- There are still a few server issues (as of writing) that might get in the way but it's being worked on
- A simple rules based bot shouldn't be too hard and is probably a good place to start
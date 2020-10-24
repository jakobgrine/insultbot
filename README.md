## Description
This bot replaces messages of a specific person with a random ~~insult~~ compliment.

## Installation
1. Clone this repository: `git clone https://github.com/jakobgrine/insultbot.git`
2. Change into the directory: `cd insultbot`
3. Install the requirements: `pip install -r requirements.txt`
4. Start the discord bot to generate the configuration file: `python main.py`
5. Configure the discord bot as described [below](#configuration)
6. Restart the discord bot: `python main.py`

## Configuration
Edit the configuration file `config.json` to configure the discord bot.

Name | Meaning
--- | ---
`command_prefix` | No special meaning for now
`insults` | List of insults to replace the messages with
`name` | Name to substitute for `{name}` in the insult messages
`scam_id` | ID of the user whose messages are replaced
`tokens/discord` | Discord token

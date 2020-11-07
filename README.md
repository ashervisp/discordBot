# DiscordBot
This is a Discord bot built for personal server use.

## What they mean!

**discordBot.py** : This is where all the commands and authorization are written. Uses the Discord.py Discord API.\
**quotedata.py**: A web scrapper that takes quotes from Goodreads.com and outputs results into an excel file. \
**redditbot.py**: A reddit bot that uses the Reddit API to gather 100 results from a specific subreddit and outputs results into an excel file.\
**cog.py** : This enables the cog function in discordBot.py, enabling a change in the !help command in Discord.\
**.env** : Stores the Discord API authorization token, server name, and channel name to output in.

## How to use!

1.Go to https://discord.com/ and create an account.\
2.Go to https://discord.com/developers/, sign up, and start a new application.\
3.Grab your personal bot authorization token. Input key in .env where it says DISCORD_TOKEN.\
4.Open Discord. Make your own server.\
5.Place server name in after DISCORD_GUILD.\
6.Create a text channel. Right click on the channel to get the ID and place that ID into DISCORD_CHANNEL.\
7.You're all set (The reddit bot is the only thing that won't work at the moment though!)\

(In progress)

from telegram.ext import Updater, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater('1389188838:AAH8qW2LXnc6mlnzeo3x3G_q1E4jwuGam5k')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()


# Requirements:
### Request to best on UFC fight 1 of 5
### Display the 2 fighters A and B
#### Hon selects A --> save
#### Van selects A --> save
#### Diggy selects B --> save

## Fighter A wins
### Hon receives 1 point --> save
### Van receives 1 point --> save
### Diggy receives 0 points --> save

## Request to show leaderboard
### Display Hon 1-0, Van 1-0, Diggy 0-1



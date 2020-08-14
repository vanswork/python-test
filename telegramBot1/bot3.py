from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1389188838:AAH8qW2LXnc6mlnzeo3x3G_q1E4jwuGam5k', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    text_intro1 = 'Hi, welcome to Mixtape Legends Experience, Volume 3: NYC Love letter.'
    text_intro2 = 'My name is Wizard. I come from the land of smoke, eat, and chill. I will be your guide today through NYC.'
    text_intro3 = 'My job is to tell you what to do and when to do it. If you follow through, you will experience one of the most magical nights in NYC'
    text_intro4 = 'Would you like to go on this adventure? To continue, type:' \
                  '\n''/wizard yes\''
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro3)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro4)


def wizard(update, context):
    text_initial = ' '.join(context.args).lower()
    text_msg = text_initial
    if text_msg == 'yes':
        text_pt1 = 'To activate the adventure, begin by saying this aloud, three times, ' \
                    'in sync with friends: "Wizard, take me on a magical NYC adventure." '
        text_next = '\n\n Upon completing the spell, type ' \
                           '\n\'/wizard we cast the spell\''
        text_send = text_pt1 + text_next
    elif text_msg == 'we cast the spell':
        text_pt1 = 'Good. The adventure now begins... '
        text_next = '\n\n To receive the first big step of your adventure, type: ' \
                    '\n\'/wizard 1\''
        text_send = text_pt1 + text_next
    elif text_msg == '1':
        text_pt1 = 'Hangout on Notorious B.I.G.\'s childhood stoop at 197 St James Place, Brooklyn, NY, '
        text_pt2 = 'and SMOKE a joint of Wedding Cake.'
        text_pt3 = '\n\nThe strain is an uplifting indica-dominant hybrid strain known for it\'s relaxing and euphoric effects.'
        text_next = '\n\n When finished up, and you want the next part of your adventure, type: ' \
                    '\n\'/wizard 2\''
        text_send = text_pt1 + text_pt2 + text_pt3 + text_next
    elif text_msg == '2':
        text_pt1 = 'Head over to X at Brooklyn, NY to EAT one of the best crafted sandwiches in the last 2 decades.'
        text_next = '\n\n When finished up, and you want the next part of your adventure, type: ' \
                    '\n\'/wizard 3\''
        text_send = text_pt1 + text_next
    elif text_msg == '3':
        text_pt1 = 'Make your way to Christopher Wallace playground and play basketball.'
        text_next = '\n\n When your done hoopin\', let me know by typing:' \
                    '\n\'/wizard we finished chapter 1\''
        text_send = text_pt1 + text_next
    elif text_msg == 'we finished chapter 1':
        text_pt1 = 'Congratulations. You are 1/3 through the adventure. For the next chapter, travel to Chinatown [Address]'
        text_next = '\n\n When you arrived, type:' \
                    '\n\'/wizard 4\''
        text_send = text_pt1 + text_next
    elif text_msg == '4':
        text_pt1 = 'Welcome to chapter 2. Hangout on [X] stoop at [Address] '
        text_pt2 = 'and SMOKE a joint of Big Gas.'
        text_pt3 = '\n\nThe strain is a pure indica that soothes your body from back of the head and spine through the rest of your body.'
        text_next = '\n\n When finished up, and you want the next part of your adventure, type: ' \
                    '\n\'/wizard 5\''
        text_send = text_pt1 + text_pt2 + text_pt3 + text_next
    elif text_msg == '5':
        text_pt1 = 'Head over Nom Wah (Dim Sum) to eat their delicious pork steam buns.'
        text_next = '\n\n When finished, and you want the next part of your adventure, type: ' \
                    '\n\'/wizard 6\''
        text_send = text_pt1 + text_next
    elif text_msg == '6':
        text_pt1 = 'Film a scene from the movie "Clockwork Orange'
        text_next = '\n\n When completed, type:' \
                    '\n\'/wizard we finished chapter 2\''
        text_send = text_pt1 + text_next
    elif text_msg == 'we finished chapter 2':
        text_pt1 = 'Congratulations. You are 2/3 through the adventure. For the next chapter, travel to West Village, on bike. [Address]'
        text_next = '\n\n When you arrive, type:' \
                    '\n\'/wizard 7\''
        text_send = text_pt1 + text_next
    elif text_msg == '7':
        text_pt1 = 'Welcome to the final chapter. Hangout on [X] stoop at [Address] '
        text_pt2 = 'and SMOKE a joint of Forbidden Fruit.'
        text_pt3 = '\n\nThe strain hits hard between the eyes and lays into the body with each hit. Deep relaxation.'
        text_next = '\n\n When finished, and you want the next part of your adventure, type: ' \
                    '\n\'/wizard 8\''
        text_send = text_pt1 + text_pt2 + text_pt3 + text_next
    elif text_msg == '8':
        text_pt1 = 'Visit Magnolia\'s and eat their banana pudding.'
        text_next = '\n\n When finished, and you want the last step of your adventure, type: ' \
                    '\n\'/9\''
        text_send = text_pt1 + text_next
    elif text_msg == '9':
        text_pt1 = 'Wear your headphones, play this [track] and take a stroll around the block.'
        text_next = '\n\n When completed, type:' \
                    '\n\'/wizard we finished the final chapter'
        text_send = text_pt1 + text_next
    elif text_msg == 'we finished the final chapter':
        text_pt1 = 'Congratulations. You have completed Mixtape Legends Experience volume 3: NYC Love Letter'
        text_send = text_pt1
    else:
        text_send = "Huh? What?"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# NON FUNCTIONS


# from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# from telegram.ext import CommandHandler
start_handler = CommandHandler('wizard', wizard)
dispatcher.add_handler(start_handler)

# from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()


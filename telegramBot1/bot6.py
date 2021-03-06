import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token='1318955569:AAGZoK3VxDz1nNWNYvv7_avjcM4b06Kp5Zw', use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/wizard-12.jpg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)

    text_intro1 = 'Welcome to Mixtape Legends Experience, Volume 3'
    text_intro2 = 'Today\'s mixtape is a tour of NYC and my job is to be your tour bot guide.'
    text_intro3 = '\n\nDo you want to know more about the tour? Type:' \
                  '\n\n\'/guide tell me more\''

    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro1)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro2)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_intro3)


def wizard(update, context):
    text_initial = ' '.join(context.args).lower()
    text_msg = text_initial
    if text_msg == 'tell me more':
        text_pt1 = 'The pandemic sucks, and there aren\'t many ways to socially connect at the moment. A temporary emotional cure is hanging out with friends and going on an adventure, via a tour of NYC. '
        text_pt2 = '\n\nThe tour carries you and friends across 3 NYC neighborhoods, where you will smoke, eat, and chill. '
        text_pt3 = '\n\nI can guide you by giving you step by step instructions. '
        text_send = text_pt1 + text_pt2 + text_pt3
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

        text_next = 'Would you like to know which supplies are required to complete the tour? To learn more, type:' \
                    '\n\n\'/guide supplies\''
        text_send = text_next
    elif text_msg == 'supplies':
        photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/inventory.jpg'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)

        text_pt1 = 'You will need the following for each participant:'
        text_pt2 = '\n\n1x Joint with Sativa (Birthday Cake)'
        text_pt3 = '\n1x Joint with Sativa/Indica mix (Survival)'
        text_pt4 = '\n1x Joint with Indica (Forbidden Fruit)'
        text_pt5 = '\nA lighter for the joints'
        text_pt6 = '\nPrinted map for one of the tour activities'
        text_pt7 = '\nWalking Shoes'
        text_pt8 = '\nA Basketball (to be shared among everyone)'
        text_pt9 = '\nAccess to a bike, like Citibike'
        text_pt10 = '\nHeadphones'
        text_pt11 = '\nMoney for food'
        text_pt12 = '\nDrinking water'
        text_send = text_pt1 + text_pt2 + text_pt3 + text_pt4 + text_pt5 + text_pt6 + text_pt7 + text_pt8 + text_pt9 + text_pt10 + text_pt11 + text_pt12
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

        text_next = '\n\nWhen you are ready to begin the tour, type:' \
                    '\n\n\'/guide play mixtape legends volume 3\''
        text_send = text_next
    elif text_msg == 'play mixtape legends volume 3':
        text_pt1 = 'Inserting tape...'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt1)
        time.sleep(2)
        photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/Legends2020.jpg'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)
        text_pt3 = 'The tour begins in Brooklyn...'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt3)
        text_next = '\n\n To receive instructions for the first activity, type: ' \
                    '\n\n\'/guide 1\''
        text_send = text_next
    elif text_msg == '1':
        text_pt1 = 'Remember this song? One moment, digging through my archives...'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt1)
        text_pt2 = 'assets/BIGGIE-JUICY3.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(text_pt2, 'rb'), supports_streaming=True, timeout=10000)
        text_next = '\n\nTo continue, type: ' \
                    '\n\n\'/guide 1a\''
        text_send = text_next
    elif text_msg == '1a':
        text_pt1 = 'The Notorious B.I.G. had far reaching aspirations that were never realized because his life was cut short. '
        text_pt2 = '\n\nI want you to celebrate his life by smoking a Birthday Cake joint on his childhood stoop. '
        text_send = text_pt1 + text_pt2
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

        text_pt3 = 'Address:'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt3)
        text_pt4 = '226 Saint James Place, Brooklyn, NY'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt4)

        text_pt5 = '\n\nThe strain is an uplifting strain known for it\'s relaxing' \
                   ' and euphoric effects.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt5)

        text_next = '\n\nWhen finished, and ready for the next activity, type: ' \
                    '\n\n\'/guide 2\''
        text_send = text_next
    elif text_msg == '2':
        text_pt1 = 'It\'s time to eat. Biggie had unrealized aspirations to open a soul food restaurant. Visit Napoleon Southern Cuisine and try their wings.'
        text_next = '\n\nWhen finished, and ready for the next activity, type: ' \
                    '\n\n\'/guide 3\''
        text_send = text_pt1 + text_next
    elif text_msg == '3':
        text_pt1 = 'Make your way to Christopher \'Biggie\' Wallace basketball courts, named in his honor. Enjoy the space by playing basketball.'
        text_next = '\n\nWhen finished, and ready for the next activity, type: ' \
                    '\n\n\'/guide 4\''
        text_send = text_pt1 + text_next
    elif text_msg == '4':
        text_pt1 = 'Congratulations. You are a third of the way through the tour. ' \
                   'For the next neighborhood, travel to Chinatown to learn about Five Points.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt1)
        text_pt2 = '105 Mosco Street, NY, NY'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt2)
        text_next = '\n\nWhen you arrive, type:' \
                    '\n\n\'/guide 4a\''
        text_send = text_next
    elif text_msg == '4a':
        text_pt1 = 'Welcome to modern day NYC chinatown. You are currently standing on the last remaining streets of America\'s first melting pot.'

        photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/five-points.jpg'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)

        text_pt2 = '\n\n1822: Emancipation ended, African Americans and Irish moved here.'
        text_pt3 = '\n1846: Battle of Five Points (Dead Rabbits vs Natives).'
        text_pt4 = '\n1863: Draft Riots. Navy bombard Paradise Square.'
        text_pt5 = '\n1870: Chinese and Italians expanded.'
        text_pt6 = '\n1965: End of US immigration restrictions.'
        text_pt7 = '\n1980: NYC Chinatown holds the largest Chinese community in America.'
        text_next = '\n\nTo learn more, type: ' \
                    '\n\n\'/guide 4b\''
        text_send = text_pt1 + text_pt2 + text_pt3 + text_pt4 + text_pt5 + text_pt6 + text_pt7 + text_next
    elif text_msg == '4b':
        text_pt1 = 'Mosco street is one of the last remaining roads that lead to Five Points (Remember the movie Gangs of New York?)'
        text_pt2 = '\n\nRead what Charles Dickens wrote about Five points:'
        text_pt3 = '\n\n“What place is this, to which the squalid street conducts us? A kind of square of leprous houses, some of which are attainable only by crazy wooden stairs without. What lies behind this tottering flight of steps? Let us go on again, and plunge into the Five Points. This is the place; these narrow ways diverging to the right and left, and reeking everywhere with dirt and filth. \n\nSuch lives as are led here, bear the same fruit as elsewhere. The coarse and bloated faces at the doors have counterparts at home and all the world over. Debauchery has made the very houses prematurely old. See how the rotten beams are tumbling down, and how the patched and broken windows seem to scowl dimly, like eyes that have been hurt in drunken forays. Many of these pigs live here. Do they ever wonder why their masters walk upright instead of going on all fours, and why they talk instead of grunting?"'
        text_next = '\n\nTo learn more, type: ' \
                    '\n\n\'/guide 4c\''
        text_send = text_pt1 + text_pt2 + text_pt3 + text_next
    elif text_msg == '4c':
        text_pt1 = 'Only the strong and scrappy could survive: In 1840\'s, for 15 years, a person was murdered every night. '
        text_pt2 = 'Watch a clip from Gangs of New York to get glimpse of what it was like:'
        text_send = text_pt1 + text_pt2
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)
        video_pt1 = 'assets/five-points.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(video_pt1, 'rb'), supports_streaming=True, timeout=10000)
        text_next = '\n\nTo learn more, type: ' \
                    '\n\n\'/guide 4d\''
        text_send = text_next
    elif text_msg == '4d':
        text_pt1 = 'Check out this map to understand where you are standing in the original Five Points.'
        text_send = text_pt1
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

        photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/five-points-map2.jpg'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)

        text_next = '\n\nTo learn what you should do here, type: ' \
                    '\n\n\'/guide 4e\''
        text_send = text_next
    elif text_msg == '4e':
        text_pt1 = 'SMOKE a Survival Joint.'
        text_pt2 = '\n\nThe strain is a pure indica that soothes your body from back of the head and spine through the rest of your body.'
        text_next = '\n\nWhen finished, and ready for the next activity, type: ' \
                    '\n\n\'/guide 5\''
        text_send = text_pt1 + text_pt2 + text_next
    elif text_msg == '5':
        text_pt1 = 'Head over Nom Wah to eat their delicious pork steam buns.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt1)
        text_pt2 = '13 Doyers St, ny, ny'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt2)
        text_next = '\n\nWhen finished, and ready for the next activity, type: ' \
                    '\n\n\'/guide 6\''
        text_send = text_next
    elif text_msg == '6':
        text_pt1 = 'On bike, travel to the final neighborhood, West Village. (Dock your bikes before starting the next activity) '
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt1)
        text_pt2 = '10 St Lukes Pl, New York, NY'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt2)
        text_next = '\n\nWhen you arrive and are ready to start the next activity, type:' \
                    '\n\n\'/guide 7\''
        text_send = text_next
    elif text_msg == '7':
        text_pt1 = 'Welcome to the final neighborhood. The affluent and mighty live here. '
        text_pt2 = 'They can wield their power for entertainment, and for the good. Or, for bad, like Bill Cosby.'
        text_next = '\n\nTo learn more, type: ' \
                    '\n\n\'/guide 7a\''
        text_send = text_pt1 + text_pt2 + text_next
    elif text_msg == '7a':
        text_pt1 = '\n\nYou are standing at the stoop portrayed in the Bill Cosby show.'
        text_pt2 = '\n\nWatch this clip from Dave Chappelle.'
        text_send = text_pt1 + text_pt2
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

        video_pt1 = 'assets/dave.mp4'
        context.bot.send_video(chat_id=update.effective_chat.id, video=open(video_pt1, 'rb'), supports_streaming=True, timeout=10000)

        text_next = '\n\nTo learn what you should do here, type: ' \
                    '\n\n\'/guide 7b\''
        text_send = text_next
    elif text_msg == '7b':
        text_pt1 = 'SMOKE Forbidden Fruit joint and hang out on Cosby\'s stoop'
        text_pt2 = '\n\nThe strain hits hard between the eyes and lays into the body with each hit. Deep relaxation.'
        text_next = '\n\nWhen finished, and ready for the next activity, type: ' \
                    '\n\n\'/guide 8\''
        text_send = text_pt1 + text_pt2 + text_next
    elif text_msg == '8':
        text_pt1 = 'Eat at Magnolia\'s. Try their banana pudding.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt1)
        text_pt2 = 'West 11th Street, 401 Bleecker St, NY, NY'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt2)
        text_next = '\n\nWhen finished, and ready for the final activity, type: ' \
                    '\n\n\'/guide 9\''
        text_send = text_next
    elif text_msg == '9':
        text_pt1 = 'The end of the tour is near. I want to thank you for going on today\'s adventure. The project was created during the pandemic, when it felt as though all the fun had drained out of NYC and would never be replenished. This project is a love letter to NYC for friends and family to have fun one more time in the city of New York.'
        text_pt2 = '\n\nFor your last activity, I want you to enjoy the city by taking a leisurely stroll through the neighborhood, to soak up the sights and feelings, while listening to the track below.'
        text_send = text_pt1 + text_pt2
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_send)

        text_pt3 = '\n\nPlay this track:'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt3)

        audio_pt1 = 'assets/LegendsMusic.mp3'
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=open(audio_pt1, 'rb'), supports_streaming=True,timeout=10000)

        text_pt4 = '\n\nWalk this route:'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_pt4)

        photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/walk-map.png'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)

        text_next = '\n\nWhen complete, type:' \
                    '\n\n\'/guide eject mixtape'
        text_send = text_next
    elif text_msg == 'eject mixtape':
        photo_pt1 = 'https://raw.githubusercontent.com/vanswork/python-test/master/telegramBot1/assets/Legends2020.jpg'
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_pt1)

        text_pt1 = 'Thank you for participating in Mixtape Legends Experience, Volume 3. I hope you enjoyed smoking, eating, and chilling in NYC. ' \
                   '\n\nFarewell, Nathan. I hope you remember this day.'
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
start_handler = CommandHandler('guide', wizard)
dispatcher.add_handler(start_handler)

# from telegram.ext import MessageHandler, Filters
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)



updater.start_polling()


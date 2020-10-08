import telebot
from telebot.types import InlineKeyboardMarkup
import XO_logic

import config
import variables
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Начать игру", callback_data='start')
    markup.add(item1)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот-версия игры "
                     "крестики-нолики для игры с другом на одном устройстве".format(
                         message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def game(call):
    if call.data:
        if call.data == "start":
            for line in variables.field:
                print(line)
            for line in variables.field_pos:
                print(line)
            XO_logic.restarting()

            markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton(variables.filler_symbol[0], callback_data='0')
            item2 = types.InlineKeyboardButton(variables.filler_symbol[1], callback_data='1')
            item3 = types.InlineKeyboardButton(variables.filler_symbol[2], callback_data='2')
            item4 = types.InlineKeyboardButton(variables.filler_symbol[3], callback_data='3')
            item5 = types.InlineKeyboardButton(variables.filler_symbol[4], callback_data='4')
            item6 = types.InlineKeyboardButton(variables.filler_symbol[5], callback_data='5')
            item7 = types.InlineKeyboardButton(variables.filler_symbol[6], callback_data='6')
            item8 = types.InlineKeyboardButton(variables.filler_symbol[7], callback_data='7')
            item9 = types.InlineKeyboardButton(variables.filler_symbol[8], callback_data='8')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
            bot.send_message(call.message.chat.id, "Окей, начинаем\n", parse_mode="html",
                             reply_markup=markup)
        # ==============================================================================================
        elif len(call.data) == 1:
            if variables.step_counter % 2 == 0:
                character_id = 0
            else:
                character_id = 1

            y = int(call.data) // 3
            x = int(call.data) % 3
            if variables.field_pos[y][x] == 0:
                variables.field[y][x] = variables.character[character_id]
                variables.field_pos[y][x] = 1
                variables.filler_symbol[int(call.data)] = variables.character[character_id]
                markup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton(variables.filler_symbol[0], callback_data='0')
                item2 = types.InlineKeyboardButton(variables.filler_symbol[1], callback_data='1')
                item3 = types.InlineKeyboardButton(variables.filler_symbol[2], callback_data='2')
                item4 = types.InlineKeyboardButton(variables.filler_symbol[3], callback_data='3')
                item5 = types.InlineKeyboardButton(variables.filler_symbol[4], callback_data='4')
                item6 = types.InlineKeyboardButton(variables.filler_symbol[5], callback_data='5')
                item7 = types.InlineKeyboardButton(variables.filler_symbol[6], callback_data='6')
                item8 = types.InlineKeyboardButton(variables.filler_symbol[7], callback_data='7')
                item9 = types.InlineKeyboardButton(variables.filler_symbol[8], callback_data='8')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                variables.step_counter += 1
                if XO_logic.win_checker(variables.field):
                    win_markup = types.InlineKeyboardMarkup(row_width=1)
                    win_markup_item = types.InlineKeyboardButton("Начать заново", callback_data='start')
                    win_markup.add(win_markup_item)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="<b>Игра окончена</b>\nВыиграл <b>{}</b>\n{}\n{}\n{}".format(
                                              variables.character[character_id], variables.field[0], variables.field[1],
                                              variables.field[2]),
                                          parse_mode="html", reply_markup=win_markup)
                elif XO_logic.tie_checker(variables.field_pos):
                    tie_markup = types.InlineKeyboardMarkup(row_width=1)
                    tie_markup_item = types.InlineKeyboardButton("Начать заново", callback_data='start')
                    tie_markup.add(tie_markup_item)

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="<b>Ничья</b>\n{}\n{}\n{}".format(variables.field[0],
                                                                                 variables.field[1],
                                                                                 variables.field[2]),
                                          parse_mode="html", reply_markup=tie_markup)
                else:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="Ходит <b>{}</b>".format(variables.character[1 - character_id]),
                                          parse_mode="html", reply_markup=markup)
            else:
                markup: InlineKeyboardMarkup = types.InlineKeyboardMarkup(row_width=3)
                item1 = types.InlineKeyboardButton(variables.filler_symbol[0], callback_data='0')
                item2 = types.InlineKeyboardButton(variables.filler_symbol[1], callback_data='1')
                item3 = types.InlineKeyboardButton(variables.filler_symbol[2], callback_data='2')
                item4 = types.InlineKeyboardButton(variables.filler_symbol[3], callback_data='3')
                item5 = types.InlineKeyboardButton(variables.filler_symbol[4], callback_data='4')
                item6 = types.InlineKeyboardButton(variables.filler_symbol[5], callback_data='5')
                item7 = types.InlineKeyboardButton(variables.filler_symbol[6], callback_data='6')
                item8 = types.InlineKeyboardButton(variables.filler_symbol[7], callback_data='7')
                item9 = types.InlineKeyboardButton(variables.filler_symbol[8], callback_data='8')
                markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="<b>Невозможный ход</b>\nХодит <b>{}</b>".format(
                                          variables.character[character_id]),
                                      parse_mode="html", reply_markup=markup)


bot.polling(none_stop=True, interval=0)

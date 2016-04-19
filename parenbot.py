#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A telegram bot that hates unmatched parentheses.

TOKEN=""

from telegram.ext import Updater
import logging

maps="(,)|（,）|<,>|[,]|{,}|［,］|｛,｝|⦅,⦆|〚,〛|⦃,⦄|“,”|‘,’|‹,›|«,»|「,」|〈,〉|《,》|【,】|〔,〕|⦗,⦘|『,』|〖,〗|〘,〙|｢,｣|⟦,⟧|⟨,⟩|⟪,⟫|⟮,⟯|⟬,⟭|⌈,⌉|⌊,⌋|⦇,⦈|⦉,⦊|❛,❜|❝,❞|❨,❩|❪,❫|❴,❵|❬,❭|❮,❯|❰,❱"

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def str_make (str_, length):
	return str_ * length

def balance(bot, update):
	msg=update.message.text
	complete=""
	for pair in maps.split("|"):
		left=pair.split(",")[0]
		right=pair.split(",")[1]
		if left in msg:
			left_c=msg.count(left)
			right_c=msg.count(right)
			num=left_c-right_c
			complete=complete + str_make (right, num)
	if complete:
		send=complete + " ○(￣□￣○)"
		del complete
		bot.sendMessage(update.message.chat_id, text=send)

def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.addTelegramMessageHandler(balance)
	dp.addErrorHandler(error)
	updater.start_polling()
	updater.idle()
	
if __name__ == '__main__':
	main()

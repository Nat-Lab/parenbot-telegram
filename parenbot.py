#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# A telegram bot that hates unmatched parentheses.

TOKEN=""

from telegram.ext import Updater
import logging

logging.basicConfig(
        format='[%(levelname)s] %(asctime)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def log(bot, update):
	if "private" not in update.message.chat.type:
		logger.info('<%s %s (%s@%s)> %s' % (update.message.chat.first_name, update.message.chat.last_name, update.message.chat.username, update.message.chat.title, update.message.text))
	else:
		logger.info('<%s %s (%s)> %s' % (update.message.chat.first_name, update.message.chat.last_name, update.message.chat.username, update.message.text))

def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))

def str_make (str_, length):
	return str_ * length

def balance(bot, update):
	#log (bot, update)
	openbrckt = ('<([{（［｛⦅〚⦃“‘‹«「〈《【〔⦗『〖〘｢⟦⟨⟪⟮⟬⌈⌊⦇⦉❛❝❨❪❴❬❮❰❲'
		     '⏜⎴⏞〝︵⏠﹁﹃︹︻︗︿︽﹇︷〈⦑⧼﹙﹛﹝⁽₍⦋⦍⦏⁅⸢⸤⟅⦓⦕⸦⸨｟⧘⧚⸜⸌⸂⸄⸉᚛༺༼')
	clozbrckt = ('>)]}）］｝⦆〛⦄”’›»」〉》】〕⦘』〗〙｣⟧⟩⟫⟯⟭⌉⌋⦈⦊❜❞❩❫❵❭❯❱❳'
		     '⏝⎵⏟〞︶⏡﹂﹄︺︼︘﹀︾﹈︸〉⦒⧽﹚﹜﹞⁾₎⦌⦎⦐⁆⸣⸥⟆⦔⦖⸧⸩｠⧙⧛⸝⸍⸃⸅⸊᚜༻༽')
	stack = []
	for ch in update.message.text:
		index = openbrckt.find(ch)
		if index >= 0:
			stack.append(index)
			continue
		index = clozbrckt.find(ch)
		if index >= 0:
			if stack and stack[-1] == index:
				stack.pop()
	closed = ''.join(reversed(tuple(map(clozbrckt.__getitem__, stack))))
	if closed:
		bot.sendMessage(update.message.chat_id, text=closed + " ○(￣□￣○)")

def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.addTelegramMessageHandler(balance)
	dp.addErrorHandler(error)
	updater.start_polling()
	updater.idle()
	
if __name__ == '__main__':
	main()

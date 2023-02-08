my_quiz = await bot.send_poll(message.chat.id, 'Мессенджер, автор которого Павел Дуров', ['Telegram', 'Viber', 'WhatsApp', 'Messenger'], type='quiz', correct_option_id=0, is_anonymous=False)

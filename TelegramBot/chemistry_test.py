import random

# как только нужно отправить юзеру викторину - обращаемся к функции `pre_poll`
...
def pre_poll(message):
    # подключение к бд, обнуление счетчиков и выбор ответов
    # предположим, что res[0] - это вопрос, res[1] - верный ответ
    # все остальные ответы - неверные
    # также записываем верный ответ для последующей проверки
    # к примеру это будет записано в переменную ans
    data = [res[1], res[2], res[3], res[4]]
    random.shuffle(data)
    return bot.send_poll(chat_id=message.chat.id, question=res[0],
                         is_anonymous=False, options=data, type="quiz",
                         correct_option_id=data.index(res[1]))


# этот хендлер будет срабатывать каждый раз, когда юзер делает выбор в викторине
@bot.poll_answer_handler(func=lambda message: True)
def my_poll(message):
    # подключение к бд
    # предположим, что res[0] - это вопрос, res[1] - верный ответ
    # все остальные ответы - неверные
    data = [res[1], res[2], res[3], res[4]]
    random.shuffle(data)
    if [ans] == message.options_ids:
        # если ответ, который мы записали совпадает с тем, который выбрал юзер
        # тогда инкрементируем счетчик на +1
        correct_count += 1
    # инкрементируем счетчик отправленных викторин
    # если счетчик не равен 5, тогда отправляем следующую викторину
    if count != 3:
        # перезаписываем верный ответ для следующей проверки викторины
        bot.send_poll(chat_id=message.user.id, question=res[0],
                      is_anonymous=False, options=data, type="quiz",
                      correct_option_id=data.index(res[1]))
    else:
        bot.send_message(message.user.id,
                 f'Тестирование завершено.\nВерных ответов {correct_count} из 3.')
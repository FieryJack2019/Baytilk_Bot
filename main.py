#1 ИМПОРТ!
import telebot
from telebot import TeleBot
from telebot import types
import apiai
from apiai import ApiAI
import json


#Рассылка
name = '';
surname = '';
age = 0;
kids = []
admins = []
password = ['paSSword', '1']
#КОНЕЦ
message_special = []
name_quest = ""
quest_info = []
number_question_in_quest = 0
#ТОКЕН
bot = telebot.TeleBot(token="")
#ТОКЕН

#
hide_keyboard = types.ReplyKeyboardRemove()
help_button = types.KeyboardButton('Помощь')

cancel_button = types.KeyboardButton("Отмена")
cancel_keyboard = types.ReplyKeyboardMarkup()
cancel_keyboard.row(cancel_button)

next_button = types.KeyboardButton("Дальше")
next_keyboard = types.ReplyKeyboardMarkup()
next_keyboard.row(next_button)

yes_button = types.KeyboardButton("Да")
no_button = types.KeyboardButton("Нет")
is_qr_keyboard = types.ReplyKeyboardMarkup()
is_qr_keyboard.row(yes_button)
is_qr_keyboard.row(no_button)

yes_button_1 = types.KeyboardButton("Подтвердить")
quest_accept_keyaboard = types.ReplyKeyboardMarkup()
quest_accept_keyaboard.row(yes_button_1)
quest_accept_keyaboard.row(cancel_button)

quest_button_1 = types.KeyboardButton("Создать квест")
quest_button_2 = types.KeyboardButton("Учавствовать в квесте")
quest_keyboard_1 = types.ReplyKeyboardMarkup()
quest_keyboard_1.row(quest_button_1)
quest_keyboard_1.row(quest_button_2)

quest_keyboard_2 = types.ReplyKeyboardMarkup()
quest_keyboard_2.row(quest_button_2)

help_keyboard = types.ReplyKeyboardMarkup()
help_keyboard.row(help_button)
break_button = types.KeyboardButton('Поломка')
otryad_button = types.KeyboardButton('Списки отрядов')
rating_button = types.KeyboardButton('Рейтинг отрядов')
timetable_button = types.KeyboardButton('Расписание')
quest_button = types.KeyboardButton('Квесты')
commands_keyboard_1 = types.ReplyKeyboardMarkup()

commands_keyboard_1.row(break_button)

commands_keyboard_2 = types.ReplyKeyboardMarkup()
commands_keyboard_2.row(break_button)
commands_keyboard_2.row(rating_button)
commands_keyboard_2.row(timetable_button)
commands_keyboard_2.row(quest_button)

load = types.KeyboardButton("Загрухить xlsx таблицу")
get = types.KeyboardButton('Получить данные по отряду')
insert = types.KeyboardButton('Добавить данные по отряду')
update = types.KeyboardButton('Изменить данные по отряду')

edit_rating_but = types.KeyboardButton("Изменить рейтинг отрядов")
veiw_rating_but = types.KeyboardButton('Посмотреть рейтинг отрядов')

rating_keyboard_1 = types.ReplyKeyboardMarkup()
rating_keyboard_1.row(edit_rating_but)
rating_keyboard_1.row(veiw_rating_but)
rating_keyboard_1.row(cancel_button)

rating_keyboard_2 = types.ReplyKeyboardMarkup()
rating_keyboard_2.row(veiw_rating_but)
rating_keyboard_2.row(cancel_button)

squad_keyboard = types.ReplyKeyboardMarkup()
squad_keyboard.row(load)
squad_keyboard.row(get)
squad_keyboard.row(insert)
squad_keyboard.row(update)
squad_keyboard.row(cancel_button)

avtoriz = types.KeyboardButton("Авторизироваться")
avtoriz_keyboard = types.ReplyKeyboardMarkup()
avtoriz_keyboard.row(avtoriz)

get_values_1 = types.KeyboardButton("Скачать xlsx таблицу")
get_values_2 = types.KeyboardButton("Получить по конкретному человеку")
get_values_keyboard = types.ReplyKeyboardMarkup()
get_values_keyboard.row(get_values_1)
get_values_keyboard.row(get_values_2)
get_values_keyboard.row(cancel_button)

load_xlsx_table_but = types.KeyboardButton("Загрузить расписание в формате xlsx")
upcoming_event_but = types.KeyboardButton("Показать ближайшее по времени мероприятие")
all_timetable_but = types.KeyboardButton("Показать расписание")

timetable_keyboard_1 = types.ReplyKeyboardMarkup()
timetable_keyboard_1.row(load_xlsx_table_but)
timetable_keyboard_1.row(upcoming_event_but)
timetable_keyboard_1.row(all_timetable_but)
timetable_keyboard_1.row(cancel_button)

timetable_keyboard_2 = types.ReplyKeyboardMarkup()
timetable_keyboard_2.row(upcoming_event_but)
timetable_keyboard_2.row(all_timetable_but)
timetable_keyboard_2.row(cancel_button)
#


#Кнопка
connection = types.KeyboardButton('Связь с кураторами📱')
timetable = types.KeyboardButton('Расписание🧾')
review = types.KeyboardButton('Отзывы🗓')
success = types.KeyboardButton('Успехи ребят🏆')
map = types.KeyboardButton('Карта Байтика🗺')
structure = types.KeyboardButton('Состав отряда📝')
information = types.KeyboardButton('Сказать информацию о тебе🐶')
graduates = types.KeyboardButton('Выпускники👩🏻‍🎓')
details = types.KeyboardButton('Подробности о лагере🏫')
future = types.KeyboardButton('Будущие смены➡️')
raiting = types.KeyboardButton('Рейтинг отрядов📈')#ДОДЕЛАТЬ
bag = types.KeyboardButton('Поломки🛠')#ДОДЕЛАТЬ
menu = types.KeyboardButton('Меню🍕')#ДОДЕЛАТЬ
playlist = types.KeyboardButton('Голосование✅')#ДОДЕЛАТЬ
napravlenie = types.KeyboardButton('Направление💻')#ДОДЕЛАТЬ
vopros = types.KeyboardButton('❓Задать вопрос❔')#ДОДЕЛАТЬ



markup = types.ReplyKeyboardMarkup()

markup.row(connection, timetable, review)
markup.row(success, map, structure)
markup.row(information, graduates, details)
markup.row(future, raiting, menu)
markup.row(playlist, napravlenie, vopros)
markup.row(bag)
hide = types.ReplyKeyboardRemove()
#Кнопка(к)

#Кнопка1
v1 = types.KeyboardButton('Oтряд 1')
v2 = types.KeyboardButton('Oтряд 2')
v3 = types.KeyboardButton('Oтряд 3')
v4 = types.KeyboardButton('Oтряд 4')
v5 = types.KeyboardButton('Oтряд 5')
v6 = types.KeyboardButton('Oтряд 6')
v = types.KeyboardButton('Назад')


markup1 = types.ReplyKeyboardMarkup()

markup1.row(v1, v2, v3, v4)
markup1.row(v5, v6, v)
#Кнопка1(к)


#Кнопка2
o1 = types.KeyboardButton('Полина')
o2 = types.KeyboardButton('Асия')
o3 = types.KeyboardButton('Данил')
o4 = types.KeyboardButton('Аделя')
o5 = types.KeyboardButton('Дарья')
o6 = types.KeyboardButton('Артур')
o7 = types.KeyboardButton('Камиля(фотограф)')
o8 = types.KeyboardButton('Виолета')
o9 = types.KeyboardButton('Назад')

markup2 = types.ReplyKeyboardMarkup()

markup2.row(o1, o2, o3)
markup2.row(o4, o5, o6)
markup2.row(o7, o8, o9)
#Кнопка2(к)


#Кнопка3
fut = types.KeyboardButton('Зимние каникулы 2020. С 2 по 8 января')
fut1 = types.KeyboardButton('Летние каникулы 2020. С 1 июня до 25 августа')

markup3 = types.ReplyKeyboardMarkup()

markup3.row(fut)
markup3.row(fut1)
#Кнопка3(к)

#Кнопка4
rai1 = types.KeyboardButton('Добавить баллы')
rai2 = types.KeyboardButton('Посмотреть баллы')

markup4 = types.ReplyKeyboardMarkup()

markup4.row(rai1, rai2)
#Кнопка4(к)

#Кнопка5 День домашних животных
golos = types.KeyboardButton('Да')
golos1 = types.KeyboardButton('Нет')
golos3 = types.KeyboardButton('Свой вариант')

markup5 = types.ReplyKeyboardMarkup()

markup5.row(golos, golos1)
markup5.row(golos3)
#Кнопка5(к)

#Кнопка6
nap = types.KeyboardButton('Pyton')
nap1 = types.KeyboardButton('Sas-сервис')
nap2 = types.KeyboardButton('DVR')

markup6 = types.ReplyKeyboardMarkup()

markup6.row(nap, nap2)
markup6.row(nap1)
#Кнопка6(к)


#Кнопка7
p1 = types.KeyboardButton('Python-1')
p2 = types.KeyboardButton('Python-2')
p3 = types.KeyboardButton('Python-3')

markup7 = types.ReplyKeyboardMarkup()

markup7.row(p1, p2, p3)
#Кнопка7(к)


#Кнопка8
s1 = types.KeyboardButton('S-1')
s2 = types.KeyboardButton('S-2')
s3 = types.KeyboardButton('S-3')

markup8 = types.ReplyKeyboardMarkup()

markup8.row(s1, s2, s3)
#Кнопка8(к)


#Кнопка9
vr1 = types.KeyboardButton('VR-1')
vr2 = types.KeyboardButton('VR-2')
dvr = types.KeyboardButton('DVR')

markup9 = types.ReplyKeyboardMarkup()

markup8.row(vr1, vr2, dvr)
#Кнопка9(к)

dobav = types.KeyboardButton('Добавить рейтинг')
posmotr = types.KeyboardButton('Посмотреть рейтинг')

markup10 = types.ReplyKeyboardMarkup()

markup10.row(dobav, posmotr)

#start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в чат-бот.\n'
                                      'Если у вас есть доступ к аккаунту участника лагеря, то выберите меню "Мой код" и введите 6-ти значный код.\n'
                                      'Есл нет, то вам доступны эти функции:\n'
                                      '- Выпускники.\n'
                                      '- Будущие смены.\n'
                                      '- Подробности о лагере.\n'
                                      '- Отзывы.\n'
                                      '- Связь с куратором.\n'
                                      'Выбирите что вас интересует.', reply_markup=markup)
    bot.register_next_step_handler(message, q)



#Kod
#def


@bot.message_handler(content_types=['text'])
#Связь с кураторами
def q(message):
    if message.text == 'Связь с кураторами📱':
        bot.send_message(message.chat.id, 'Выбери отряд, в котором ты состоишь', reply_markup=markup2)
        bot.register_next_step_handler(message, w)

    elif message.text == 'Расписание🧾':
        bot.send_message(message.chat.id, 'Расписание на 18.11.2019:\n'
                                          '8.45 зарядка\n'
                                           '9.00 завтрак\n'
                                            '9.40 оргсбор\n'
                                            '10.30-13.00 занятия\n'
                                            '13.30 обед\n'
                                            '14.00 веревочный курс\n'
                                            '16.30 полдник\n'
                                            '15.00-16.00 тихий час\n'
                                            '16.30 полдник\n'
                                            '17.35 тренинг в 1а(сас)\n'
                                            '18.30 ужин\n'
                                            '20.30 гостевание', reply_markup=markup)
        bot.send_message(message.chat.id, 'Что-то ещё?')
        bot.register_next_step_handler(message, q)

    elif message.text == 'Отзывы🗓':
        bot.send_message(message.chat.id, "Дата пребывания в лагере: 30.05.2016\nДобрый вечер! Буквально только что приехали из вашего лагеря, "
                         "отпраздновав выпускной наших деток из садика. Очень понравилось! Огромное спасибо всем организаторам. "
                         "Впервые задумались всерьез отправить детей на летнее время в лагерь на отдых. Отдельное огромное и душевное "
                         "спасибо хочется сказать ребятам, которые шикарно делают свое дело. Молодцы! От ворот встретили и сразу "
                         "погрузили всех нас в сказку, чудесно провели всю программу и проводили до автобуса при прощании. "
                         "Ни разу не вышли из образа! Дети визжали от восторга. Родители до сих пор аплодируют стоя! "
                         "Огромное спасибо! (Мы даже имен их не спросили. Отблагодарите от нас, пожалуйста пиратов "
                         "Джека Воробья и еще одного капитана.....))))! )Успехов и процветания всем вам - особенного "
                         "строения души людям, которые работают с детьми и у которых так здорово это получается. "
                         "Высокая гора.д/сад Бэлэкэч родители Фантазеров.")
        bot.send_photo(message.chat.id, 'https://baytik-kazan.ru/kcfinder/upload/images/1%282%29.jpg')
        bot.send_message(message.chat.id, 'Что-то ещё?')
        bot.register_next_step_handler(message, q)

    elif message.text == 'Успехи ребят🏆':
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂️\n'
                                  '❓Кто же он такой?❓\n'
                                  'Это очеень хороший человек, который за свои 22 года добился очень много.\n'
                                  '💰Когда он учился в 10-ом классе, он со своей командой написали IT-проект, который продали за 1 000 000 рублей.💵\n'
                                  'Замечу что это случилось после неских поездок в лагерь "Байтик".\n'
                                  'Если хотите узнать больше об Амире, то вот его инстаграм: https://www.instagram.com/vafinamir/ . Вы ему также можете написать в direct.')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=markup)
        bot.send_photo(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Что-то ещё?')
        bot.register_next_step_handler(message, q)

    elif message.text == 'Карта Байтика🗺':
        bot.send_photo(message.chat.id, "http://fest.krutushka.ru/data/viewers/map2016-big.jpg")
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)
        bot.register_next_step_handler(message, q)

    elif message.text == 'Состав отряда📝':
        bot.send_message(message.chat.id, 'Какой отряд вас конкретно интересует?', reply_markup=markup1)
        bot.register_next_step_handler(message, u)

    elif message.text == "Сказать информацию о тебе🐶":
        bot.send_message(message.chat.id, 'Напиши своё ФИО полностью в И.П.', reply_markup=hide)
        bot.register_next_step_handler(message, i)


    elif message.text == 'Выпускники👩🏻‍🎓':
        bot.send_message(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=markup)
        bot.register_next_step_handler(message, q)

    elif message.text == 'Подробности о лагере🏫':
        bot.send_message(message.chat.id, 'Проект предусматривает проведение смен, на которых участники занимаются проектной деятельностью и развивают цифровые компетенции.'
                         'Педагогами - экспертами и тренерами являются практики бизнес-сферы и успешные предприниматели, которые профессионально ведут школьников к запланированным результатам.'
                         'Работа ведется в команде от трёх до пяти человек. А по окончанию смены каждая из них проходит трёхэтапный конкурсный отбор, где представляет работающий прототип IT-продукта.'
                         'На первом этапе все команды презентуют свои проекты экспертам в учебных группах. Лучшие два проекта от группы проходят на следующий этап, где их ожидает расширенное жюри и разбор со стороны других команд.'
                         'Завершается смена защитой приобретенных компетенций в формате Фестиваля проектов, куда приглашаются победители предыдущего этапа. Фестиваль будет проходить в Технопарке высоких технологий '
                         '«ИТ парк» (г.Казань). На этом этапе участники представляют свои проекты приглашенным экспертам из числа представителей учебных заведений, министерств, предприятий IT-сферы, потенциальных инвесторов, представителей бизнес-инкубаторов.')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)
        bot.register_next_step_handler(message, q)


    elif message.text == 'Будущие смены➡️':
        bot.send_message(message.chat.id, 'Выбери смены которые тебя интересуют', reply_markup=markup3)
        bot.register_next_step_handler(message, p)

    elif message.text == 'Рейтинг отрядов📈':
        bot.send_message(message.chat.id, 'Вы хотите добавить или посмотреть рейтинг', reply_markup=markup10)
        bot.register_next_step_handler(message, fgghj)

    elif message.text == 'Меню🍕':
        bot.send_message(message.chat.id, 'ЗАВТРАК:\nКаша молочная овсяная\nЙогурт\nМасло сливочное\nБатон\nЧай с '
                                          'сахаром\nОБЕД:\nОвощная нарезка\nСуп лапша\nРис опущенный\nГовядина тушёная\n'
                                          'Говядина тушёная с черносливом\nКомпот из сухофруктов\nХлеб\nПОЛДНИК:\nСок '
                                          'фруктовый\nПеченье Сормовское\nФрукт\nУЖИН:\nОвощная нарезка\nГречка '
                                          'рассыпчатая\nКотлеты куриные\nЧай сладкий с лионом\nХлеб сельский\n2-ОЙ УЖИН\nКоктейл молочный')
        bot.send_message(message.chat.id, 'Чем могу помощь ещё?', reply_markup=markup)
        bot.register_next_step_handler(message, q)

    elif message.text == '❓Задать вопрос❔':
        bot.send_message(message.chat.id, 'Хорошо. Задай мне вопрос который тебя интересует. Если хочешь закончить диалог, напиши "Назад"')
        bot.register_next_step_handler(message, send_message23)

    elif message.text == 'Голосование✅':
        bot.send_message(message.chat.id, 'Скажи мне друг мой. Хочешь ли ты праздновать Всемирный день приветствий?', reply_markup=markup5)
        bot.register_next_step_handler(message, d)

    elif message.text == 'Поломки🛠':
        bot.send_message(message.chat.id, 'Напиши мне Поломка')
        bot.register_next_step_handler(message, send_text)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю(', reply_markup=markup)
        bot.register_next_step_handler(message, q)


#Сами кураторы
def w(message):
    if message.text == 'Полина':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Асия':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 917 257-81-66", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Данил':
        bot.send_message(message.chat.id, "Напиши ему в телеграмме по этому номеру +7 937 616-49-39", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Аделя':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 953 496-66-10", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Дарья':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру + 7 965 585-71-19", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Артур':
        bot.send_message(message.chat.id, "Напиши ему в телеграмме по этому номеру +7 967 360-26-83", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Камиля(фотограф)':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 987 267-05-77", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Виолета':
        bot.send_message(message.chat.id, "Напиши ей в телеграмме по этому номеру +7 999 145-40-28", reply_markup=hide)
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)

    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Ок', reply_markup=markup)
    #else:
     #   bot.send_message(message.chat.id, 'Я тебя не понимаю(', reply_markup=markup)



#Расписание
def e(message):
    if message.text == 'Расписание🧾':
        bot.send_message(message.chat.id, 'Расписание на 18.11.2019:\n'
                                          '8.45 зарядка\n'
                                           '9.00 завтрак\n'
                                            '9.40 оргсбор\n'
                                            '10.30-13.00 занятия\n'
                                            '13.30 обед\n'
                                            '14.00 веревочный курс\n'
                                            '16.30 полдник\n'
                                            '15.00-16.00 тихий час\n'
                                            '16.30 полдник\n'
                                            '17.35 тренинг в 1а(сас)\n'
                                            '18.30 ужин\n'
                                            '20.30 гостевание', reply_markup=markup)
        bot.send_message(message.chat.id, 'Что-то ещё?')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю(', reply_markup=markup)



#Отзывы
def r(massage):
    if message.text == 'Отзывы🗓':
        bot.send_message(message,chat.id, "Дата пребывания в лагере: 30.05.2016\nДобрый вечер! Буквально только что приехали из вашего лагеря, "
                         "отпраздновав выпускной наших деток из садика. Очень понравилось! Огромное спасибо всем организаторам. "
                         "Впервые задумались всерьез отправить детей на летнее время в лагерь на отдых. Отдельное огромное и душевное "
                         "спасибо хочется сказать ребятам, которые шикарно делают свое дело. Молодцы! От ворот встретили и сразу "
                         "погрузили всех нас в сказку, чудесно провели всю программу и проводили до автобуса при прощании. "
                         "Ни разу не вышли из образа! Дети визжали от восторга. Родители до сих пор аплодируют стоя! "
                         "Огромное спасибо! (Мы даже имен их не спросили. Отблагодарите от нас, пожалуйста пиратов "
                         "Джека Воробья и еще одного капитана.....))))! )Успехов и процветания всем вам - особенного "
                         "строения души людям, которые работают с детьми и у которых так здорово это получается. "
                         "Высокая гора.д/сад Бэлэкэч родители Фантазеров.")
        bot.send_photo(message.chat.id, 'https://baytik-kazan.ru/kcfinder/upload/images/1%282%29.jpg')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)



#подробности о лагере
def pod(massage):
    if message.text == 'Подробности о лагере🏫':
        bot.send_message(message.chat.id,
                         'Проект предусматривает проведение смен, на которых участники занимаются проектной деятельностью и развивают цифровые компетенции.'
                         'Педагогами - экспертами и тренерами являются практики бизнес-сферы и успешные предприниматели, которые профессионально ведут школьников к запланированным результатам.'
                         'Работа ведется в команде от трёх до пяти человек. А по окончанию смены каждая из них проходит трёхэтапный конкурсный отбор, где представляет работающий прототип IT-продукта.'
                         'На первом этапе все команды презентуют свои проекты экспертам в учебных группах. Лучшие два проекта от группы проходят на следующий этап, где их ожидает расширенное жюри и разбор со стороны других команд.'
                         'Завершается смена защитой приобретенных компетенций в формате Фестиваля проектов, куда приглашаются победители предыдущего этапа. Фестиваль будет проходить в Технопарке высоких технологий '
                         '«ИТ парк» (г.Казань). На этом этапе участники представляют свои проекты приглашенным экспертам из числа представителей учебных заведений, министерств, предприятий IT-сферы, потенциальных инвесторов, представителей бизнес-инкубаторов.')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)





#Успехи ребят
def t(message):
    if message.text == 'Успехи ребят🏆':
        bot.send_photo(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂️\n'
                                  '❓Кто же он такой?❓\n'
                                  'Это очеень хороший человек, который за свои 22 года добился очень много.\n'
                                  '💰Когда он учился в 10-ом классе, он со своей командой написали IT-проект, который продали за 1 000 000 рублей.💵\n'
                                  'Замечу что это случилось после неских поездок в лагерь "Байтик".\n'
                                  'Если хотите узнать больше об Амире, то вот его инстаграм: https://www.instagram.com/vafinamir/ . Вы ему также можете написать в direct.')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=markup)


#Карта Байтика
def y(message):
    if message.text == 'Карта Байтика🗺':
        bot.send_photo(message.chat.id, "http://fest.krutushka.ru/data/viewers/map2016-big.jpg")
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)



#Состав отряда
def u(message):
    if message.text == 'Отряд 1':
        bot.send_message(message.chat.id, 'Отряд 1')
        bot.send_photo(message.chat.id, 'https://vk.com/photo306776368_457242681')

    elif message.text == 'Отряд 2':
        bot.send_message(message.chat.id, 'Отряд 2')
        bot.send_photo(message.chat.id, 'https://vk.com/photo306776368_457242682')

    elif message.text == 'Отряд 3':
        bot.send_message(message.chat.id, 'Отряд 3')
        bot.send_photo(message.chat.id, 'https://sun9-47.userapi.com/c857124/v857124923/56290/2qDimRApft8.jpg')

    elif message.text == 'Отряд 4':
        bot.send_message(message.chat.id, 'Отряд 4')
        bot.send_photo(message.chat.id, 'https://sun9-50.userapi.com/c857124/v857124923/56297/WuAV71ZFW7A.jpg')

    elif message.text == 'Отряд 5':
        bot.send_message(message.chat.id, 'Отряд 5')
        bot.send_photo(message.chat.id, 'https://sun9-48.userapi.com/c857124/v857124923/5629e/TgrEFJAFGVo.jpg')

    elif message.text == 'Отряд 6':
        bot.send_message(message.chat.id, 'Отряд 6')
        bot.send_photo(message.chat.id, 'https://sun9-33.userapi.com/c857124/v857124923/562a5/QkmvOmmINiw.jpg')




#Сказать информацию о тебе
def i(message):
    if message.text == 'Мукиев Ибрахим Ирекович':
        bot.send_message(message.chat.id, 'Ты живёшь в корпусе №7. В комнате 210. Ты живёшь вместе с Аделем. Твои вожатые это Руслан и Асия', reply_markup=markup)


#Выпускники
def o(message):
    if message.text == 'Выпускники👩🏻‍🎓':
        bot.send_photo(message.chat.id, 'https://sun9-18.userapi.com/c855636/v855636889/137ce5/1raOUWylZG8.jpg')
        bot.send_message(message.chat.id, 'Вафин Амир Аделевич.🙎🏻‍♂')
        bot.send_message(message.chat.id, 'Чем могу ещё помощь?', reply_markup=markup)


#Будущие смены
def p(message):
    if message.text == 'Зимние каникулы 2020. С 2 по 8 января':
        bot.send_message(message.chat.id, 'Даты: с 3 по 9 января 2020 года\nВозраст: 7-17 лет\nСтоимость: 16 500 рублей\nПроживание: 7 корпус\n'
                                       'Участники проекта разместятся в комфортабельном седьмом корпусе с 4-х и 6-ти местными комнатами со всеми удобствами. На каждом этаже есть площадки, на которых будут проходить  мастер-классы и отрядные мероприятия.\n'
                                       'Новогодние каникулы всегда таят в себе что-то волшебное и сказочное, а  когда их можно провести в компании друзей в живописном месте, то отдых превращается в чудо. Традиционно, с боем курантов в лагере «Байтик» наступает '
                                       'Зимняя сказка, и каждый день наполняется незабываемыми событиями.\n'
                                       'О программе  смены:\n'
                                       'Программа смены разнообразна.\n'
                                       'Каждый участник  найдет для себя интересные и полезные занятия. Мероприятия будут проходить как всем лагерем  так и делиться по возрастам. \n'
                                       'Необычная тематика, опытные вожатые  обеспечат яркий отдых и безопасность. Профильные мастер-классы и занятия дадут много новых  знаний и впечатлений.\n'
                                       'Помимо этого, ребят ждут:\n'
                                       '- увлекательные квесты,  приключенческие "вертушки", вечерние  шоу-программы и дискотеки. До последнего момента тема смены остается в секрете!!!\n'
                                       '- новогодний и рождественский праздники, встреча с Дедом Морозом и его друзьями\n'
                                       '- командно-спортивная игра «Лазертаг» (за доп.оплату )\n'
                                       '- зимние забавы (катание на коньках, лыжах, санках)  и спортивные мероприятия на свежем воздухе\n- катание на санях, запряженных лошадьми.')
        bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)
        bot.register_next_step_handler(message, q)

    elif message.text == 'Летние каникулы 2020. С 1 июня до 25 августа':
        bot.send_message(message.chat.id, 'Приехав в наш лагерь,  ребенок выбирает интересующую его область  и ежедневно в первой половине дня посещает занятия по выбранному направлению. У нас 9  профильных направлений на выбор:\n\n'

                                            'IT-технологии\n'
                                            'Робототехника\n'
                                            'Английский язык\n'
                                            'Нарды\n'
                                            'Театральное искусство\n'
                                            'Архитектура и дизайн\n'
                                            'Маленькая леди\n'
                                            'Хореография\n'
                                            'Кулинарная школа\n\n'
                                            'Во второй половине дня предусмотрены студиные занятия также на выбор ребенка более 20 студий, точный перечень становится ивестен в первые дни смены. Среди них различные спортивные, вокальные, хореографические, компьютерные и другие студии.')
        bot.send_message(message.chat.id, 'Что-то ещё', reply_markup=markup)
        bot.register_next_step_handler(message, q)

#Рейтинг
def fgghj(message):
    if message.text == 'Добавить рейтинг':
        bot.send_message(message.chat.id, 'Хорошо. Напиши мне "Рейтинг"')
        bot.register_next_step_handler(message, start)

    elif message.text == 'Посмотреть рейтинг':
        bot.send_message(message.chat.id, 'Топ 6 по рейтенгу:\n'
                                          '1. 6 отряд - 10 000 000 000 баллов\n'
                                          '2. 5 отряд - 31 балл\n'
                                          '3. 3 отряд - 10 баллов\n'
                                          '4. 1 отряд - 7 баллов\n'
                                          '5. 4 отряд - 3 балла\n'
                                          '6. 2 отряд - 0 баллов')

def start(message):
    if message.text == 'Рейтинг':
        bot.send_message(message.from_user.id, "Какой у тебя отряд?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /reg');

def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Напиши количество баллов?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('За что эти баллы?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    while age == 0: #проверяем что возраст изменился
        try:
             age = int(message.text) #проверяем, что возраст введен корректно
        except Exception:
             bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.send_message(message.from_user.id, 'Тебе '+str(age)+' лет, тебя зовут '+name+' '+surname+'?')
    bot.send_message(message.chat.id, 'Что-то ещё?', reply_markup=markup)
    bot.register_next_step_handler(message, q)


#Поломки



#Меню
def a(message):
    if message.text == 'Меню🍕':
        bot.send_message(message.chat.id, 'ЗАВТРАК:\nКаша молочная овсяная\nЙогурт\nМасло сливочное\nБатон\nЧай с '
                                          'сахаром\nОБЕД:\nОвощная нарезка\nСуп лапша\nРис опущенный\nГовядина тушёная\n'
                                          'Говядина тушёная с черносливом\nКомпот из сухофруктов\nХлеб\nПОЛДНИК:\nСок '
                                          'фруктовый\nПеченье Сормовское\nФрукт\nУЖИН:\nОвощная нарезка\nГречка '
                                          'рассыпчатая\nКотлеты куриные\nЧай сладкий с лионом\nХлеб сельский\n2-ОЙ УЖИН\nКоктейл молочный')
        bot.send_message(message.chat.id, 'Что-тоещё?', reply_markup=markup)



#Голосование


def d(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Хорошо, + 1 голоса За. Всего за проголосовали 1 человек', reply_markup=markup)

    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'Хорошо +1 голос против')

#Направление
def f(message):
    if message.text == 'Направление💻':
        bot.send_message(message.chat.id, 'Выбери направление', reply_markup=markup6)
        if message.text == 'Pyton':
            bot.send_message(message.chat.id, 'Выбери группу', reply_markup=markup7)
            if message.text == 'Python-1':
                bot.send_message(message.chat.id, 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214', reply_markup=markup)
            elif message.text == 'Python-2':
                bot.send_message(message.chat.id, 'Преподаватель-Каскаров Родион\nНомер телефона-89061100743\nЗанятия проходят в 7 корпусе в кабинете №213', reply_markup=markup)
            elif message.text == 'Python-3':
                bot.send_message(message.chat.id, 'Преподаватель-Лотфуллин Камиль\nНомер телефона-89856660205\nЗанятия проходят в холле 7 корпуса', reply_markup=markup)

        elif message.text == 'Sas-сервис':
            bot.send_message(message.chat.id, 'Выбери группу', reply_markup=markup8)
            if message.text == 'S-1':
                bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=markup)
            elif message.text == 'S-2':
                bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=markup)
            elif message.text == 'S-3':
                bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=markup)

        elif message.text == 'DVR':
            bot.send_message(message.chat.id, 'Выбери группу', reply_markup=markup9)
            if message.text == 'VR-1':
                bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=markup)
            elif message.text == 'VR-2':
                bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=markup)
            elif message.text == 'D-VR':
                bot.send_message(message.chat.id,
                                 'Преподаватель-Хакимов Роман\nНомер телефона-89503100100\nЗанятия проходят в 7 корпусе в кабинете №214',
                                 reply_markup=markup)


#Поломка
@bot.message_handler(content_types1=['text'])
def send_text(message):
    print(message)
    # try:

    if message.text == 'Поломка':
        bot.send_message(message.chat.id, 'Опишите вашу проблему.', reply_markup=cancel_keyboard)
        bot.register_next_step_handler(message, location_w)

    else:
        bot.send_message(message.chat.id,
                         """Привет, вот что я умею:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.""",
                         reply_markup=commands_keyboard_1)
        bot.register_next_step_handler(message, send_text)


def location_w(message):
    print('location_success')
    print(message.text)
    if message.text == "Отмена":
        bot.send_message(message.chat.id,
                         "Список команд:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.")
        return
    bot.send_message(message.chat.id, 'Опишите место, где произошла поломка:\n1)Корпус.\n2)Номер комнаты.')
    bot.register_next_step_handler(message, photo_w)
    message_special.append(message.text)


def photo_w(message):
    print('info_success')
    if message.text == "Отмена":
        bot.send_message(message.chat.id,
                         "Список команд:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.")
        return
    bot.send_message(message.chat.id, 'Прикрепите фото поломки.')
    bot.register_next_step_handler(message, info_w)
    message_special.append(message.text)


def info_w(message):
    print('photo_success')
    if message.text == "Отмена":
        bot.send_message(message.chat.id,
                         "Список команд:\n1)Работа с списками отрядов.\n2)Получать данные о поломках.\n3)Работать с рейтингом отрядов.\n4)Отправлять вам расписание.")
        return
    bot.send_message(message.chat.id, 'Хорошо, скоро мы устраним эту проблему.')
    bot.register_next_step_handler(message, send_text)
    bot.send_message(-1001468779187, "\n".join(message_special))
    try:
        file_info = bot.get_file(message.photo[0].file_id)
        bot.send_photo(-1001468779187, message.photo[0].file_id)
    except:
        bot.send_message(-1001468779187, "Ошибка при отправке фотографии")


def unknown_error(message):
    bot.send_message(message.chat.id, 'Неизветная ошибка, попробуйте позже',
                     reply_markup=hide_keyboard)


@bot.message_handler(content_types=['voice'])
def voice_fail(message):
    bot.send_message(message.chat.id, 'Извини, я не принимаю голосовые сообщения. Попробуй перейти в меню "Помощь"',
                     reply_markup=help_keyboard)


@bot.message_handler(content_types=['photo'])
def message_for_photo(message):
    bot.send_message(message.chat.id, 'Зачем ты скидываешь мне это фото? Попробуй перейти в меню "Помощь"',
                     reply_markup=help_keyboard)


@bot.message_handler(content_types=['location'])
def location_message(message):
    bot.send_message(message.chat.id, 'Зачем ты отправил мне своё местоположение? Перейди в меню "Помощь"',
                     reply_markup=help_keyboard)


def send_message23(message):
    request = apiai.ApiAI('a3121094db294780a1525cbb93725ea6').text_request()  # токен DialogFlow
    request.lang = 'ru'
    request.session_id = 'session_1'  # сюда можно писать что захотите
    request.query = message.text
    response = json.loads(request.getresponse().read().decode('utf-8'))
    answer = str(response['result']['fulfillment']['speech'])
    if answer != '':
        bot.send_message(message.chat.id, answer)
        bot.register_next_step_handler(message, send_message23)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Хорошо\nВыбирите что хотите?', reply_markup=markup
                         )
        bot.register_next_step_handler(message, q)
    else:
        bot.send_message(message.chat.id, 'Прости, но я тебя не понимаю😓\n'
                                          'Напиши /start или /help и я тебе обязательно постораюсь помощь)')



bot.polling(none_stop=True)
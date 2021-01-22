import vk_api #библиотеки вк
import time #время
import random #рандом
import sqlite3 #для базы данных
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType #Библиотеки бота группы ВК

from Bot_Words import BotWordsInit #класс с ответами

#Блок размышлений +
#Прикрутить базу данных - добавлять туда людей, кому бот что-то писал
#https://habr.com/ru/post/321510/

#Модифицировать и вынести в отдельную процедурку проверку на нужность отправки сообщения

#Сделать нормально в отдельной процедуре шансы на отправление сообщения и фильтрацию повторов

#Блок размышлений -


def writemessage(event, vk, botanswer):
    FN =  vk.users.get(user_id=event.message.from_id)[0]['first_name'] #Имя изверя
    LN =  vk.users.get(user_id=event.message.from_id)[0]['last_name'] #Фамилия юзверя
    #print(LN + ' ' + FN + ' ' + event.message.text)
    botanswer = FN + ', ' + botanswer #Добавим к ответу имя юзверя. Не рекомендую отвечать через уникальные ссылки/цитирования, чтобы не дергать человека лишний раз
    #print('i am: ' + botanswer)
    #print('')
    vk.messages.send(random_id = int(time.time()), peer_id = event.message.peer_id, message = botanswer) 
    #Метод вк - отправить сообщение. гуглить тут https://vk.com/dev/messages
    #Первый параметр обязательно хотя бы немного уникальный
    #Пир_ид - из какого чата
    #месага - само сообщение

x = 0

#conn = sqlite3.connect('Chinook_Sqlite.sqlite')
#cur = conn.cursor()

#try:
#    RegWordsFile = open('RegWords.txt', 'r')
#except:
#    print("File RegWords not found")

#try:
#    OrdWordsFile = open('OrdWords.txt', 'r')
#except:
#    print("File not found")

#data = RegWordsFile.read()
#data = data.split()

#for i in range(0, len(data)):
#    Name = data[i]
#    cur.execute('INSERT INTO RegWords (Name) VALUES (?)', (Name,))

#data1 = OrdWordsFile.read()
#data1 = data1.split()

#for i in range(0, len(data1)):
#    Name = data1[i]
#    cur.execute('INSERT INTO OrdWords (Name) VALUES (?)', (Name,))

#conn.commit()
#conn.close()
#print("THis is the End!")

while x < 100:
    try:

        vk_session = vk_api.VkApi(token='4842ab42fc8ab6aa6860269222be707fe712ab2f417086f766e39e84aeb7e04572610aa3adcb21f663bc7') #Авторизация в вк через сообщество

        vk = vk_session.get_api() #Получаем доступ к методам ВК

        longpoll = VkBotLongPoll(vk_session, '198202940') #Получаем доступ к боту

        if x == 0: #Счетчик запусков бота
            print('Server started')
        else:
            print('Server started again')

        print('')
        lastword = '' #Предыдущий ответ
        repeated = 0 #счетчик повторений ответов бота
                    
        for event in longpoll.listen(): #каждый эвент на сервере вк для нашего бота

            #print(event)

            if event.type == VkBotEventType.MESSAGE_NEW: #Если новое сообщение в конфе

                if event.message.from_id > 0: #Айди ботов меньше нуля. Нужно фильтровать, чтобы не крашился метод получения имени юзверя (на ботов ошибку вк отдает)
                    botanswer = BotWordsInit.report(event.message.text) #Получаем ответ от БотВордс 
                    if botanswer != 'Нуль': #Бот нашел ответ на сообщение в своей базе
                        if lastword == botanswer: #Если он так же уже отвечал
                            repeated = repeated + 1 #Значит плюс к счетчику повтора
                            if (repeated <5): #Если первый раз
                                  
                                if 7 < random.randint(0, 9): #Бахнем шанс на ответ
                                    lastword = botanswer #Запомним ответ
                                    writemessage(event, vk, botanswer) #отправим в чат

                                    ##Для отладки в терминале
                                    #print('До:')
                                    #if event.message.from_id < 0:
                                    #    print('до бота')
                                    #else:
                                    #    print(vk.users.get(user_id=event.message.peer_id)[0]['first_name'])
                                    #print('i am: ' + botanswer)
                                    #print('')

                                #else:
                                    #print('Кубики сломались') #не повезло с шансом
                            elif repeated >5: #если третий раз повтор - сбрасывает счетчик повторов
                                repeated = 0
                        else: #Если новый ответ 
                            writemessage(event, vk, botanswer) #отправим в чат

                            ##Для отладки в терминале
                            #print('До:')
                            #if event.message.from_id < 0:
                            #    print('до бота')
                            #else:
                            #    print(vk.users.get(user_id=event.message.peer_id)[0]['first_name'])
                            #print('i am: ' + botanswer)
                            #print('')
                            lastword = botanswer #запомним ответ
                            repeated = 0 #сбросим повтор
                    
            #Другие виды эвентов вк. Проверить можно, отладив метод VkBotEventType
            #elif event.type == VkBotEventType.MESSAGE_REPLY:
            
            #elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            
            #else: #Не понятно, что за эвент

            ##Для отладки в терминале
            #    print(event.type)
            #    print()

    except: #Сломалось что-то
        try:
            print(event) #попробуем узнать, что было последним
        except:
            print('хрен пойми что случилось')
        x = x +1 #счетчик ошибок
        print('some error')
print('Error more than 9000!') #все, конец
            
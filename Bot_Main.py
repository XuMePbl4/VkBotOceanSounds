import vk_api
import time
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from Bot_Words import BotWords

def writemessage(event, vk, botanswer):
    FN =  vk.users.get(user_id=event.message.from_id)[0]['first_name']
    LN =  vk.users.get(user_id=event.message.from_id)[0]['last_name']
    print(LN + ' ' + FN + ' ' + event.message.text)
    botanswer = FN + ', ' + botanswer
    #print('i am: ' + botanswer)
    #print('')
    vk.messages.send(random_id = int(time.time()), peer_id = event.message.peer_id, message = botanswer)

x = 0

while x < 100:
    try:

        vk_session = vk_api.VkApi(token='4842ab42fc8ab6aa6860269222be707fe712ab2f417086f766e39e84aeb7e04572610aa3adcb21f663bc7')

        vk = vk_session.get_api() 

        longpoll = VkBotLongPoll(vk_session, '198202940')

        if x == 0:
            print('Server started')
        else:
            print('Server started again')

        print('')
        lastword = ''
        repeated = 0
        nr = 0
                    
        for event in longpoll.listen():

            #print(event)

            if event.type == VkBotEventType.MESSAGE_NEW:
                #print('Новое сообщение:')

                #print('От: ', end='')
                #if event.message.from_id < 0:
                #    print('от бота')
                #else:
                #    print(vk.users.get(user_id=event.message.from_id)[0]['first_name'])

                #print('До:')
                #if event.message.from_id < 0:
                #    print('до бота')
                #else:
                #    print(vk.users.get(user_id=event.message.peer_id)[0]['first_name'])

                #print('Текст: ', event.message.text)
                if event.message.from_id > 0:
                    botanswer = BotWords.report(event.message.text)
                    if botanswer != 'Нуль':
                        if lastword == botanswer:
                            repeated = repeated + 1
                            if (repeated == 1):
                                nr = random.randint(0, 9)
                                if nr < 2:
                                    lastword = botanswer
                                    writemessage(event, vk, botanswer) #тут надо пришить ответ-аналог
                                    print('До:')
                                    if event.message.from_id < 0:
                                        print('до бота')
                                    else:
                                        print(vk.users.get(user_id=event.message.peer_id)[0]['first_name'])
                                    print('i am: ' + botanswer)
                                    print('')
                                    #user_id идентификатор пользователя, которому отправляется сообщение. целое число
                                    #random_id уникальный (в привязке к API_ID и ID отправителя) идентификатор, предназначенный для предотвращения повторной отправки одинакового сообщения. Сохраняется вместе с сообщением и доступен в истории сообщений.
                                    #Заданный random_id используется для проверки уникальности за всю историю сообщений, поэтому используйте большой диапазон (до int32). целое число, доступен начиная с версии 5.45
                                    #peer_id идентификатор назначения. Для групповой беседы: 2000000000 + id беседы
                                    #chat_id идентификатор беседы, к которой будет относиться сообщение. положительное число, максимальное значение 100000000
                                else:
                                    print('Кубики сломались')
                            elif repeated >3:
                                repeated = 0
                        else:
                            writemessage(event, vk, botanswer)
                            print('До:')
                            if event.message.from_id < 0:
                                print('до бота')
                            else:
                                print(vk.users.get(user_id=event.message.peer_id)[0]['first_name'])
                            print('i am: ' + botanswer)
                            print('')
                            lastword = botanswer
                            repeated = 0
                    #print('Ответ: ', )
                    #print()

            #elif event.type == VkBotEventType.MESSAGE_REPLY:
            #    print('Новое сообщение:')

            #    print('От:')
            #    if event.message.from_id < 0:
            #        print('от бота')
            #    else:
            #        print(vk.users.get(user_id=event.message.from_id)[0]['first_name'])

            #    print('До:')
            #    if event.message.from_id < 0:
            #        print('до бота')
            #    else:
            #        print(vk.users.get(user_id=event.message.peer_id)[0]['first_name'])

            #    print('Текст: ', event.message.text)
            #    print('Ответ: ', BotWords.report(event.message.text))
            #    print()

            #elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            #    print('Печатает ', end='')

            #    print(vk.users.get(user_id=event.message.from_id)[0]['first_name'], end=' ')

            #    print('для ', end='')

            #    print(vk.users.get(user_id=event.message.to_id)[0]['first_name'])
            #    print()

            #else:
            #    print(event.type)
            #    print()
    except:
        try:
            print(event)
        except:
            print('хрен пойми что случилось')
        x = x +1
        print('some error')
print('Error more than 9000!')
            
import random #рандом
import re #Библиотека регулярных выражений
#Через регулярные выражения определяем сообщение и ищем ответ
#https://habr.com/ru/post/349860/
import sqlite3 #для базы данных

import time #время
import vk_api #библиотеки вк
from vk_api import audio
import vk_audio
import lxml
from itertools import islice

import requests
import bs4
import json

class BotWordsInit:

    def report(message,user_id): #Основная процедура класса

        Answer = 'Нуль' #дабы не было рандомных крашей

        # Создаем соединение с нашей базой данных
        conn = sqlite3.connect('Chinook_Sqlite.sqlite')

        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()

        sqlstr =  "Select * FROM Messages where Template not null" #Считываем все шаблоны с базы
        sqlanswer = cursor.execute(sqlstr).fetchall()

        if len(sqlanswer) >= 1: #Если шаблоны найдены:
            for x in range(0,len(sqlanswer)): #До конца прогоняем цикл: Проверка сообщения пользователя на шаблон регуляркой
                if re.search(sqlanswer[x][2],message): #Если найдено сообщение сервисного типа
                    if sqlanswer[x][3] == 2: #Сервисные
                        Answer = BotWords.ServiceMessage(message,sqlanswer[x][2],sqlanswer[x][4],sqlanswer[x][5],sqlanswer[x][6],user_id) #Отправляемся в специальную процедуру для сервисника
                    
                    elif sqlanswer[x][3] == 3: #Регулярка 
                        #Если найден обычный тип, то выбираем один из 3 вариантов ответа и заканчиваем цикл досрочно
                        VarT = random.randint(4, 6)
                        Answer = sqlanswer[x][VarT] 
                        break
                    
                    elif sqlanswer[x][3] == 1: #Резерв
                        Answer = BotWords.BaseMessage(message) 

        #Не забываем закрыть соединение с базой данных
        conn.close()

        return Answer


class BotWords:

    def BaseMessage(message): #базовое
        #if re.search(r'\b[П,п]ривет\b', message):
        #    return f'привет :) '
    
        #elif re.search(r'\b[П,п]ока\b', message):
        #    return f"ну пока..."

        #else:
            return f'Нуль'

    def ServiceMessage(message,template,a1,a2,a3,user_id): #служебное (команда)

        if template == "\\b[И,и]нфа\\b":
            VarT = random.randint(1, 3)
            NameVarT = "a"+str(VarT)
            Info = random.randint(0, 100)
            answer = str(eval(NameVarT)) +" инфа составляет примерно " + str(Info) + "%"
        elif (template == "\\b[М,м]узыка\\b") or ("\\b[Д\д]ай [М,м]узыка\\b"):
            try:
                authorizationFile = open('authorization.txt', 'r')
                data = authorizationFile.read()
                data = data.split()
                vk_login = data[0]
                vk_password = data[1]
                vk_appid = data[2]
                vk_user_id = data[3]
                vk_state = data[4]
                authorizationFile.close()
            
                vk_sX = vk_api.VkApi(login=vk_login, password=vk_password, captcha_handler=BotService.captcha_handler)
                try:
                    vk_sX.auth()
                except vk_api.AuthError as error_msg:
                    print(error_msg)

                vkX = vk_audio.VkAudio(vk=vk_sX)
                DataMusic = vkX.load(user_id)
                if DataMusic == False:
                    answer = 'Досуп к твоим аудиозаписям закрыт :('
                elif DataMusic.Count > 0:
                    rnd_music = random.randint(1, DataMusic.Count-1)
                    VarT = random.randint(1, 3)
                    NameVarT = "a"+str(VarT)
                    answer = str(eval(NameVarT)) +" "+ str(DataMusic.Audios[rnd_music].artist + " - "+ DataMusic.Audios[rnd_music].title)
                else:
                    answer = 'Не смог найти музыку вообще... :('
                    

            except:
                print("Авторизация не найдена")
                answer = 'Нуль'
        else:
            answer = 'Нуль'
        return answer

class BotService:

    def captcha_handler(captcha):
        """ При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Enter captcha code {0}: ".format(captcha.get_url())).strip()

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

    def musicGet(id): # функция будет принимать только id пользователя
        siteUrl = requests.get('https://vrit.me' + '/audios{0}'.format(id)) # открытие сайта 
        htmlMusicContent = bs4.BeautifulSoup(siteUrl.text , 'html.parser')
        allLinks = htmlMusicContent.find_all('a') # выбор всех ссылок
        allTitles = htmlMusicContent.find_all('div' , attrs={'class':'title'}) # выбор всех названий песен
        reallyLinks = allLinks[7:-1] # отсев настоящих ссылок
        i = 0
        answer = []
        while  i < len(reallyLinks):
            value = {'title': allTitles[i+1].getText(), 'link':MUSIC_URL + reallyLinks[i]['href']}
            answer.append(value)
            i += 1
        # создание ответа
        return answer
        

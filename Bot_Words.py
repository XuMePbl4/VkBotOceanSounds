import random #рандом
import re #Библиотека регулярных выражений
#Через регулярные выражения определяем сообщение и ищем ответ
#https://habr.com/ru/post/349860/
import sqlite3 #для базы данных

class BotWordsInit:

    def report(message): #Основная процедура класса

        Answer = 'Нуль' #дабы не было рандомных крашей

        # Создаем соединение с нашей базой данных
        conn = sqlite3.connect('Chinook_Sqlite.sqlite')

        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        cursor = conn.cursor()

        sqlstr =  "Select * FROM Messages where Template not null" #Считываем все шаблоны с базы
        sqlanswer = cursor.execute(sqlstr).fetchall()

        if len(sqlanswer) >= 1: #Если шаблоны найдены:
            for x in range(0,len(sqlanswer)-1): #До конца прогоняем цикл: Проверка сообщения пользователя на шаблон регуляркой
                if re.search(sqlanswer[x][2],message): #Если найдено сообщение сервисного типа
                    if sqlanswer[x][3] == 2: #Сервисные
                        Answer = BotWords.ServiceMessage(message,sqlanswer[x][2],sqlanswer[x][4],sqlanswer[x][5],sqlanswer[x][6]) #Отправляемся в специальную процедуру для сервисника
                    
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

    def ServiceMessage(message,template,a1,a2,a3): #служебное (команда)

        if template == "\\b[И,и]нфа\\b":
            VarT = random.randint(1, 3)
            NameVarT = "a"+str(VarT)
            Info = random.randint(0, 100)
            answer = str(eval(NameVarT)) +" инфа составляет примерно " + str(Info) + "%"
        else:
            answer = 'Нуль'
        return answer
        

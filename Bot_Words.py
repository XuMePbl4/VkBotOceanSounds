import re

class BotWords:
    #def __init__(self, message):

    def report(message):

        if re.search(r'\b[П,п]ривет\b', message):
            return f'привет :) '
    
        elif re.search(r'\b[П,п]ока\b', message):
            return f"ну пока..."

        elif re.search(r'\b[Д,д]оброе утро\b', message):
            return f"утро доброе!"

        elif re.search(r'\b[П,п]огода\b', message):
            return f"погода супер."

        elif re.search(r'\b[П,п]ока\b', message):
            return f"ну пока..."

        elif re.search(r'\b[Л,л]юблю\b', message):
            return f"а я тебя люблю <3"

        elif re.search(r'\b[П,п]издец\b', message):
            return f"зачем ругаешься, насяльника?"

        elif re.search(r'\b[О,о]тношения', message):
            return f"опять про отношения..."

        elif re.search(r'\b[М,м]ожно\b', message):
            return f"тебе все можно <3"

        elif re.search(r'\b[Ж,ж]ена\b', message):
            return f"жена на кухне, не отвлекай!"

        elif re.search(r'\b[Ж,ж]иза\b', message):
            return f"эх, мне бы так..."

        elif re.search(r'\b[С,с]пать\b', message):
            return f"спокойной ночи <3"

        elif re.search(r'\b[С,с]опли\b', message):
            return f"отставить сопли!"

        elif re.search(r'\b[Х,х]андр', message):
            return f"отставить хандру!"

        elif re.search(r'\b[О,о]бнять\b', message):
            return f"можно я тебя обниму?"

        elif re.search(r'\b[О,о]бнимашки\b', message):
            return f"обнимашки!"

        elif re.search(r'\b[К,к]ать', message):
            return f"кать кать кать"

        elif re.search(r'[Х,х,X,x][Y,y,У,у][Й,й,y,Y,u,U]', message):
            return f"не матерись!"

        elif re.search(r'\b[М,м]яу', message):
            return f"мяу"

        elif re.search(r'\b[М,м]иу', message):
            return f"миу-миу!"

        elif re.search(r'\b[П,п]оздравл[яю,ем]\b', message):
            return f"присоединяюсь к поздравлениям :)"

        elif re.search(r'\b[Р,р]ебята\b', message):
            return f"и Взрослые тоже"

        elif re.search(r'\b[Р,р]ак', message):
            return f"гороскопы - туфта!"

        elif re.search(r'\b[О,о]д[на,ин]\b', message):
            return f"я с тобой <3"

        elif re.search(r'\b[К,к]усь\b', message):
            return f"не кусайся!"

        elif re.search(r'\b[С,с]ука\b', message):
            return f"не ругайся, а то по жепе выдеру."

        #elif re.search(r'\b[Б,б]от', message):
        #    return f"между прочим, боты очень логические существа."
        
        elif re.search(r'\b[С,с]ерафим.\b', message):
            return f"где-то в небе разбудили ангела."

        elif re.search(r'\b[Д,д]жесс', message):
            return f"теперь с тебя 100 рублей для Джесс"

        elif re.search(r'\b[В,в]ан.\b', message):
            return f"не буди Ваньку-Встаньку! А то встанет и вставит :Р"

        elif re.search(r'\b[Е,е]гор\b', message):
            return f"что ты наделал? сейчас ми-ми-ми картинки прилетят в чат!"
   
        elif re.search(r'\b[П,п]итон\b', message):
            return f"Python - лучший язык программирования!" 
    
        elif re.search(r'\b[P,p]ython\b', message):
            return f"Python - лучший язык программирования!"     

        elif re.search(r'\b[С,с]тереотип[п,пы]\b', message):
            return f"сейчас Джонни взбесится..."    
    
        elif re.search(r'\b[А,а]лександрос.\b', message):
            return f"только не говори о СССР-Тян!"
    
        elif re.search(r'\b[Р,р]омка\b', message):
            return f"мы с Ромкой бухаем, отстаньте!"
    
        elif re.search(r'\b[Б,б]ывш..\b', message):
            return f"на**й бывших!"
    
        #elif re.search(r'\b[Т,т]ак\b', message):
        #    return f"так-так оО"

        #elif re.search(r'\b[К,к]а[я,ю,й]\b', message):
        #    return f"Кай мой младший братик. За него любого порву."

        elif re.search(r'\b[Ж,ж]ен.\b', message):
            return f"Евгена нет, я за него. Что надо?"
    
        elif re.search(r'\bXuMePbl4\b', message):
            return f"Евгена нет, я за него. Что надо?"

        elif re.search(r'\b[X,x]umepbl4\b', message):
            return f"Евгена нет, я за него. Что надо?"

        elif re.search(r'\b[A,a]ll\b', message):
            return f"сейчас тебе за это жопу надерут...?"
        
        elif re.search(r'\b[Г,г]рустно\b', message):
            return f"почему грустишь? :с"

        elif re.search(r'[Г,г]руст', message):
            return f"Кто тут грустит? Че за дела? :О"

        else:
            return "Нуль"
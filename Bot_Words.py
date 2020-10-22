import re

class BotWords:
    #def __init__(self, message):

    def report(message):

        ## Привет
        #if message == "Привет":
        #    return f"Привет-привет!"

        ## Пока
        #elif message == "Пока":
        #    return f"Пока-пока!"

        if re.search(r'\bпривет\b', message):
            return f'привет :) '
    
        elif re.search(r'\bпока\b', message):
            return f"ну пока..."

        elif re.search(r'\bпогода\b', message):
            return f"погода супер."

        elif re.search(r'\bпока\b', message):
            return f"ну пока..."

        elif re.search(r'\bлюблю\b', message):
            return f"а я тебя люблю <3"

        elif re.search(r'\bпиздец\b', message):
            return f"зачем ругаешься, насяльника?"

        elif re.search(r'\bотношения\b', message):
            return f"опять про отношения..."

        elif re.search(r'\bможно?\b', message):
            return f"тебе все можно <3"

        elif re.search(r'\bжена\b', message):
            return f"жена на кухне, не отвлекай!"

        elif re.search(r'\bжиза\b', message):
            return f"эх, мне бы так..."

        elif re.search(r'\bЖиза\b', message):
            return f"эх, мне бы так..."

        elif re.search(r'\bспать\b', message):
            return f"спокойной ночи <3"

        elif re.search(r'\bсопли\b', message):
            return f"отставить сопли!"

        elif re.search(r'\bхандра\b', message):
            return f"отставить хандру!"

        elif re.search(r'\bобнять\b', message):
            return f"можно я тебя обниму?"

        elif re.search(r'\bобнимашки\b', message):
            return f"обнимашки!"

        elif re.search(r'\bкать\b', message):
            return f"кать кать кать"

        elif re.search(r'\bхуйня\b', message):
            return f"не матерись!"

        elif re.search(r'\bмяу\b', message):
            return f"мяу"

        elif re.search(r'\bМяу\b', message):
            return f"Мяу!"

        elif re.search(r'\bмиу\b', message):
            return f"миу-миу"

        elif re.search(r'\bМиу\b', message):
            return f"миу-миу!"

        elif re.search(r'\bпоздравляю\b', message):
            return f"присоединяюсь к поздравлениям :)"

        elif re.search(r'\bПоздравляю\b', message):
            return f"присоединяюсь к поздравлениям :)"

        elif re.search(r'\bпоздравляю)\b', message):
            return f"присоединяюсь к поздравлениям :)"

        elif re.search(r'\bПоздравляю)\b', message):
            return f"присоединяюсь к поздравлениям :)"

        elif re.search(r'\bребята\b', message):
            return f"и взрослые тоже"

        elif re.search(r'\bРебята\b', message):
            return f"и Взрослые тоже"

        elif re.search(r'\bрак\b', message):
            return f"гороскопы - туфта!"

        elif re.search(r'\bРак\b', message):
            return f"гороскопы - туфта!"

        elif re.search(r'\bодна\b', message):
            return f"я с тобой <3"

        elif re.search(r'\bКусь\b', message):
            return f"не кусайся!"

        elif re.search(r'\bкусь\b', message):
            return f"не кусайся!"

        elif re.search(r'\bсука\b', message):
            return f"не ругайся, а то по жепе выдеру."

        elif re.search(r'\bхуй\b', message):
            return f"***"

        elif re.search(r'\bбот\b', message):
            return f"между прочим, боты очень логические существа. И кстати, раз я тебе пишу, значит я существую."

        elif re.search(r'\bсерафима\b', message):
            return f"где-то в небе разбудили ангела."

        elif re.search(r'\bджесс\b', message):
            return f"теперь с тебя 100 рублей для Джесс"

        elif re.search(r'\bваня\b', message):
            return f"не буди Ваньку-Встаньку! А то встанет и вставит :Р"

        elif re.search(r'\bегор\b', message):
            return f"что ты наделал? сейчас ми-ми-ми картинки прилетят в чат!"
        
        elif re.search(r'\bСерафима\b', message):
            return f"где-то в небе разбудили ангела."

        elif re.search(r'\bДжесс\b', message):
            return f"теперь с тебя 100 рублей для Джесс"

        elif re.search(r'\bВаня\b', message):
            return f"не буди Ваньку-Встаньку! А то встанет и вставит :Р"

        elif re.search(r'\bЕгор\b', message):
            return f"что ты наделал? сейчас ми-ми-ми картинки прилетят в чат!"
   
        elif re.search(r'\bпитон\b', message):
            return f"Python - лучший язык программирования!" 
    
        elif re.search(r'\bPython\b', message):
            return f"Python - лучший язык программирования!" 
    
        elif re.search(r'\bстереотип\b', message):
            return f"сейчас Джонни взбесится..."

        elif re.search(r'\bстереотипы\b', message):
            return f"сейчас Джонни взбесится..."    
    
        elif re.search(r'\bалександрос\b', message):
            return f"только не говори о СССР-Тян!"
    
        elif re.search(r'\bромка\b', message):
            return f"хватит Ромку мучать, не мешайте нам с ним бухать!"
    
        elif re.search(r'\bбывший\b', message):
            return f"на**й бывших!"
    
        elif re.search(r'\bтак\b', message):
            return f"так-так. оО"
    
        elif re.search(r'\bженя\b', message):
            return f"Евгена нет, я за него. Что надо?"

        elif re.search(r'\bЖеня\b', message):
            return f"Евгена нет, я за него. Что надо?"
    
        elif re.search(r'\bXuMePbl4\b', message):
            return f"Евгена нет, я за него. Что надо?"

        elif re.search(r'\bxumepbl4\b', message):
            return f"Евгена нет, я за него. Что надо?"

        elif re.search(r'\ball\b', message):
            return f"сейчас тебе за это жопу надерут...?"

        else:
            return "Нуль"
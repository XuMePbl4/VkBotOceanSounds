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
    
        elif re.search(r'\bXuMePbl4\b', message):
            return f"Евгена нет, я за него. Что надо?"

        else:
            return "Нуль"
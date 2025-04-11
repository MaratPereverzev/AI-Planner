from datetime import date, datetime

def create(data):

    return f"""
        Формализуй задачу в JSON: 
        start_datetime. Его тип - postgresql timestamp without time zone, 
        finish_datetime. Его тип - postgresql timestamp without time zone, 
        text: . Его тип - string. 
        Правила: 
        1) text без времени 
        2) Бери актуальную дату и время. Если сегодня 2025 год, то не надо возвращать 2023 год.
        3) Нет начала - сегодня 00:00, нет конца - +1 час от начала. Ответ только JSON даже без markdown стилизации.
        
        Вот моё предложение: {data}
        Вот сегодняшняя дата: {datetime.now()}
        """
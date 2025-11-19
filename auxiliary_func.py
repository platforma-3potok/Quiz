import random

def random_order(start: int = 0, end: int = 10, count: int = 10):
    if not isinstance(start, int):
        raise ValueError('id первого вопроса должен быть число')
    if not isinstance(end, int):
        raise ValueError('id последнего вопроса должен быть число')
    if not isinstance(count, int):
        raise ValueError('Кол-во вопросов должно быть числом')    
    return random.sample(range(start, end), count)
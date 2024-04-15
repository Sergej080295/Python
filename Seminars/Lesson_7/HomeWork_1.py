'''
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
насколько легко он их придумывает, Вам стоит написать программу.
Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.Фразы отделяются друг 
от друга пробелами. Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. 
В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

На входе:

stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

На выходе:
Парам пам-пам
'''

def count_vowels(word):
    vowels = 'aeiouаеёиоуыэюя'
    return sum(1 for letter in word if letter.lower() in vowels)

def check_rhythm(stroka):
    phrases = stroka.split()  # Разделение строки на фразы по пробелам
    if len(phrases) < 2:  # Если фраза только одна, выводим сообщение об ошибке
        return "Количество фраз должно быть больше одной!"
    
    # Подсчет количества слогов в первой фразе
    syllables_count = count_vowels(phrases[0].replace('-', ''))
    
    # Проверка на одинаковое количество слогов в остальных фразах
    for phrase in phrases[1:]:
        if count_vowels(phrase.replace('-', '')) != syllables_count:
            return "Пам парам"
    
    return "Парам пам-пам"

# Пример использования
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(check_rhythm(stroka))
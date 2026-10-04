string = str(input('Введите текст: ')).lower()

words = string.lower().split()
words_frequency = {w: words.count(w) for w in words}
sorted_words = sorted(words_frequency, key = words_frequency.get, reverse = True)

print('Самые частоиспользуемые слова: ', ', '.join(map(str, sorted_words[:5]))+'.')
# few few few few few 5 5 5 5 u u u o o o p p 0 ) ) (о) (о) (о)

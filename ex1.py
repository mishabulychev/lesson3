with open('referat.txt' , 'r' , encoding='utf-8') as text:
    words_total = 0
    for line in text:
        words_total += len(line.split())
    print('В тексте всего' + ' ' + str(words_total) + ' ' + 'слов(а)')
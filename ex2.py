import csv

answers={
    'привет': 'И тебе привет!',
    'как дела': 'Лучше всех',
    'пока': 'Увидимся'
    }

with open ('answers_list.csv','w',encoding='utf-8') as qa:
    fields = ['question', 'answer']
    writer = csv.DictWriter(qa, fields, delimiter=';')
    writer.writeheader()
    for question,answer in answers.items():
        writer.writerow({'question':question, 'answer':answer})
import random
a=['Capybara','Honey','Beer','Fish','Crackers','Gleb','Bread','Person','Friends','Numbers']
b=['Капибара','Мед','Пиво','Рыба','Сухарики','Клоун','Хлеб','Человек','Друзья','Цифры']
print('Сейчас вам будут выводится слова на английском языке, а вы должны написать их перевод на русский с большой буквы')
f = 0
while len(a)>0:
    s = random.randint(0, len(a)-1)
    print(a[s])
    if input()==b[s]:
        print('верно\n-----------')
        a.pop(s)
        b.pop(s)
    else:
        print(f'не верно, попробуйте снова\n-----------')
        f+=1
print(f'вы совершили {f} ошибок')

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10


print('Введите количество поделок, изготовленных детьми: ')
bastelarbeit = int(input())
if bastelarbeit % 3 == 0:
    ein_Kind_basteln = bastelarbeit / 3

    # результат работы трудоголика
    harter_Arbeiter = bastelarbeit - ein_Kind_basteln

    # результат работы леньтяев
    faulpelz = (bastelarbeit - harter_Arbeiter) / 2
    print('Петя изготовил:', faulpelz, 'поделок')
    print('Катя изготовила:', harter_Arbeiter, 'поделок')
    print('Серёжа изготовил:', faulpelz, 'поделок')
else:
    print('Ошибка! Дети должны были изготовить целое количество игрушек.')
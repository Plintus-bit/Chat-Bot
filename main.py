# -*- coding: utf-8 -*-
robo_replics = []
user_replics = []
RoboTalk = "Бот: "
robot_dk = "Я ещё не умею отвечать на ваш вопрос.\nЧто мне следует отвечать? (перечислите через запятую)"
robot_thanks = "Спасибо! Теперь буду знать"

def onStart() -> None:
    # Чтение из файла ответов
    with open('ans.txt', encoding='UTF-8') as ansfile:
        for st in ansfile:
            st = st.replace('\n', '')
            robo_replics.append(st.split(','))

    # Чтение из файла реплик
    with open('rep.txt', encoding='UTF-8') as repfile:
        for st in repfile:
            st = st.replace('\n', '')
            user_replics.append(st)


# Функция записи в файлы
def exitProc() -> None:
    pass


# Функция обучения бота
def learn(answer: str = 'none') -> None:
    if answer == 'none':
        return


# Функция получения рандомного ответа из массива ответов бота
def getRandomBotAnswer(answer_index: int) -> int:
    # если в массиве больше одного символа,
    # рекомендую сделать shuffle
    # и взять первое (нулевое) значение из массива
    pass


def isInUsRep(us_rep: str, us_rep_index: int) -> bool:
    if us_rep == user_replics[us_rep_index]:
        return True
    elif us_rep == user_replics[us_rep_index] + '?':
        return True
    elif us_rep == user_replics[us_rep_index]\
            [:len(user_replics[us_rep_index]) - 1]:
        return True
    return False


# Функция ответа бота при получении реплики от пользователя
def reply(us_rep='пока') -> bool:
    if us_rep == 'пока':
        # тут рандом будет
        print(RoboTalk + robo_replics[1][0])
        return False
    for i in range(len(user_replics)):
        if isInUsRep(us_rep, i):
            # тут рандом будет
            print(RoboTalk + robo_replics[i][0])
            return True
    print(robot_dk)
    rep = input()
    print(robot_thanks)
    return True


# Основная функция, которая запускает цикл чат-бота и запрашивает реплики
def main():
    onStart()
    gameloop = True
    print('Для выхода напишите "пока"')
    while gameloop:
        print('Вы: ')
        rep = input().lower()
        gameloop = reply(rep)


if __name__ == '__main__':
    main()

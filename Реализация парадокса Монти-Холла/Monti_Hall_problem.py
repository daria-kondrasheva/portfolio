import PySimpleGUI as sg

import numpy as np
import pandas as pd
import random


def MontiHall(number_of_simulations):
    where_is_the_car = []
    goats = []
    my_choice = []
    my_choice_excluded = []
    host_opens_the_door = []
    change_my_choice = []
    win_if_keep_my_choice = []
    win_if_change_my_choice = []

    for i in range(number_of_simulations): 

        where_is_the_car.append(random.randint(1,3)), 
        goats.append([x for x in [1,2,3] if x != where_is_the_car[i]]), 
        my_choice.append(random.randint(1,3)),

        my_choice_excluded.append([x for x in goats[i] if x != my_choice[i]]), 

        if(len(my_choice_excluded[i]) == 1):
            host_opens_the_door.append(my_choice_excluded[i].pop())
        else: host_opens_the_door.append(random.choice(my_choice_excluded[i])),

        change_my_choice.append([x for x in [1,2,3] if x not in [my_choice[i], host_opens_the_door[i]]].pop()),

        win_if_keep_my_choice.append(where_is_the_car[i] == my_choice[i]), 
        win_if_change_my_choice.append(where_is_the_car[i] == change_my_choice[i])

    keep_choice_res   = sum(win_if_keep_my_choice) / number_of_simulations
    change_choice_res = sum(win_if_change_my_choice) / number_of_simulations
    
    return(keep_choice_res, change_choice_res)

sg.theme('BlueMono')

layout = [
     [sg.T('Парадокс Монти Холла', font='arial 16')],
     [sg.T(f'''
        Представьте, что Вы стали участником игры, в которой Вам нужно выбрать одну из трёх дверей. 
           За одной из дверей находится автомобиль, за двумя другими дверями — козы. Вы выбираете 
           одну из дверей, например, номер 1, после этого ведущий, который знает, где находится 
           автомобиль, а где — козы, открывает одну из оставшихся дверей, например, номер 3, за 
           которой находится коза. После этого он спрашивает вас, не желаете ли вы изменить свой 
           выбор и выбрать дверь номер 2. 
           
           Увеличатся ли ваши шансы выиграть автомобиль, если вы примете предложение ведущего 
            и измените свой выбор?
            ''', font='arial 13')],
     [sg.T(f'''
            При этом участнику игры заранее известны следующие правила:
                1. автомобиль равновероятно размещён за любой из 3 дверей;
                2. ведущий в любом случае обязан открыть дверь с козой (но не ту, которую выбрал игрок) 
                    и предложить игроку изменить выбор;
                3. если у ведущего есть выбор, какую из 2 дверей открыть, он выбирает любую из них 
                    с одинаковой вероятностью.
           ''', font='arial 11')],
     [sg.T('Введите количество симуляций: ', key='lbl_a', font='arial 13'), sg.I('', size=(20,2),pad=(10,10))],
    [sg.B('Посчитать', key='calc', border_width=5, pad=(10,10))],
     [sg.T('Вероятность выиграть, если НЕ ИЗМЕНИТЬ выбор: ', font='arial 13'), sg.I('', key='keep_ch', size=(30,2),pad=(10,10))],
     [sg.T('Вероятность выиграть, если ПОМЕНЯТЬ дверь: ', font='arial 13'), sg.I('', key='chnge_ch', size=(30,2),pad=(10,10))]
  ]

window = sg.Window('Парадокс Монти-Холла', layout, size=(900,600))

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if event == 'calc':
        try:
            num_of_sims = int(values[0])
        except:
            type(num_of_sims) != int
            sg.popup_error("Вводите только целочисленные переменные!")
            break
       
        keep_choice, change_choice = MontiHall(num_of_sims)
        window['keep_ch'].update(str(keep_choice))
        window['chnge_ch'].update(str(change_choice))

window.close()
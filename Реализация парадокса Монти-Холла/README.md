# Реализация парадокса Монти Холла

---
#### Используемые библиотеки:

*Основные:*
- numpy
- pandas
- random

*Интерфейс:*
- PySimpleGUI

---
#### Задача:
Задача - реализовать Парадокс Монти-Холла на множестве симуляций в доступной форме для тех, кто не знаком с написанием кода. 

Интерфейс получился как в 90-е, но, главное, работает ведь! 

Файл с расширением `.py` можно скачать себе на компьютер и запустить у себя локально на машине)) Вам останется только задать число симуляций. 

---

Нижеприведенный код функции симуляций по Монти-Холлу написан исключительно из интереса к самому парадоксу (и от избытка свободного времени):

```python
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
```
# -*- coding: utf-8 -*-
import os
my_text = "'''\n\n'''" 
path = "D:\\Coding\My_courses\Stepik - 'Поколение Python' курс для продвинутых\\13. Модули decimal, fraction и complex\\13.3 Тип данных complex"

# Создаем файл и записываем в него текст
n = 3 # кол-во задач в модуле 
for i in range(1, n + 1):
    with open(os.path.join(path, f'task_{i}.py'), 'w', encoding='utf-8') as f:
        f.write(my_text)
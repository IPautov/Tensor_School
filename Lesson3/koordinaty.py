#!/usr/bin/python3

print("Ваш персонаж наоходится в точке с координатами 0:0. Введите куда Ваш персонаж должен идти")

x = 0
y = 0
x_r = int(input('Вправо на:'))
x_l = int(input('Влево на:'))
y_u = int(input('Вверх на:'))
y_d = int(input('Вниз на:'))

print("Новые координаты персонажа:", x + x_r - x_l,':',y+y_u-y_d, sep='')
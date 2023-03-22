import pygame as pg
import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from config import K, S, H, m, e, s, dt, T0

def calculate_energy(particles):
    E = 0
    for obj in particles:
        v2 = obj.vx**2 + obj.vy**2 + obj.vz**2
        E += 1 * m * v2/2 #считаем кинетическую энергию
        for part in particles:
            if obj != part:
                if part.x - obj.x > H/2:
                    part.xt = part.x - H
                if part.x - obj.x < - H/2:
                    part.xt = part.x + H
                if part.x - obj.x < H/2 and part.x - obj.x > -H/2:
                    part.xt = part.x

                if part.y - obj.y > H/2:
                    part.yt = part.y - H
                if part.y - obj.y < - H/2:
                    part.yt = part.y + H
                if part.y - obj.y < H/2 and part.y - obj.y > -H/2:
                    part.yt = part.y

                if part.z - obj.z > H/2:
                    part.zt = part.z - H
                if part.z - obj.z < - H/2:
                    part.zt = part.z + H
                if part.z - obj.z < H/2 and part.z - obj.z > -H/2:
                    part.zt = part.z

                x = part.xt - obj.x
                y = part.yt - obj.y
                z = part.zt - obj.z
                r = (x**2 + y**2 + z**2)**0.5
                E += 1/2 * 4 * e * ((s/r) ** 12 - (s/r) ** 6) # считаем потенциал взаимодействия частиц
    #print("E: ", E)
    return E   

def draw(screen, particles):
    for part in particles:
        part.pos = (K * part.x + S/2, K * part.y + S/2)
        pg.draw.circle(screen, (0,0,1), part.pos, K/2)

def update_files(H, T, v, n):
    file = open("data/coords.xyz.txt", "w")
    file.close()

    file = open("data/config.txt", "w")
    file.write('сторона клетки: ' + str(H) + '\n' +
            'количество частиц: ' + str(n ** 3) + '\n' +
            'начальная скорость: ' + str(v) + '\n' +
            'время моделирвоания: ' + str(T) + '\n' +
            'время начала подсчета распределения: ' + str(T0))
    file.close()

    file = open("data/E_t.txt", "w")
    file.close()

    file = open("data/vx_vy_vz_t.txt", "w")
    file.close()

def write_coords(N, particles, t):
    file = open("data/coords.xyz.txt", "a")
    n_str = str(N)
    file.write(n_str + '\n \n')
    for obj in particles:
        file.write('H ' + str(obj.x) + ' ' + str(obj.y) + ' ' + str(obj.z) + ' \n')
    file.close()

def write_data(particles, t):
    file = open("data/E_t.txt", "a")
    file.write(str(calculate_energy(particles)) + ' ' + str(t) + '\n')
    file.close()

    if t > T0:
        file = open("data/vx_vy_vz_t.txt", "a")
        for obj in particles:
            file.write(str(obj.vx) + ' ' + str(obj.vy) + ' ' + str(obj.vz) + ' ' + str(t) + ' \n')
        file.close()
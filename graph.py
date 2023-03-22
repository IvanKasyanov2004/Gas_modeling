import pygame as pg
import math
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from config import K, S, H, m, e, s, dt

def graph_E_t():
    E = [0]
    t = [0]
    with open('data/E_t.txt', 'r') as file:
        for line in file:
            E.append(float(line.split()[0]))
            t.append(float(line.split()[1]))
    E = np.array(E)
    t = np.array(t)

    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'minor', alpha = 0.2)

    plt.scatter(t, E, s = 3)

    plt.ylabel("energy")
    plt.xlabel("time")
    plt.title("graph E(t)")
    plt.savefig('graphs/graph_E_t.png', dpi = 1000)

    plt.clf()

def graph_T_t():
    vx = []
    vy = []
    vz = []
    t = [0]
    T = [0]
    with open('data/vx_vy_vz_t.txt', 'r') as file:
        for line in file:
            vx.append(float(line.split()[0]))
            vy.append(float(line.split()[1]))
            vz.append(float(line.split()[2]))
            t.append(float(line.split()[3]))

    vx = np.array(vx)
    vy = np.array(vy)
    vz = np.array(vz)
    t = np.array(t)

    v2 = np.array(vx ** 2 + vy ** 2 + vz ** 2)

    for i in range(len(v2)):
        kT = m * np.mean(v2[:i]) / 3
        T.append(kT)

    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'minor', alpha = 0.2)

    plt.scatter(t, T, s = 3)

    plt.ylabel("temperature")
    plt.xlabel("time")
    plt.title("graph T(t)")

    plt.savefig('graphs/graph_T_t.png', dpi = 1000)
    plt.clf()

def graph_histogram_f_vx():
    vx = []
    vy = []
    vz = []
    t = [0]
    with open('data/vx_vy_vz_t.txt', 'r') as file:
        for line in file:
            vx.append(float(line.split()[0]))
            vy.append(float(line.split()[1]))
            vz.append(float(line.split()[2]))
            t.append(float(line.split()[3]))

    vx = np.array(vx)
    vy = np.array(vy)
    vz = np.array(vz)
    t = np.array(t)

    v2 = np.array(vx ** 2 + vy ** 2 + vz ** 2)

    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'minor', alpha = 0.2)

    kT = m * np.mean(v2) / 3
    A = (m / (2 * math.pi * kT)) ** 0.5
    v = np.linspace(np.amin(vx), np.amax(vx), 100)
    f = np.array(A * np.exp( -(m * v**2) / (2 * kT)))
    plt.hist(vx, bins = 30, density=True)
    plt.plot(v, f)

    plt.ylabel("probability")
    plt.xlabel("vx")
    plt.title("Histogram f(vx)")

    plt.savefig('graphs/histogram_f_vx.png', dpi = 1000)
    plt.clf()

def graph_histogram_f_v():
    vx = []
    vy = []
    vz = []
    t = [0]
    with open('data/vx_vy_vz_t.txt', 'r') as file:
        for line in file:
            vx.append(float(line.split()[0]))
            vy.append(float(line.split()[1]))
            vz.append(float(line.split()[2]))
            t.append(float(line.split()[3]))

    vx = np.array(vx)
    vy = np.array(vy)
    vz = np.array(vz)
    t = np.array(t)

    v2 = np.array(vx ** 2 + vy ** 2 + vz ** 2)
    v = np.array((vx ** 2 + vy ** 2 + vz ** 2) ** 0.5)

    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which = 'minor', alpha = 0.2)

    kT = m * np.mean(v2) / 3
    A = 4 * math.pi * (m / (2 * math.pi * kT)) ** 1.5
    v0 = np.linspace(np.amin(v), np.amax(v), 100)
    f0 = np.array(A * np.exp( -(m * v0**2) / (2 * kT)) * v0**2)
    plt.hist(v, bins = 30, density=True)
    plt.plot(v0, f0)

    plt.ylabel("probability")
    plt.xlabel("v")
    plt.title("Histogram f(v)")

    plt.savefig('graphs/histogram_f_v.png', dpi = 1000)

    plt.clf()


print("graphing in progress...")

graph_E_t()
graph_T_t()
graph_histogram_f_vx()
graph_histogram_f_v()

print("graphing finished")
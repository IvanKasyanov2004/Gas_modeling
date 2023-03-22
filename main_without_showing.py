import pygame as pg
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from config import dt, T, S, H, v, m, k, n
from model import move, move_tel, generate_particles
from object import Particle
from stats import calculate_energy, write_coords, update_files, write_data
from graph import graph_E_t, graph_T_t, graph_histogram_f_vx, graph_histogram_f_v


particles = []

generate_particles(particles, H, n, v)

t = 0
E0 = calculate_energy(particles)

update_files(H, T, v, n)
print("modeling in progress...")

while t < T:
    move_tel(particles)
    
    t += dt

    write_data(particles, t)
    write_coords(n**3, particles, t)

print("modeling finished")

print("graphing in progress...")

graph_E_t()
graph_T_t()
graph_histogram_f_vx()
graph_histogram_f_v()

print("graphing finished")

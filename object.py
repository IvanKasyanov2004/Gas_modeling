import numpy as np

class Particle:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.xt = 0
        self.yt = 0
        self.zt = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.ax = 0
        self.ay = 0
        self.az = 0
        self.ax1 = 0
        self.ay1 = 0
        self.az1 = 0
        self.pos = (0,0)
        self.buckets = np.zeros(20)
import pygame
import numpy as np
# Can make this class its own file, improves readability of the code
class Car:
    def __init__(self, number, x0, y0, v0, a0, angle0, car_size, max_speed, max_neg_acc, max_pos_acc, car_color):
        self.number = number
        self.x = x0
        self.y = y0
        self.v = v0
        self.a = a0
        self.size = car_size
        self.max_speed = max_speed
        self.max_neg_acc = max_neg_acc
        self.max_pos_acc = max_pos_acc
        self.color = car_color
        self.angle = angle0

    def get_velo(self):
        return self.v
    
    def get_acc(self):
        return self.a

    def get_size(self):
        return self.size

    def get_angle(self):
        return self.angle

    def set_acc(self, set_acc):
        self.a = set_acc

    def set_velo(self, set_velo):
        self.a = set_velo

    def print_summary(self):
        # Originally used when I had a 1D simulation, not corrected for a circular track
        print(f"Car #{self.number}, size {self.size}, is at x = {self.x} m and y = {self.y} m with a speed of {self.v} m/s and an acceleration of {self.a} m/s^2.")

    def draw_car(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

    def move(self, track_radius, screen_width, screen_height):
        """
        Should put all of this functionality elsewhere instead of a method in the class
        """

        self.v += self.a*np.pi/180

        if self.v < 0:
            self.v = 0
        elif self.v > self.max_speed:
            self.v = self.max_speed

        self.angle += self.v

        self.angle = self.angle % 360

        self.x = np.cos(self.angle * np.pi/180)*track_radius + screen_width/2
        self.y = np.sin(self.angle * np.pi/180)*track_radius + screen_height/2

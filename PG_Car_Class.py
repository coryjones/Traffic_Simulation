import pygame
import numpy as np
# Can make this class its own file, improves readability of the code
class Car:
    def __init__(self, number, x0, y0, v0, a0, angle0, car_size, max_speed, max_pos_acc, car_color, chicken):
        self.number = number
        self.x = x0
        self.y = y0
        self.v = v0
        self.a = a0
        self.size = car_size
        self.max_speed = max_speed
        self.max_pos_acc = max_pos_acc
        self.color = car_color
        self.angle = angle0
        self.chicken_factor = chicken

    def get_velo(self):
        return self.v
    
    def get_acc(self):
        return self.a

    def get_size(self):
        return self.size

    def get_angle(self):
        return self.angle

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_chicken(self):
        return self.chicken_factor

    def get_size(self):
        return self.size

    def set_acc(self, set_acc):
        self.a = set_acc

    def print_summary(self):
        # Originally used when I had a 1D simulation, not corrected for a circular track
        print(f"Car #{self.number}, size {self.size}, is at x = {self.x} m and y = {self.y} m with a speed of {self.v} m/s and an acceleration of {self.a} m/s^2.")

    def draw_car(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)

    def move(self, track_radius, screen_width, screen_height):
        """
        Should put all of this functionality elsewhere instead of a method in the class
        """

        if self.a > self.max_pos_acc:
            self.a = self.max_pos_acc

        self.v += self.a*np.pi/180

        if self.v < 0:
            self.v = 0
        elif self.v > self.max_speed:
            self.v = self.max_speed

        self.angle += self.v

        self.angle = self.angle % 360

        self.x = np.cos(self.angle * np.pi/180)*track_radius + screen_width/2
        self.y = np.sin(self.angle * np.pi/180)*track_radius + screen_height/2

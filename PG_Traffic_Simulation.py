import numpy as np
import pygame
from PG_Car_Class import Car
import random
import time


"""
Variables needed:
current pos
Size of car
current speed
current acc
max speed
max acceleration (not necessarily symmetric)
reaction time
Chicken factor? (don't like people behind you, don't like being close, or want to get as close as possible)

functions
setters
getters
update v, a, etc.
checks
check of crash
check of distance in front
"""

# Setting basic variables
background_color = "black"

track_radius = 250 # Radius to the center of the track

# Initializes pygame
pygame.init()

# Setting Font For Printouts
font_color=(255,255,255)
font_obj=pygame.font.Font("/System/Library/Fonts/Supplemental/Futura.ttc",15)

# Screen size generated with pygame
screen_width = 750
screen_height = 750
(width, height) = (screen_width, screen_height)

# Infinite loop variable that'll be used later when actually running the simulation
running = True


# Function to draw track that'll be called every loop
def draw_track():
    pygame.draw.circle(screen, "gray", (screen_width/2, screen_height/2), 300)
    pygame.draw.circle(screen, "black", (screen_width/2, screen_height/2), 200)



number_of_cars = 5
my_cars = []

color_list = ["blue", "red", "green", "purple", "white"]

# Generating all of the cars
for n in range(number_of_cars):
    # starting_angle = 2*np.pi + n*(2*np.pi)/(number_of_cars) + (random.randint(-100, 100)/number_of_cars)*np.pi/180
    starting_angle = 360 + n*(360)/(number_of_cars) + (random.randint(-100, 100)/number_of_cars)
    starting_x = np.cos(starting_angle * np.pi/180)*track_radius + screen_width/2
    starting_y = np.sin(starting_angle * np.pi/180)*track_radius + screen_height/2

    starting_v = random.randint(0,3)
    starting_acc = random.randint(0,5)


    car = Car(1, starting_x, starting_y, starting_v, starting_acc, starting_angle, 20, 40, -20, 10, color_list[n])

    my_cars.append(car)


# Printing the stats
def draw_text(current_time):
    # Render the objects
    time_obj=font_obj.render(f"Current Time: {current_time//60} min {current_time%60} s",True,font_color)
    screen.blit(time_obj,(450,0))
    num_car_obj=font_obj.render(f"Number of cars: {number_of_cars}",True,font_color)
    screen.blit(num_car_obj,(450,20))

    sum_velos = 0
    for i in my_cars:
        sum_velos += i.get_velo()
    av_velos = round(sum_velos/number_of_cars,2)

    av_velo_obj=font_obj.render(f"Average Rot. Velo: {av_velos} deg/s",True,font_color)
    screen.blit(av_velo_obj,(450,40))

    




# Setting up the pygame window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Traffic Simulation")
screen.fill(background_color)

# Time counter
current_time = 0

# Drawing the initial position
draw_track()

draw_text(current_time)

for car in my_cars:
    car.draw_car(screen)

pygame.display.flip()



# Running the simulation
while running:
    for event in pygame.event.get():
        # Allows the code to be quit
        if event.type == pygame.QUIT:
            running = False
        

        current_time += 1

        screen.fill(background_color)
        draw_track()
        draw_text(current_time)

        for i in range(len(my_cars)):
            car_in_front_pos = my_cars[i-number_of_cars+1].get_angle()

            if car_in_front_pos <= (my_cars[i].get_angle() + my_cars[i].get_velo()) % 360:
                my_cars[i].set_acc(-10)
            else:
                my_cars[i].set_acc(my_cars[i].get_acc()+1)


            my_cars[i].move(track_radius, screen_width, screen_height)
            my_cars[i].draw_car(screen)

            pygame.display.flip()

            # Wait one second after every loop
        time.sleep(1)



"""
Update 3 Todo

Initialized at random spots

Doubly linked list (look this up)
"""



import numpy as np
import pygame
import random
from PG_Car_Class import Car



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
crash_font_obj=pygame.font.Font("/System/Library/Fonts/Supplemental/Futura.ttc",25)

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

car_size = 20

color_list = ["blue", "red", "green", "purple", "white"]

# Generating all of the cars
for n in range(number_of_cars):
    # starting_angle = 2*np.pi + n*(2*np.pi)/(number_of_cars) + (random.randint(-100, 100)/number_of_cars)*np.pi/180
    starting_angle = 360 + n*(360)/(number_of_cars) + (random.randint(-150, 150)/number_of_cars)
    starting_x = np.cos(starting_angle * np.pi/180)*track_radius + screen_width/2
    starting_y = np.sin(starting_angle * np.pi/180)*track_radius + screen_height/2

    starting_v = random.randint(0,3)

    c=random.randomint(0,4)
    carcolor=color_list[c]

    car = Car(1, starting_x, starting_y, starting_v, 0, starting_angle, car_size, 40, 10, carcolor, random.randint(75, 85))

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


crash_check = False

# Running the simulation
while running:
    for event in pygame.event.get():
        # Allows the code to be quit
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:

            #Time keeper
            current_time += 1

            screen.fill(background_color)
            draw_track()
            draw_text(current_time)

            # Littlest distance for each round
            # Used as a crash checker later
            min_distance = 1000

            for i in range(len(my_cars)):
                # Finding the car in front position
                cif_x = my_cars[i-number_of_cars+1].x
                cif_y = my_cars[i-number_of_cars+1].y

                # Cartesian distance apart
                # Had trouble using the angle as distance control because of the circular nature
                # (Tough to compare 355 to 5)
                distance_apart = np.sqrt((my_cars[i].x - cif_x)**2 + (my_cars[i].y- cif_y)**2)

                #
                if distance_apart < my_cars[i].chicken_factor:
                    my_cars[i].set_acc(-15)
                elif distance_apart <= 1.25*my_cars[i].chicken_factor:
                    my_cars[i].set_acc(0)
                else:
                    my_cars[i].set_acc(my_cars[i].a+1.5)



                my_cars[i].move(track_radius, screen_width, screen_height)
                my_cars[i].draw_car(screen)

                if distance_apart < min_distance:
                    min_distance = distance_apart

            if min_distance < car_size * 2.35:
                crash_obj=crash_font_obj.render(f"CRASH!  Game Over",True, "Red")
                screen.blit(crash_obj,(0, 0))
                crash_check = True

            pygame.display.flip()

                    

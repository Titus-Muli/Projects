import turtle
import random as rd
import math

start_coor= [-230,-230]
end_coor= [230,230]
x= 0; y=1

start= turtle.Turtle('square'); end= turtle.Turtle('square')
start.teleport(start_coor[0],start_coor[1]); end.teleport(end_coor[0],end_coor[1])
start.color('green'); end.color('green')
start.shapesize(2); end.shapesize(2)

car= turtle.Turtle('square')
car.teleport(start_coor[0],start_coor[1]); car.left(90)
car.penup(); car.shapesize(1.5)
car.speed(1.3); car.setheading(45)

obstacles_number= rd.randint(4,6)
obstacle_coors= []
obstacles= []

obstacle_blocks= [[-200,50],[-50,200]]

car_position= [-230,-230]
car_angle= 45

def towards_end(car_position, end_coor):
    dy= car_position[1]-end_coor[1]
    dx= car_position[0]-end_coor[0]
    tan= dy/dx
    end_angle= math.degrees(math.atan(tan))    
    if (end_angle > 360) or (end_angle < 0):
        end_angle= correct_angle(end_angle)
    return end_angle

def correct_angle(new_angle):
    if new_angle>360:
        new_angle= new_angle-360
    elif new_angle<0:
        new_angle= new_angle+360
    return new_angle

def get_position(car_position,car_angle,turn_angle,forward):
    new_angle= car_angle+turn_angle        
    new_angle_radians= math.radians(new_angle)
    dx= forward*math.cos(new_angle_radians)
    dy= forward*math.sin(new_angle_radians)    
    car_position[0]+= dx
    car_position[1]+= dy
    car_angle= new_angle    
    return car_position, car_angle

def create_obstacles(obstacles_number,obstacle_blocks):
    for [s,e] in obstacle_blocks:
        for _ in range(obstacles_number):
            x= rd.randint(s,e)
            y= rd.randint(s,e)
            obstacle= turtle.Turtle('circle')
            obstacle.shapesize(1.8)
            obstacle.teleport(x,y)
            obstacle_coors.append([x,y])
            obstacles.append(obstacle)
    return obstacles, obstacle_coors
obstacles, obstacle_coors= create_obstacles(obstacles_number,obstacle_blocks)

def get_nearest_obstacle(obstacle_coors):
    obstacles_ahead= []
    for [ox,oy] in obstacle_coors:
        angle= car.towards(ox,oy)-car.heading()
        distance= car.distance(ox,oy)
        if (-25 < angle <25 ) and (distance < 60):
            obstacles_ahead.append([ox,oy])
            
    if obstacles_ahead== []:
        shortest_distance= 0
        side= 'right'
    else:
        distances= [car.distance(ax,ay) for [ax,ay] in obstacles_ahead]
        shortest_distance= min(distances)
        side= rd.choice(['left','right'])

    return shortest_distance, side
shortest_distance, side = get_nearest_obstacle(obstacle_coors)

running= True
while running:
    if  shortest_distance== 0:
        end_angle= towards_end(car_position, end_coor)
        turn_angle= end_angle-car_angle
        if (-5 < turn_angle < 5):
            car.forward(10)        
            car_position, car_angle= get_position(car_position, car_angle, turn_angle, 10)
            shortest_distance, side = get_nearest_obstacle(obstacle_coors)
        else:            
            while True:
                turn_angle= end_angle-car_angle                                
                if turn_angle > 5:
                    car.left(5)
                    turn= 5
                elif turn_angle < -5:
                    car.right(5)
                    turn= -5
                if (-5 < turn_angle < 5):
                    break
                car.forward(6)        
                car_position, car_angle= get_position(car_position, car_angle, turn, 6)
                shortest_distance, side = get_nearest_obstacle(obstacle_coors)
                if shortest_distance != 0:
                    break
                if (end_coor[x]-40 < car.xcor() < end_coor[x]+40) and (end_coor[y]-40 < car.ycor() < end_coor[y]+40):
                    break                
    else:
        reverse_distance= shortest_distance-80
        car.forward(reverse_distance)
        car_position, car_angle= get_position(car_position,car_angle,0,reverse_distance)
        if side== 'left':
            for _i in range(2):
                car.left(30)
                car.forward(10)
                shortest_distance, side = get_nearest_obstacle(obstacle_coors)
                car_position, car_angle= get_position(car_position,car_angle,30,10)
                if shortest_distance!=0:
                    break
            for _ in range(8):
                car.speed(1.3)
                car.right(8)
                car.forward(12)                
                shortest_distance, side = get_nearest_obstacle(obstacle_coors)
                car_position, car_angle= get_position(car_position,car_angle,-8,12)
                if shortest_distance!=0:
                    break
        elif side== 'right':
            for _i in range(2):
                car.right(30)
                car.forward(10)
                shortest_distance, side = get_nearest_obstacle(obstacle_coors)
                car_position, car_angle= get_position(car_position,car_angle,-30,10)
                if shortest_distance!=0:
                    break
            for _ in range(8):
                car.speed(1.3)
                car.left(8)
                car.forward(12)                
                shortest_distance, side = get_nearest_obstacle(obstacle_coors)
                car_position, car_angle= get_position(car_position,car_angle,8,12)
                if shortest_distance!=0:
                    break                
                
    if (end_coor[x]-40 < car.xcor() < end_coor[x]+40) and (end_coor[y]-40 < car.ycor() < end_coor[y]+40):
        car.setheading(90)
        running = False

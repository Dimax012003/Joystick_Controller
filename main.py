import time
import serial
from turtle import Screen
from test_player import Player
seria=serial.Serial(port='COM7',baudrate=9600)
screen=Screen()
screen.title("square")
screen.setup(height=600,width=600)
screen.tracer(0)
player=Player()
movement={
    "move_x":   0,
    "move_y":   0
}
direction={
    "read_x":   0,
    "read_y":   0
}
while True:
    time.sleep(0.001)
    screen.update()
    data=str(seria.readline(1000),"UTF-8")
    new_data = data.split(' ')
    # append direction and movement for the object
    movement["move_x"] = float(new_data[0])
    movement["move_y"] = float(new_data[1])
    direction["read_x"] = float(new_data[3])
    direction["read_y"] = float(new_data[4])
    player.move(movement["move_x"],movement["move_y"])
    player.set_direction(direction["read_x"],direction["read_y"])


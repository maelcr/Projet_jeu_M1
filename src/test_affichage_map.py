import pandas as pd 
import numpy as np
import scipy as sp
import matplotlib.pylab as mp
import csv

csv_file_path = 'src\map1.csv'

with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    map = []
    for row in csv_reader:
        map.append(row[0].split(';'))

map_a_print=""
#x_position_joueur=joueur.position_x
#y_position_joueur=joueur.position_y

x_position_joueur=11
y_position_joueur=11

for i in range(len(map)):
    for j in range(len(map[i])): 

        if(j==x_position_joueur and i==y_position_joueur):
               map_a_print+=(chr(35))
        else :
                tuille = map[i][j]
                if(tuille=="0"):    
                        map_a_print+=(chr(46))
                elif(tuille=="1"):    
                        map_a_print+=(chr(64))
                elif(tuille=="2"):    
                        map_a_print+=(chr(21))
                elif(tuille=="3"):    
                        map_a_print+=(chr(47))
                elif(tuille=="4"):    
                        map_a_print+=(chr(27))
                elif(tuille=="5"):    
                        map_a_print+=(chr(26))
                elif(tuille=="6"):    
                        map_a_print+=(chr(25))
                elif(tuille=="7"):    
                        map_a_print+=(chr(24))
                elif(tuille=="8"):    
                        map_a_print+=(chr(36))
                elif(tuille=="9"):    
                        map_a_print+=(chr(77))
                elif(tuille=="10"):    
                        map_a_print+=(chr(20))
                elif(tuille=="11"):    
                        map_a_print+=(chr(33))
                elif(tuille=="12"):    
                        map_a_print+=(chr(63))
                elif(tuille=="13"):    
                        map_a_print+=(chr(14))
                elif(tuille=="14"):    
                        map_a_print+=(chr(15))
                elif(tuille=="15"):    
                        map_a_print+=(chr(19))
                elif(tuille=="16"):    
                        map_a_print+=(chr(23))
                else:
                        map_a_print+="-"

    map_a_print+="\n"

print(map_a_print)
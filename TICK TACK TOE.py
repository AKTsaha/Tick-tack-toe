#!/usr/bin/env python
# coding: utf-8
from IPython.display import clear_output

def check(values):
    for i in range(1,3):
        if values[i][1]==values[i][2] and values[i][2]==values[i][3] :
            return values[i][1]
    i=0
    for i in range(1,3):
        if values[1][i]==values[2][i] and values[2][i]==values[3][i]:
            return values[1][i]
    if values[1][1]==values[2][2] and values[2][2]==values[3][3]:
        return values[1][1]
    if values[1][3]==values[2][2] and values[2][2]==values[3][1]:
        return values[1][3]
    return 0    

def bord(values):
    
    print('')
    print("   |   |   ")
    print(f" {values[1][1]} | {values[1][2]} | {values[1][3]} ")
    print("-----------")
    print("   |   |   ")
    print(f" {values[2][1]} | {values[2][2]} | {values[2][3]} ")
    print("-----------")
    print("   |   |   ")
    print(f" {values[3][1]} | {values[3][2]} | {values[3][3]} ")
    print()
            

def position_definer(position,present_option,values): 
    '''
        position_definer is to allot the O/X at the position asked
        input: position: where you want to enter the O/X (not index just position means no starting from zero)
               present_option: O or X which needed to be establish
               values: the list that has the values 
        output: return list value
    '''
    if(position==1):
        values[1].pop(1)
        values[1].insert(1,f'{present_option}')
        return values
    elif(position==2):
        values[1].pop(2)
        values[1].insert(2,f'{present_option}')
        return values
    elif(position==3):
        values[1].pop(3)
        values[1].insert(3,f'{present_option}')
        return values
    elif(position==4):
        values[2].pop(1)
        values[2].insert(1,f'{present_option}')
        return values
    elif(position==5):
        values[2].pop(2)
        values[2].insert(2,f'{present_option}')
        return values
    elif(position==6):
        values[2].pop(3)
        values[2].insert(3,f'{present_option}')
        return values
    elif(position==7):
        values[3].pop(1)
        values[3].insert(1,f'{present_option}')
        return values
    elif(position==8):
        values[3].pop(2)
        values[3].insert(2,f'{present_option}')
        return values
    elif(position==9):
        values[3].pop(3)
        values[3].insert(3,f'{present_option}')
        return values


def start():
    values=['#',['#','1','2','3'],['#','4','5','6'],['#','7','8','9']]
    options_chosen=[]
    print("O will go first")
    box_used = 1
    while box_used<=9: 
         
        if box_used%2==0:
            present_option='X'
        else:
            present_option='O'
        position = int(input(f'enter where you want to enter the {present_option}  '))
        clear_output()
        if position in options_chosen:
            print("position is allready occupied")
            continue
        else:
            options_chosen.append(position)
        values=position_definer(position,present_option,values)
        bord(values)
        result=check(values)
        if result == 'O' or result == 'X':
            print('')
            print(f'---------------{result} has Won the game-------------------')
            print('')
            break
        box_used +=1   
    if(box_used == 10):
        print('---------match is draw----------')
        


# In[15]:

start()

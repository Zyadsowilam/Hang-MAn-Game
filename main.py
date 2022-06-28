#0:2 could be used in str to neglict some char var[0:2](0,1) negative could be used to rev
#out of range gives error string out of range
# in could be usedto check if it is their or not
# first:end:step
#input can take take  parameter message
#input default is string you should put in var
#in x=int(input('try')) u restrict the data type
# logic is and not or
#if stat we use : after the condition
# we use space before the excution
# else if is elif
# for i in range(3) 0 1 2 range(start,end,step)
# for  in string index in range(len(s)) for access index
# for in string char s for access each char
# bisection algo 3 var high low mis(avg)
# divide data each time using med
# print takes only string
#def is used before any fun
#array is called tubles to declare tuble t=(parameter,) note their should be ,
# you cannot change the var but can overwrite
#tube cold be used for swap x y (x,y)=(y,x)
#tube could be used to return many param
#list[parameter]
#list.append add one element list.extend add list []
#del(list[index]) delete element L.remove(value) it removes the first value it give error if valnot found
#list.pop() take pop last element l.pop(3) pop elment with index 3
#if s is string list(s) to change string to list
#s.split('') to split the list
#''.join(list) change list to string
#sorted(list) asen but list doent change l.sort() l change to sort l.reverse()
#l1=l2  same memory l1=l2[:] copying l1=sorted(l2)
#in for loop copy listand loop in it but change in original
#intiate dictionary {key:value}
#add entery dic[key]=value del[dic[key]] d1.get(key) to get value d1.update(d2) merge
#check key in dic dic.keys() dic.values for sepration


import tkinter as tk
window=tk.Tk()

from random_word import RandomWords
import random
import json
import  draw
from  draw import Draw
import turtle
from turtle import *
turtle.hideturtle()
color("red")
compare=0
randomwords = RandomWords()
word = randomwords.get_random_word()
letters=list(word)
shuffle= {}
chances=0

for x in range(len(letters)):
    shuffle[x]="-"
check=0

while(check==0):
    print("test")
    print(''.join(list(shuffle.values())))



    guess=input('Take a guess')

    if guess in letters:
        for z in range(len(letters)):
            if guess == letters[z]:
                shuffle[z]=letters[z]
            for j in range(len(letters)):
                if shuffle[j]==letters[j]:

                    compare=compare+1

                    if compare == len(letters):

                        check=1
                        color("black")
                        style = ('Arial', 30, 'bold')
                        turtle.write('You WIN', font=style, align='center')


                else:
                    compare=0

                    break

    else:
        print("sorry wrong answer")
        Draw(chances)




    print(list(shuffle.values()))


    ex=input("to exit press y else to know the answer p else any letter ")
    if ex=='y':
        check=1
    elif ex=='p':
        print(word)
        check=1

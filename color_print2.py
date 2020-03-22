import os
from colorama import init
from termcolor import colored
init()

def prRed(skk): print(colored("{}".format(skk),'red'),end="")
def prGreen(skk): print(colored("{}".format(skk),'green'),end="")
def prBlue(skk): print(colored("{}".format(skk),'blue'),end="")
def prWhite(skk): print(colored("{}".format(skk),'white'),end="")
def prPurple(skk): print(colored("{}".format(skk),'purple'),end="")
def prYellow(skk): print(colored("{}".format(skk),'yellow'),end="")


def color_print(text, text_class):
    for c, n in zip(text, text_class):
        if n == 1:
            prRed(c)
        elif n == 2:
            prGreen(c)
        elif n == 3:
            prBlue(c)
        elif n!=0:
            prPurple(c)
        else:
            prWhite(c)
    # print()


data = os.listdir("ground_truth")
x = 1
skip = 0
for i in range(1,len(data)):
    print("\n####################\nFILE NAME:            {}\n####################\n".format(i))
    if x==0: break
    if x==2 and skip!=5:
        skip += 1
        continue
    skip = 0
    with open("data/{}.txt".format(i),"r") as f:
        text = list(f.read())
    with open("ground_truth/{}.txt".format(i),"r") as f:
        # print("ground_truth/{}.txt", f.read())
        text_class = list(map(int,list(f.read())))
        # print(text_class)
    color_print(text, text_class)
    prYellow("\n\nWant to see more?\n\t0 to exit\n\tPress 1 for next\n\tPress 2 to skip 5 images")
    x = int(input())

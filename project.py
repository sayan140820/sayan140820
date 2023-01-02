import os

import csv

import sys

import subprocess

import time

try:

import matplotlib.pyplot as plt

except:

subprocess.run(['pip', 'install', 'matplotlib']) import matplotlib.pyplot as plt


path='C:/PythonProgramming Project_main-folder'

print("*50)

 #ALL the Functions used Throughout the code

def loading screen():

for i in range(10):

sys.stdout.write("\rLoading" + "." * i)

sys.stdout.flush()

time.sleep(0.5)

sys.stdout.write("\rLoading complete!")

def createfile(name, 1st):

with open('(path)/(name)', a',newline='') as f:

script= csv.writer(f)

script.writerow(1st)

print("{name} file has been UPDATED")

def percent (num):

if stream. lower()=='cse' or stream.lower()=='cseal' or stream. lower()='cseaiml or stream. lower()=='cselotcsbs": num (num*100)//600

elif stream, lower()=='it' or stream. lower()=='ece' or stream.lower()=='me' or stream. lower()=='EEE';

num-(num*100)//600

return num
#Madlibs utilizing user input for word choices
import random

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
noun1 = input("Noun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")

print("Welcome to Python Madlibs!")

madlib = f"Hi, I'm John. I'm very new to programming and am trying to teach myself with udemy and freecodecamp. \
         I find it really {adj1} so far, and want to go into the field of programming eventually. \
         I really enjoy the {noun1} of solving problems that comes with programming. Still, sometimes it can feel like my brain is {verb1} when I'm stuck on a problem for a long time. \
         I enjoy {verb2} projects like this, because it's a fun way to learn. \
         Coding is {adj2} and I will be sticking with it."

print(madlib)

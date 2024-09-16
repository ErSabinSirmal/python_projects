# import turtle

# from turtle import Turtle, Screen
# sora = Turtle()
# print(sora)
# sora.shape("turtle")
# # sora.forward(50)
# # sora.left(90)
# # sora.forward(50)
# # sora.left(90)
# # sora.forward(50)
# # sora.left(90)
# # sora.forward(50)
# sora.teleport(45,45)
# sora.color("DarkSeaGreen1")
# sora.fillcolor("DarkSlateGray3")
# sora.shapesize(20,20)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","water","Fire"])

# Adding row one by one.......
# table.add_row(["Pikachu","Electric"])
# table.add_row(["Squirtle","Water"])
# table.add_row(["Charmader","Fire"])


# Adding all row at one time.....
# table.add_row(
#     [
#         ["Pikachu","Electric"],
#         ["Squirtle","Water"],
#         ["Charmader","Fire"],
#     ]
# )

table.align = "l"
print(table)

# from turtle import Turtle, Screen
# timmy = Turtle()
# my_screen = Screen()
# print(my_screen.canvheight)
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)


from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["Pokemon Name", "Type"]
# table.add_rows(
#     [
#         ["Pikachu", "Electric"],
#         ["Squirtle", "Water"],
#         ["Charmander", "Fire"],
#     ]
# )
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water", "Fire"])
table.align = "r"

print(table)

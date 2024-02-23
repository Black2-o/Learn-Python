################### Scope ####################

enemies = 1

def increase_enemies(enemies):
  enemies += 1
  print(f"enemies inside function: {enemies}")
  # or return enemies +1

increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


pi = 3.14159
PI = 3.14159
URL = "https://www.google.com"
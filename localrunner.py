import json
import random

config = input() # получение конфигурации игры
    
while True:    
    state = input()  # получение тика
    commands = ['left', 'right', 'up', 'down']  # доступные команды
    cmd = random.choice(commands)  # случайный выбор действия
    print(json.dumps({"command": cmd, 'debug': cmd}))  # отправка результата
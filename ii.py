import json
import random

# with open('log.txt', 'w') as f:


config = json.loads(input()) # получение конфигурации игры   
# raise Exception(config)


log = []
start_XY = None
# f.write(str(config))
while True:
    try:   
        state = json.loads(input())
    except:
        break
    
    if state['type'] == 'end_game':
        break

    commands = ['left', 'right', 'up', 'down']  # доступные команды
    # raise Exception(state['params']['players']['i']['position'][0]/config['params']['width'])
    # f.write(state['params']['players']['i']['position'])
    
    x = int(state['params']['players']['i']['position'][0]/config['params']['width']-0.5)
    y = int(state['params']['players']['i']['position'][1]/config['params']['width']-0.5)

    if start_XY is None:
        start_XY = x, y

    log.append((x, y))

    if y==30 and x > 0:
        if x == start_XY[0]+1:
            print(json.dumps({"command": 'down', 'debug': 'down'}))
        else:
            print(json.dumps({"command": 'left', 'debug': 'left'}))
    elif x==0 and y > 0:
        print(json.dumps({"command": 'down', 'debug': 'down'}))
    elif y==0 and x < 30:
        print(json.dumps({"command": 'right', 'debug': 'right'}))
    elif x==30 and y < 30:
        print(json.dumps({"command": 'up', 'debug': 'up'}))
    else:
        print(json.dumps({"command": 'up', 'debug': 'up'}))
    
raise Exception((config, log))
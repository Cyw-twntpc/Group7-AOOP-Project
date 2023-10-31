import json

pygame_config = {
    'window_width': 800,
    'window_height': 600,
    'background_color': (0, 0, 0), 
    'fps': 60,
    'sound_volume': 0.8,
}

with open('./bomb_superman_game/src/config/config.json', 'w') as file:
    json.dump(pygame_config, file)

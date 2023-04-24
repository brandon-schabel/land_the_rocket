_CONFIG = {
    'WIDTH': 1280,
    'HEIGHT': 720,
    'GRAVITY': 0.5,
    'ACC': 2.0,
    'FRICTION': -0.08,
    'PROPULSION': 0.3,
    'LANDING_ZONE_SPEED': 5,
    'PROPULSION_TIME': 1,
    'PROPULSION_MAX': 0.5,
    'AIR_RESISTANCE': 0.1,
    'BLACK': (0, 0, 0),
    'WHITE': (255, 255, 255),
    'GREEN': (53, 235, 8),
    'RED': (255, 0, 0),
    'FONT_SIZE': 25,
    'LANDING_PAD_X': 400,
    'LANDING_PAD_Y': 500,
    'LANDING_PAD_WIDTH': 200,
    'LANDING_PAD_HEIGHT': 20,
    'BEST_SCORE': 0,
    'PROPULSION_DEC': 0.1,
}

_DEFAULT_CONFIG = _CONFIG.copy()


def get(key, default=None):
    return _CONFIG.get(key, default)


def update(key, value):
    _CONFIG[key] = value

def get_color(key):
    color = _CONFIG.get(key, _DEFAULT_CONFIG.get(key))
    if color:
        return tuple(color)
    return (255, 255, 255)
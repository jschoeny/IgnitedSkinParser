from enum import Enum


class GameTypeIdentifier(Enum):
    GBC = 'com.rileytestut.delta.game.gbc'
    GBA = 'com.rileytestut.delta.game.gba'
    NDS = 'com.rileytestut.delta.game.nds'
    NES = 'com.rileytestut.delta.game.nes'
    SNES = 'com.rileytestut.delta.game.snes'
    N64 = 'com.rileytestut.delta.game.n64'
    GENESIS = 'com.rileytestut.delta.game.genesis'


class Device(Enum):
    IPHONE = 'iphone'
    IPAD = 'ipad'
    TV = 'tv'


class Orientation(Enum):
    PORTRAIT = 'portrait'
    LANDSCAPE = 'landscape'


class DisplayType(Enum):
    STANDARD = 'standard'
    EDGE_TO_EDGE = 'edgeToEdge'
    SPLIT_VIEW = 'splitView'


class AssetSize(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    PREVIEW = 'preview'
    RESIZABLE = 'resizable'


class Input(Enum):
    NULL = 'null'

    # Game inputs
    A = 'a'
    B = 'b'
    C = 'c'
    X = 'x'
    Y = 'y'
    Z = 'z'
    SELECT = 'select'
    START = 'start'
    MODE = 'mode'
    C_UP = 'cUp'
    C_DOWN = 'cDown'
    C_LEFT = 'cLeft'
    C_RIGHT = 'cRight'
    L = 'l'
    R = 'r'

    # Directional inputs
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    # Action inputs
    MENU = 'menu'
    RESTART = 'restart'
    QUICK_SAVE = 'quickSave'
    QUICK_LOAD = 'quickLoad'
    SCREENSHOT = 'screenshot'
    STATUS_BAR = 'statusBar'
    QUICK_SETTINGS = 'quickSettings'
    FAST_FORWARD = 'fastForward'
    TOGGLE_FAST_FORWARD = 'toggleFastForward'
    TOGGLE_ALT_REPRESENTATION = 'toggleAltRepresentations'


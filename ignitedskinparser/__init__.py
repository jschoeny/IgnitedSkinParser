from .enums import (
    GameTypeIdentifier, Device, Orientation, DisplayType, AssetSize, Input
)
from .types import (
    Asset, Size, Rect, ExtendedEdges, Item, Screen, Representation
)
from .live_skin import (
    Color, Address, BitInfo, DecryptionMethod, Image, CircularHP, RectangularHP, Number, Text, IndexedText
)
from .skin import IgnitedSkin


class LiveSkin:
    Color = Color
    Address = Address
    BitInfo = BitInfo
    DecryptionMethod = DecryptionMethod
    Image = Image
    CircularHP = CircularHP
    RectangularHP = RectangularHP
    Number = Number
    Text = Text
    IndexedText = IndexedText


__all__ = [
    'GameTypeIdentifier',
    'Device',
    'Orientation',
    'DisplayType',
    'AssetSize',
    'Input',
    'Asset',
    'Size',
    'Rect',
    'ExtendedEdges',
    'Item',
    'Screen',
    'Representation',
    'IndexedText',
    'IgnitedSkin',
    'LiveSkin'
]

__version__ = '1.0.0'
__author__ = 'Jared Schoeny'

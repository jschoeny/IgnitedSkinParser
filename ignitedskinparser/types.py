import os
from typing import ClassVar

from .enums import AssetSize, Device, DisplayType, Input, Orientation


class Asset:
    def __init__(self, file_path: str, size: AssetSize):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.size = size
        self.__verify_image()

    # Private methods
    def __verify_image(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")
        if not self.file_path.endswith('.png') and self.size != AssetSize.RESIZABLE:
            raise ValueError(f"Only PNGs can be used with {self.size} assets.")
        elif not self.file_path.endswith('.pdf') and self.size == AssetSize.RESIZABLE:
            raise ValueError(f"Only PDFs can be used with {AssetSize.RESIZABLE} assets.")


class Size:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __dict__(self):
        return {"width": self.width, "height": self.height}


class Rect:
    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __dict__(self):
        return {"x": self.x, "y": self.y, "width": self.width, "height": self.height}


class ExtendedEdges:
    ZERO: ClassVar['ExtendedEdges']

    def __init__(self, top: int = None, left: int = None, bottom: int = None, right: int = None):
        if all(s is None for s in [top, left, bottom, right]):
            raise ValueError("At least one side must be defined.")
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def __dict__(self):
        output = {}
        if self.top is not None:
            output['top'] = self.top
        if self.bottom is not None:
            output['bottom'] = self.bottom
        if self.left is not None:
            output['left'] = self.left
        if self.right is not None:
            output['right'] = self.right
        return output

    @staticmethod
    def all(all_sides: int):
        return ExtendedEdges(all_sides, all_sides, all_sides, all_sides)


ExtendedEdges.ZERO = ExtendedEdges(0, 0, 0, 0)


class Item:
    def __init__(self, inputs: [Input], frame: Rect, extended_edges: ExtendedEdges = None):
        self.inputs = inputs
        self.frame = frame
        self.extended_edges = extended_edges

    def __dict__(self):
        output = {
            "inputs": [i.value for i in self.inputs],
            "frame": self.frame.__dict__()
        }
        if self.extended_edges:
            output['extendedEdges'] = self.extended_edges.__dict__()
        return output

    class Dpad:
        def __init__(self, frame: Rect, extended_edges: ExtendedEdges = None, up: Input = Input.UP,
                     down: Input = Input.DOWN, left: Input = Input.LEFT, right: Input = Input.RIGHT):
            self.up = up
            self.down = down
            self.left = left
            self.right = right
            self.frame = frame
            self.extended_edges = extended_edges

        def __dict__(self):
            output = {
                'inputs': {
                    'up': self.up.value,
                    'down': self.down.value,
                    'left': self.left.value,
                    'right': self.right.value
                },
                'frame': self.frame.__dict__()
            }
            if self.extended_edges:
                output['extendedEdges'] = self.extended_edges.__dict__()
            return output

    class Thumbstick:
        def __init__(self, file_path: str, image_size: Size, frame: Rect, extended_edges: ExtendedEdges = None):
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            self.file_path = file_path
            self.file_name = os.path.basename(file_path)
            self.image_size = image_size
            self.up = 'analogStickUp'
            self.down = 'analogStickDown'
            self.left = 'analogStickLeft'
            self.right = 'analogStickRight'
            self.frame = frame
            self.extended_edges = extended_edges

        def __dict__(self):
            output = {
                'thumbstick': {
                    'name': self.file_name,
                    **self.image_size.__dict__()
                },
                'inputs': {
                    'up': self.up,
                    'down': self.down,
                    'left': self.left,
                    'right': self.right
                },
                'frame': self.frame.__dict__()
            }
            if self.extended_edges:
                output['extendedEdges'] = self.extended_edges.__dict__()
            return output


class Screen:
    def __init__(self, output_frame: Rect, input_frame: Rect = None):
        self.output_frame = output_frame
        self.input_frame = input_frame

    def __dict__(self):
        if self.input_frame:
            return {"inputFrame": self.input_frame.__dict__(), "outputFrame": self.output_frame.__dict__()}
        return {"outputFrame": self.output_frame.__dict__()}


class Representation:
    from .live_skin import LiveSkinItems

    def __init__(self, device: Device, display_type: DisplayType, orientation: Orientation, mapping_size: Size,
                 extended_edges: ExtendedEdges, translucent: bool = None):
        from .live_skin import LiveSkinItems
        # Edge to edge can only be used with iPhone
        if display_type == DisplayType.EDGE_TO_EDGE and device != Device.IPHONE:
            raise ValueError("Edge to edge can only be used with iPhone.")
        # Split view can only be used with iPad
        if display_type == DisplayType.SPLIT_VIEW and device != Device.IPAD:
            raise ValueError("Split view can only be used with iPad.")
        self.device = device
        self.display_type = display_type
        self.orientation = orientation
        self.__assets: [Asset] = []
        self.__items: [Item | Item.Dpad | Item.Thumbstick] = []
        self.__liveSkinItems: [LiveSkinItems] = []
        self.__screens = []
        self.mapping_size = mapping_size
        self.extended_edges = extended_edges
        self.translucent = translucent
        self.compatible_with_delta = True

    def __dict__(self):
        output = {
            'assets': {},
            'items': [],
            'mappingSize': self.mapping_size.__dict__(),
        }
        if self.extended_edges:
            output['extendedEdges'] = self.extended_edges.__dict__()
        if self.translucent is not None:
            output['translucent'] = self.translucent

        for i, asset in enumerate(self.__assets):
            output['assets'][asset.size.value] = asset.file_name

        for i, item in enumerate(self.__items):
            output['items'].append(item.__dict__())

        if self.__liveSkinItems:
            output['liveSkin'] = []
        for i, item in enumerate(self.__liveSkinItems):
            output['liveSkin'].append(item.__dict__())

        if self.__screens:
            output['screens'] = []
        for i, screen in enumerate(self.__screens):
            output['screens'].append(screen.__dict__())

        return output

    @property
    def assets(self):
        return self.__assets

    @property
    def items(self):
        return self.__items

    @property
    def live_skin_items(self):
        return self.__liveSkinItems

    @property
    def screens(self):
        return self.__screens

    def add_asset(self, asset: Asset):
        # self.assets can only contain either one resizable asset or multiple non-resizable assets, but not both
        if asset.size == AssetSize.RESIZABLE and any(a.size == AssetSize.RESIZABLE for a in self.__assets):
            raise ValueError("Only one resizable asset can be added to a representation.")
        elif asset.size != AssetSize.RESIZABLE and asset.size != AssetSize.PREVIEW and any(a.size == AssetSize.RESIZABLE for a in self.__assets):
            raise ValueError("Non-resizable assets cannot be added to a representation with a resizable asset.")
        self.__assets.append(asset)

    def add_item(self, item: Item | Item.Dpad | Item.Thumbstick):
        # Mark representation as incompatible with Delta if Ignited-specific inputs are used
        if isinstance(item, Item):
            if any(i in item.inputs for i in [Input.RESTART, Input.SCREENSHOT, Input.STATUS_BAR, Input.QUICK_SETTINGS,
                                              Input.TOGGLE_ALT_REPRESENTATION]):
                self.compatible_with_delta = False
        self.__items.append(item)

    def add_screen(self, screen: Screen):
        self.__screens.append(screen)

    def add_live_skin_item(self, item: LiveSkinItems):
        self.compatible_with_delta = False
        self.__liveSkinItems.append(item)



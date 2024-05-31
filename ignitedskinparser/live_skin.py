import os
import warnings
from abc import abstractmethod, ABC


class Color:
    def __init__(self, r: int, g: int, b: int, a: int = None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        r_hex = hex(self.r)[2:].zfill(2)
        g_hex = hex(self.g)[2:].zfill(2)
        b_hex = hex(self.b)[2:].zfill(2)
        if self.a is not None:
            a_hex = hex(self.a)[2:].zfill(2)
            return f"#{r_hex}{g_hex}{b_hex}{a_hex}"
        return f"#{r_hex}{g_hex}{b_hex}"


class Addresses(ABC):
    def __init__(self, address: int):
        self.address = address

    @abstractmethod
    def __str__(self):
        pass


class Address:
    class Standard(Addresses):
        def __init__(self, address: int):
            super().__init__(address)

        def __str__(self):
            return hex(self.address)

    class Pointer(Addresses):
        def __init__(self, address: int, offset: int):
            super().__init__(address)
            self.offset = offset

        def __str__(self):
            return f"*{hex(self.address)}+{self.offset}"


class BitInfo:
    def __init__(self, width: int, offset: int = 0):
        self.width = width
        self.offset = offset
        self.width_label = 'bitWidth'
        self.offset_label = 'bitOffset'

    def __dict__(self):
        if self.offset == 0:
            return {self.width_label: self.width}
        return {self.width_label: self.width, self.offset_label: self.offset}


class DecryptionMethods(ABC):
    @abstractmethod
    def __dict__(self):
        pass


class DecryptionMethod:
    class Xor(DecryptionMethods):
        def __init__(self, key_address: Addresses, key_bit_info: BitInfo):
            self.key_address = key_address
            self.key_bit_info = key_bit_info
            self.key_bit_info.width_label = 'keyBitWidth'
            self.key_bit_info.offset_label = 'keyBitOffset'

        def __dict__(self):
            return {
                "method": "xor",
                "keyAddress": str(self.key_address),
                **self.key_bit_info.__dict__()
            }

    class GBAPokemonParty(DecryptionMethods):
        def __init__(self, mon_address: Addresses, personality_address: Addresses, ot_id_address: Addresses):
            self.mon_address = mon_address
            self.personality_address = personality_address
            self.ot_id_address = ot_id_address

        def __dict__(self):
            return {
                "method": "gbaPokemonParty",
                "monAddress": str(self.mon_address),
                "personalityAddress": str(self.personality_address),
                "otIdAddress": str(self.ot_id_address)
            }


class LiveSkinItems(ABC):
    from .types import Rect

    def __init__(self, frame: Rect, decryption_method: DecryptionMethods | None = None):
        self.frame = frame
        self.decryption_method: DecryptionMethods | None = decryption_method
        self.kind = None

    def __dict__(self):
        if not self.kind:
            raise ValueError("The kind attribute must be set.")
        output = {
            "kind": self.kind,
            "frame": self.frame.__dict__(),
            "data": self.data_dict()
        }
        if self.decryption_method:
            output["decryptionMethod"] = self.decryption_method.__dict__()
        return output

    @abstractmethod
    def data_dict(self):
        pass


class Image(LiveSkinItems):
    from .types import Rect, Size

    def __init__(self, frame: Rect, file_path: str, address: Addresses, bit_info: BitInfo,
                 tiled_image_size: Size, decryption_method: DecryptionMethods | None = None):
        super().__init__(frame, decryption_method)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        # Make sure the image size is a multiple of tiled_image_size
        try:
            from PIL import Image
        except ImportError:
            warnings.warn("Pillow is not installed. Cannot verify image size.")
        else:
            image = Image.open(file_path)
            if image.size[0] % tiled_image_size.width != 0 and image.size[1] % tiled_image_size.height != 0:
                raise ValueError("The image size must be a multiple of the tiled image size.")
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.address = address
        self.bit_info = bit_info
        self.tiled_image_size = tiled_image_size
        self.kind = 'image'

    def data_dict(self):
        return {
            "address": str(self.address),
            **self.bit_info.__dict__(),
            "filename": self.file_name,
            "size": self.tiled_image_size.__dict__()
        }


class CircularHP(LiveSkinItems):
    from .types import Rect

    def __init__(self, frame: Rect, hp_address: Addresses, hp_bit_info: BitInfo, hp_max_address: Addresses,
                 hp_max_bit_info: BitInfo, colors: [Color], decryption_method: DecryptionMethods | None = None):
        super().__init__(frame, decryption_method)
        if hp_bit_info.width != hp_max_bit_info.width:
            raise ValueError("The width of the HP and HP Max bit info must be the same.")
        self.hp_address = hp_address
        self.hp_bit_info = hp_bit_info
        self.hp_max_address = hp_max_address
        self.hp_max_bit_info = hp_max_bit_info
        if len(colors) > 3:
            raise ValueError("There can be no more than 3 colors in a CircularHP item.")
        if len(colors) < 1:
            raise ValueError("There must be at least 1 color in a CircularHP item.")
        while len(colors) < 3:
            colors.append(colors[-1])
        self.colors = colors
        self.kind = 'circularHP'

    def data_dict(self):
        return {
            "hpAddress": str(self.hp_address),
            "hpMaxAddress": str(self.hp_max_address),
            "bitWidth": self.hp_bit_info.width,
            "hpBitOffset": self.hp_bit_info.offset,
            "hpMaxBitOffset": self.hp_max_bit_info.offset,
            "colors": {
                "full": str(self.colors[0]),
                "half": str(self.colors[1]),
                "quarter": str(self.colors[2])
            }
        }


class RectangularHP(LiveSkinItems):
    from .types import Rect

    def __init__(self, frame: Rect, hp_address: Addresses, hp_bit_info: BitInfo, hp_max_address: Addresses,
                 hp_max_bit_info: BitInfo, colors: [Color], decryption_method: DecryptionMethods | None = None):
        super().__init__(frame, decryption_method)
        self.hp_address = hp_address
        self.hp_bit_info = hp_bit_info
        self.hp_max_address = hp_max_address
        self.hp_max_bit_info = hp_max_bit_info
        if len(colors) > 3:
            raise ValueError("There can be no more than 3 colors in a RectangularHP item.")
        if len(colors) < 1:
            raise ValueError("There must be at least 1 color in a RectangularHP item.")
        while len(colors) < 3:
            colors.append(colors[-1])
        self.colors = colors
        self.kind = 'rectangularHP'

    def data_dict(self):
        return {
            "hpAddress": str(self.hp_address),
            "hpMaxAddress": str(self.hp_max_address),
            "bitWidth": self.hp_bit_info.width,
            "hpBitOffset": self.hp_bit_info.offset,
            "hpMaxBitOffset": self.hp_max_bit_info.offset,
            "colors": {
                "full": str(self.colors[0]),
                "half": str(self.colors[1]),
                "quarter": str(self.colors[2])
            }
        }


class Number(LiveSkinItems):
    from .types import Rect

    def __init__(self, frame: Rect, address: Addresses, bit_info: BitInfo, font_size: float, font_color: Color,
                 font_name: str = None, decryption_method: DecryptionMethods | None = None):
        super().__init__(frame, decryption_method)
        self.address = address
        self.bit_info = bit_info
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.kind = 'number'

    def data_dict(self):
        output = {
            "address": str(self.address),
            **self.bit_info.__dict__(),
            "fontSize": self.font_size,
            "color": str(self.font_color)
        }
        if self.font_name:
            output["fontName"] = self.font_name
        return output


class Text(LiveSkinItems):
    from .types import Rect

    def __init__(self, frame: Rect, address: Addresses, bit_info: BitInfo, font_size: float, font_color: Color,
                 char_map: [str], font_name: str = None, decryption_method: DecryptionMethods | None = None):
        super().__init__(frame, decryption_method)
        self.address = address
        self.bit_info = bit_info
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.char_map = char_map
        self.kind = 'text'

    def data_dict(self):
        output = {
            "address": str(self.address),
            **self.bit_info.__dict__(),
            "fontSize": self.font_size,
            "color": str(self.font_color),
            "charmap": self.char_map
        }
        if self.font_name:
            output["fontName"] = self.font_name
        return output


class IndexedText(LiveSkinItems):
    from .types import Rect

    """
    This class is used for text that is indexed by a value in memory. For example, a Pokemon's species ID
    could be used to index a list of species names.
    """
    def __init__(self, frame: Rect, address: Addresses, bit_info: BitInfo, font_size: float, font_color: Color,
                 text: [str], font_name: str = None, decryption_method: DecryptionMethods | None = None):
        super().__init__(frame, decryption_method)
        self.address = address
        self.bit_info = bit_info
        self.font_size = font_size
        self.font_color = font_color
        self.font_name = font_name
        self.text = text
        self.kind = 'indexedText'

    def data_dict(self):
        output = {
            "address": str(self.address),
            **self.bit_info.__dict__(),
            "fontSize": self.font_size,
            "color": str(self.font_color),
            "text": self.text
        }
        if self.font_name:
            output["fontName"] = self.font_name
        return output


class Battery(LiveSkinItems):
    from .types import Rect

    def __init__(self, frame: Rect, unplugged_file_path: str, unplugged_low_file_path: str, charging_file_path: str,
                 charging_low_file_path: str):
        """
        This class is used to represent the battery indicator of a device (e.g. the LEDs on a Game Boy Advance SP). The
        battery indicator can have 4 states: unplugged, unplugged with low battery, charging, and charging with low
        battery. Each state has an associated image.
        :param frame: The position and size of the battery images on the screen.
        :param unplugged_file_path: The file path to the image of the battery when the device is not charging.
        :param unplugged_low_file_path: The file path to the image of the battery when the device is not charging and the battery is low.
        :param charging_file_path The file path to the image of the battery when the device is charging.
        :param charging_low_file_path: The file path to the image of the battery when the device is charging and the battery is low.
        """
        super().__init__(frame)
        if not os.path.exists(unplugged_file_path):
            raise FileNotFoundError(f"The file {unplugged_file_path} does not exist.")
        if not os.path.exists(unplugged_low_file_path):
            raise FileNotFoundError(f"The file {unplugged_low_file_path} does not exist.")
        if not os.path.exists(charging_file_path):
            raise FileNotFoundError(f"The file {charging_file_path} does not exist.")
        if not os.path.exists(charging_low_file_path):
            raise FileNotFoundError(f"The file {charging_low_file_path} does not exist.")
        # Make sure all images are the same size
        try:
            from PIL import Image
        except ImportError:
            warnings.warn("Pillow is not installed. Cannot verify image size.")
        else:
            unplugged_image = Image.open(unplugged_file_path)
            unplugged_low_image = Image.open(unplugged_low_file_path)
            charging_image = Image.open(charging_file_path)
            charging_low_image = Image.open(charging_low_file_path)
            if unplugged_image.size != unplugged_low_image.size or unplugged_image.size != charging_image.size or \
                    unplugged_image.size != charging_low_image.size:
                raise ValueError("All battery images must be the same size.")

        self.unplugged_file_path = unplugged_file_path
        self.unplugged_file_name = os.path.basename(unplugged_file_path)
        self.unplugged_low_file_path = unplugged_low_file_path
        self.unplugged_low_file_name = os.path.basename(unplugged_low_file_path)
        self.charging_file_path = charging_file_path
        self.charging_file_name = os.path.basename(charging_file_path)
        self.charging_low_file_path = charging_low_file_path
        self.charging_low_file_name = os.path.basename(charging_low_file_path)
        self.kind = 'battery'

    def data_dict(self):
        return {
            "unplugged": self.unplugged_file_name,
            "unplugged-low": self.unplugged_low_file_name,
            "charging": self.charging_file_name,
            "charging-low": self.charging_low_file_name
        }

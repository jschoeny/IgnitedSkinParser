import json
import zipfile
from zipfile import ZipFile

from .types import Representation, Device, DisplayType, Orientation, Item
from .enums import GameTypeIdentifier


class DeltaSkin:
    def __init__(self, name, identifier, game_type_identifier: GameTypeIdentifier, debug=False,
                 allow_ignited_elements=False):
        self.name = name
        self.identifier = identifier
        self.game_type_identifier = game_type_identifier
        self.debug = debug
        self.representations: [Representation] = []
        self.__allow_ignited_elements = allow_ignited_elements

    def __check_for_representation_duplicates(self, representation: Representation):
        for rep in self.representations:
            if rep.device == representation.device and rep.display_type == representation.display_type and rep.orientation == representation.orientation:
                raise ValueError(f"Representation for device {rep.device}, display type {rep.display_type}, and orientation {rep.orientation} already exists.")

    def add_representation(self, representation: Representation):
        # Ensure the representation is unique (by device, display type, and orientation)
        self.__check_for_representation_duplicates(representation)
        if not representation.compatible_with_delta and not self.__allow_ignited_elements:
            raise ValueError("Representation is not compatible with Delta.")
        self.representations.append(representation)

    def generate_json(self):
        # Print a warning if not all representations are compatible with Delta
        for rep in self.representations:
            if not rep.compatible_with_delta:
                print(f"Warning: Representation for device {rep.device}, display type {rep.display_type}, "
                      f"and orientation {rep.orientation} contains element(s) not compatible with Delta.")

        output = {
            'name': self.name,
            'identifier': self.identifier,
            'gameTypeIdentifier': self.game_type_identifier.value,
            'debug': self.debug,
            'representations': {}
        }

        for i, rep in enumerate(self.representations):
            device: Device = rep.device
            display_type: DisplayType = rep.display_type
            orientation: Orientation = rep.orientation
            if device.value not in output['representations']:
                output['representations'][device.value] = {}
            if display_type.value not in output['representations'][device.value]:
                output['representations'][device.value][display_type.value] = {}
            output['representations'][device.value][display_type.value][orientation.value] = rep.__dict__()

        return json.dumps(output, indent=2)

    def save(self, path, compress=False):
        from .live_skin import Image

        if not path.endswith('.deltaskin'):
            raise ValueError("The path must end with '.deltaskin'")

        # Generate the info.json file
        info_json = self.generate_json()

        # Make a zip archive of the skin
        compression = zipfile.ZIP_DEFLATED if compress else zipfile.ZIP_STORED
        comp_level = 9 if compress else None
        with ZipFile(path, 'w', compression=compression, compresslevel=comp_level) as zipf:
            zipf.writestr('info.json', info_json)
            files = {}
            for rep in self.representations:
                for asset in rep.assets:
                    if asset.file_name in files and files[asset.file_name] != asset.file_path:
                        raise ValueError(f"File {asset.file_name} already exists in the skin.\n"
                                         f"Duplicate names for {files[asset.file_name]} and {asset.file_path}")
                    files[asset.file_name] = asset.file_path
                for item in rep.items:
                    if isinstance(item, Item.Thumbstick):
                        if item.file_name in files and files[item.file_name] != item.file_path:
                            raise ValueError(f"File {item.file_name} already exists in the skin.\n"
                                             f"Duplicate names for {files[item.file_name]} and {item.file_path}")
                        files[item.file_name] = item.file_path
                for item in rep.live_skin_items:
                    if isinstance(item, Image):
                        if item.file_name in files and files[item.file_name] != item.file_path:
                            raise ValueError(f"File {item.file_name} already exists in the skin.\n"
                                             f"Duplicate names for {files[item.file_name]} and {item.file_path}")
                        files[item.file_name] = item.file_path
            for file_name, file_path in files.items():
                zipf.write(file_path, file_name)

        return zipf.filename


class IgnitedSkin(DeltaSkin):
    def __init__(self, name, identifier, game_type_identifier: GameTypeIdentifier, debug=False):
        super().__init__(name, identifier, game_type_identifier, debug, allow_ignited_elements=True)
        self.alt_representation: [Representation] = []

    def __check_for_alt_representation_duplicates(self, representation: Representation):
        for rep in self.alt_representation:
            if rep.device == representation.device and rep.display_type == representation.display_type and rep.orientation == representation.orientation:
                raise ValueError(f"Alt representation for device {rep.device}, display type {rep.display_type}, and orientation {rep.orientation} already exists.")

    def add_alt_representation(self, representation: Representation):
        # Ensure the representation is unique (by device, display type, and orientation)
        self.__check_for_alt_representation_duplicates(representation)
        self.alt_representation.append(representation)

    def generate_json(self):
        output = {
            'name': self.name,
            'identifier': self.identifier,
            'gameTypeIdentifier': self.game_type_identifier.value,
            'debug': self.debug,
            'representations': {}
        }

        for i, rep in enumerate(self.representations):
            device: Device = rep.device
            display_type: DisplayType = rep.display_type
            orientation: Orientation = rep.orientation
            if device.value not in output['representations']:
                output['representations'][device.value] = {}
            if display_type.value not in output['representations'][device.value]:
                output['representations'][device.value][display_type.value] = {}
            output['representations'][device.value][display_type.value][orientation.value] = rep.__dict__()

        if self.alt_representation:
            output['altRepresentations'] = {}
            for i, rep in enumerate(self.alt_representation):
                device: Device = rep.device
                display_type: DisplayType = rep.display_type
                orientation: Orientation = rep.orientation
                if device.value not in output['altRepresentations']:
                    output['altRepresentations'][device.value] = {}
                if display_type.value not in output['altRepresentations'][device.value]:
                    output['altRepresentations'][device.value][display_type.value] = {}
                output['altRepresentations'][device.value][display_type.value][orientation.value] = rep.__dict__()

        return json.dumps(output, indent=2)

    def save(self, path, compress=False):
        from .live_skin import Image

        if not path.endswith('.ignitedskin'):
            raise ValueError("The path must end with '.ignitedskin'")

        # Generate the info.json file
        info_json = self.generate_json()

        # Make a zip archive of the skin
        compression = zipfile.ZIP_DEFLATED if compress else zipfile.ZIP_STORED
        comp_level = 9 if compress else None
        with ZipFile(path, 'w', compression=compression, compresslevel=comp_level) as zipf:
            zipf.writestr('info.json', info_json)
            all_reps = self.representations + self.alt_representation
            files = {}
            for rep in all_reps:
                for asset in rep.assets:
                    if asset.file_name in files and files[asset.file_name] != asset.file_path:
                        raise ValueError(f"File {asset.file_name} already exists in the skin.\n"
                                         f"Duplicate names for {files[asset.file_name]} and {asset.file_path}")
                    files[asset.file_name] = asset.file_path
                for item in rep.items:
                    if isinstance(item, Item.Thumbstick):
                        if item.file_name in files and files[item.file_name] != item.file_path:
                            raise ValueError(f"File {item.file_name} already exists in the skin.\n"
                                             f"Duplicate names for {files[item.file_name]} and {item.file_path}")
                        files[item.file_name] = item.file_path
                for item in rep.live_skin_items:
                    if isinstance(item, Image):
                        if item.file_name in files and files[item.file_name] != item.file_path:
                            raise ValueError(f"File {item.file_name} already exists in the skin.\n"
                                             f"Duplicate names for {files[item.file_name]} and {item.file_path}")
                        files[item.file_name] = item.file_path
            for file_name, file_path in files.items():
                zipf.write(file_path, file_name)

        return zipf.filename

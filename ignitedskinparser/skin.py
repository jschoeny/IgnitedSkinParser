import json
from zipfile import ZipFile

from .types import *


class IgnitedSkin:
    def __init__(self, name, identifier, game_type_identifier: GameTypeIdentifier, debug=False):
        self.name = name
        self.identifier = identifier
        self.game_type_identifier = game_type_identifier
        self.debug = debug
        self.representations: [Representation] = []
        self.alt_representation: [Representation] = []

    def add_representation(self, representation: Representation):
        # Ensure the representation is unique (by device, display type, and orientation)
        for rep in self.representations:
            if rep.device == representation.device and rep.display_type == representation.display_type and rep.orientation == representation.orientation:
                raise ValueError(f"Representation for device {rep.device}, display type {rep.display_type}, and orientation {rep.orientation} already exists.")
        self.representations.append(representation)

    def add_alt_representation(self, representation: Representation):
        # Ensure the representation is unique (by device, display type, and orientation)
        for rep in self.alt_representation:
            if rep.device == representation.device and rep.display_type == representation.display_type and rep.orientation == representation.orientation:
                raise ValueError(f"Representation for device {rep.device}, display type {rep.display_type}, and orientation {rep.orientation} already exists.")
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

    def save(self, path):
        from .live_skin import LiveSkinItem

        if not path.endswith('.ignitedskin'):
            raise ValueError("The path must end with '.ignitedskin'")

        # Generate the info.json file
        info_json = self.generate_json()

        # Make a zip archive of the skin
        with ZipFile(path, 'w') as zipf:
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
                    if isinstance(item, LiveSkinItem.Image):
                        if item.file_name in files and files[item.file_name] != item.file_path:
                            raise ValueError(f"File {item.file_name} already exists in the skin.\n"
                                             f"Duplicate names for {files[item.file_name]} and {item.file_path}")
                        files[item.file_name] = item.file_path
            for file_name, file_path in files.items():
                zipf.write(file_path, file_name)


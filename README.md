# IgnitedSkinParser

[![Python version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![GitHub license](https://img.shields.io/github/license/jschoeny/ignitedskinparser)](LICENSE.md)
[![GitHub issues](https://img.shields.io/github/issues/jschoeny/ignitedskinparser)](https://github.com/jschoeny/ignitedskinparser/issues)


IgnitedSkinParser is a Python package designed to simplify the creation of custom controller skins for the Ignited emulator app. It provides built-in error checking, easy configuration, and the ability to export to a `.ignitedskin` file.

## Features

- **Error Checking**: Ensures unique representations and prevents conflicting file names. Also makes sure some types are used properly.
- **Flexible Configuration**: As versatile as working with the info.json file, but without all the debugging headaches.
- **Comprehensive Skin Definition**: Has everything you need to make an Ignited skin, including assets, items, representations, and LiveSkins.

*Note: LiveSkins are not yet supported in Ignited, but hopefully will be at a later date.*

## Installation

*Eventually I might get around to uploading this to PyPI, but for now...*

To use IgnitedSkinParser, clone the repository and create a new Python file in the root directory. This file will hold your custom skin configuration.

Import the package in your Python file:

```python
import ignitedskinparser as isp
```

...and you're ready to start creating your custom skin!

## Usage

### Creating a Skin

1. **Initialize Skin**: Declare an `IgnitedSkin` to hold all information about your skin. Must specify a name, identifier, and the game console.
2. **Create Representations**: Create a `Representation` for different devices, display types, and orientations.
3. **Add Assets**: Add the background image of your skin to the `Representation` using `.add_asset()`.
4. **Add Items**: Add the controller inputs to your `Representation` using `.add_item()`.
5. **Add Representation to Skin**: Once your `Representation` is set up properly, use `.add_representation()` to add it to your `IgnitedSkin`. For alt representations, use `.add_alt_representation()`.
6. **Export**: Once you have finished and added all of your representations, call `.save()` on your `IgnitedSkin` to create your `.ignitedskin` file.

### Example

Below is an example of how to create a standard portrait representation for an iPhone device:

```python
import ignitedskinparser as isp

# Initialize the skin
skin = isp.IgnitedSkin(
    name="My Custom Skin",
    identifier="com.example.myskin",
    game_type_identifier=isp.GameTypeIdentifier.N64
)

# Define the items
thumbstick = isp.Item.Thumbstick(
    file_path="assets/portrait_thumbstick.pdf",
    image_size=isp.Size(width=85, height=87),
    frame=isp.Rect(x=39, y=77, width=71, height=71),
    extended_edges=isp.ExtendedEdges.all(20),
)
dpad = isp.Item.Dpad(
    frame=isp.Rect(x=17, y=195, width=120, height=120),
    extended_edges=isp.ExtendedEdges(top=15, left=17, bottom=15, right=7)
)
a = isp.Item(
    inputs=[isp.Input.A],
    frame=isp.Rect(x=247, y=122, width=56, height=56),
    extended_edges=isp.ExtendedEdges(right=17, top=15)
)
# Define other items...

# Create a representation
rep = isp.Representation(
    device=isp.Device.IPHONE,
    display_type=isp.DisplayType.STANDARD,
    orientation=isp.Orientation.PORTRAIT,
    mapping_size=isp.Size(width=320, height=480),
    extended_edges=isp.ExtendedEdges.all(7)
)
rep.add_asset(isp.Asset('assets/iphone_portrait.pdf', isp.AssetSize.RESIZABLE))
rep.add_item(thumbstick)
rep.add_item(dpad)
rep.add_item(a)
# Add other items...

# Add the representation to the skin
skin.add_representation(rep)

# Save the skin
skin.save("my_custom_skin.ignitedskin")
```

You can also find a full example under [samples](samples).

### Contribution

Feel free to contribute to the project by submitting [issues](https://github.com/jschoeny/ignitedskinparser/issues) or [pull requests](https://github.com/jschoeny/ignitedskinparser/pulls).

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

---
For more information on the components of Delta/Ignited skins, check out this [skin documentation](https://noah978.gitbook.io/delta-docs/skins).

For more information on the Ignited app, visit the [official website](https://litritt.com/ignited).

---

Happy skinning! 🎮

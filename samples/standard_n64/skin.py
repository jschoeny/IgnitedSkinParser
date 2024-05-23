import ignitedskinparser.skin as skin
import rep_iphone as iphone
import rep_ipad as ipad

# The export of this skin is equivalent to the standard N64 skin found in Delta
# https://github.com/rileytestut/NESDeltaCore/tree/master/NESDeltaCore/Controller%20Skin

if __name__ == "__main__":
    # Initialize the skin
    my_skin = skin.IgnitedSkin(
        "Standard N64",
        "com.delta.n64.standard",
        skin.GameTypeIdentifier.N64
    )

    # Add the iPhone representations (defined in rep_iphone.py)
    my_skin.add_representation(iphone.standard_portrait())
    my_skin.add_representation(iphone.edgetoedge_portrait())
    my_skin.add_representation(iphone.standard_landscape())
    my_skin.add_representation(iphone.edgetoedge_landscape())

    # Add the iPad representations (defined in rep_ipad.py)
    my_skin.add_representation(ipad.standard_portrait())
    my_skin.add_representation(ipad.splitview_portrait())
    my_skin.add_representation(ipad.standard_landscape())
    my_skin.add_representation(ipad.splitview_landscape())

    # Export the skin
    path = my_skin.save("standard_n64.ignitedskin", compress=True)
    print(f"Skin exported to {path}")

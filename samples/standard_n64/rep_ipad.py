import ignitedskinparser.skin as skin


class PortraitItems:
    thumbstick = skin.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=skin.Size(94, 94),
        frame=skin.Rect(18, 100, 150, 150),
        extended_edges=skin.ExtendedEdges.all(25),
    )
    dpad = skin.Item.Dpad(
        frame=skin.Rect(19, 286, 145, 145),
        extended_edges=skin.ExtendedEdges(top=10)
    )
    a = skin.Item(
        inputs=[skin.Input.A],
        frame=skin.Rect(717, 189, 67, 67),
        extended_edges=skin.ExtendedEdges(top=10, left=10)
    )
    b = skin.Item(
        inputs=[skin.Input.B],
        frame=skin.Rect(626, 160, 67, 67),
        extended_edges=skin.ExtendedEdges(top=10, right=10)
    )
    z = skin.Item(
        inputs=[skin.Input.Z],
        frame=skin.Rect(696, 103, 67, 67),
        extended_edges=skin.ExtendedEdges(bottom=10, left=10)
    )
    l = skin.Item(
        inputs=[skin.Input.L],
        frame=skin.Rect(18, 18, 120, 48),
        extended_edges=skin.ExtendedEdges(bottom=10)
    )
    r = skin.Item(
        inputs=[skin.Input.R],
        frame=skin.Rect(663, 18, 120, 48)
    )
    start = skin.Item(
        inputs=[skin.Input.START],
        frame=skin.Rect(356, 401, 88, 31)
    )
    menu = skin.Item(
        inputs=[skin.Input.MENU],
        frame=skin.Rect(356, 18, 88, 31)
    )
    c_u = skin.Item(
        inputs=[skin.Input.C_UP],
        frame=skin.Rect(691, 296, 47, 47),
        extended_edges=skin.ExtendedEdges(bottom=0, left=10, right=10)
    )
    c_d = skin.Item(
        inputs=[skin.Input.C_DOWN],
        frame=skin.Rect(691, 385, 47, 47),
        extended_edges=skin.ExtendedEdges(top=0, left=10, right=10)
    )
    c_l = skin.Item(
        inputs=[skin.Input.C_LEFT],
        frame=skin.Rect(646, 340, 47, 47),
        extended_edges=skin.ExtendedEdges(top=10, bottom=10, right=0)
    )
    c_r = skin.Item(
        inputs=[skin.Input.C_RIGHT],
        frame=skin.Rect(735, 340, 47, 47),
        extended_edges=skin.ExtendedEdges(top=10, bottom=10, left=0)
    )


def standard_portrait() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPAD,
        orientation=skin.Orientation.PORTRAIT,
        display_type=skin.DisplayType.STANDARD,
        mapping_size=skin.Size(800, 550),
        extended_edges=skin.ExtendedEdges.all(20)
    )
    rep.add_asset(skin.Asset('assets/ipad_portrait.pdf', skin.AssetSize.RESIZABLE))

    rep.add_item(PortraitItems.thumbstick)
    rep.add_item(PortraitItems.dpad)
    rep.add_item(PortraitItems.a)
    rep.add_item(PortraitItems.b)
    rep.add_item(PortraitItems.z)
    rep.add_item(PortraitItems.l)
    rep.add_item(PortraitItems.r)
    rep.add_item(PortraitItems.start)
    rep.add_item(PortraitItems.menu)
    rep.add_item(PortraitItems.c_u)
    rep.add_item(PortraitItems.c_d)
    rep.add_item(PortraitItems.c_l)
    rep.add_item(PortraitItems.c_r)

    return rep


def splitview_portrait() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPAD,
        orientation=skin.Orientation.PORTRAIT,
        display_type=skin.DisplayType.SPLIT_VIEW,
        mapping_size=skin.Size(800, 550),
        extended_edges=skin.ExtendedEdges.all(20)
    )
    rep.add_asset(skin.Asset('assets/ipad_portrait.pdf', skin.AssetSize.RESIZABLE))

    rep.add_item(PortraitItems.thumbstick)
    rep.add_item(PortraitItems.dpad)
    rep.add_item(PortraitItems.a)
    rep.add_item(PortraitItems.b)
    rep.add_item(PortraitItems.z)
    rep.add_item(PortraitItems.l)
    rep.add_item(PortraitItems.r)
    rep.add_item(PortraitItems.start)
    rep.add_item(PortraitItems.menu)
    rep.add_item(PortraitItems.c_u)
    rep.add_item(PortraitItems.c_d)
    rep.add_item(PortraitItems.c_l)
    rep.add_item(PortraitItems.c_r)

    return rep


def standard_landscape() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPAD,
        orientation=skin.Orientation.LANDSCAPE,
        display_type=skin.DisplayType.STANDARD,
        mapping_size=skin.Size(1024, 768),
        extended_edges=skin.ExtendedEdges.all(20),
        translucent=True
    )
    rep.add_asset(skin.Asset('assets/ipad_landscape.pdf', skin.AssetSize.RESIZABLE))

    rep.add_item(skin.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=skin.Size(94, 94),
        frame=skin.Rect(18, 419, 150, 150),
        extended_edges=skin.ExtendedEdges.all(25)
    ))
    rep.add_item(skin.Item.Dpad(
        frame=skin.Rect(19, 604, 145, 145),
        extended_edges=skin.ExtendedEdges(top=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.A],
        frame=skin.Rect(941, 507, 67, 67),
        extended_edges=skin.ExtendedEdges(top=10, left=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.B],
        frame=skin.Rect(850, 478, 67, 67),
        extended_edges=skin.ExtendedEdges(top=10, right=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.Z],
        frame=skin.Rect(920, 421, 67, 67),
        extended_edges=skin.ExtendedEdges(bottom=10, left=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.L],
        frame=skin.Rect(18, 336, 120, 48),
        extended_edges=skin.ExtendedEdges(bottom=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.R],
        frame=skin.Rect(887, 336, 120, 48),
        extended_edges=skin.ExtendedEdges(bottom=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.START],
        frame=skin.Rect(470, 721, 85, 29)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.MENU],
        frame=skin.Rect(469, 18, 88, 31)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_UP],
        frame=skin.Rect(915, 614, 47, 47),
        extended_edges=skin.ExtendedEdges(bottom=0, left=10, right=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_DOWN],
        frame=skin.Rect(915, 703, 47, 47),
        extended_edges=skin.ExtendedEdges(top=0, left=10, right=10)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_LEFT],
        frame=skin.Rect(870, 658, 47, 47),
        extended_edges=skin.ExtendedEdges(top=10, bottom=10, right=0)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_RIGHT],
        frame=skin.Rect(959, 658, 47, 47),
        extended_edges=skin.ExtendedEdges(top=10, bottom=10, left=0)
    ))

    return rep


def splitview_landscape() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPAD,
        orientation=skin.Orientation.LANDSCAPE,
        display_type=skin.DisplayType.SPLIT_VIEW,
        mapping_size=skin.Size(1024, 450),
        extended_edges=skin.ExtendedEdges.all(20),
        translucent=False
    )
    rep.add_asset(skin.Asset('assets/ipad_splitview_landscape.pdf', skin.AssetSize.RESIZABLE))

    rep.add_item(skin.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=skin.Size(94, 94),
        frame=skin.Rect(17, 102, 150, 150),
        extended_edges=skin.ExtendedEdges(top=25, bottom=25, left=25, right=25),
    ))
    rep.add_item(skin.Item.Dpad(
        frame=skin.Rect(17, 285, 150, 145),
        extended_edges=skin.ExtendedEdges(top=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.A],
        frame=skin.Rect(938, 187, 71, 67),
        extended_edges=skin.ExtendedEdges(top=10, left=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.B],
        frame=skin.Rect(848, 158, 71, 67),
        extended_edges=skin.ExtendedEdges(top=10, right=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.Z],
        frame=skin.Rect(919, 100, 71, 67),
        extended_edges=skin.ExtendedEdges(bottom=10, left=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.L],
        frame=skin.Rect(17, 18, 121, 48),
        extended_edges=skin.ExtendedEdges(bottom=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.R],
        frame=skin.Rect(886, 18, 121, 48),
        extended_edges=skin.ExtendedEdges(bottom=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.START],
        frame=skin.Rect(469, 401, 86, 32)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.MENU],
        frame=skin.Rect(469, 17, 86, 31)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_UP],
        frame=skin.Rect(909, 294, 58, 47),
        extended_edges=skin.ExtendedEdges(bottom=0, left=10, right=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_DOWN],
        frame=skin.Rect(909, 384, 58, 47),
        extended_edges=skin.ExtendedEdges(top=0, left=10, right=10),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_LEFT],
        frame=skin.Rect(864, 339, 58, 47),
        extended_edges=skin.ExtendedEdges(top=10, bottom=10, right=0),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_RIGHT],
        frame=skin.Rect(955, 339, 58, 47),
        extended_edges=skin.ExtendedEdges(top=10, bottom=10, left=0),
    ))

    return rep

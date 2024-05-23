import ignitedskinparser as isp


class PortraitItems:
    thumbstick = isp.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=isp.Size(94, 94),
        frame=isp.Rect(18, 100, 150, 150),
        extended_edges=isp.ExtendedEdges.all(25),
    )
    dpad = isp.Item.Dpad(
        frame=isp.Rect(19, 286, 145, 145),
        extended_edges=isp.ExtendedEdges(top=10)
    )
    a = isp.Item(
        inputs=[isp.Input.A],
        frame=isp.Rect(717, 189, 67, 67),
        extended_edges=isp.ExtendedEdges(top=10, left=10)
    )
    b = isp.Item(
        inputs=[isp.Input.B],
        frame=isp.Rect(626, 160, 67, 67),
        extended_edges=isp.ExtendedEdges(top=10, right=10)
    )
    z = isp.Item(
        inputs=[isp.Input.Z],
        frame=isp.Rect(696, 103, 67, 67),
        extended_edges=isp.ExtendedEdges(bottom=10, left=10)
    )
    l = isp.Item(
        inputs=[isp.Input.L],
        frame=isp.Rect(18, 18, 120, 48),
        extended_edges=isp.ExtendedEdges(bottom=10)
    )
    r = isp.Item(
        inputs=[isp.Input.R],
        frame=isp.Rect(663, 18, 120, 48)
    )
    start = isp.Item(
        inputs=[isp.Input.START],
        frame=isp.Rect(356, 401, 88, 31)
    )
    menu = isp.Item(
        inputs=[isp.Input.MENU],
        frame=isp.Rect(356, 18, 88, 31)
    )
    c_u = isp.Item(
        inputs=[isp.Input.C_UP],
        frame=isp.Rect(691, 296, 47, 47),
        extended_edges=isp.ExtendedEdges(bottom=0, left=10, right=10)
    )
    c_d = isp.Item(
        inputs=[isp.Input.C_DOWN],
        frame=isp.Rect(691, 385, 47, 47),
        extended_edges=isp.ExtendedEdges(top=0, left=10, right=10)
    )
    c_l = isp.Item(
        inputs=[isp.Input.C_LEFT],
        frame=isp.Rect(646, 340, 47, 47),
        extended_edges=isp.ExtendedEdges(top=10, bottom=10, right=0)
    )
    c_r = isp.Item(
        inputs=[isp.Input.C_RIGHT],
        frame=isp.Rect(735, 340, 47, 47),
        extended_edges=isp.ExtendedEdges(top=10, bottom=10, left=0)
    )


def standard_portrait() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPAD,
        orientation=isp.Orientation.PORTRAIT,
        display_type=isp.DisplayType.STANDARD,
        mapping_size=isp.Size(800, 550),
        extended_edges=isp.ExtendedEdges.all(20)
    )
    rep.add_asset(isp.Asset('assets/ipad_portrait.pdf', isp.AssetSize.RESIZABLE))

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


def splitview_portrait() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPAD,
        orientation=isp.Orientation.PORTRAIT,
        display_type=isp.DisplayType.SPLIT_VIEW,
        mapping_size=isp.Size(800, 550),
        extended_edges=isp.ExtendedEdges.all(20)
    )
    rep.add_asset(isp.Asset('assets/ipad_portrait.pdf', isp.AssetSize.RESIZABLE))

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


def standard_landscape() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPAD,
        orientation=isp.Orientation.LANDSCAPE,
        display_type=isp.DisplayType.STANDARD,
        mapping_size=isp.Size(1024, 768),
        extended_edges=isp.ExtendedEdges.all(20),
        translucent=True
    )
    rep.add_asset(isp.Asset('assets/ipad_landscape.pdf', isp.AssetSize.RESIZABLE))

    rep.add_item(isp.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=isp.Size(94, 94),
        frame=isp.Rect(18, 419, 150, 150),
        extended_edges=isp.ExtendedEdges.all(25)
    ))
    rep.add_item(isp.Item.Dpad(
        frame=isp.Rect(19, 604, 145, 145),
        extended_edges=isp.ExtendedEdges(top=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.A],
        frame=isp.Rect(941, 507, 67, 67),
        extended_edges=isp.ExtendedEdges(top=10, left=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.B],
        frame=isp.Rect(850, 478, 67, 67),
        extended_edges=isp.ExtendedEdges(top=10, right=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.Z],
        frame=isp.Rect(920, 421, 67, 67),
        extended_edges=isp.ExtendedEdges(bottom=10, left=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.L],
        frame=isp.Rect(18, 336, 120, 48),
        extended_edges=isp.ExtendedEdges(bottom=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.R],
        frame=isp.Rect(887, 336, 120, 48),
        extended_edges=isp.ExtendedEdges(bottom=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.START],
        frame=isp.Rect(470, 721, 85, 29)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.MENU],
        frame=isp.Rect(469, 18, 88, 31)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_UP],
        frame=isp.Rect(915, 614, 47, 47),
        extended_edges=isp.ExtendedEdges(bottom=0, left=10, right=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_DOWN],
        frame=isp.Rect(915, 703, 47, 47),
        extended_edges=isp.ExtendedEdges(top=0, left=10, right=10)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_LEFT],
        frame=isp.Rect(870, 658, 47, 47),
        extended_edges=isp.ExtendedEdges(top=10, bottom=10, right=0)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_RIGHT],
        frame=isp.Rect(959, 658, 47, 47),
        extended_edges=isp.ExtendedEdges(top=10, bottom=10, left=0)
    ))

    return rep


def splitview_landscape() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPAD,
        orientation=isp.Orientation.LANDSCAPE,
        display_type=isp.DisplayType.SPLIT_VIEW,
        mapping_size=isp.Size(1024, 450),
        extended_edges=isp.ExtendedEdges.all(20),
        translucent=False
    )
    rep.add_asset(isp.Asset('assets/ipad_splitview_landscape.pdf', isp.AssetSize.RESIZABLE))

    rep.add_item(isp.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=isp.Size(94, 94),
        frame=isp.Rect(17, 102, 150, 150),
        extended_edges=isp.ExtendedEdges(top=25, bottom=25, left=25, right=25),
    ))
    rep.add_item(isp.Item.Dpad(
        frame=isp.Rect(17, 285, 150, 145),
        extended_edges=isp.ExtendedEdges(top=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.A],
        frame=isp.Rect(938, 187, 71, 67),
        extended_edges=isp.ExtendedEdges(top=10, left=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.B],
        frame=isp.Rect(848, 158, 71, 67),
        extended_edges=isp.ExtendedEdges(top=10, right=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.Z],
        frame=isp.Rect(919, 100, 71, 67),
        extended_edges=isp.ExtendedEdges(bottom=10, left=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.L],
        frame=isp.Rect(17, 18, 121, 48),
        extended_edges=isp.ExtendedEdges(bottom=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.R],
        frame=isp.Rect(886, 18, 121, 48),
        extended_edges=isp.ExtendedEdges(bottom=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.START],
        frame=isp.Rect(469, 401, 86, 32)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.MENU],
        frame=isp.Rect(469, 17, 86, 31)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_UP],
        frame=isp.Rect(909, 294, 58, 47),
        extended_edges=isp.ExtendedEdges(bottom=0, left=10, right=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_DOWN],
        frame=isp.Rect(909, 384, 58, 47),
        extended_edges=isp.ExtendedEdges(top=0, left=10, right=10),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_LEFT],
        frame=isp.Rect(864, 339, 58, 47),
        extended_edges=isp.ExtendedEdges(top=10, bottom=10, right=0),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_RIGHT],
        frame=isp.Rect(955, 339, 58, 47),
        extended_edges=isp.ExtendedEdges(top=10, bottom=10, left=0),
    ))

    return rep

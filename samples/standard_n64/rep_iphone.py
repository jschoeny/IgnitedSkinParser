import ignitedskinparser.skin as skin


class PortraitItems:
    thumbstick = skin.Item.Thumbstick(
        file_path="assets/portrait_thumbstick.pdf",
        image_size=skin.Size(85, 87),
        frame=skin.Rect(39, 77, 71, 71),
        extended_edges=skin.ExtendedEdges.all(20),
    )
    dpad = skin.Item.Dpad(
        frame=skin.Rect(17, 195, 120, 120),
        extended_edges=skin.ExtendedEdges(15, 17, 15, 7)
    )
    a = skin.Item(
        inputs=[skin.Input.A],
        frame=skin.Rect(247, 122, 56, 56),
        extended_edges=skin.ExtendedEdges(right=17, top=15)
    )
    b = skin.Item(
        inputs=[skin.Input.B],
        frame=skin.Rect(171, 98, 56, 56)
    )
    z = skin.Item(
        inputs=[skin.Input.Z],
        frame=skin.Rect(229, 50, 56, 56),
        extended_edges=skin.ExtendedEdges(bottom=15)
    )
    l = skin.Item(
        inputs=[skin.Input.L],
        frame=skin.Rect(0, 0, 95, 30)
    )
    r = skin.Item(
        inputs=[skin.Input.R],
        frame=skin.Rect(225, 0, 95, 30)
    )
    start = skin.Item(
        inputs=[skin.Input.START],
        frame=skin.Rect(144, 179, 32, 32),
        extended_edges=skin.ExtendedEdges(left=0)
    )
    menu = skin.Item(
        inputs=[skin.Input.MENU],
        frame=skin.Rect(150, 34, 18, 18)
    )
    c_u = skin.Item(
        inputs=[skin.Input.C_UP],
        frame=skin.Rect(215, 197, 42, 42),
        extended_edges=skin.ExtendedEdges(bottom=0, left=0, right=0)
    )
    c_d = skin.Item(
        inputs=[skin.Input.C_DOWN],
        frame=skin.Rect(215, 276, 42, 42),
        extended_edges=skin.ExtendedEdges(top=0, left=0, right=0)
    )
    c_l = skin.Item(
        inputs=[skin.Input.C_LEFT],
        frame=skin.Rect(177, 236, 42, 42),
        extended_edges=skin.ExtendedEdges(top=0, bottom=0, right=0)
    )
    c_r = skin.Item(
        inputs=[skin.Input.C_RIGHT],
        frame=skin.Rect(255, 237, 42, 42),
        extended_edges=skin.ExtendedEdges(top=0, bottom=0, left=0, right=23)
    )


def standard_portrait() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPHONE,
        display_type=skin.DisplayType.STANDARD,
        orientation=skin.Orientation.PORTRAIT,
        mapping_size=skin.Size(320, 328),
        extended_edges=skin.ExtendedEdges.all(7)
    )
    rep.add_asset(skin.Asset('assets/iphone_portrait.pdf', skin.AssetSize.RESIZABLE))

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


def edgetoedge_portrait() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPHONE,
        display_type=skin.DisplayType.EDGE_TO_EDGE,
        orientation=skin.Orientation.PORTRAIT,
        mapping_size=skin.Size(320, 362),
        extended_edges=skin.ExtendedEdges.all(7)
    )
    rep.add_asset(skin.Asset('assets/iphone_edgetoedge_portrait.pdf', skin.AssetSize.RESIZABLE))

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
        device=skin.Device.IPHONE,
        display_type=skin.DisplayType.STANDARD,
        orientation=skin.Orientation.LANDSCAPE,
        mapping_size=skin.Size(667, 375),
        extended_edges=skin.ExtendedEdges.all(15),
        translucent=True
    )
    rep.add_asset(skin.Asset('assets/iphone_landscape.pdf', skin.AssetSize.RESIZABLE))

    rep.add_item(skin.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=skin.Size(78, 78),
        frame=skin.Rect(34, 103, 86, 86),
        extended_edges=skin.ExtendedEdges(top=30, bottom=30, left=34, right=30),
    ))
    rep.add_item(skin.Item.Dpad(
        frame=skin.Rect(15, 237, 123, 123)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.A],
        frame=skin.Rect(597, 158, 56, 56)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.B],
        frame=skin.Rect(522, 134, 56, 56)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.Z],
        frame=skin.Rect(580, 86, 56, 56)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.L],
        frame=skin.Rect(15, 14, 100, 41)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.R],
        frame=skin.Rect(552, 14, 100, 41)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.START],
        frame=skin.Rect(297, 334, 73, 26)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.MENU],
        frame=skin.Rect(299, 15, 73, 26)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_UP],
        frame=skin.Rect(575, 246, 40, 40),
        extended_edges=skin.ExtendedEdges(bottom=0, left=0, right=0)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_DOWN],
        frame=skin.Rect(575, 320, 40, 40),
        extended_edges=skin.ExtendedEdges(top=0, left=0, right=0)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_LEFT],
        frame=skin.Rect(538, 283, 40, 40),
        extended_edges=skin.ExtendedEdges(top=0, bottom=0, right=0)
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_RIGHT],
        frame=skin.Rect(612, 283, 40, 40),
        extended_edges=skin.ExtendedEdges(top=0, bottom=0, left=0)
    ))

    return rep


def edgetoedge_landscape() -> skin.Representation:
    rep = skin.Representation(
        device=skin.Device.IPHONE,
        display_type=skin.DisplayType.EDGE_TO_EDGE,
        orientation=skin.Orientation.LANDSCAPE,
        mapping_size=skin.Size(812, 375),
        extended_edges=skin.ExtendedEdges.all(15),
        translucent=True
    )
    rep.add_asset(skin.Asset('assets/iphone_edgetoedge_landscape.pdf', skin.AssetSize.RESIZABLE))

    rep.add_item(skin.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=skin.Size(78, 78),
        frame=skin.Rect(49, 103, 86, 86),
        extended_edges=skin.ExtendedEdges(top=30, bottom=30, left=49, right=30),
    ))
    rep.add_item(skin.Item.Dpad(
        frame=skin.Rect(30, 237, 123, 123),
        extended_edges=skin.ExtendedEdges(left=30),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.A],
        frame=skin.Rect(727, 158, 56, 56),
        extended_edges=skin.ExtendedEdges(right=30),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.B],
        frame=skin.Rect(652, 134, 56, 56),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.Z],
        frame=skin.Rect(710, 86, 56, 56),
        extended_edges=skin.ExtendedEdges(right=46),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.L],
        frame=skin.Rect(15, 14, 100, 41),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.R],
        frame=skin.Rect(697, 14, 100, 41),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.START],
        frame=skin.Rect(370, 334, 73, 26),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.MENU],
        frame=skin.Rect(370, 15, 73, 26),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_UP],
        frame=skin.Rect(705, 246, 40, 40),
        extended_edges=skin.ExtendedEdges(bottom=0, left=0, right=0),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_DOWN],
        frame=skin.Rect(705, 320, 40, 40),
        extended_edges=skin.ExtendedEdges(top=0, left=0, right=0),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_LEFT],
        frame=skin.Rect(668, 283, 40, 40),
        extended_edges=skin.ExtendedEdges(top=0, bottom=0, right=0),
    ))
    rep.add_item(skin.Item(
        inputs=[skin.Input.C_RIGHT],
        frame=skin.Rect(742, 283, 40, 40),
        extended_edges=skin.ExtendedEdges(top=0, bottom=0, left=0, right=30),
    ))

    return rep

import ignitedskinparser as isp


class PortraitItems:
    thumbstick = isp.Item.Thumbstick(
        file_path="assets/portrait_thumbstick.pdf",
        image_size=isp.Size(85, 87),
        frame=isp.Rect(39, 77, 71, 71),
        extended_edges=isp.ExtendedEdges.all(20),
    )
    dpad = isp.Item.Dpad(
        frame=isp.Rect(17, 195, 120, 120),
        extended_edges=isp.ExtendedEdges(15, 17, 15, 7)
    )
    a = isp.Item(
        inputs=[isp.Input.A],
        frame=isp.Rect(247, 122, 56, 56),
        extended_edges=isp.ExtendedEdges(right=17, top=15)
    )
    b = isp.Item(
        inputs=[isp.Input.B],
        frame=isp.Rect(171, 98, 56, 56)
    )
    z = isp.Item(
        inputs=[isp.Input.Z],
        frame=isp.Rect(229, 50, 56, 56),
        extended_edges=isp.ExtendedEdges(bottom=15)
    )
    l = isp.Item(
        inputs=[isp.Input.L],
        frame=isp.Rect(0, 0, 95, 30)
    )
    r = isp.Item(
        inputs=[isp.Input.R],
        frame=isp.Rect(225, 0, 95, 30)
    )
    start = isp.Item(
        inputs=[isp.Input.START],
        frame=isp.Rect(144, 179, 32, 32),
        extended_edges=isp.ExtendedEdges(left=0)
    )
    menu = isp.Item(
        inputs=[isp.Input.MENU],
        frame=isp.Rect(150, 34, 18, 18)
    )
    c_u = isp.Item(
        inputs=[isp.Input.C_UP],
        frame=isp.Rect(215, 197, 42, 42),
        extended_edges=isp.ExtendedEdges(bottom=0, left=0, right=0)
    )
    c_d = isp.Item(
        inputs=[isp.Input.C_DOWN],
        frame=isp.Rect(215, 276, 42, 42),
        extended_edges=isp.ExtendedEdges(top=0, left=0, right=0)
    )
    c_l = isp.Item(
        inputs=[isp.Input.C_LEFT],
        frame=isp.Rect(177, 236, 42, 42),
        extended_edges=isp.ExtendedEdges(top=0, bottom=0, right=0)
    )
    c_r = isp.Item(
        inputs=[isp.Input.C_RIGHT],
        frame=isp.Rect(255, 237, 42, 42),
        extended_edges=isp.ExtendedEdges(top=0, bottom=0, left=0, right=23)
    )


def standard_portrait() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPHONE,
        display_type=isp.DisplayType.STANDARD,
        orientation=isp.Orientation.PORTRAIT,
        mapping_size=isp.Size(320, 328),
        extended_edges=isp.ExtendedEdges.all(7)
    )
    rep.add_asset(isp.Asset('assets/iphone_portrait.pdf', isp.AssetSize.RESIZABLE))

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


def edgetoedge_portrait() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPHONE,
        display_type=isp.DisplayType.EDGE_TO_EDGE,
        orientation=isp.Orientation.PORTRAIT,
        mapping_size=isp.Size(320, 362),
        extended_edges=isp.ExtendedEdges.all(7)
    )
    rep.add_asset(isp.Asset('assets/iphone_edgetoedge_portrait.pdf', isp.AssetSize.RESIZABLE))

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
        device=isp.Device.IPHONE,
        display_type=isp.DisplayType.STANDARD,
        orientation=isp.Orientation.LANDSCAPE,
        mapping_size=isp.Size(667, 375),
        extended_edges=isp.ExtendedEdges.all(15),
        translucent=True
    )
    rep.add_asset(isp.Asset('assets/iphone_landscape.pdf', isp.AssetSize.RESIZABLE))

    rep.add_item(isp.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=isp.Size(78, 78),
        frame=isp.Rect(34, 103, 86, 86),
        extended_edges=isp.ExtendedEdges(top=30, bottom=30, left=34, right=30),
    ))
    rep.add_item(isp.Item.Dpad(
        frame=isp.Rect(15, 237, 123, 123)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.A],
        frame=isp.Rect(597, 158, 56, 56)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.B],
        frame=isp.Rect(522, 134, 56, 56)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.Z],
        frame=isp.Rect(580, 86, 56, 56)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.L],
        frame=isp.Rect(15, 14, 100, 41)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.R],
        frame=isp.Rect(552, 14, 100, 41)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.START],
        frame=isp.Rect(297, 334, 73, 26)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.MENU],
        frame=isp.Rect(299, 15, 73, 26)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_UP],
        frame=isp.Rect(575, 246, 40, 40),
        extended_edges=isp.ExtendedEdges(bottom=0, left=0, right=0)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_DOWN],
        frame=isp.Rect(575, 320, 40, 40),
        extended_edges=isp.ExtendedEdges(top=0, left=0, right=0)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_LEFT],
        frame=isp.Rect(538, 283, 40, 40),
        extended_edges=isp.ExtendedEdges(top=0, bottom=0, right=0)
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_RIGHT],
        frame=isp.Rect(612, 283, 40, 40),
        extended_edges=isp.ExtendedEdges(top=0, bottom=0, left=0)
    ))

    return rep


def edgetoedge_landscape() -> isp.Representation:
    rep = isp.Representation(
        device=isp.Device.IPHONE,
        display_type=isp.DisplayType.EDGE_TO_EDGE,
        orientation=isp.Orientation.LANDSCAPE,
        mapping_size=isp.Size(812, 375),
        extended_edges=isp.ExtendedEdges.all(15),
        translucent=True
    )
    rep.add_asset(isp.Asset('assets/iphone_edgetoedge_landscape.pdf', isp.AssetSize.RESIZABLE))

    rep.add_item(isp.Item.Thumbstick(
        file_path="assets/thumbstick_landscape.pdf",
        image_size=isp.Size(78, 78),
        frame=isp.Rect(49, 103, 86, 86),
        extended_edges=isp.ExtendedEdges(top=30, bottom=30, left=49, right=30),
    ))
    rep.add_item(isp.Item.Dpad(
        frame=isp.Rect(30, 237, 123, 123),
        extended_edges=isp.ExtendedEdges(left=30),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.A],
        frame=isp.Rect(727, 158, 56, 56),
        extended_edges=isp.ExtendedEdges(right=30),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.B],
        frame=isp.Rect(652, 134, 56, 56),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.Z],
        frame=isp.Rect(710, 86, 56, 56),
        extended_edges=isp.ExtendedEdges(right=46),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.L],
        frame=isp.Rect(15, 14, 100, 41),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.R],
        frame=isp.Rect(697, 14, 100, 41),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.START],
        frame=isp.Rect(370, 334, 73, 26),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.MENU],
        frame=isp.Rect(370, 15, 73, 26),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_UP],
        frame=isp.Rect(705, 246, 40, 40),
        extended_edges=isp.ExtendedEdges(bottom=0, left=0, right=0),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_DOWN],
        frame=isp.Rect(705, 320, 40, 40),
        extended_edges=isp.ExtendedEdges(top=0, left=0, right=0),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_LEFT],
        frame=isp.Rect(668, 283, 40, 40),
        extended_edges=isp.ExtendedEdges(top=0, bottom=0, right=0),
    ))
    rep.add_item(isp.Item(
        inputs=[isp.Input.C_RIGHT],
        frame=isp.Rect(742, 283, 40, 40),
        extended_edges=isp.ExtendedEdges(top=0, bottom=0, left=0, right=30),
    ))

    return rep

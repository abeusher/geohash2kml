header="""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <name>__title__</name>
    <StyleMap id="redbox">
        <Pair>
            <key>normal</key>
            <styleUrl>#redbox1</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#redbox2</styleUrl>
        </Pair>
    </StyleMap>
    <Style id="redbox1">
        <IconStyle>
            <scale>1.1</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff0000aa</color>
        </LineStyle>
        <PolyStyle>
            <color>ff0000aa</color>
        </PolyStyle>
    </Style>
    <Style id="redbox2">
        <IconStyle>
            <scale>1.3</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff0000aa</color>
        </LineStyle>
        <PolyStyle>
            <color>ff0000aa</color>
        </PolyStyle>
    </Style>
<StyleMap id="orangebox">
        <Pair>
            <key>normal</key>
            <styleUrl>#orangebox1</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#orangebox2</styleUrl>
        </Pair>
    </StyleMap>
    <Style id="orangebox1">
        <IconStyle>
            <scale>1.1</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff0076fe</color>
        </LineStyle>
        <PolyStyle>
            <color>ff0076fe</color>
        </PolyStyle>
    </Style>
    <Style id="orangebox2">
        <IconStyle>
            <scale>1.3</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff0076fe</color>
        </LineStyle>
        <PolyStyle>
            <color>ff0076fe</color>
        </PolyStyle>
    </Style>
<StyleMap id="yellowbox">
        <Pair>
            <key>normal</key>
            <styleUrl>#yellowbox1</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#yellowbox2</styleUrl>
        </Pair>
    </StyleMap>
    <Style id="yellowbox2">
        <IconStyle>
            <scale>1.3</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff00ffff</color>
        </LineStyle>
        <PolyStyle>
            <color>ff00ffff</color>
        </PolyStyle>
    </Style>
    <Style id="yellowbox1">
        <IconStyle>
            <scale>1.1</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff00ffff</color>
        </LineStyle>
        <PolyStyle>
            <color>ff00ffff</color>
        </PolyStyle>
    </Style>
    <StyleMap id="greenbox">
        <Pair>
            <key>normal</key>
            <styleUrl>#greenbox1</styleUrl>
        </Pair>
        <Pair>
            <key>highlight</key>
            <styleUrl>#greenbox2</styleUrl>
        </Pair>
    </StyleMap>
    <Style id="greenbox1">
        <IconStyle>
            <scale>1.1</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff00cc00</color>
        </LineStyle>
        <PolyStyle>
            <color>ff00cc00</color>
        </PolyStyle>
    </Style>
    <Style id="greenbox2">
        <IconStyle>
            <scale>1.3</scale>
            <Icon>
                <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
            </Icon>
            <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
        </IconStyle>
        <LineStyle>
            <color>ff00cc00</color>
        </LineStyle>
        <PolyStyle>
            <color>ff00cc00</color>
        </PolyStyle>
    </Style>
    """

footer = """</Document>
</kml>"""

box_template = """
<Placemark>
        <name>__name__</name>
        <styleUrl>#redbox</styleUrl>
        <Polygon>
            <extrude>1</extrude>
            <tessellate>1</tessellate>
            <altitudeMode>relativeToGround</altitudeMode>
            <outerBoundaryIs>
                <LinearRing>
                    <coordinates>
                        __coordinates__
                    </coordinates>
                </LinearRing>
            </outerBoundaryIs>
        </Polygon>
    </Placemark>"""

red_template = """
<Placemark>
        <name>__name__</name>
        <styleUrl>#redbox</styleUrl>
        <Polygon>
            <extrude>1</extrude>
            <tessellate>1</tessellate>
            <altitudeMode>relativeToGround</altitudeMode>
            <outerBoundaryIs>
                <LinearRing>
                    <coordinates>
                        __coordinates__
                    </coordinates>
                </LinearRing>
            </outerBoundaryIs>
        </Polygon>
    </Placemark>"""

orange_template = """
<Placemark>
        <name>__name__</name>
        <styleUrl>#orangebox</styleUrl>
        <Polygon>
            <extrude>1</extrude>
            <tessellate>1</tessellate>
            <altitudeMode>relativeToGround</altitudeMode>
            <outerBoundaryIs>
                <LinearRing>
                    <coordinates>
                        __coordinates__
                    </coordinates>
                </LinearRing>
            </outerBoundaryIs>
        </Polygon>
    </Placemark>"""

yellow_template = """
<Placemark>
        <name>__name__</name>
        <styleUrl>#yellowbox</styleUrl>
        <Polygon>
            <extrude>1</extrude>
            <tessellate>1</tessellate>
            <altitudeMode>relativeToGround</altitudeMode>
            <outerBoundaryIs>
                <LinearRing>
                    <coordinates>
                        __coordinates__
                    </coordinates>
                </LinearRing>
            </outerBoundaryIs>
        </Polygon>
    </Placemark>"""

green_template = """
<Placemark>
        <name>__name__</name>
        <styleUrl>#greenbox</styleUrl>
        <Polygon>
            <extrude>1</extrude>
            <tessellate>1</tessellate>
            <altitudeMode>relativeToGround</altitudeMode>
            <outerBoundaryIs>
                <LinearRing>
                    <coordinates>
                        __coordinates__
                    </coordinates>
                </LinearRing>
            </outerBoundaryIs>
        </Polygon>
    </Placemark>"""
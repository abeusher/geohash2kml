#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import geohash
from kml_template import header, footer, box_template, red_template, orange_template, yellow_template, green_template

class KmlMaker(object):
    def __init__(self,filename):
        self.filename = filename
        print "walking",filename
        self.locations = {}

    def makeGoogleEarthBox(self,geo):
        bbox = geohash.bbox(geo)
        lowerleft = "%s,%s,elevation"%(bbox['w'],bbox['s'])
        upperleft = "%s,%s,elevation"%(bbox['w'],bbox['n'])
        lowerright = "%s,%s,elevation"%(bbox['e'],bbox['s'])
        upperright = "%s,%s,elevation"%(bbox['e'],bbox['n'])
        polygon = "%s %s %s %s %s"%(lowerleft,upperleft,upperright,lowerright,lowerleft)
        return polygon

    def loadLocations(self):
        counts = {}
        for line in open(self.filename,"rU"):
            (geohashcode, count) = line.strip().split("\t")
            self.locations[geohashcode] = count
        print 'Done loading geohashcode counts.'

    def get_template(self,input_value,color_ramp=[4,7,15]):
        low = color_ramp[0]
        medium = color_ramp[1]
        high = color_ramp[2]
        template = box_template
        if input_value < low:
            template = green_template
        elif input_value < medium:
            template = yellow_template
        elif input_value < high:
            template = orange_template
        else:
            template = red_template
        return template


    def simple_kml_output(self,title='Location Indicators',output_filename ='output_simple.kml' ):
        f = open(output_filename,"w")
        header2 = header.replace('__title__',title)
        f.write(header2)
        for key,value in self.locations.items():
            value = int(value)
            if value < 1: continue
            print key,value
            t = box_template
            poly = self.makeGoogleEarthBox(key)
            #TODO: remove this constraint for visualization
            if value > 40:
                value = 40
            height = value * 400
            height = str(height)
            poly = poly.replace("elevation",height)
            t = t.replace("__name__",key)
            t = t.replace("__coordinates__",poly)
            f.write(t+"\n")
        f.write(footer)

    def advanced_kml_output(self,title='Location Indicators',output_filename ='output_advanced.kml',color_ramp=[1,500,1000],polygon_height=1000):
        f = open(output_filename,"w")
        header2 = header.replace('__title__',title)
        f.write(header2)
        for key,value in self.locations.items():
            value = int(value)
            if value < 1: continue
            print key,value
            t = self.get_template(value,color_ramp=color_ramp)
            poly = self.makeGoogleEarthBox(key)
            #TODO: remove this constraint for visualization
            if value > 50000:
                value = 50000
            height = value * polygon_height
            height = str(height)
            poly = poly.replace("elevation",height)
            t = t.replace("__name__",key)
            t = t.replace("__coordinates__",poly)
            t = t.replace('__title__',title)
            f.write(t+"\n")
        f.write(footer)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Usage: python geohash2kml.py <input file> <output file>"
        sys.exit(-1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    kml = KmlMaker(input_file)
    kml.loadLocations()
    # kml.simple_kml_output()
    kml.advanced_kml_output(output_filename=output_file, color_ramp=[300,800,1600], polygon_height=1)

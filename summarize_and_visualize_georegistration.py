import json
import sys
import pprint
import time
from geohash2kml import KmlMaker

"""
Code to extract georegistration elements and:
 (1) Save them to a tab-delimited file for viewing in a Spreadsheet for
 (2) Aggregate counts of the geolocations in geohash5 as a KML output 

author: Abe U.
"""


class SuperJsonProcessor(object):
    """
    Parses JSONL data given a specific input format.
    Creates outputs as TSV, aggregate geohash5 count, and descriptive statistics table.
    """
    def __init__(self):
        self.data_table = [] # we will store rows of georegistration data here

    def load_data(self, input_file="default.json"):
        """
        Read in the data in input_file, convert it from string to json to python dict
        pluck out the georegistration details
        [object_id, country_code, admin1, admin2, geohash5, lat, lng, mgrs, placename, precision, confidence_level]
        and store then in the list self.data_table
        """
        lines = open(input_file,"rU", encoding="utf-8")
        counter = 0
        for line in lines:
            counter +=1
            if counter % 10000 == 0:
                print (counter)
            #print(line)            
            json_object = json.loads(line)
            #pprint.pprint(json_object)
            #time.sleep(10.0)
            object_id = str(json_object.get('id',12345678))
            georegistration = json_object.get("enrichment",{}).get("georegistration",{})
            for node in georegistration:                         
                #pprint.pprint(node)
                #time.sleep(1.0)
                #print (result)
                results = node.get('results',[])
                for result in results:                
                    country_code = result.get("country_code","Unknown Country")
                    admin1 = str(result.get("admin1","unknown admin1"))
                    admin2 = str(result.get("admin2","unknown admin2"))
                    geohash5 = str(result.get("geohash", "s0000"))
                    lat = str(result.get("lat","0.0"))
                    lng = str(result.get("lng","0.0"))
                    mgrs = str(result.get("mgrs","Unknown"))
                    placename = str(result.get("placename",""))
                    precision = str(result.get("precision","5"))
                    confidence_level = str(result.get("confidence",{}).get("confidence_level", "Unknown"))
                    item = [object_id, country_code, admin1, admin2, geohash5, lat, lng, mgrs, placename, precision, confidence_level]
                    #print (item)
                    self.data_table.append(item)
                    #time.sleep(1.0)
        return
        #pprint.pprint(json_object)

    def save_tsv(self, output_file="default_output.tsv"):
        """
        Save the results of self.data_table to a tsv file.
        """
        fout = open(output_file,"w", encoding="utf-8")
        for item in self.data_table:
            text = "\t".join(item)
            fout.write(text+"\n")
        print("Done writing TSV output to", output_file)

    def make_geohash_kml(self, output_file="default_kml_output.kml"):
        """
        Makes a thematic KML visual of the geolocated points, by drawing geohash5 boxes in a KML file.
        Example of this technique applied to 
        twitter data in Minneapolis https://github.com/abeusher/geohash2kml/blob/master/minneapolis.png
        """
        fout = open(output_file, "w", encoding="utf-8")
        geohash_counter = {}
        for item in self.data_table:
            object_id, country_code, admin1, admin2, geohash_value, lat, lng, mgrs, placename, precision, confidence_level = item
            geo5 = geohash_value[0:5]
            geohash_counter[geo5] = geohash_counter.get(geo5,0)+1            
        # write out the counts into KML
        kml = KmlMaker()
        kml.locations = geohash_counter
        kml.advanced_kml_output(output_filename=output_file, color_ramp=[300,800,1600], polygon_height=1)
        print("Done writing kml output to", output_file)

    def make_statistics_table(self, output_file = ""):
        """
        A simple table of stats.  Looks like David T. already made this!
        """
        return


def main():
    """

    1. Reads in a filename that is supplied as sys.argv[1] or uses a default input file name
    2. Create a SuperJsonProcessor object and writes the two outputs that it supports.

    Assumption: input is a JSONL file
    """
    if len (sys.argv) > 1:
        filename = sys.argv[1]
    else: 
        filename = "enriched_Clin_1_data_drop_documents.jsonl"
    sjp = SuperJsonProcessor()

    # load the data
    sjp.load_data(input_file=filename) 

    # save georegistration rows in TSV
    sjp.save_tsv(output_file="georegistration_table.tsv") 

    # save 3d KML file of aggregated geohash5s
    sjp.make_geohash_kml(output_file="output.kml") 

    # write out some statistics.
    #sjp.make_statistics_table(output_file="statistics.txt") 

    print("All done!")
    
if __name__ == "__main__":
    main()

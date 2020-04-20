import json
import sys
import pprint
import time

"""
Code to extract georegistration elements and:
 (1) Save them to a tab-delimited file for viewing in a Spreadsheet for
 (2) Aggregate counts of the geolocations in geohash5 as a KML output
 (3) Make a table with descriptive statistics of what was captured.
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
        pluck out the georegistration country, admin1, admin2, latitude, longitude and store those
        in self.data_table
        """
        lines = open(input_file,"rU", encoding="utf-8")
        for line in lines:
            #print(line)            
            json_object = json.loads(line)
            #pprint.pprint(json_object)
            #time.sleep(10.0)
            object_id = json_object.get('id',12345678)
            georegistration = json_object.get("enrichment",{}).get("georegistration",{})
            for result in georegistration:         
                # item = [id, country_code, admin1, admin2, geohash5, latitude, longitude]   
                country_code = result.get("country_code","Unknown Country")
                admin1 = str(result.get("admin1","unknown admin1"))
                admin2 = str(result.get("admin2","unknown admin2"))
                lat = str(result.get("lat","0.0"))
                lng = str(result.get("lng","0.0"))
                mgrs = str(result.get("mgrs","Unknown")))
                placename = str(result.get("placename",""))
                precision = str(result.get("precision","5"))
                confidence_level = str(result.get("confidence",{}).get("confidence_level":"Unknown"))
                pprint.pprint(result)
                time.sleep(1.0)

        
        #pprint.pprint(json_object)

    def save_tsv(self, output_file="default_output.tsv"):
        pass

    def make_geohash_kml(self):
        pass

    def make_statistics_table(self):
        pass


def main():
    """
    Create a SuperJsonProcessor object and write the three outputs that it supports.

    Assumes input is a JSONL file
    """
    
    filename = "enriched_Clin_1_data_drop_documents.jsonl"
    sjp = SuperJsonProcessor()

    # load the data
    sjp.load_data(input_file=filename) 

    # save georegistration rows in TSV
    sjp.save_tsv(output_file="output.tsv") 

    # save 3d KML file of aggregated geohash5s
    sjp.make_geohash_kml(output_file="output.kml") 

    # write out some statistics.
    sjp.make_statistics_table(output_file="statistics.txt") 

    print("All done!")
    
if __name__ == "__main__":
    main()

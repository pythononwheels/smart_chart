#
# generate a bubble chart using  google chart tools
# see: https://developers.google.com/chart/interactive/docs/gallery/bubblechart#Example
#
# khz (2.7.2012); khz@tzi.org
# For usage use: python create_bubble_chart.py --help
# 
# example: python create_bubble_chart.py -f input.csv

import sys, os, os.path
from optparse import OptionParser
import datetime
import ConfigParser


if __name__ == "__main__":#
 
    parser = OptionParser()
    
    parser.add_option("-f", "--file",  action="store", type="string", dest="infile", 
        help="set the csv file to read the data from", default=None)
    parser.add_option("--cf", "--config-file",  action="store",  dest="config_file", 
        help="define the config file ro read all attributes and options from. (give without .py ending)", default="tree_chart_config")           
    
    (options, args) = parser.parse_args()
    
    #print options,args 
    
    if options.infile == None:
        parser.error("you must give an input filename and the config_file. Use --help to see the options")
        
    print "...reading files: ", options.infile
        
    # import the options
    if options.config_file:
        exec("from " + str(options.config_file) +" import CHART_OPTIONS")
        exec("from " + str(options.config_file) +" import COLUMN_TYPES")
        exec("from " + str(options.config_file) +" import PARSE_OPTIONS")
        #print CHART_OPTIONS
    
    otemplate_file = open( os.path.normpath( "./tree_chart_template.html"), "r" )
    ostr = otemplate_file.read()
    
    infile = open( os.path.normpath(options.infile), "r" )
   
    print "...starting to process data"
    line_counter = 1
    olist = []
    #
    # process the data input
    #
    tmpostr = ""
    num_cols = int(PARSE_OPTIONS["NUM_COLS"])
    # for every line in input file
    for line in infile.readlines():
        line = line.strip(PARSE_OPTIONS["STRIPCHARS"])
        tmpline = line.split(PARSE_OPTIONS["SPLITCHARS"])
        print tmpline
        col_counter = 1
        tmpostr += "["
        # for every token in inputline
        for item in tmpline:
            # get rid of preexisting quotes.
            item = item.replace('"', "")
            item = item.replace("'", "")
            if line_counter <= 1:
            # this is the headerline, just take it as STRING
                tmpostr += "'" + str(item) + "'"
            else:
            # these are the DATALINES handle as specified in bubble_chart_config.py
                if COLUMN_TYPES.has_key(str(col_counter)):
                    # A Datatype was specified for this column, so handle appropriately
                    if COLUMN_TYPES[str(col_counter)] == "INT":
                        # handle INT
                        tmpostr += str(int(item))
                    elif COLUMN_TYPES[str(col_counter)] == "FLOAT":
                        # handle FLOAT
                        tmpostr += str(float(item.replace(",",".")))
                    elif COLUMN_TYPES[str(col_counter)] == "STRING":
                        # handle STRING
                        if item != "null":
                            tmpostr += "'" + str(item) + "'"
                        else:
                            tmpostr += str(item)
                else:
                    # nothing specifically specified for this column, so handle as STRING
                    tmpostr += "'" + str(item) + "'"
            if col_counter < num_cols:
                tmpostr += ","
            col_counter += 1
            #print item, " -> ", tmpostr    
        tmpostr += "]," + "\n"
        line_counter += 1
    tmpostr = tmpostr[0:-2]
    print tmpostr
    
    ostr = ostr.replace("#WIDTH", CHART_OPTIONS["WIDTH"])        
    ostr = ostr.replace("#HEIGHT", CHART_OPTIONS["HEIGHT"])   
    ostr = ostr.replace("#DATA", str(tmpostr))
    
    out = os.path.join(CHART_OPTIONS["OUTPUT_DIR"], CHART_OPTIONS["OUT_FILE"] )
    print "...writing to: ", out
    ofile = open( os.path.normpath(out),"w" )
    ofile.write( ostr )
    
    infile.close()
    otemplate_file.close()
    ofile.close()
    
    print "...processed: ", line_counter, " lines"
    sys.exit(0)    
    
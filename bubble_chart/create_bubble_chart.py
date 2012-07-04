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

def str_replace( instr, replace_string, ifnot_equals=None):
    if ifnot_equals != None:
        if CHART_OPTIONS[replace_string] == ifnot_equals:
            return instr
    instr = instr.replace(str("#"+replace_string), CHART_OPTIONS[replace_string])
    return instr
    
if __name__ == "__main__":#
 
    parser = OptionParser()
    
    parser.add_option("-f", "--file",  action="store", type="string", dest="infile", 
        help="set the csv file to read the data from", default=None)
    parser.add_option("--cf", "--config-file",  action="store",  dest="config_file", 
        help="define the config file ro read all attributes and options from. (give without .py ending)", default="bubble_chart_config")           
    
    (options, args) = parser.parse_args()
    
    #print options,args 
    
    if options.infile == None:
        parser.error("you must give an input filename and the config_file. Use --help to see the options")
    
    # import the options
    if options.config_file:
        exec("from " + str(options.config_file) +" import CHART_OPTIONS")
        exec("from " + str(options.config_file) +" import COLUMN_TYPES")
        exec("from " + str(options.config_file) +" import PARSE_OPTIONS")
        #print CHART_OPTIONS
        
        
    infile = open( os.path.normpath(options.infile), "r" )
    if len(sys.argv) > 2:
        SPLITCHAR = sys.argv[2]
    print "...starting to process data"
    line_counter = 1
    olist = []
    #
    # process the data input
    #
    tmpostr = ""
    # for every line in input file
    for line in infile.readlines():
        line = line.strip(PARSE_OPTIONS["STRIPCHARS"])
        tmpline = line.split(PARSE_OPTIONS["SPLITCHARS"])
        #print tmpline
        col_counter = 1
        num_cols = int(PARSE_OPTIONS["NUM_COLS"])
        tmpostr += "["
        # for every token in inputline
        for item in tmpline:
            item = item.replace('"', "")
            item = item.replace("'", "")
            if line_counter <= 1:
            # this is the headerline, just take it as STRING
                tmpostr += "'" + str(item) + "'"
                #if col_counter < num_cols:
                #    tmpostr += ","
            else:
            # these are the DATALINES handle as specified in bubble_chart_config.py
                if COLUMN_TYPES.has_key(str(col_counter)):
                    # A Datatype was specified for this column, so handle appropriately
                    # first try t oguess input type.
                    if COLUMN_TYPES[str(col_counter)] == "INT":
                        # handle INT
                        tmpostr += str(int(item))
                    elif COLUMN_TYPES[str(col_counter)] == "FLOAT":
                        # handle FLOAT
                        item = item.replace(",",".")
                        tmpostr += str(float(item))
                    elif COLUMN_TYPES[str(col_counter)] == "STRING":
                        # handle STRING
                        tmpostr += "'" + str(item) + "'"
                else:
                    # nothing specifically specified for this column, so handle as STRING
                    tmpostr += "'" + str(item) + "'"
            if col_counter < num_cols:
                tmpostr += ","
            col_counter += 1
             
        tmpostr += "]," + "\n"
        line_counter += 1
    tmpostr = tmpostr[0:-2]
    print tmpostr
    print "...found chart_type: ", CHART_OPTIONS["CHART_TYPE"].upper()
    if str(CHART_OPTIONS["CHART_TYPE"]).upper() == "GRADIENT":
        otemplate_file = open( os.path.normpath( "./bubble_chart_gradient_template.py"), "r" )
        ostr = otemplate_file.read()
        col1, col2 = str(CHART_OPTIONS["GRAD_COLORS"]).split(",")
        ostr = ostr.replace("#COL1", col1.lower())
        ostr = ostr.replace("#COL2", col2.lower())
    else:
        otemplate_file = open( os.path.normpath( "./bubble_chart_series_template.py"), "r" )
        ostr = otemplate_file.read()
    
    
    # for both templates
    ostr = ostr.replace("#BUBBLE_ID_FONTSIZE", CHART_OPTIONS["BUBBLE_ID_FONTSIZE"])        
    ostr = ostr.replace("#TITLE_CHART", CHART_OPTIONS["TITLE_CHART"])
    ostr = ostr.replace("#TITLE_XAXIS", CHART_OPTIONS["TITLE_XAXIS"])
    ostr = ostr.replace("#TITLE_YAXIS", CHART_OPTIONS["TITLE_YAXIS"])
    
    
    ostr = str_replace(ostr, "VAXIS_MAX", "auto")
    ostr = str_replace(ostr, "VAXIS_MIN", "auto")
    ostr = str_replace(ostr, "HAXIS_MAX", "auto")
    ostr = str_replace(ostr, "HAXIS_MIN", "auto")
    ostr = str_replace(ostr, "WIDTH")
    ostr = str_replace(ostr, "HEIGHT")
    ostr = str_replace(ostr, "SIZE_AXIS_MIN")
    ostr = str_replace(ostr, "SIZE_AXIS_MAX")
    
    ostr = ostr.replace("#CHART_DATA", str(tmpostr))
    out = os.path.join(CHART_OPTIONS["OUTPUT_DIR"], CHART_OPTIONS["OUT_FILE"] )
    print "...writing to: ", out
    ofile = open( os.path.normpath(out),"w" )
    ofile.write( ostr )
    
    infile.close()
    otemplate_file.close()
    ofile.close()
    
    print "...processed: ", line_counter, " lines"
    sys.exit(0)    
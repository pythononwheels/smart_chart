#
# options for chart generation
# khz (2.7.2012); khz@tzi.org

PARSE_OPTIONS = {
    "STRIPCHARS"    :   " \n\t",
    "SPLITCHARS"    :   ";",
    "NUM_COLS"      :   "4"
}
CHART_OPTIONS = {
    "TITLE_CHART" : "TITLE",
    "TITLE_XAXIS" : "TITLE",
    "TITLE_YAXIS" : "TITLE",
    "FONTSIZE"   : "11",
    "OUTPUT_DIR"    :   "c:/xampp/htdocs/smartchart",
    "OUT_FILE"  : "1.html"
}

#
# 1st parameter defines the colum to convert
# 2nd parameter defines the goal datatype. Can Be STRING,INT, FLOAT so far.
# By Default, any Column is handled as STRING as is, if nothing else is 
# specified here.
#
COLUMN_TYPES = {
    "1"    : "STRING",
    "2"    : "INT",
    "3"    : "INT",    
    "4"    : "FLOAT" 
}
#
# options for chart generation
# khz (2.7.2012); khz@tzi.org

PARSE_OPTIONS = {
    "STRIPCHARS"    :   " \n\t",
    "SPLITCHARS"    :   ";",
    "NUM_COLS"      :   "5"
}
# chart options:
#       CHART_TYPE  : [SERIES || GRADIENT]
#       GRAD_COLORS : only used when chart_type is GRADIENT.
#       in a SERIES Chart, the 4th column has to be STRING and to be used to group the Values
#       V/H Axis Min and Max Options work as follows: 
#        AUTO       =>   all set to 0 then sizes are calculated automatically.
#        MAX ONLY   =>   same size for min and max will set max sizes (min will be taken automatically)
#        MIN & MAX  =>   different values for min and max will use these.
CHART_OPTIONS = {
    "CHART_TYPE"    : "GRADIENT",
    "GRAD_COLORS"   : "RED,BLUE",
    "TITLE_CHART"   : "A beautiful Chart made by smart_chart and python",
    "TITLE_XAXIS"   : "Importance",
    "TITLE_YAXIS"   : "Costs",
    "BUBBLE_ID_FONTSIZE"      : "3",
    "OUTPUT_DIR"    : "./",
    "OUT_FILE"      : "series_chart.html",
    "VAXIS_MIN"     : "0",
    "VAXIS_MAX"     : "0",
    "HAXIS_MIN"     : "0",
    "HAXIS_MAX"     : "0",
    "SORTBUBBLESBYSIZE" : "true",
    "WIDTH"         : "1400",
    "HEIGHT"        : "1000",
    "SIZE_AXIS_MIN" : "6",
    "SIZE_AXIS_MAX" : "12"
    
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
    "4"    : "STRING",
    "5"    : "INT",
}
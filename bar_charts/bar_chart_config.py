#
# options for chart generation
# khz (2.7.2012); khz@tzi.org

PARSE_OPTIONS = {
    "STRIPCHARS"    :   " \n\t",
    "SPLITCHARS"    :   ",",
    "NUM_COLS"      :   "4"
}
# chart options:
#       CHART_TYPE  : [SERIES || GRADIENT]
#       GRAD_COLORS : only used when chart_type is GRADIENT.
CHART_OPTIONS = {
    "TITLE_CHART"       : "A beautiful Chart made by smart_chart and python",
    "TITLE_XAXIS"       : "Importance",
    "TITLE_YAXIS"       : "Costs",
    "FONTSIZE"          : "11",
    "OUTPUT_DIR"        : "./",
    "OUT_FILE"          : "barchart.html",
    "BAR_TYPE"          : "line",
    "TOGGLE_BUTTON_TEXT" : "toggle me",
    "TOGGLE1_TEXT"      : "1st view",
    "TOGGLE2_TEXT"      : "2nd view",
    "WIDTH"             : "500",
    "HEIGHT"            : "300"
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
    "4"    : "INT" 
}
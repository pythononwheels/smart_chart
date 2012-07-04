Description of the input format for tree_map chart generation.

Taken from: https://google-developers.appspot.com/chart/interactive/docs/gallery/treemap


Data Format

Each row in the data table describes one node (a rectangle in the graph). 
Each node (except the root node) has one or more parent nodes. 
Each node is sized and colored according to its values relative to the other nodes currently shown.

The data table should have four columns in the following format:

    Column 0 - [string] - An ID for this node. It can be any valid JavaScript string, 
                          including spaces, and any length that a string can hold. This value is displayed as the node header.
    Column 1 - [string] - The ID of the parent node. If this is a root node, leave this blank. 
                          Only one root is allowed per treemap.
    Column 2 - [number] - The size of the node. Any positive value is allowed. 
                          This value determines the size of the node, computed relative to all other nodes currently 
                          shown. This value is ignored for non-leaf nodes (it is actually calculated from the 
                          size of all its children).
    Column 3 - [optional, number] - An optional value used to calculate a color for this node. 
                                    Any value, positive or negative, is allowed. The color value 
                                    is first recomputed on a scale from minColorValue to maxColorValue, 
                                    and then the node is assigned a color from the gradient between 
                                    minColor and maxColor.

                                    
Full documentation see: https://google-developers.appspot.com/chart/interactive/docs/gallery/treemap
<html>
  <!-- Author: khz (2.7.2012); khz@tzi.org -->
  <head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          #CHART_DATA
        ]);

        var options = {
          title: '#TITLE_CHART', 
          hAxis: {title: '#TITLE_XAXIS' },
          vAxis: {title: '#TITLE_YAXIS' },
          bubble: {textStyle: {fontSize: #BUBBLE_ID_FONTSIZE }},
          sizeAxis: {minValue: #SIZE_AXIS_MIN,  maxSize: #SIZE_AXIS_MAX}
        };

        var chart = new google.visualization.BubbleChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: #WIDTHpx; height: #HEIGHTpx;"></div>
  </body>
</html>
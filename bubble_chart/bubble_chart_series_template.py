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
          hAxis: {title: '#TITLE_XAXIS'},
          vAxis: {title: '#TITLE_YAXIS'},
          bubble: {textStyle: {fontSize: #FONTSIZE }},
          hAxis: {maxValue: #HAXIS_MAX},
          vAxis: {maxValue: #VAXIS_MAX},
          hAxis: {minValue: #HAXIS_MIN},
          vAxis: {minValue: #VAXIS_MIN}
        };

        var chart = new google.visualization.BubbleChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>
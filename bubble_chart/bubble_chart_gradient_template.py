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
          hAxis: {title: '#TITLE_XAXIS', maxValue: #HAXIS_MAX, minValue: #HAXIS_MIN },
          vAxis: {title: '#TITLE_YAXIS', maxValue: #VAXIS_MAX, minValue: #VAXIS_MIN },
          colorAxis: {colors: ['#COL1', '#COL2']},
          bubble: {textStyle: {fontSize: #BUBBLE_ID_FONTSIZE }}
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
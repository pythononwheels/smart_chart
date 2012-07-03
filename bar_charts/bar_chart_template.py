<!DOCTYPE html>
<html>
  <head>
    <title>Google Developers</title>
    <link rel="stylesheet" type="text/css" href="/css/screen.css" />
    <link rel="stylesheet" href="//www.google.com/cse/style/look/default.css" type="text/css" />
    <link href='//fonts.googleapis.com/css?family=Open+Sans:300,400' rel='stylesheet' type='text/css'>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js"></script>
    <script id="jqueryui" src="//ajax.googleapis.com/ajax/libs/jqueryui/1.8.10/jquery-ui.min.js" defer async></script>
    <script src="//www.google.com/jsapi?key=AIzaSyCZfHRnq7tigC-COeQRmoa9Cxr0vbrK6xw"></script>
    <!--[if lt IE 9]>
    <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>
  <body class="docs framebox_body">

<script type="text/javascript" src="https://www.google.com/jsapi"></script>

<script type="text/javascript">

google.load('visualization', '1.1', {packages: ['corechart']});

google.setOnLoadCallback(drawExample2);

function drawExample2() {
  // Some raw data (not necessarily accurate)
  var rowData1 = [#DATA0];
  var rowData2 = [#DATA1];

  // Create and populate the data tables.
  var data = [];
  data[0] = google.visualization.arrayToDataTable(rowData1);
  data[1] = google.visualization.arrayToDataTable(rowData2);

  var options = {
    width: #WIDTH,
    height: #HEIGHT,
    vAxis: {title: "#TITLE_XAXIS"},
    hAxis: {title: "#TITLE_YAXIS"},
    seriesType: "bars",
    series: {5: {type: "#BAR_TYPE"}},
    animation:{
      duration: 1000,
      easing: 'out'
    }
  };
  var current = 0;
  // Create and draw the visualization.
  var chart = new google.visualization.ComboChart(document.getElementById('example2-visualization'));
  var button = document.getElementById('example2-b1');
  function drawChart() {
     // Disabling the button while the chart is drawing.
    button.disabled = true;
    google.visualization.events.addListener(chart, 'ready',
        function() {
          button.disabled = false;
          button.value = '#TOGGLE_BUTTON_TEXT' + (current ? '#TOGGLE1_TEXT' : '#TOGGLE2_TEXT');
        });
    options['title'] = '#TITLE_CHART ' + (current ? '#TOGGLE1_TEXT' : '#TOGGLE2_TEXT') + ' ....';

    chart.draw(data[current], options);
  }
  drawChart();

  button.onclick = function() {
    current = 1 - current;
    drawChart();
  }
}

</script>

<form><input id="example2-b1" type="button" value="Switch to Tea"></input></form>

<div id="example2-visualization"></div>

</body>
</html>

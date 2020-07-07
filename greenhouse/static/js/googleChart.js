	let graph = function(urlEnd, chartDiv, title, element){
	// load current chart package
	google.charts.load("current", {
		packages: ["corechart", "line"]
	});

	// set callback function when api loaded
	google.charts.setOnLoadCallback(drawChart);

	function drawChart() {

		// create data object with default value
		let data = new google.visualization.DataTable();
		data.addColumn('datetime', 'Time');
		data.addColumn('number', element);
		//data.addColumn('datetime', 'Time');
		
		$.ajax({
		url: "/api/json/" + urlEnd + 'start',
		dataType: "json",
		type: "GET",
		success: function (dJS) {
		let dataStart = [];
		for (let i of dJS){
			dataStart.push([new Date(i[0],i[1]-1,i[2],i[3],i[4],i[5]), i[6]])
		}
		data.addRows(dataStart);
		}
		})
	
		
		// create options object with titles, colors, etc.
		let options = {
			title: title,
			curveType: 'function',
			hAxis: {
				title: "Time",
			},
			vAxis: {
				title: "Usage",
			},
			explorer: { actions: ['dragToZoom', 'rightClickToReset'] }
		};

		// draw chart on load
		let chart = new google.visualization.LineChart(
			document.getElementById(chartDiv)
		);
		chart.draw(data, options);

		// interval for adding new data every 250ms
		setInterval(function() {

			// instead of this random, you can make an ajax call for the current cpu usage or what ever data you want to display

			$.ajax({
			url: "/api/json/" + urlEnd,
			dataType: "json",
			type: "GET",
			success: function (dJ) {
			data.addRow([new Date(dJ[0],dJ[1]-1,dJ[2],dJ[3],dJ[4],dJ[5]), dJ[6]]);
			chart.draw(data, options);
			}
			})
		}, 6000);

	}
	}

<template>
	<h1 class="mt-10 mb-5 text-3xl text-center font-bold">View data</h1>

	<v-container class="mt-5">
		<v-card class="mb-5 rounded-lg">
			<v-card-text>
				<h2 class="text-bold text-base">System status</h2>
				<h3 class="text-bold text-2xl text-center mb-5">
					<span id="systemStatus" class="font-bold">{{ systemStatus }}</span>
				</h3>
				<div class="flex justify-between">
					<div>
						<v-btn class="m-2" color="info" id="coolingBtn">
							<i class="fa-solid fa-fan"></i>&nbsp; Cool</v-btn
						>
						<v-btn class="m-2" color="error" id="heatingBtn"
							><i class="fa-sharp fa-solid fa-fire"></i>&nbsp; Heat</v-btn
						>
					</div>
					<div>
						<v-btn class="m-2" color="success" id="startBtn">
							<i class="fa-solid fa-play"></i>&nbsp; Start</v-btn
						>
						<v-btn class="m-2" color="error" id="stopBtn">
							<i class="fa-solid fa-stop"></i>&nbsp; Stop</v-btn
						>
					</div>
				</div>
			</v-card-text>
		</v-card>

		<div class="flex">
			<v-card class="m-1 w-100 rounded-lg">
				<v-card-text>
					<h5 class="font-bold text-lg text-center mb-3">Coolant Temperature</h5>
					<h5 class="font-bold text-base">
						Min value: <span id="tempMinVal">{{ tempMinValue }}</span>
					</h5>
					<h5 class="font-bold text-base">
						Max value: <span id="tempMaxVal">{{ tempMaxValue }}</span>
					</h5>
					<h5 class="font-bold text-base">
						Measured value: <span id="temperature"></span>
					</h5>
					<canvas class="p-10" id="myChart1"></canvas>
				</v-card-text>
			</v-card>

			<v-card class="m-1 w-100 rounded-lg">
				<v-card-text>
					<h5 class="font-bold text-lg text-center mb-3">Coolant Pressure</h5>
					<h5 class="font-bold text-base">
						Min value: <span id="pressMinVal">{{ pressMinValue }}</span>
					</h5>
					<h5 class="font-bold text-base">
						Max value: <span id="pressMaxVal">{{ pressMaxValue }}</span>
					</h5>
					<h5 class="font-bold text-base">Measured value: <span id="pressure"></span></h5>
					<canvas class="p-10" id="myChart2"></canvas>
				</v-card-text>
			</v-card>
		</div>

		<div class="flex mb-3">
			<v-card class="m-1 w-100 rounded-lg">
				<v-card-text>
					<div class="d-flex justify-between items-center mb-3">
						<h5 class="font-bold">Temperature Data Table</h5>
						<v-btn class="bg-gray-900 text-white"
							><i class="fa-regular fa-floppy-disk"></i>&nbsp; Save</v-btn
						>
					</div>
					<v-data-table
						:headers="tempHeaders"
						:items="tempData"
						:rows-per-page-items="[5, 10, 15]"
						class="elevation-1"
						:search="searchTemp"
						:pagination.sync="tempPagination"
					>
						<template v-slot:item.id="{ item }">{{ item.id }}</template>
						<template v-slot:item.timestamp="{ item }">{{ item.timestamp }}</template>
						<template v-slot:item.value="{ item }">{{ item.value }}</template>
					</v-data-table>
				</v-card-text>
			</v-card>

			<v-card class="m-1 w-100 rounded-lg">
				<v-card-text>
					<div class="d-flex justify-between items-center mb-3">
						<h5 class="font-bold">Pressure Data Table</h5>
						<v-btn class="bg-gray-900 text-white"
							><i class="fa-regular fa-floppy-disk"></i>&nbsp; Save</v-btn
						>
					</div>
					<v-data-table
						:headers="pressHeaders"
						:items="pressData"
						:rows-per-page-items="[5, 10, 15]"
						class="elevation-1"
						:search="searchPress"
						:pagination.sync="pressPagination"
					>
						<template v-slot:item.id="{ item }">{{ item.id }}</template>
						<template v-slot:item.timestamp="{ item }">{{ item.timestamp }}</template>
						<template v-slot:item.value="{ item }">{{ item.value }}</template>
					</v-data-table>
				</v-card-text>
			</v-card>
		</div>

		<!-- <div v-if="!isAuthenticated" class="mt-5">
			<h1 class="text-danger text-center">You must be logged in to access this page!</h1>
		</div> -->
	</v-container>
</template>

<script>
export default {
	data() {
		return {
			systemStatus: "Initializing",
			temperature: "",
			pressure: "",
			tempMinValue: "",
			tempMaxValue: "",
			pressMinValue: "",
			pressMaxValue: "",
			tempGraphData: {
				type: "line",
				data: {
					labels: [],
					datasets: [
						{
							label: "Temperature(°C)",
							data: [],
							backgroundColor: ["rgba(73,198,230,1)"],
							borderWidth: 5,
						},
					],
				},
				options: {},
			},
			presGraphData: {
				type: "line",
				data: {
					labels: [],
					datasets: [
						{
							label: "Pressure(bar)",
							data: [],
							backgroundColor: ["rgba(0,0,0,1)"],
							borderWidth: 5,
						},
					],
				},
				options: {},
			},
			socket: null,
		};
	},
	mounted() {
		const ctx = document.getElementById("myChart1").getContext("2d");
		const ctx2 = document.getElementById("myChart2").getContext("2d");

		const myTempChart = new Chart(ctx, this.tempGraphData);
		const myPresChart = new Chart(ctx2, this.presGraphData);

		this.socket = new WebSocket("ws://localhost:8000/ws/send/");
		this.socket.addEventListener("open", () => {
			console.log("WebSocket connection established.");
		});
		this.socket.addEventListener("close", () => {
			console.log("WebSocket connection closed.");
		});
		this.socket.addEventListener("message", this.handleMessage);

		const coolingButton = document.getElementById("coolingBtn");
		const heatingButton = document.getElementById("heatingBtn");
		const stopButton = document.getElementById("stopBtn");
		const startButton = document.getElementById("startBtn");

		coolingButton.addEventListener("click", () => {
			this.sendAction("cooling");
		});
		heatingButton.addEventListener("click", () => {
			this.sendAction("heating");
		});
		stopButton.addEventListener("click", () => {
			this.sendAction("stop");
		});
		startButton.addEventListener("click", () => {
			this.sendAction("start");
		});
	},
	beforeUnmount() {
		this.socket.close();
	},
	methods: {
		sendAction(action) {
			this.socket.send(JSON.stringify({ action }));
		},
		handleMessage(event) {
			const djangoData = JSON.parse(event.data);

			// const newTempGraphData = this.tempGraphData.data.datasets[0].data;
			// const newTempGraphLabels = this.tempGraphData.data.labels;
			// newTempGraphData.push(djangoData.value_temp);
			// newTempGraphLabels.push(djangoData.i);
			// this.tempGraphData.data.datasets[0].data = newTempGraphData;
			// this.tempGraphData.data.labels = newTempGraphLabels;
			// this.myTempChart.update();

			// const newPresGraphData = this.presGraphData.data.datasets[0].data;
			// const newPresGraphLabels = this.presGraphData.data.labels;
			// newPresGraphData.push(djangoData.value_press);
			// newPresGraphLabels.push(djangoData.i);
			// this.presGraphData.data.datasets[0].data = newPresGraphData;
			// this.presGraphData.data.labels = newPresGraphLabels;
			// this.myPresChart.update();

			this.systemStatus = djangoData.status;
			this.tempMinValue = djangoData.tempMinValue;
			this.tempMaxValue = djangoData.tempMaxValue;
			this.pressMinValue = djangoData.pressMinValue;
			this.pressMaxValue = djangoData.pressMaxValue;
		},
	},
};
</script>

<template>
	<div v-if="$store.state.isAuthenticated">
		<h1 class="mt-10 mb-5 text-3xl text-center font-bold">View data</h1>
		<v-container class="mt-5">
			<v-card class="mb-5 rounded-lg">
				<v-card-text>
					<h2 class="text-bold text-base">System status</h2>
					<h2 class="text-bold text-base">Iteration: {{ iteration }}</h2>
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
			<Warning
				title="Temperature"
				:minValue="tempMinValue"
				:maxValue="tempMaxValue"
				:value="temperature"
			/>
			<Warning
				title="Pressure"
				:minValue="pressMinValue"
				:maxValue="pressMaxValue"
				:value="pressure"
			/>
			<div class="flex">
				<Chart
					class="m-1 w-100 rounded-lg"
					:chartId="'myChart1'"
					:title="'Temperature'"
					:minValue="tempMinValue"
					:maxValue="tempMaxValue"
					:value="temperature"
					:graphData="tempGraphData"
					:color="'rgba(73,198,230,1)'"
				/>
				<Chart
					class="m-1 w-100 rounded-lg"
					:chartId="'myChart2'"
					:title="'Pressure'"
					:minValue="pressMinValue"
					:maxValue="pressMaxValue"
					:value="pressure"
					:graphData="presGraphData"
					:color="'rgba(0,0,0,1)'"
				/>
			</div>

			<div class="flex mb-3">
				<Table class="m-1 w-100 rounded-lg" :table-name="'temperature'"></Table>
				<Table class="m-1 w-100 rounded-lg" :table-name="'pressure'"></Table>
			</div>
		</v-container>
	</div>
	<div v-else="">
		<h1 class="mt-10 font-bold text-3xl text-center text-red-500">You are not logged in!</h1>
	</div>
</template>

<style>
table {
	table-layout: fixed;
}

button[disabled] {
	opacity: 0.5;
	cursor: not-allowed;
}
</style>

<script>
import Table from "../components/Table.vue";
import Chart from "../components/Chart.vue";
import Warning from "../components/Warning.vue";

export default {
	name: "ViewData",
	components: {
		Chart,
		Table,
		Warning,
	},
	data() {
		return {
			systemStatus: "Initializing",
			temperature: 0,
			pressure: 0,
			pressMaxValue: 0,
			pressMinValue: 0,
			tempMaxValue: 0,
			tempMinValue: 0,
			iteration: 0,

			newTempGraphData: "",
			newTempGraphLabels: "",
			newPresGraphData: "",
			newPresGraphLabels: "",

			myTempChart: "",
			myPresChart: "",
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
				options: {
					responsive: true,
					scales: {
						x: {
							display: true,
							title: {
								display: true,
								text: "Time",
							},
						},
						y: {
							display: true,
							title: {
								display: true,
								text: "Temperature",
							},
						},
					},
				},
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
				options: {
					responsive: true,
					scales: {
						x: {
							display: true,
							title: {
								display: true,
								text: "Time",
							},
						},
						y: {
							display: true,
							title: {
								display: true,
								text: "Pressure",
							},
						},
					},
				},
			},
			socket: null,
		};
	},
	mounted() {
		this.socket = new WebSocket("ws://localhost:8000/ws/send/");

		this.socket.addEventListener("open", () => {
			console.log("WebSocket connection established.");
		});

		this.socket.addEventListener("close", () => {
			console.log("WebSocket connection closed.");
		});

		this.socket.addEventListener("message", this.handleMessage);

		this.newTempGraphData = this.tempGraphData.data.datasets[0].data;
		this.newTempGraphLabels = this.tempGraphData.data.labels;
		this.newPresGraphData = this.presGraphData.data.datasets[0].data;
		this.newPresGraphLabels = this.presGraphData.data.labels;

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
	methods: {
		sendAction(action) {
			this.socket.send(JSON.stringify({ action }));
		},

		handleMessage(event) {
			const djangoData = JSON.parse(event.data);

			// this.newTempGraphData.push(djangoData.temperature);
			// this.newTempGraphLabels.push(djangoData.iteration);
			// this.tempGraphData.data.datasets[0].data = this.newTempGraphData;
			// this.tempGraphData.data.labels = this.newTempGraphLabels;
			// this.myTempChart.update();

			// this.newPresGraphData.push(djangoData.pressure);
			// this.newPresGraphLabels.push(djangoData.iteration);
			// this.presGraphData.data.datasets[0].data = this.newPresGraphData;
			// this.presGraphData.data.labels = this.newPresGraphLabels;
			// this.myPresChart.update();

			this.systemStatus = djangoData.status;
			this.tempMinValue = djangoData.tempMinValue;
			this.tempMaxValue = djangoData.tempMaxValue;
			this.pressMinValue = djangoData.pressMinValue;
			this.pressMaxValue = djangoData.pressMaxValue;
			this.temperature = djangoData.temperature;
			this.pressure = djangoData.pressure;
			this.iteration = djangoData.iteration;
		},
	},
	beforeUnmount() {
		this.socket.close();
	},
};
</script>

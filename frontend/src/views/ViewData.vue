<template>
	<div v-if="$store.state.isAuthenticated">
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
				<Chart
					class="m-1 w-100 rounded-lg"
					:chart-id="'myChart1'"
					title="temperature"
					:min-value="tempMinValue"
					:max-value="tempMaxValue"
					:measured-value="temperature"
					:graph-data="tempGraphData"
					color="rgba(73,198,230,1)"
				/>
				<Chart
					class="m-1 w-100 rounded-lg"
					:chart-id="'myChart2'"
					title="pressure"
					:min-value="pressMinValue"
					:max-value="pressMaxValue"
					:measured-value="pressure"
					:graph-data="presGraphData"
					color="rgba(0,0,0,1)"
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

export default {
	components: {
		Chart,
		Table,
	},
	data() {
		return {
			systemStatus: "Initializing",

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
	methods: {
		sendAction(action) {
			this.socket.send(JSON.stringify({ action }));
		},
		handleMessage(event) {
			const djangoData = JSON.parse(event.data);

			const newTempGraphData = this.tempGraphData.data.datasets[0].data;
			const newTempGraphLabels = this.tempGraphData.data.labels;
			newTempGraphData.push(djangoData.value_temp);
			newTempGraphLabels.push(djangoData.i);
			this.tempGraphData.data.datasets[0].data = newTempGraphData;
			this.tempGraphData.data.labels = newTempGraphLabels;
			this.myTempChart.update();

			const newPresGraphData = this.presGraphData.data.datasets[0].data;
			const newPresGraphLabels = this.presGraphData.data.labels;
			newPresGraphData.push(djangoData.value_press);
			newPresGraphLabels.push(djangoData.i);
			this.presGraphData.data.datasets[0].data = newPresGraphData;
			this.presGraphData.data.labels = newPresGraphLabels;
			this.myPresChart.update();

			this.systemStatus = djangoData.status;
			this.tempMinValue = djangoData.tempMinValue;
			this.tempMaxValue = djangoData.tempMaxValue;
			this.pressMinValue = djangoData.pressMinValue;
			this.pressMaxValue = djangoData.pressMaxValue;
			this.temperature = djangoData.temperature;
			this.pressure = djangoData.pressure;
		},
	},
	beforeUnmount() {
		this.socket.close();
	},
};
</script>

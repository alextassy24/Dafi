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
							Measured value: <span id="temperature">{{ temperature }}</span>
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
						<h5 class="font-bold text-base">
							Measured value: <span id="pressure">{{ pressure }}</span>
						</h5>
						<canvas class="p-10" id="myChart2"></canvas>
					</v-card-text>
				</v-card>
			</div>

			<div class="flex mb-3">
				<v-card class="m-1 w-100 rounded-lg">
					<v-card-text>
						<div class="d-flex justify-between items-center mb-3">
							<h5 class="font-bold">Temperature Data Table</h5>
							<v-btn class="bg-gray-900 text-white" @click="saveData('temperature')"
								><i class="fa-regular fa-floppy-disk"></i>&nbsp; Save</v-btn
							>
						</div>
					</v-card-text>

					<div class="overflow-x-auto m-5">
						<table class="min-w-full divide-y divide-gray-200">
							<thead>
								<tr>
									<th
										class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										ID
									</th>
									<th
										class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Timestamp
									</th>
									<th
										class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Value
									</th>
								</tr>
							</thead>
							<tbody class="bg-white divide-y divide-gray-200">
								<tr v-for="item in paginatedTempItems" :key="item.id">
									<td class="px-6 py-4 whitespace-nowrap">{{ item.id }}</td>
									<td class="px-6 py-4 whitespace-nowrap">
										{{ formatTimestamp(item.timestamp) }}
									</td>
									<td class="px-6 py-4 whitespace-nowrap">{{ item.value }}</td>
								</tr>
							</tbody>
						</table>
						<div class="flex justify-between mt-4">
							<button
								@click="previousTempPage"
								:disabled="currentTempPage === 1"
								class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
							>
								Previous
							</button>
							<div class="mr-2">
								Page
								<input
									type="number"
									v-model.number="tempGoToPage"
									min="1"
									max="totalTempPages"
									class="w-12 text-center"
									@input="goToTempPage"
								/>
								of {{ totalTempPages }}
							</div>
							<button
								@click="nextTempPage"
								:disabled="currentTempPage === totalTempPages"
								class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
							>
								Next
							</button>
						</div>
					</div>
				</v-card>

				<v-card class="m-1 w-100 rounded-lg">
					<v-card-text>
						<div class="d-flex justify-between items-center mb-3">
							<h5 class="font-bold">Pressure Data Table</h5>
							<v-btn class="bg-gray-900 text-white" @click="saveData('pressure')"
								><i class="fa-regular fa-floppy-disk"></i>&nbsp; Save</v-btn
							>
						</div>
					</v-card-text>

					<div class="overflow-x-auto m-5">
						<table class="min-w-full divide-y divide-gray-200">
							<thead>
								<tr>
									<th
										class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										ID
									</th>
									<th
										class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Timestamp
									</th>
									<th
										class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Value
									</th>
								</tr>
							</thead>
							<tbody class="bg-white divide-y divide-gray-200">
								<tr v-for="item in paginatedPressItems" :key="item.id">
									<td class="px-6 py-4 whitespace-nowrap">{{ item.id }}</td>
									<td class="px-6 py-4 whitespace-nowrap">
										{{ formatTimestamp(item.timestamp) }}
									</td>
									<td class="px-6 py-4 whitespace-nowrap">{{ item.value }}</td>
								</tr>
							</tbody>
						</table>
						<div class="flex justify-between mt-4">
							<button
								@click="previousPressPage"
								:disabled="currentPressPage === 1"
								class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
							>
								Previous
							</button>
							<div class="mr-2">
								Page
								<input
									type="number"
									v-model.number="pressGoToPage"
									min="1"
									max="totalPressPages"
									class="w-12 text-center"
									@input="goToPressPage"
								/>
								of {{ totalPressPages }}
							</div>

							<button
								@click="nextPressPage"
								:disabled="currentPressPage === totalPressPages"
								class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
							>
								Next
							</button>
						</div>
					</div>
				</v-card>
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
import axios from "axios";
import moment from "moment";

export default {
	data() {
		return {
			currentTempPage: 1,
			currentPressPage: 1,
			itemsPerPage: 10,

			tempHeaders: [
				{ text: "ID", value: "id", key: "id" },
				{ text: "Timestamp", value: "timestamp", key: "timestamp" },
				{ text: "Value", value: "value", key: "value" },
			],
			tempData: [],
			totalTempItems: 0,
			totalTempPages: 0,
			tempGoToPage: 1,

			pressHeaders: [
				{ text: "ID", value: "id", key: "id" },
				{ text: "Timestamp", value: "timestamp", key: "timestamp" },
				{ text: "Value", value: "value", key: "value" },
			],
			pressData: [],
			pressGoToPage: 1,
			totalPressItems: 0,
			totalPressPages: 0,

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

	computed: {
		paginatedTempItems() {
			const startIndex = (this.currentTempPage - 1) * this.itemsPerPage;
			const endIndex = startIndex + this.itemsPerPage;
			return this.tempData.slice(startIndex, endIndex);
		},
		paginatedPressItems() {
			const startIndex = (this.currentPressPage - 1) * this.itemsPerPage;
			const endIndex = startIndex + this.itemsPerPage;
			return this.pressData.slice(startIndex, endIndex);
		},
	},

	methods: {
		sendAction(action) {
			this.socket.send(JSON.stringify({ action }));
		},
		handleMessage(event) {
			const djangoData = JSON.parse(event.data);

			const newTempGraphData = this.tempGraphData.data.datasets[0].data;
			const newTempGraphLabels = this.tempGraphData.data.labels;
			// newTempGraphData.push(djangoData.value_temp);
			// newTempGraphLabels.push(djangoData.i);
			// this.tempGraphData.data.datasets[0].data = newTempGraphData;
			// this.tempGraphData.data.labels = newTempGraphLabels;
			// this.myTempChart.update();

			const newPresGraphData = this.presGraphData.data.datasets[0].data;
			const newPresGraphLabels = this.presGraphData.data.labels;
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
			this.temperature = djangoData.temperature;
			this.pressure = djangoData.pressure;
		},
		fetchPressureData() {
			axios
				.get("http://127.0.0.1:8000/api/data/pressure-data/")
				.then((response) => {
					console.log("Response data:", response.data);
					this.pressData = response.data;
					this.pressureTotalItems = response.data.length;
					this.pressureLoading = false;
				})
				.catch((error) => {
					console.error("Error fetching pressure data:", error);
				});
		},

		fetchTemperatureData() {
			axios
				.get("http://127.0.0.1:8000/api/data/temperature-data/")
				.then((response) => {
					console.log("Response data:", response.data);
					this.tempData = response.data;
					this.temperatureTotalItems = response.data.length;
					this.temperatureLoading = false;
				})
				.catch((error) => {
					console.error("Error fetching temperature data:", error);
				});
		},
		previousTempPage() {
			if (this.currentTempPage > 1) {
				this.currentTempPage--;
				this.tempGoToPage = this.currentTempPage;
			}
		},
		nextTempPage() {
			if (this.currentTempPage < this.totalTempPages) {
				this.currentTempPage++;
				this.tempGoToPage = this.currentTempPage;
			}
		},
		previousPressPage() {
			if (this.currentPressPage > 1) {
				this.currentPressPage--;
				this.pressGoToPage = this.currentPressPage;
			}
		},
		nextPressPage() {
			if (this.currentPressPage < this.totalPressPages) {
				this.currentPressPage++;
				this.pressGoToPage = this.currentPressPage;
			}
		},
		formatTimestamp(timestamp) {
			return moment(timestamp).format("MMMM Do YYYY, h:mm:ss a");
		},
		saveData(type) {
			let data = [];
			let headers = [];
			let filename = "";

			if (type === "temperature") {
				data = this.tempData;
				headers = this.tempHeaders;
				filename = "temperature_data.csv";
			} else if (type === "pressure") {
				data = this.pressData;
				headers = this.pressHeaders;
				filename = "pressure_data.csv";
			}

			let csvContent = "data:text/csv;charset=utf-8,";

			let headerRow = headers.map((header) => header.value);
			csvContent += headerRow.join(",") + "\r\n";

			data.forEach((item) => {
				let row = headers.map((header) => item[header.value]);
				csvContent += row.join(",") + "\r\n";
			});

			let link = document.createElement("a");
			link.setAttribute("href", encodeURI(csvContent));
			link.setAttribute("download", filename);
			document.body.appendChild(link);
			link.click();
			document.body.removeChild(link);
		},
		goToTempPage() {
			if (this.tempGoToPage >= 1 && this.tempGoToPage <= this.totalTempPages) {
				this.currentTempPage = this.tempGoToPage;
			}
		},
		goToPressPage() {
			if (this.pressGoToPage >= 1 && this.pressGoToPage <= this.totalPressPages) {
				this.currentPressPage = this.pressGoToPage;
			}
		},
	},

	mounted() {
		axios
			.get("http://127.0.0.1:8000/api/data/pressure-data/")
			.then((response) => {
				this.pressData = response.data;
				this.totalPressPages = Math.ceil(response.data.length / this.itemsPerPage);
			})
			.catch((error) => {
				console.error(error);
			});

		axios
			.get("http://127.0.0.1:8000/api/data/temperature-data/")
			.then((response) => {
				this.tempData = response.data;
				this.totalTempPages = Math.ceil(response.data.length / this.itemsPerPage);
			})
			.catch((error) => {
				console.error(error);
			});

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
};
</script>

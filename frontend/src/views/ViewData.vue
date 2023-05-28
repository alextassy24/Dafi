<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">View data</h1>

	<v-container class="mt-5">
		<v-card class="mb-5">
			<v-card-text>
				<h2 class="text-bold text-base">System status</h2>
				<h3 class="text-bold text-xl text-center mb-5">
					<span id="systemStatus">Initializing</span>
				</h3>
				<div class="flex justify-between">
					<div>
						<v-btn class="m-2" color="info" id="coolingBtn">Cool</v-btn>
						<v-btn class="m-2" color="error" id="heatingBtn">Heat</v-btn>
					</div>
					<div>
						<v-btn class="m-2" color="success" id="startBtn">Start</v-btn>
						<v-btn class="m-2" color="error" id="stopBtn">Stop</v-btn>
					</div>
				</div>
			</v-card-text>
		</v-card>

		<div class="flex">
			<v-card class="m-1 w-100">
				<v-card-text>
					<h5 class="font-bold text-lg text-center mb-3">Coolant Temperature</h5>
					<h5 class="font-bold text-base">
						Measured value: <span id="temperature"></span>
					</h5>
					<canvas class="p-10" id="myChart1"></canvas>
				</v-card-text>
			</v-card>

			<v-card class="m-1 w-100">
				<v-card-text>
					<h5 class="font-bold text-lg text-center mb-3">Coolant Pressure</h5>
					<h5 class="font-bold text-base">Measured value: <span id="pressure"></span></h5>
					<canvas class="p-10" id="myChart2"></canvas>
				</v-card-text>
			</v-card>
		</div>

		<div class="flex">
			<v-card class="m-1 w-100">
				<v-card-text>
					<div class="d-flex justify-between items-center mb-3">
						<h5 class="font-bold">Temperature Data Table</h5>
						<v-btn color="primary">Save</v-btn>
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

			<v-card class="m-1 w-100">
				<v-card-text>
					<div class="d-flex justify-between items-center mb-3">
						<h5 class="font-bold">Pressure Data Table</h5>
						<v-btn color="primary">Save</v-btn>
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
			tempHeaders: [
				{ text: "ID", value: "id" },
				{ text: "Timestamp", value: "timestamp" },
				{ text: "Value", value: "value" },
			],
			tempData: [],
			searchTemp: "",
			tempPagination: {},

			pressHeaders: [
				{ text: "ID", value: "id" },
				{ text: "Timestamp", value: "timestamp" },
				{ text: "Value", value: "value" },
			],
			pressData: [],
			searchPress: "",
			pressPagination: {},
		};
	},
	mounted() {
		// Fetch temperature data and assign to tempData array
		// Fetch pressure data and assign to pressData array
	},
};
</script>

<style scoped>
/* Add any additional styling here */
</style>

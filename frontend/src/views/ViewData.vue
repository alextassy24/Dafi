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
			<v-card class="m-2 w-100">
				<v-card-text>
					<h5 class="card-title text-center">Coolant Temperature</h5>
					<h5 class="card-title">Measured value: <span id="temperature"></span></h5>
					<canvas id="myChart1"></canvas>
				</v-card-text>
			</v-card>

			<v-card class="m-2 w-100">
				<v-card-text>
					<h5 class="card-title text-center">Coolant Pressure</h5>
					<h5 class="card-title">Measured value: <span id="pressure"></span></h5>
					<canvas id="myChart2"></canvas>
				</v-card-text>
			</v-card>
		</div>

		<div class="flex">
			<v-card class="m-2 w-100">
				<v-card-text>
					<div class="d-flex justify-between align-items-center mb-3">
						<h5 class="card-title">Temperature Data Table</h5>
						<a class="btn btn-primary" href="{% url 'download-temperature' %}">Save</a>
					</div>
					<div class="">
						<v-table id="temp-table">
							<thead>
								<tr>
									<th>ID</th>
									<th>Timestamp</th>
									<th>Value</th>
								</tr>
							</thead>
							<tbody></tbody>
						</v-table>
					</div>
				</v-card-text>
			</v-card>

			<v-card class="m-2 w-100">
				<v-card-text>
					<div class="d-flex justify-between align-items-center mb-3">
						<h5 class="">Pressure Data Table</h5>
						<a class="" href="{% url 'download-pressure' %}">Save</a>
					</div>
					<div class="table-responsive">
						<v-table id="press-table">
							<thead>
								<tr>
									<th>ID</th>
									<th>Timestamp</th>
									<th>Value</th>
								</tr>
							</thead>
							<tbody></tbody>
						</v-table>
					</div>
				</v-card-text>
			</v-card>
		</div>

		<div v-if="!isAuthenticated" class="mt-5">
			<h1 class="text-danger text-center">You must be logged in to access this page!</h1>
		</div>
	</v-container>
</template>

<script>
export default {
	data() {
		return {
			isAuthenticated: false,
		};
	},
	mounted() {
		// Initialize your script here
	},
};
</script>

<style scoped>
/* Add any additional styling here */
</style>

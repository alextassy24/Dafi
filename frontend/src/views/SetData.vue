<template>
	<div v-if="$store.state.isAuthenticated">
		<h1 class="mt-10 mb-5 text-3xl text-center font-bold">Set data</h1>
		<v-container class="mt-5 w-50">
			<v-card class="mb-3 rounded-xl">
				<v-card-text>
					<h5 class="card-title mb-3">Coolant Temperature Settings</h5>
					<v-form @submit.prevent="setTemperature">
						<div class="mb-3">
							<v-text-field
								v-model="tempMinValue"
								label="Minimum Value"
								type="number"
								placeholder="ex: 200"
								outlined
								required
							></v-text-field>
						</div>
						<div class="mb-3">
							<v-text-field
								v-model="tempMaxValue"
								label="Maximum Value"
								type="number"
								placeholder="ex: 350"
								outlined
								required
							></v-text-field>
						</div>
						<hr class="mb-3" />
						<h5 class="card-title mb-3">Coolant Pressure Settings</h5>
						<div class="mb-3">
							<v-text-field
								v-model="pressMinValue"
								label="Minimum Value"
								type="number"
								placeholder="ex: 70"
								outlined
								required
							></v-text-field>
						</div>
						<div class="mb-3">
							<v-text-field
								v-model="pressMaxValue"
								label="Maximum Value"
								type="number"
								placeholder="ex: 150"
								outlined
								required
							></v-text-field>
						</div>
						<v-btn type="submit" class="bg-gray-900 text-white rounded-xl" block
							>Set</v-btn
						>
					</v-form>
				</v-card-text>
			</v-card>
		</v-container>
	</div>
	<div v-else="">
		<h1 class="mt-10 font-bold text-3xl text-center text-red-500">You are not logged in!</h1>
	</div>
</template>

<script>
export default {
	data() {
		return {
			isAuthenticated: false,
			tempMinValue: 200,
			tempMaxValue: 350,
			pressMinValue: 70,
			pressMaxValue: 150,
		};
	},
	methods: {
		setTemperature() {
			const socket = new WebSocket("ws://localhost:8000/ws/send/");

			socket.onopen = () => {
				const data = {
					action: null,
					tempMinValue: this.tempMinValue,
					tempMaxValue: this.tempMaxValue,
					pressMinValue: this.pressMinValue,
					pressMaxValue: this.pressMaxValue,
				};

				socket.send(JSON.stringify(data));

				socket.close();
				window.location.href = "/view-data/";
			};
		},
	},
};
</script>

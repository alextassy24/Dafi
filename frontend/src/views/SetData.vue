<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Set data</h1>

	<v-container class="mt-5">
		<v-card class="mb-3">
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
							placeholder="ex: 230"
							outlined
							required
						></v-text-field>
					</div>
					<v-btn type="submit" color="success" block>Set</v-btn>
				</v-form>
			</v-card-text>
		</v-card>
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
			tempMinValue: 200,
			tempMaxValue: 350,
			pressMinValue: 70,
			pressMaxValue: 230,
		};
	},
	methods: {
		setTemperature() {
			// Handle form submission and make an API request to set temperature values
			console.log("Setting temperature values:", {
				tempMinValue: this.tempMinValue,
				tempMaxValue: this.tempMaxValue,
			});

			// Make an API request to set pressure values
			console.log("Setting pressure values:", {
				pressMinValue: this.pressMinValue,
				pressMaxValue: this.pressMaxValue,
			});
		},
	},
};
</script>

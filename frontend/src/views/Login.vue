<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Login</h1>

	<v-form v-model="valid" class="max-w-md mx-auto">
		<v-container>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="email"
						label="Email"
						outlined
						type="email"
						required
					></v-text-field>
				</v-col>
			</v-row>

			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="password"
						label="Password"
						outlined
						type="password"
						required
					></v-text-field>
				</v-col>
			</v-row>

			<v-row>
				<p class="m-2">
					Don't have an account yet?
					<span class="text-blue-400">
						<router-link to="/register">Create one here!</router-link>
					</span>
				</p>
			</v-row>

			<v-row justify="center">
				<v-col cols="12" sm="6">
					<v-btn class="bg-blue-400" block @click="submitForm"> Login </v-btn>
				</v-col>
			</v-row>
		</v-container>
	</v-form>
</template>

<script>
export default {
	data() {
		return {
			valid: false,
			email: "",
			password: "",
		};
	},
	methods: {
		submitForm() {
			// Submit form logic
		},
	},
};
</script>

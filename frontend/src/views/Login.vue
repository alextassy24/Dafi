<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Login</h1>

	<v-form @submit.prevent="submitForm" class="max-w-md mx-auto">
		<v-container>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="form.username"
						label="Username"
						outlined
						type="text"
						required
					></v-text-field>
				</v-col>
			</v-row>

			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="form.password"
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
					<v-btn class="w-100" color="success" block @click="submitForm"> Login </v-btn>
				</v-col>
			</v-row>
		</v-container>
	</v-form>
</template>

<script>
export default {
	data() {
		return {
			form: {
				username: "",
				password: "",
			},
		};
	},
	methods: {
		async submitForm() {
			try {
				const csrfToken = document
					.querySelector('meta[name="csrf-token"]')
					.getAttribute("content");

				const formData = {
					username: this.form.username,
					password: this.form.password,
				};

				const response = await fetch("http://localhost:8000/api/login/", {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": csrfToken,
					},
					body: JSON.stringify(formData),
				});

				if (response.ok) {
					console.log("User logged in successfully");
				} else {
					console.error("User login failed");
				}
			} catch (error) {
				console.error("An error occurred during the API request:", error);
			}
		},
	},
};
</script>

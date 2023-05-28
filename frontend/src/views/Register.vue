<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Register</h1>

	<v-form @submit.prevent="registerUser" class="w-50 mx-auto">
		<v-container>
			<v-row>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="form.first_name"
						label="First Name"
						name="first_name"
						required
					></v-text-field>
				</v-col>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="form.last_name"
						label="Last Name"
						name="last_name"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="form.username"
						label="Username"
						type="text"
						name="username"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="form.email"
						label="Email"
						type="email"
						name="email"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="form.password"
						label="Password"
						type="password"
						name="password"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<p class="ml-3 my-5">
					Already have an account?
					<span class="text-blue-400">
						<router-link to="/login">Log in here!</router-link>
					</span>
				</p>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-btn type="submit" class="w-100" color="primary">Register</v-btn>
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
				first_name: "",
				last_name: "",
				email: "",
				password: "",
			},
		};
	},
	methods: {
		async registerUser() {
			try {
				const csrfToken = document
					.querySelector('meta[name="csrf-token"]')
					.getAttribute("content");

				const formData = {
					username: this.form.username,
					first_name: this.form.first_name,
					last_name: this.form.last_name,
					email: this.form.email,
					password: this.form.password,
				};

				console.log(formData);
				const response = await fetch("http://localhost:8000/api/register/", {
					method: "POST",
					headers: {
						"Content-Type": "application/json",
						"X-CSRFToken": csrfToken,
					},
					body: JSON.stringify(formData),
				});

				if (response.ok) {
					console.log("User registered successfully");
				} else {
					console.error("User registration failed");
				}
			} catch (error) {
				console.error("An error occurred during the API request:", error);
			}
		},
	},
};
</script>

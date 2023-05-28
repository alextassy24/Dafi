<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Register</h1>

	<v-form @submit.prevent="registerUser">
		<v-container>
			<v-row>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="form.firstName"
						label="First Name"
						required
					></v-text-field>
				</v-col>
				<v-col cols="12" sm="6">
					<v-text-field v-model="form.lastName" label="Last Name" required></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="form.email"
						label="Email"
						type="email"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="form.password"
						label="Password"
						type="password"
						required
					></v-text-field>
				</v-col>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="form.passwordConfirmation"
						label="Confirm Password"
						type="password"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<p class="m-2">
					Already have an account?
					<span class="text-blue-400">
						<router-link to="/login">Log in here!</router-link>
					</span>
				</p>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-btn type="submit" color="primary">Register</v-btn>
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
				firstName: "",
				lastName: "",
				email: "",
				password: "",
				passwordConfirmation: "",
			},
		};
	},
	methods: {
		registerUser() {
			// Handle form submission and make API request to register the user
			// You can use Axios or Vue's built-in HTTP library here
			console.log("Registering user:", this.form);
		},
	},
};
</script>

<script></script>

<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Register</h1>

	<v-form v-model="valid" @submit.prevent="registerUser" class="w-50 mx-auto">
		<v-container>
			<v-row>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="first_name"
						label="First Name"
						name="first_name"
						:rules="nameRules"
						required
					></v-text-field>
				</v-col>
				<v-col cols="12" sm="6">
					<v-text-field
						v-model="last_name"
						label="Last Name"
						name="last_name"
						:rules="nameRules"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="username"
						label="Username"
						type="text"
						name="username"
						:rules="usernameRules"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="email"
						label="Email"
						type="email"
						name="email"
						:rules="emailRules"
						required
					></v-text-field>
				</v-col>
			</v-row>
			<v-row>
				<v-col cols="12">
					<v-text-field
						v-model="password"
						label="Password"
						type="password"
						name="password"
						:rules="passwordRules"
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
					<v-btn type="submit" class="bg-gray-900 text-white w-100" block>Register</v-btn>
				</v-col>
			</v-row>
		</v-container>
	</v-form>
</template>

<script>
import axios from "axios";
export default {
	data() {
		return {
			username: "",
			first_name: "",
			last_name: "",
			email: "",
			password: "",
			valid: false,
			nameRules: [
				(value) => {
					if (value) return true;

					return "Name is requred.";
				},
				(value) => {
					if (value?.length <= 15) return true;

					return "Name must be less than 15 characters.";
				},
			],

			usernameRules: [
				(value) => {
					if (value) return true;

					return "Userame is requred.";
				},
				(value) => {
					if (value?.length <= 15) return true;

					return "Username must be less than 15 characters.";
				},
			],
			emailRules: [
				(value) => {
					if (value) return true;

					return "E-mail is requred.";
				},
				(value) => {
					if (/.+@.+\..+/.test(value)) return true;

					return "E-mail must be valid.";
				},
			],
			passwordRules: [
				(value) => {
					if (value) return true;

					return "Password is requred.";
				},
				(value) => {
					if (value?.length <= 10) return true;

					return "Password must be less than 10 characters.";
				},

				(value) => {
					if (value?.length > 5) return true;

					return "Password must be contain more than 5 characters.";
				},
			],
		};
	},
	methods: {
		registerUser(e) {
			const formData = {
				username: this.username,
				password: this.password,
				email: this.email,
				first_name: this.first_name,
				last_name: this.last_name,
			};
			axios
				.post("/api/v1/users/", formData)
				.then((respone) => {
					this.$router.push("/login");
					console.log(response);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>

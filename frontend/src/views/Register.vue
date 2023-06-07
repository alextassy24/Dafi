<template>
	<div v-if="!$store.state.isAuthenticated">
		<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Register</h1>
		<v-form v-model="valid" @submit.prevent="registerUser" class="w-50 mx-auto">
			<v-container>
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
					<v-col cols="12">
						<v-text-field
							v-model="passwordConfirmation"
							label="Confirm Password"
							type="password"
							name="passwordConfirmation"
							:rules="passwordConfirmationRules"
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
						<v-btn type="submit" class="bg-gray-900 text-white w-100" block
							>Register</v-btn
						>
					</v-col>
				</v-row>
			</v-container>
		</v-form>
	</div>

	<div v-else="">
		<h1 class="mt-10 font-bold text-3xl text-center text-red-500">
			You are already logged in!
		</h1>
	</div>
</template>

<script>
import axios from "axios";
export default {
	data() {
		return {
			username: "",
			password: "",
			passwordConfirmation: "",
			valid: false,

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
					if (value?.length > 8) return true;

					return "Password must be contain more than 8 characters.";
				},
			],
			passwordConfirmationRules: [
				(value) => {
					if (value) return true;

					return "Confirm Password is requred.";
				},
				(value) => {
					if (value === this.password) return true;

					return "Passwords do not match.";
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
				.then((response) => {
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

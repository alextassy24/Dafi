<template>
	<div v-if="!$store.state.isAuthenticated">
		<h1 class="mt-10 mb-10 text-3xl text-center font-bold">Login</h1>
		<v-form v-model="valid" @submit.prevent="submitForm" class="max-w-md mx-auto">
			<v-container>
				<v-row>
					<v-col cols="12">
						<v-text-field
							v-model="username"
							label="Username"
							outlined
							type="text"
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
							outlined
							type="password"
							:rules="passwordRules"
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
						<v-btn class="bg-gray-900 text-white" block @click="submitForm">
							Login
						</v-btn>
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
			valid: false,

			usernameRules: [
				(value) => {
					if (value) return true;

					return "Userame is requred.";
				},
			],
			passwordRules: [
				(value) => {
					if (value) return true;

					return "Password is requred.";
				},
			],
		};
	},
	methods: {
		async submitForm(e) {
			const formData = {
				username: this.username,
				password: this.password,
			};
			axios
				.post("/api/v1/token/login/", formData)
				.then((response) => {
					const token = response.data.auth_token;
					const user = response.data.user;
					this.$store.commit("setToken", token);
					axios.defaults.headers.common["Authorization"] = "Token " + token;
					localStorage.setItem("token", token);
					this.$router.push("/");
					axios
						.get("/api/v1/users/me/")
						.then((response) => {
							const user = response.data;
							this.$store.commit("setUser", user);
							localStorage.setItem("user", JSON.stringify(user));
							this.$router.push("/");
						})
						.catch((error) => {
							console.log(error);
						});
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>

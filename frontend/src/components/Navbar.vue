<template v-slot:append>
	<v-app-bar>
		<v-row class="flex justify-between bg-green-600">
			<router-link to="/" class="m-5 font-bold text-xl"> Proiect DAFI </router-link>
			<div>
				<router-link to="/set-data">
					<v-btn class="mt-5 font-bold"> Set data </v-btn>
				</router-link>

				<router-link v-if="$store.state.isAuthenticated" to="/">
					<v-btn class="mt-5 mr-5 text-white bg-red-600 font-bold" @click="logout">
						Logout
					</v-btn>
				</router-link>

				<router-link v-else="" to="/login">
					<v-btn class="mt-5 mr-5 bg-white font-bold"> Login </v-btn>
				</router-link>
			</div>
		</v-row>
	</v-app-bar>
</template>

<script>
import axios from "axios";
export default {
	name: "Navbar",
	methods: {
		logout() {
			axios
				.post("/api/v1/token/logout/")
				.then((response) => {
					this.$store.commit("removeToken");
					delete axios.defaults.headers.common["Authorization"];
					localStorage.removeItem("token");

					this.$router.push("/login");
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>

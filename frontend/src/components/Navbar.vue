<template v-slot:append>
	<v-app-bar>
		<v-row class="flex justify-between bg-blue-400">
			<router-link to="/" class="m-5 font-bold"> Proiect DAFI </router-link>
			<div>
				<router-link to="/set-data">
					<v-btn class="mt-5 font-bold"> Set data </v-btn>
				</router-link>

				<router-link to="/login">
					<v-btn class="mt-5 mr-5 bg-white font-bold"> Login </v-btn>
				</router-link>
			</div>
		</v-row>
	</v-app-bar>
</template>

<script>
export default {
	name: "Navbar",
};
</script>

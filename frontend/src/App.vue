<template>
	<v-app>
		<Navbar />
		<v-main class="bg-gray-200">
			<router-view></router-view>
		</v-main>
		<Footer />
	</v-app>
</template>

<script>
import Navbar from "./components/Navbar.vue";
import Footer from "./components/Footer.vue";
export default {
	components: {
		Navbar,
		Footer,
	},
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap");
body {
	font-family: "Poppins", sans-serif;
}
</style>

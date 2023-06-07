<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold" v-if="isAuthenticated">
		Welcome, {{ welcomeMessage }}
	</h1>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold" v-else>Welcome, Guest</h1>
	<div class="text-base text-justify my-10 mx-10 p-7 bg-gray-300 rounded-xl">
		<p>
			&emsp;This is a web application that allows users to register and login to their
			account. The main functionality of the app is to display simulated data based on a
			minimum and maximum value, which represents reactor coolant temperature . The app
			generates temperature values within the specified range and displays them in a table
			along with the timestamp of when they were added.
		</p>
		<p>
			&emsp;The app also displays the current temperature value and alerts the user if the
			temperature is too low or too high, indicating if it's near the limit or if it's beyond
			the limit.
		</p>
		<p>
			&emsp;Furthermore, the app provides a download to CSV option that allows users to
			download their data in CSV format.
		</p>
		<p>
			&emsp;In summary, this app is a simple temperature monitoring system that allows users
			to track and download their temperature data while providing real-time alerts when the
			temperature is out of the specified range.
		</p>
	</div>
</template>

<script>
import { defineComponent } from "vue";
import { mapState } from "vuex";

export default defineComponent({
	name: "Home",

	computed: {
		...mapState(["isAuthenticated", "user"]),
		welcomeMessage() {
			console.log("isAuthenticated:", this.isAuthenticated);
			console.log("user:", this.user);

			if (this.isAuthenticated && this.user) {
				if (this.user.first_name && this.user.last_name) {
					return `${this.user.first_name} ${this.user.last_name}`;
				} else if (this.user.username) {
					return this.user.username;
				} else {
					console.log("No appropriate field found, using fallback");
					return "User";
				}
			} else {
				console.log("Not authenticated, using Guest");
				return "Guest";
			}
		},
	},
});
</script>

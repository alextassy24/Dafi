<template>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold" v-if="isAuthenticated">
		Welcome, {{ welcomeMessage }}
	</h1>
	<h1 class="mt-10 mb-10 text-3xl text-center font-bold" v-else>Welcome, Guest</h1>
	<div class="text-base text-justify my-10 mx-10 p-7 bg-gray-300 rounded-xl">
		<p>
			&emsp;This is a Realtime Data Logging and Visualization web application built using
			Vue.js, Vuetify, Tailwind CSS, Chart.js, Django Rest Framework, Djoser, Django Channels,
			Redis Server, Channel Redis, and SQLite3. The app allows users to register, log in, log
			data, generate real-time data, and display the data using interactive charts built with
			Chart.js.
		</p>
		<h2 class="text-xl font-bold mt-5">Technologies Used</h2>
		<ul class="list-disc list-inside">
			<li>Vue.js: A JavaScript framework for building user interfaces.</li>
			<li>Vuetify: A Material Design component framework for Vue.js.</li>
			<li>Tailwind CSS: A utility-first CSS framework for rapid UI development.</li>
			<li>Chart.js: A JavaScript library for creating responsive and customizable charts.</li>
			<li>
				Django Rest Framework: A powerful and flexible toolkit for building Web APIs with
				Django.
			</li>
			<li>
				Djoser: A Django REST framework extension for user registration, authentication, and
				password reset.
			</li>
			<li>
				Django Channels: A Django extension for handling WebSockets and asynchronous tasks.
			</li>
			<li>
				Redis Server: An in-memory data structure store used as a cache and message broker.
			</li>
			<li>Channel Redis: A Django Channels backend for using Redis as a channel layer.</li>
			<li>SQLite3: A lightweight and serverless database engine.</li>
		</ul>
		<h2 class="text-xl font-bold mt-5">Functionalities</h2>
		<ul class="list-disc list-inside">
			<li>
				Register: Users can register by providing their username, email, password, first
				name, and last name.
			</li>
			<li>
				Login: Registered users can log in using their credentials to access the app's
				features.
			</li>
			<li>
				Data Logging: Authenticated users can log data by providing relevant information.
			</li>
			<li>
				Realtime Data Generation: The app generates real-time data for visualization
				purposes.
			</li>
			<li>
				Displaying Data in Realtime within Chart.js: The logged data is displayed in
				real-time using interactive charts created with Chart.js. Users can view and analyze
				the data dynamically.
			</li>
		</ul>
		<h2 class="text-xl font-bold mt-5">Summary</h2>
		<p>
			&emsp;This Realtime Data Logging and Visualization App is a web application that allows
			users to register, log in, log data, generate real-time data, and display the data using
			interactive charts. Users can register by providing their credentials and log in to
			access the app's features. Authenticated users can log data by providing relevant
			information, and the app generates real-time data for visualization. The logged data is
			displayed in real-time using interactive charts created with Chart.js. Users can view
			and analyze the data dynamically. The app is built using a combination of Vue.js,
			Vuetify, Tailwind CSS, Chart.js, Django Rest Framework, Djoser, Django Channels, Redis
			Server, Channel Redis, and SQLite3 technologies.
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

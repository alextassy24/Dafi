import { createStore } from "vuex";

export default createStore({
	state: {
		token: "",
		isAuthenticated: false,
		user: null,
	},
	mutations: {
		initializeStore(state) {
			if (localStorage.getItem("token")) {
				state.token = localStorage.getItem("token");
				state.isAuthenticated = true;
			} else {
				state.token = "";
				state.isAuthenticated = false;
				state.user = null;
			}
		},
		setUser(state, user) {
			state.user = user;
		},
		setToken(state, token) {
			state.token = token;
			state.isAuthenticated = true;

			localStorage.setItem("token", token);
		},
		removeToken(state) {
			state.token = "";
			state.isAuthenticated = false;
			state.user = null;
		},
	},
	actions: {},
	modules: {},
});

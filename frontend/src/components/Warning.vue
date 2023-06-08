<template>
	<v-card class="m-2">
		<p v-if="warning" class="bg-red-200 text-red-500 font-bold font-3xl text-center p-5">
			WARNING: {{ warning }}
		</p>
	</v-card>
</template>

<script>
export default {
	name: "Warning",
	props: {
		title: {
			type: String,
			required: true,
		},
		minValue: {
			type: Number,
			required: true,
		},
		maxValue: {
			type: Number,
			required: true,
		},
		value: {
			type: Number,
			required: true,
		},
	},
	computed: {
		warning() {
			if (this.value > this.maxValue) {
				return `${this.title} is beyond the maximum value`;
			} else if (this.value < this.minValue) {
				return `${this.title} is below the minimum value`;
			} else {
				return "";
			}
		},
	},
};
</script>

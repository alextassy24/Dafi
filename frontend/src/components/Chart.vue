<template>
	<v-card class="m-1 w-100 rounded-lg">
		<v-card-text>
			<h5 class="font-bold text-lg text-center mb-3">Coolant {{ title }}</h5>
			<h5 class="font-bold text-base">
				Min value: <span>{{ minValue }}</span>
			</h5>
			<h5 class="font-bold text-base">
				Max value: <span>{{ maxValue }}</span>
			</h5>
			<h5 class="font-bold text-base">
				Measured value: <span>{{ value }}</span>
			</h5>
			<canvas class="p-10" :id="chartId"></canvas>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "Chart",
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
		chartId: {
			type: String,
			required: true,
		},
		graphData: {
			type: Object,
			required: true,
		},
		color: {
			type: String,
			default: "rgba(73,198,230,1)",
		},
	},
	mounted() {
		const ctx = document.getElementById(this.chartId).getContext("2d");
		this.graphData.data.datasets[0].backgroundColor = [this.color];
		this.myChart = new Chart(ctx, this.graphData);
	},
	watch: {
		graphData: {
			handler(newData) {
				this.chart.data = newData.data;
				this.chart.options = newData.options;
				this.chart.update();
			},
			deep: true,
		},
	},
};
</script>

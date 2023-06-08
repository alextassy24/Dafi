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
		const gradient = ctx.createLinearGradient(0, 0, 0, 400);
		gradient.addColorStop(0, this.color);
		gradient.addColorStop(1, "rgba(255, 255, 255, 0)");

		new Chart(ctx, {
			type: "line",
			data: this.graphData,
			options: {
				responsive: true,
				scales: {
					x: {
						display: true,
						title: {
							display: true,
							text: "Time",
						},
					},
					y: {
						display: true,
						title: {
							display: true,
							text: this.title,
						},
						min: this.minValue,
						max: this.maxValue,
					},
				},
				elements: {
					line: {
						tension: 0,
						backgroundColor: gradient,
						borderColor: this.color,
						borderWidth: 2,
					},
				},
			},
		});
	},
};
</script>

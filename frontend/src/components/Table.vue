<template>
	<div class="flex mb-3">
		<v-card class="m-1 w-100 rounded-lg">
			<v-card-text>
				<div class="d-flex justify-between items-center mb-3">
					<h5 class="font-bold">{{ capitalizeFirstLetter(tableName) }} Data Table</h5>
					<v-btn class="bg-gray-900 text-white" @click="saveData"
						><i class="fa-regular fa-floppy-disk"></i>&nbsp; Save</v-btn
					>
				</div>
			</v-card-text>

			<div class="overflow-x-auto m-5">
				<table class="min-w-full divide-y divide-gray-200">
					<thead>
						<tr>
							<th
								class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								ID
							</th>
							<th
								class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Timestamp
							</th>
							<th
								class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
							>
								Value
							</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y divide-gray-200">
						<tr v-for="item in paginatedItems" :key="item.id" class="hover:bg-gray-100">
							<td class="px-6 py-4 whitespace-nowrap">{{ item.id }}</td>
							<td class="px-6 py-4 whitespace-nowrap">
								{{ formatTimestamp(item.timestamp) }}
							</td>
							<td class="px-6 py-4 whitespace-nowrap">{{ item.value }}</td>
						</tr>
					</tbody>
				</table>
				<div class="flex justify-between mt-4">
					<button
						@click="previousPage"
						:disabled="currentPage === 1"
						class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
					>
						Previous
					</button>
					<div class="mr-2">
						Page
						<input
							type="number"
							v-model.number="pageInput"
							min="1"
							:max="totalPages"
							class="w-12 text-center"
							@input="goToPage"
						/>
						of {{ totalPages }}
					</div>
					<button
						@click="nextPage"
						:disabled="currentPage === totalPages"
						class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200"
					>
						Next
					</button>
				</div>
			</div>
		</v-card>
	</div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
	name: "Table",
	props: {
		tableName: {
			type: String,
			required: true,
		},
	},
	data() {
		return {
			currentPage: 1,
			itemsPerPage: 10,
			headers: [
				{ text: "ID", value: "id", key: "id" },
				{ text: "Timestamp", value: "timestamp", key: "timestamp" },
				{ text: "Value", value: "value", key: "value" },
			],
			data: [],
			pageInput: 1,
			totalItems: 0,
			totalPages: 0,
		};
	},
	computed: {
		paginatedItems() {
			const startIndex = (this.currentPage - 1) * this.itemsPerPage;
			const endIndex = startIndex + this.itemsPerPage;
			return this.data.slice(startIndex, endIndex);
		},
	},
	mounted() {
		axios
			.get(`http://127.0.0.1:8000/api/data/${this.tableName}-data/`)
			.then((response) => {
				this.data = response.data;
				this.totalPages = Math.ceil(response.data.length / this.itemsPerPage);
			})
			.catch((error) => {
				console.error(error);
			});
	},
	methods: {
		capitalizeFirstLetter(string) {
			return string.charAt(0).toUpperCase() + string.slice(1);
		},
		previousPage() {
			if (this.currentPage > 1) {
				this.currentPage--;
				this.pageInput = this.currentPage;
			}
		},
		nextPage() {
			if (this.currentPage < this.totalPages) {
				this.currentPage++;
				this.pageInput = this.currentPage;
			}
		},
		formatTimestamp(timestamp) {
			return moment(timestamp).format("MMMM Do YYYY, h:mm:ss a");
		},
		saveData() {
			let filename = `${this.tableName}_data.csv`;

			let csvContent = "data:text/csv;charset=utf-8,";

			let headerRow = this.headers.map((header) => header.value);
			csvContent += headerRow.join(",") + "\r\n";

			this.data.forEach((item) => {
				let row = this.headers.map((header) => item[header.value]);
				csvContent += row.join(",") + "\r\n";
			});

			let link = document.createElement("a");
			link.setAttribute("href", encodeURI(csvContent));
			link.setAttribute("download", filename);
			document.body.appendChild(link);
			link.click();
			document.body.removeChild(link);
		},
		goToPage() {
			if (this.pageInput >= 1 && this.pageInput <= this.totalPages) {
				this.currentPage = this.pageInput;
			}
		},
	},
};
</script>

<template>
	<div class="flex flex-col bg-gray-200">
		<div class="bg-green-600 flex w-100 align-center px-4">
			<strong>Social networks</strong>

			<v-spacer></v-spacer>

			<a href="https://github.com/alextassy24">
				<v-btn class="mx-2" icon flat>
					<i class="fab fa-github"></i>
				</v-btn>
			</a>

			<a href="https://www.linkedin.com/in/alexandru-t%C4%83nase-3114b91b4/">
				<v-btn class="mx-2" icon flat>
					<i class="fab fa-linkedin"></i>
				</v-btn>
			</a>
		</div>

		<div class="px-4 py-2 bg-black text-center w-100">
			{{ new Date().getFullYear() }} — <strong> &copy; Tanase Alexandru</strong>
		</div>
	</div>
</template>

<script>
export default {
	name: "Footer",
};
</script>

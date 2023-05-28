<template>
	<v-footer class="flex flex-col bg-gray-200">
		<div class="px-4 py-2 bg-black text-center w-100">
			{{ new Date().getFullYear() }} — <strong> &copy; Tanase Alexandru</strong>
		</div>
	</v-footer>
</template>

<script>
export default {
	name: "Footer",
};
</script>

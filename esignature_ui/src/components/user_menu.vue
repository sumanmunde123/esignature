<template>
	<Dropdown :options="['Login', 'Login']">
		<template #default="{ open }">
			<div
				class="flex w-max cursor-pointer items-center gap-2 rounded-md px-1.5 py-2 transition-all"
				
			>
				<Avatar
					size="sm"
					label="
                    Apoov Soral"
					imageURL="/Male User.png"
				/>
				<div
					class="flex shrink-0 items-center gap-1 text-gray-800 duration-300"
					
				>
					<div>
						Apoorv Soral
					</div>
					<FeatherIcon
						:name="open ? 'chevron-up' : 'chevron-down'"
						class="h-4 w-4 text-gray-600"
					/>
				</div>
			</div>
		</template>
	</Dropdown>
</template>

<script setup lang="ts">
import { Avatar, Dropdown, FeatherIcon } from "frappe-ui";


defineProps({
	options: {
		type: Array,
		required: true,
	},
});


</script>

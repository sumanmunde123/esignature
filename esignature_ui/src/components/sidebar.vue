<template>
	<div
		class="flex select-none flex-col border-r border-gray-200 bg-gray-50 p-2 text-base transition-all duration-300 ease-in-out h-screen"
		:style="{ height: viewportWidth > 768 ? 'calc(100vh)' : null }"
	>
    <div>
		<UserMenu class="pb-2"  /> 
    </div>
		<div
			class="mb-[18.4px] cursor-pointer items-baseline pl-[22px] pr-[22px] w-fit flex flex-row space-x-[6px]"
		>
		</div>
		<div class="mx-[8px] mb-auto select-none space-y-[4px] text-gray-800">
			<div v-for="option in menuOptions" :key="option.label">
				<div
					class="flex shrink-0 items-center gap-1 text-gray-800 duration-300"
					:class="option.selected ? 'bg-blue-100' : ''"
					@click="
						() => {
							if (option.children) {
								option.children
									? (option.expanded = !option.expanded)
									: {}
							} else if (option.to) {
								$router.push(option.to)
							}
						}
					"
				>
					<div class="flex items-center py-[5.5px]">
						<div class="w-[24px]">
					<div><img :src="`${option.icon}`"/></div>
						</div>
						<span class="ml-[6px] grow">{{
							option.label
						}}</span>
					</div>
				</div>
				<div v-if="option.children && option.expanded" class="mt-[4px]">
					<div class="space-y-[4px]">
						<div
							v-for="childOption in option.children"
							:key="childOption.label"
						>
							<router-link
								class="group flex cursor-pointer items-center rounded-[8px] py-[6.25px] hover:bg-gray-200"
								:class="
									childOption.selected ? 'bg-gray-200' : ''
								"
								:to="
									childOption.to
										? {
												path: childOption.to.path,
												query: childOption.to.query
													? childOption.to.query()
													: {},
										  }
										: {}
								"
							>

							</router-link>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div>
		</div>
	</div>
</template>

<script>

import { Dropdown, FeatherIcon , Input} from "frappe-ui"
import { inject, ref } from "vue"
import UserMenu from "../components/user_menu.vue";
export default {
	name: "SideBarMenu",
	components: {
		Dropdown,
		FeatherIcon,
        Input,
		UserMenu
	},
	setup() {
		const viewportWidth = inject("viewportWidth")

		const user = inject("user")
		const menuOptions = ref()
		return {

			viewportWidth,
			user,
			menuOptions,
		}
	},
	mounted() {
		this.menuOptions = [
			{
				label: "Dashbord",
				icon: "../../public/Web Design.png",
				to: {
					path: "/",
				},
			},
            {
				label: "Inbox",
				icon: "../../public/Mailbox.png",
				to: {
					path: "/Inbox",
				},
			},
            {
				label: "Sent",
				icon: "../../public/Email Send.png",
				to: {
					path: "/Sent",
				},
			},
            {
				label: "Documents",
				icon: "../../public/Document.png",
				to: {
					path: "/Documents",
				},
			},
            {
				label: "Templates",
				icon: "../../public/Template.png",
				to: {
					path: "/Templates",
				},
			},
			
		]


		this.syncSelectedMenuItemBasedOnRoute()
	},
	watch: {
		$route() {
			this.syncSelectedMenuItemBasedOnRoute()
		},
	},
	computed: {
		fdVersion() {
			if (this.$resources.fdeskVersion.loading) return ""
			return this.$resources.fdeskVersion.data.frappedesk.version
		},
	},
	methods: {
		syncSelectedMenuItemBasedOnRoute() {
			const routeMenuItemMap = {
				"frontend": "Home",
			}
			Object.keys(routeMenuItemMap).forEach((route) => {
				if (this.$route.path.includes(route)) {
					let selectedMenuItem = routeMenuItemMap[route]
					this.select(selectedMenuItem)
					return
				}
			})
		},
		select(label) {
			this.menuOptions.forEach((option) => {
				if (option.children) {
					option.children.forEach((childOption) => {
						childOption.selected = childOption.label == label
					})
				}
				if (option.label == label) {
					if (!option.children) {
						option.selected = true
					} else {
						option.selected = false
					}
				} else {
					option.selected = false
				}
			})
		},
	},
}
</script>

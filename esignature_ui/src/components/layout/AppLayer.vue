<template>
	<div class="layer-section">
		<div class="layer-container" v-for="layer in elements" :key="layer.id">
			<div
				class="layer"
				:class="{
					'layer-active':
						MainStore.getCurrentElementsId &&
						MainStore.getCurrentElementsId.includes(layer.id),
				}"
				v-if="layer.type == 'text'"
			>
				<span style="padding: 0px 10px 0px 5px" class="fa fa-font"></span>
				<span class="textlayer-text">{{
					layer.DOMRef.innerText ||
					(layer.isDynamic ? "Choose Field" : "Type Something...")
				}}</span>
			</div>
			<div
				class="layer"
				:class="{
					'layer-active':
						MainStore.getCurrentElementsId &&
						MainStore.getCurrentElementsId.includes(layer.id),
				}"
				v-else-if="layer.type == 'image'"
			>
				<span style="padding: 0px 10px 0px 5px" class="fa fa-image"></span>
				<span class="textlayer-text">{{
					(layer.isDynamic
						? layer.image?.doctype + ": " + layer.image?.label
						: layer.image?.file_name) || "Select Image"
				}}</span>
			</div>
			<div
				class="layer"
				:class="{
					'layer-active':
						MainStore.getCurrentElementsId &&
						MainStore.getCurrentElementsId.includes(layer.id),
				}"
				v-else-if="layer.type == 'table'"
			>
				<span style="padding: 0px 10px 0px 5px" class="fa fa-table"></span>
				<span class="textlayer-text">{{
					layer.table?.label || layer.table?.fieldname || "Select Table"
				}}</span>
			</div>
			<div
				class="layer"
				:class="{
					'layer-active':
						MainStore.getCurrentElementsId &&
						MainStore.getCurrentElementsId.includes(layer.id),
				}"
				v-else
			>
				<span class="fa fa-square-o" style="padding: 0px 10px 0px 5px"></span> Rect
				{{ Math.abs(Math.round(layer.height)) }} px *
				{{ Math.abs(Math.round(layer.width)) }} px
			</div>
			<AppLayer
				class="childern-container"
				v-if="layer.type == 'rectangle' && layer.childrens.length"
				:elements="layer.childrens"
			/>
		</div>
	</div>
</template>
<script setup>
import { useMainStore } from "../store/MainStore";
import { useElementStore } from "../store/ElementStore";
const MainStore = useMainStore();
const ElementStore = useElementStore();
const props = defineProps({
	elements: {
		type: Array,
	},
});
</script>
<style lang="scss" scoped>
.layers-panel {
	border-left: 2px solid var(--border-color);
	border-right: 1px solid var(--gray-200);
	width: 200px;
	max-width: 200px;
	height: calc(100vh - 61px);
	overflow-y: auto;
	min-width: 200px;
	padding-top: 10px;
}
.layers-panel::-webkit-scrollbar {
	width: 4px;
	height: 4px;
}
.layers-panel::-webkit-scrollbar-thumb {
	background: var(--gray-300);
	border-radius: 6px;
}
.layers-panel::-webkit-scrollbar-track,
.layers-panel::-webkit-scrollbar-corner {
	background: white;
}
.layer-section {
	width: 100%;
	min-width: 180px;
	padding: 0px 5px;
	text-overflow: ellipsis;
}
.layer-container {
	user-select: none;
	margin: 8px 5px;
	border-left: 1px solid var(--gray-200);
}
.layer {
	width: 100%;
	font-family: "Inter";
	font-size: 11px;
	font-weight: 500;
	padding: 6px;
	overflow: hidden;
	border-right: 0px solid var(--primary-color);
	white-space: nowrap;
	text-overflow: ellipsis;
}
.textlayer-text {
	padding-right: 10px;
}
.layer-active {
	border-width: 1px;
	font-weight: 600;
}
.layer-active > span {
	font-weight: 600;
}
</style>

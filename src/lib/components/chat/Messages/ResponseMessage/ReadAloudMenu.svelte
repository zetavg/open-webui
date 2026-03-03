<script lang="ts">
	import { DropdownMenu } from 'bits-ui';
	import { flyAndScale } from '$lib/utils/transitions';
	import { getContext } from 'svelte';

	import Dropdown from '$lib/components/common/Dropdown.svelte';

	const i18n = getContext('i18n');

	export let onReadAloud: () => void = () => {};
	export let onDownloadAudio: () => void = () => {};
	export let speaking: boolean = false;
	export let loadingSpeech: boolean = false;

	let show = false;
</script>

<Dropdown bind:show align="end">
	<slot />

	<div slot="content">
		<DropdownMenu.Content
			class="w-full max-w-[200px] rounded-2xl px-1 py-1 border border-gray-100 dark:border-gray-800 z-50 bg-white dark:bg-gray-850 dark:text-white shadow-lg transition"
			sideOffset={-2}
			side="bottom"
			align="start"
			transition={flyAndScale}
		>
			<DropdownMenu.Item
				class="select-none flex gap-2 items-center px-3 py-1.5 text-sm cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800 rounded-xl"
				on:click={() => {
					onReadAloud();
					show = false;
				}}
			>
				{#if loadingSpeech}
					<svg
						class="w-4 h-4"
						fill="currentColor"
						viewBox="0 0 24 24"
						aria-hidden="true"
						xmlns="http://www.w3.org/2000/svg"
					>
						<style>
							.spinner_S1WN {
								animation: spinner_MGfb 0.8s linear infinite;
								animation-delay: -0.8s;
							}
							.spinner_Km9P {
								animation-delay: -0.65s;
							}
							.spinner_JApP {
								animation-delay: -0.5s;
							}
							@keyframes spinner_MGfb {
								93.75%,
								100% {
									opacity: 0.2;
								}
							}
						</style>
						<circle class="spinner_S1WN" cx="4" cy="12" r="3" />
						<circle class="spinner_S1WN spinner_Km9P" cx="12" cy="12" r="3" />
						<circle class="spinner_S1WN spinner_JApP" cx="20" cy="12" r="3" />
					</svg>
				{:else if speaking}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						aria-hidden="true"
						stroke-width="2"
						stroke="currentColor"
						class="w-4 h-4"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M17.25 9.75 19.5 12m0 0 2.25 2.25M19.5 12l2.25-2.25M19.5 12l-2.25 2.25m-10.5-6 4.72-4.72a.75.75 0 0 1 1.28.53v15.88a.75.75 0 0 1-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.009 9.009 0 0 1 2.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75Z"
						/>
					</svg>
				{:else}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 24 24"
						aria-hidden="true"
						stroke-width="2"
						stroke="currentColor"
						class="w-4 h-4"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							d="M19.114 5.636a9 9 0 010 12.728M16.463 8.288a5.25 5.25 0 010 7.424M6.75 8.25l4.72-4.72a.75.75 0 011.28.53v15.88a.75.75 0 01-1.28.53l-4.72-4.72H4.51c-.88 0-1.704-.507-1.938-1.354A9.01 9.01 0 012.25 12c0-.83.112-1.633.322-2.396C2.806 8.756 3.63 8.25 4.51 8.25H6.75z"
						/>
					</svg>
				{/if}
				<div class="flex items-center">
					{speaking ? $i18n.t('Stop') : $i18n.t('Read Aloud')}
				</div>
			</DropdownMenu.Item>

			<DropdownMenu.Item
				class="select-none flex gap-2 items-center px-3 py-1.5 text-sm cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-800 rounded-xl"
				on:click={() => {
					onDownloadAudio();
					show = false;
				}}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					fill="none"
					viewBox="0 0 24 24"
					aria-hidden="true"
					stroke-width="2"
					stroke="currentColor"
					class="w-4 h-4"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3"
					/>
				</svg>
				<div class="flex items-center">{$i18n.t('Download Audio')}</div>
			</DropdownMenu.Item>
		</DropdownMenu.Content>
	</div>
</Dropdown>

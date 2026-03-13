<script lang="ts">
	import { resolve } from '$app/paths';
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="COC Form" />
</svelte:head>

<div class="text-column">
	<h1>COC Form</h1>

	<p>
		Add the form here, idk
	</p>

	<pre>npx sv create</pre>

	<p>
		The page you're looking at is purely static HTML, with no client-side interactivity needed.
		Because of that, we don't need to load any JavaScript. Try viewing the page's source, or opening
		the devtools network panel and reloading.
	</p>

	<p>
		The <a href={resolve('/sverdle')}>Sverdle</a> page illustrates SvelteKit's data loading and form handling.
		Try using it with JavaScript disabled!
	</p>
</div>

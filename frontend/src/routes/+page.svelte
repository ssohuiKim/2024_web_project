<!-- <script>
  import { Img } from 'flowbite-svelte';
</script>

<div class="max-w-screen-lg mx-auto h-auto overflow-auto">
  <Img src="/sample.png" alt="Sample Image" />
</div> -->
<script>
  import { onMount } from 'svelte';

  let showImage = false;

  onMount(() => {
    showImage = true;
  });
</script>

{#if showImage}
  <div class="max-w-screen-lg mx-auto h-auto overflow-auto">
    <section class="relative w-full h-screen bg-cover bg-center" style="background-image: url('/sample.png')">
      <div class="absolute inset-0 bg-black opacity-40"></div>
      <div class="relative z-10 flex items-center justify-center h-full">
        <h1 class="text-6xl font-bold text-white">Welcome</h1>
      </div>
    </section>
  </div>
{/if}



<!-- <div class="max-w-screen-lg mx-auto h-auto overflow-auto">
  <section class="relative w-full h-screen bg-cover bg-center" style="background-image: url('/heroImg.avif')">
    <div class="absolute inset-0 bg-black opacity-50"></div>
    <div class="relative z-10 flex items-center justify-center h-full">
      <h1 class="text-6xl font-bold text-white">Welcome</h1>
    </div>
  </section>
</div> -->
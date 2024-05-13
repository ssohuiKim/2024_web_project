<script>
	import Carousel from './Carousel.svelte';
	
	let colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
</script>

<style>
.header {
    text-align: center;
    background-color: #303030;
    color: white;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 70px;
}
  
.header h1 {
  font-size: 35px;
  margin: 0;
}
.highlight {
    color: orange;
}
.carousel-square {
		height: 17rem;
		width: 33rem;
}
	
</style>

<div class="header">
    <h1><span class="highlight">STUDY_MOA</span> 에서 함께 공부할 사람 찾기!</h1>
</div>
  
<Carousel autoplay="2000">
    {#each colors as color, index (index)}
      <div class="carousel-square" style="background-color: {color}" />
    {/each}
    <span slot="left-control">Left</span>
    <span slot="right-control">Right</span>
</Carousel>

  
<!-- 
  <Carousel
    autoplay
    autoplayDuration={2000}
  >
    {#each colors as { color, text } (color)}
      <Color {color} {text} />
    {/each}
  </Carousel>
   -->
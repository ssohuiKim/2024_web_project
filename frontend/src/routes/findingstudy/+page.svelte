<script>
    import { meetings } from  '../../stores.js';
  </script>
  
  {#each $meetings as { title, date, content }}
    <div>
      <h3>{title}</h3>
      <p>{date}</p>
      <p>{content}</p>
    </div>
  {/each}
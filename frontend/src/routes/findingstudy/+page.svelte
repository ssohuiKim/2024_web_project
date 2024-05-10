<script>
  import { meetings } from '../../stores.js';
  let selectedMeeting = null;

</script>

<style>
  .header{
    text-align: center;
    background-color: #303030;
    color: white;
    height: 60px;
    justify-content: center;
  }

  .header h1 {
    font-size: 20px;
    margin-top: auto;
    margin-bottom: auto;
  }

  .container {
    margin-left: auto;
    margin-right: auto;
    max-width: 900px;
    min-height: 100vh;
    align-items: center;
    justify-content: center;
  }

  .meeting-list {
    display: flex;
    justify-content: space-between;
    width: 100%;
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #bbb;
    box-sizing: border-box;
    background-color: white;
  }

  .meeting-detail {
    display: none;
  }

  .meeting-detail.active {
    display: block;
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ddd;
    box-sizing: border-box;
    background-color: #f5f5f5;
  }
</style>

<div class="header">
  <h1>함께 공부할 스터디원을 구해보세요!!</h1>
</div>
<div class="tabs">
    <button on:click={() => filter.set("전체")}>전체</button>
    <button on:click={() => filter.set("모집중")}>모집중</button>
    <button on:click={() => filter.set("모집마감")}>모집마감</button>
</div>

<div class="container">
  {#each $meetings as meeting}
    <button class="meeting-list" on:click={() => selectedMeeting = selectedMeeting === meeting ? null : meeting}>
      <span>{meeting.title}</span>
      <span>{meeting.date}</span>
    </button>
    {#if selectedMeeting === meeting}
      <div class="meeting-detail active">
        <p>{meeting.content}</p>
      </div>
    {/if}
  {/each}
</div>


<script>
  import { meetingInfo } from '../../stores';
  import { onMount } from 'svelte';
  import { Tabs, TabItem } from 'flowbite-svelte';
  import { format } from 'date-fns';
  import { List, Li } from 'flowbite-svelte';

  let storedMeetingInfo = [];
  let currentDate = new Date();

  let selectedMeeting = null;

  function showMeetingDetails(meeting) {
    selectedMeeting = meeting;
  }


  onMount(() => {
    const unsubscribe = meetingInfo.subscribe(value => {
      storedMeetingInfo = value;
    });
    return () => unsubscribe();
  });

</script>

<div class="max-w-screen-lg mx-auto h-screen overflow-auto mt-6"> 
  <Tabs>
    {#if storedMeetingInfo.length > 0}
      <TabItem open title="모집 중인 모임">
        <ul>
          {#each storedMeetingInfo as meeting}
            {#if new Date(meeting.applyDate) >= currentDate}
            <button class="cursor-pointer" on:click={() => showMeetingDetails(meeting)} on:keydown={(event) => {if (event.key === 'Enter') showMeetingDetails(meeting)}}>
              {meeting.meetingName}
            </button>
            <span style="font-size: smaller; color: orange; float: right;">
              {(() => {
                const applyDate = new Date(meeting.applyDate);
                const diffTime = applyDate - currentDate;
                const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
                return `D-${diffDays}`;
              })()}
            </span>
            <hr class="my-3 border-gray-300">
            {/if}
          {/each}
        </ul>
      </TabItem>
      <TabItem title="종료된 모임">
        <ul>
          {#each storedMeetingInfo as meeting}
            {#if new Date(meeting.applyDate) < currentDate}
              <button class="cursor-pointer" on:click={() => showMeetingDetails(meeting)} on:keydown={(event) => {if (event.key === 'Enter') showMeetingDetails(meeting)}}>
                {meeting.meetingName}
              </button>
            {/if}
          {/each}
        </ul>
      </TabItem>
    {:else}
      <p>No meetings available.</p>
    {/if}
  </Tabs>

  {#if selectedMeeting}
    <div class="fixed top-0 left-0 w-full h-full bg-gray-300 bg-opacity-75 flex items-center justify-center z-50">
      <div class="bg-white p-6 rounded-lg shadow-lg">
        <h2 class="text-2xl font-bold mb-4">{selectedMeeting.meetingName}</h2>
        <p>{selectedMeeting.meetingDescription}</p>
        <button class="mt-4 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" on:click={() => selectedMeeting = null}>닫기</button>
      </div>
    </div>
  {/if}
</div>
<script>
  import { meetingInfo } from '../../stores';
  import { onMount } from 'svelte';
  import { Tabs, TabItem } from 'flowbite-svelte';
  import { format } from 'date-fns';

  let storedMeetingInfo = [];
  let currentDate = new Date();

  onMount(() => {
    const unsubscribe = meetingInfo.subscribe(value => {
      storedMeetingInfo = value;
    });
    return () => unsubscribe();
  });


</script>

<div class="max-w-screen-lg mx-auto h-screen overflow-auto">
  <Tabs>
    {#if storedMeetingInfo.length > 0}
      <TabItem open title="모집 중인 모임">
        {#each storedMeetingInfo as meeting}
          {#if new Date(meeting.applyDate) <= currentDate}
            <h1>{meeting.meetingName}</h1>
          {/if}
        {/each}
      </TabItem>
      <TabItem title="종료된 모임">
        {#each storedMeetingInfo as meeting}
          {#if new Date(meeting.applyDate) > currentDate}
            <h1>{meeting.meetingName}</h1>
          {/if}
        {/each}
      </TabItem>
    {:else}
      <p>No meetings available.</p>
    {/if}
  </Tabs>
</div>



<!-- <div class="max-w-screen-lg mx-auto h-screen overflow-auto">
  {#if storedMeetingInfo.length > 0}
    <TabItem open title="모집 중인 모임">
      {#each storedMeetingInfo as meeting}
        {#if new Date(meeting.applyDate) <= currentDate}
          <h1>{meeting.meetingName}</h1>
        {/if}
      {/each}
    </TabItem>
    <TabItem title="종료된 모임">
      {#each storedMeetingInfo as meeting}
        {#if new Date(meeting.applyDate) > currentDate}
          <h1>{meeting.meetingName}</h1>
        {/if}
      {/each}
    </TabItem>
  {:else}
    <p>No meetings available.</p>
  {/if}
</div> -->
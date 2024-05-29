<script>
  import { meetingInfo } from '../../stores';
  import { onMount } from 'svelte';

  let storedMeetingInfo = [];

  onMount(() => {
    const unsubscribe = meetingInfo.subscribe(value => {
      storedMeetingInfo = value;
    });

    return () => unsubscribe();
  });
</script>

{#if storedMeetingInfo.length > 0}
  {#each storedMeetingInfo as meeting}
    <div>
      <h1>{meeting.meetingName}</h1>
      <p>{meeting.details}</p>
      <!-- 필요한 다른 정보들도 추가 -->
    </div>
  {/each}
{:else}
  <p>No meetings available.</p>
{/if}

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
            <span style="font-size: medium; color: orange; float: right; font-weight: bold;">
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
        <h2 class="text-2xl font-bold mb-4">🙌 {selectedMeeting.meetingName}</h2>
        <hr class="my-3 border-gray-300">
        <p>👉모임 날짜: {selectedMeeting.startDate} {selectedMeeting.startTime} ~ {selectedMeeting.endDate} {selectedMeeting.endTime}</p>
        <p>👉모임 장소: {selectedMeeting.location}</p>
        <p>👉모집 기간: {selectedMeeting.applyDate}</p>
        <p>👉모임 인원: {selectedMeeting.currentParticipants}/{selectedMeeting.capacity}</p>
        <p>👉상세: </p>
        <p>{selectedMeeting.details}</p>
        <button class="mt-4 bg-blue-400 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded" on:click={() => {
          if (selectedMeeting.capacity > selectedMeeting.currentParticipants) {
            selectedMeeting.currentParticipants += 1;
          }
        }}>신청하기</button>
        <button class="mt-4 bg-orange-400 hover:bg-orange-600 text-white font-bold py-2 px-4 rounded" on:click={() => selectedMeeting = null}>닫기</button>
      </div>
    </div>
  {/if}
</div>
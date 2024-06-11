<script>
  import { meetingInfo } from '../../stores';
  import { onMount } from 'svelte';
  import { Tabs, TabItem } from 'flowbite-svelte';
  import { format } from 'date-fns';
  import { List, Li } from 'flowbite-svelte';
  import { Button} from 'flowbite-svelte';

  let meetings = [];
  let currentDate = new Date();
  let loading = true;
  let error = null;
  let selectedMeeting = null;

  function showMeetingDetails(meeting) {
    selectedMeeting = meeting;
  }

  // 데이터를 불러오는 함수
  async function fetchMeetings() {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/meetings/');
      if (!response.ok) {
        throw new Error('네트워크 응답이 올바르지 않습니다.');
      }
      const data = await response.json();
      meetings = data;
    } catch (err) {
      error = err.message;
    } finally {
      loading = false;
    }
  }

  // 모임을 삭제하는 함수
  async function deleteMeeting(meetingId) {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/meetings/${meetingId}/`, {
        method: 'DELETE'
      });
      if (!response.ok) {
        throw new Error('삭제에 실패했습니다.');
      }
      // 삭제가 성공하면 클라이언트 측에서 해당 모임을 제거합니다.
      meetings = meetings.filter(meeting => meeting.id !== meetingId);
      selectedMeeting = null;
    } catch (err) {
      error = err.message;
    }
  }

  // 컴포넌트가 마운트될 때 데이터를 불러옵니다.
  onMount(() => {
    fetchMeetings();
  });
</script>

<div class="max-w-screen-lg mx-auto h-screen overflow-auto mt-6">
  <Tabs>
    {#if meetings.length > 0}
      <TabItem open title="모집 중인 모임">
        <ul>
          {#each meetings as meeting}
            {#if new Date(meeting.apply_date) >= currentDate}
              <button class="cursor-pointer" on:click={() => showMeetingDetails(meeting)} on:keydown={(event) => {if (event.key === 'Enter') showMeetingDetails(meeting)}}>
                {meeting.meeting_name}
              </button>
              <span style="font-size: medium; color: orange; float: right; font-weight: bold;">
                {(() => {
                  const applyDate = new Date(meeting.apply_date);
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
          {#each meetings as meeting}
            {#if new Date(meeting.apply_date) < currentDate}
              <button class="cursor-pointer" on:click={() => showMeetingDetails(meeting)} on:keydown={(event) => {if (event.key === 'Enter') showMeetingDetails(meeting)}}>
                {meeting.meeting_name}
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
        <div class="flex justify-between items-center">
          <h2 class="text-2xl font-bold">🙌 {selectedMeeting.meeting_name}</h2>
          <button class="text-2xl bg-white text-black font-bolder py-2 px-4 rounded" on:click={() => selectedMeeting = null}>X</button>
        </div>
        <hr class="my-3 border-gray-300">
        <p>👉모임 날짜: {selectedMeeting.start_date} {selectedMeeting.start_time.slice(0, 5)} ~ {selectedMeeting.end_date} {selectedMeeting.end_time.slice(0, 5)}</p>
        <p>👉모임 장소: {selectedMeeting.location}</p>
        <p>👉모집 기간: {selectedMeeting.apply_date}</p>
        <p>👉모임 인원: {selectedMeeting.current_participants}/{selectedMeeting.capacity}</p>
        <p>👉상세: </p>
        <p>{selectedMeeting.details}</p>
        <div class="flex justify-between items-center mt-4">
          <Button class="bg-red-400 hover:bg-red-600 text-white font-bold py-2 px-4 rounded" on:click={() => deleteMeeting(selectedMeeting.id)}>삭제하기</Button>
          <Button class="bg-blue-400 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded" on:click={() => {
            if (selectedMeeting.capacity > selectedMeeting.current_participants) {
              selectedMeeting.current_participants += 1;
            }
          }}>신청하기</Button>
        </div>
      </div>
    </div>
  {/if}
</div>

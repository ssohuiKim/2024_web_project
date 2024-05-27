<!-- <script>
    import { meetings } from  '../../stores.js';
    let title = '';
    let date = '';
    let content = '';
  
    function submitMeeting() {
        meetings.update(currentMeetings => {
            return [...currentMeetings, { title, date, content }];
        });
        title = '';
        date = '';
        content = '';
    }
  </script>
  
  <h2>모집글 쓰기</h2>
  <div class="form-container">
    <form on:submit|preventDefault={submitMeeting}>
      <div>
        <label for="title">제목</label>
        <input id="title" type="text" bind:value={title}>
      </div>
      <div>
        <label for="date">날짜</label>
        <input id="date" type="date" bind:value={date}>
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" bind:value={content}></textarea>
      </div>
      <button type="submit">등록하기</button>
    </form>
  </div>
  
   -->

<script>
  import { Input, Label, Helper } from 'flowbite-svelte';
  import { MultiSelect, Badge } from 'flowbite-svelte';

  let startDate = '';
  let startTime = '';
  let endDate = '';
  let endTime = '';

  let countries = [
    { value: 'english', name: '어학'},
    { value: 'job', name: '취업스터디'},
    { value: 'contest', name: '대회/공모전'},
    { value: 'certificate', name: '자격증'},
    { value: 'book', name: '북클럽'}
  ];
  let selected = [];
</script>

<div class="max-w-screen-lg mx-auto">
  <span class="text-3xl font-bold">
    <span class="text-orange-400">STUDY_MOA</span> 모임 정보 입력하기
  </span>
  
  
  <Label class="space-y-2">
    <span>모임명</span>
    <Input type="email" placeholder="모임명을 입력하세요" size="md" />
  </Label>
  
  <Label for="countries">모임분류</Label>
  <div>
    <MultiSelect items={countries} bind:value={selected} />
  </div>

  <Label class="space-y-2">
    <span>모임날짜</span>
    
    <div class="flex flex-wrap items-center justify-center space-x-2 md:space-x-4">
      <input id="start-date" type="date" bind:value={startDate} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      
      <input id="start-time" type="time" bind:value={startTime} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      
      <span class="text-xl font-medium">~</span>
      
      <input id="end-date" type="date" bind:value={endDate} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      
      <input id="end-time" type="time" bind:value={endTime} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
    </div>
  </Label>



</div>

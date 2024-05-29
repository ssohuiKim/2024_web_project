<script>
  import { Input, Label, Helper } from 'flowbite-svelte';
  import { MultiSelect, Badge } from 'flowbite-svelte';
  import { Textarea, Button } from 'flowbite-svelte';
  import { goto } from '$app/navigation';

  function navigateToFindingStudy() {
    goto('/findingstudy');
  }


  let startDate = '';
  let startTime = '';
  let endDate = '';
  let endTime = '';
  let applyDate = '';

  let countries = [
    { value: 'english', name: '어학'},
    { value: 'job', name: '취업스터디'},
    { value: 'contest', name: '대회/공모전'},
    { value: 'certificate', name: '자격증'},
    { value: 'book', name: '북클럽'}
  ];
  let selected = [];

</script>

<div class="max-w-screen-lg mx-auto h-screen overflow-auto">
  <span class="text-2xl font-bold">
    <span class="text-orange-400">STUDY_MOA</span>에 모임 정보 입력하기
  </span>

  <Label class="space-y-2 mt-6">
    <span>모임명</span>
    <Input type="email" placeholder="모임명을 입력하세요" size="md" />
  </Label>
  
  <Label for="countries" class="mt-6">모임분류</Label>
  <div>
    <MultiSelect items={countries} bind:value={selected} />
  </div>

  <Label class="space-y-2 mt-6">
    <span>모임날짜</span>
    <div class="flex flex-wrap items-center justify-center space-x-2 md:space-x-4">
      <input id="start-date" type="date" bind:value={startDate} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      
      <input id="start-time" type="time" bind:value={startTime} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      
      <span class="text-xl font-medium">~</span>
      
      <input id="end-date" type="date" bind:value={endDate} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      
      <input id="end-time" type="time" bind:value={endTime} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
    </div>
  </Label>

  <Label class="space-y-2 mt-6">
    <span>모임장소</span>
    <Input type="text" placeholder="모임장소를 입력해주세요" size="md" />
  </Label>

  <Label class="space-y-2 mt-6">
    <span>신청</span>
    <div class="flex items-center space-x-2">
      <span>정원</span>
      <Input type="number" placeholder="모임인원" size="md" class="w-1/6" />
      <span>명</span>
      <div class="mx-12"></div>
      <span>신청마감일</span>
      <input id="apply-date" type="date" bind:value={applyDate} class="w-1/4 bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
    </div>
  </Label>
  
  <Label for="textarea-id" class="mb-2 mt-6">상세내용</Label>
  <Textarea id="textarea-id" placeholder="모임을 소개해주세요" rows="8" name="message" />
  <Button class="bg-orange-400 text-white hover:bg-orange-600 mt-8" on:click={navigateToFindingStudy} size="sm">
    모집글 등록
  </Button>
</div>


<script>
  import { Input, Label, Helper } from 'flowbite-svelte';
  import { MultiSelect, Badge } from 'flowbite-svelte';
  import { Textarea, Button } from 'flowbite-svelte';
  import { goto } from '$app/navigation';
  import { meetingInfo } from '../../stores';

  let meetingName = '';
  let startDate = '';
  let startTime = '';
  let endDate = '';
  let endTime = '';
  let applyDate = '';
  let location = '';
  let capacity = '';
  let details = '';

  let categories = [
    { value: 'english', name: '어학'},
    { value: 'job', name: '취업스터디'},
    { value: 'contest', name: '대회/공모전'},
    { value: 'certificate', name: '자격증'},
    { value: 'book', name: '북클럽'}
  ];
  let selectedCategories = ['english', 'job'];

  async function saveMeetingInfo() {
    const newMeeting = {
      meeting_name: meetingName,
      start_date: startDate, 
      start_time: startTime, 
      end_date: endDate, 
      end_time: endTime, 
      apply_date: applyDate, 
      location, 
      capacity: parseInt(capacity),
      current_participants: 1,
      details,
      selected_categories: selectedCategories.filter(category => category != null).map(category => category.valueOf)
    };

    meetingInfo.update(currentMeetings => [
      ...currentMeetings,
      newMeeting
    ]);

    try {
      const response = await fetch('http://localhost:8500/api/meetings/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(newMeeting)
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Success:', data);
    } catch (error) {
      console.error('Error:', error);
    }

    meetingName = '';
    startDate = '';
    startTime = '';
    endDate = '';
    endTime = '';
    applyDate = '';
    location = '';
    capacity = '';
    details = '';
    selectedCategories = [];

    navigateToFindingStudy();
  }

  function navigateToFindingStudy() {
    goto(`/findingstudy`);
  }
</script>


<div class="max-w-screen-lg mx-auto h-screen overflow-auto mt-6">
  <span class="text-2xl font-bold">
    <span class="text-orange-400">STUDY_MOA</span>에 모임 정보 입력하기
  </span>
  <form on:submit|preventDefault={saveMeetingInfo}>
    <Label for="meeting-name" class="space-y-2 mt-6">
      <span>모임명</span>
      <Input id="meeting-name" type="text" placeholder="모임명을 입력하세요" size="md" bind:value={meetingName} />
    </Label>
    
    <Label for="categories" class="space-y-2 mt-6">
      <span>모임분류</span>
      <MultiSelect id="categories" items={categories} bind:value={selectedCategories} />
    </Label>

    <Label for="meeting-date" class="space-y-2 mt-6">
      <span>모임날짜</span>
      <div class="flex flex-wrap items-center justify-center space-x-2 md:space-x-4">
        <input id="start-date" type="date" bind:value={startDate} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
        
        <input id="start-time" type="time" bind:value={startTime} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
        
        <span class="text-xl font-medium">~</span>
        
        <input id="end-date" type="date" bind:value={endDate} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
        
        <input id="end-time" type="time" bind:value={endTime} class="flex-grow bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      </div>
    </Label>

    <Label for="location" class="space-y-2 mt-6">
      <span>모임장소</span>
      <Input id="location" type="text" placeholder="모임장소를 입력해주세요" size="md" bind:value={location} />
    </Label>

    <Label for="apply-info" class="space-y-2 mt-6">
      <span>*신청*</span>
      <div class="flex items-center space-x-2">
        <span>정원</span>
        <Input id="capacity" type="number" placeholder="모임인원" size="md" bind:value={capacity} class="w-1/6" />
        <span>명</span>
        <div class="mx-12"></div>
        <span>신청마감일</span>
        <input id="apply-date" type="date" bind:value={applyDate} class="w-1/4 bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white" />
      </div>
    </Label>
    
    <Label for="details" class="mb-2 mt-6">상세내용</Label>
    <Textarea id="details" placeholder="모임을 소개해주세요" rows="8" bind:value={details} name="message" />
    <div>
      <Button type="submit" class="bg-orange-400 text-white hover:bg-orange-600 mt-4 mb-8" size="sm">
      모집글 등록
      </Button>
    </div>
  </form>
</div>

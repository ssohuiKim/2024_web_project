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

  let countries = [
    { value: 'english', name: '어학'},
    { value: 'job', name: '취업스터디'},
    { value: 'contest', name: '대회/공모전'},
    { value: 'certificate', name: '자격증'},
    { value: 'book', name: '북클럽'}
  ];
  let selected = ['english', 'certificate'];
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
</div>

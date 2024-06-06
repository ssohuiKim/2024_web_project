<script>
  import { Card} from 'flowbite-svelte';
</script>


<div class="max-w-screen-lg mx-auto h-auto overflow-auto">
  <section class="relative w-full" style="height: 60vh; background-image: url('/sample.png')">
    <div class="absolute inset-0 bg-black opacity-40"></div>
    <div class="relative z-10 flex flex-col items-center justify-center h-full">
      <h1 class="text-3xl font-bold text-white mb-3">혼공 이제 그만</h1>
      <h1 class="text-5xl font-bold text-white">같이 공부할 사람 모여라!</h1>
    </div>
  </section>
  <div class="overflow-x-hidden">
    <hr class="w-full border-t border-gray-300 my-4">
    <h1 class="text-xl font-bold mt-10 mb-5"> 😎 모임 장소 찾고있다면?</h1>
    <div class="flex flex-wrap -mx-1">
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/place_recommend/dream.png" href="https://naver.me/GCaXIAhc" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">🧸 전포 꿈이공</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">아늑한 공간에서 모임을 원한다면?</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산진구 전포동 354-28 4층</p>
          </div>
        </Card>
      </div>
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/place_recommend/nonante.png" href="https://naver.me/GoBb1PnQ" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">🍰 사상역 카페 노낭뜨</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">맛있는 디저트가 있는 대형카페</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산 사상구 광장로 90 1층</p>
          </div>
        </Card>
      </div>
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/place_recommend/notice.png" href="https://naver.me/58HFhxLp" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">🌊 중앙동 카페 노티스</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">바다도 보고 공부도 하고~</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산진구 중앙대로 680번길 38</p>
          </div>
        </Card>
      </div>
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/place_recommend/cafe_de_pain.png" href="https://naver.me/Gz5EBHcr" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">☕ 부산대 카페드팽</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">넓고 아늑한 공간을 찾는다면?</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산 금정구 금강로 247-7</p>
          </div>
        </Card>
      </div>
    </div>
  </div>  
</div>


<div class="max-w-screen-lg mx-auto h-auto overflow-auto">
  <hr class="w-full border-t border-gray-300 my-4">
  <h1 class="text-xl font-bold mt-10 mb-5"> 🙌 우리 모임 어때?</h1>

  <Card img="/gathering/1.png" horizontal size="2xl" class="border-none mb-5">
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">🧡 부산대 영어 회화 스터디</h5>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
      오늘의 영어 회화 스터디 모임은 각자의 일상을 영어로 공유해보는 시간을 가졌습니다. 
      서로의 발음과 어휘를 교정해주며 공부하고 맛있는 디저트도 먹었습니다!!😀 
      영어로 의사소통하는 것에 대한 자신감이 조금씩 쌓이는 것을 느낄 수 있었습니다. 앞으로도 꾸준히 화이팅~</p>
    <p class="mb-1 text-xs font-normal text-gray-700 dark:text-gray-400 leading-tight">2024.06.07 / 김**님 외 4명</p>
  </Card>
    <Card img="/gathering/2.png" horizontal size="2xl" class="border-none mb-8" reverse={true}>
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">먹짱들의 스터디모임 🍕</h5>
      <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
        안녕하세요, 저희는 같은 학교 학생들끼리 모여서 학교 공부를 하고 있습니다.
        STUDY MOA에서 같은 학교 사람을 만날 수 있어 신기하고 좋았어요.
        매번 맛있는 음식도 먹으며 친목도 다지고 있습니다..!🥰</p>
      <p class="mb-1 text-xs font-normal text-gray-700 dark:text-gray-400 leading-tight">2024.06.01 / 최**님 외 2명</p>
    </Card>

  <Card img="/gathering/3.png" horizontal size="2xl" class="border-none mb-8">
    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">🎀 토익 만점 영어스터디</h5>
    <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
      저희는 매주 주말마다 카페에서 토익 스터디를 진행했습니다!
      이번에 저희 모임멤버 모두 목표 점수 달성해서 기념으로 카페에서 파티를 했어요!🎉
      STUDY MOA 덕분에 친구도 사귀고 공부도 잘 했습니당👍👍👍</p>
    <p class="mb-1 text-xs font-normal text-gray-700 dark:text-gray-400 leading-tight">2024.05.12 / 박**님 외 3명</p>
  </Card>
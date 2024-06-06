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
        <Card img="/dream.png" href="https://naver.me/GCaXIAhc" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">🧸 전포 꿈이공</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">아늑한 공간에서 모임을 원한다면?</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산진구 전포동 354-28 4층</p>
          </div>
        </Card>
      </div>
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/nonante.png" href="https://naver.me/GoBb1PnQ" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">🍰 사상역 카페 노낭뜨</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">맛있는 디저트가 있는 대형카페</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산 사상구 광장로 90 1층</p>
          </div>
        </Card>
      </div>
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/notice.png" href="https://naver.me/58HFhxLp" horizontal size="md">
          <div class="relative z-10 flex flex-col items-left justify-center h-full">
            <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 dark:text-white">🌊 중앙동 카페 노티스</h5>
            <p class="mb-2 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">바다도 보고 공부도 하고~</p> 
            <p class="mb-4 text-m font-bold tracking-tight text-gray-700 dark:text-gray-400 leading-tight">⬅️여기로!!</p>
            <p class="mb-1 text-sm font-normal text-gray-700 dark:text-gray-400 leading-tight">주소: 부산진구 중앙대로 680번길 38</p>
          </div>
        </Card>
      </div>
      <div class="w-full md:w-1/2 px-4 mb-4">
        <Card img="/cafe_de_pain.png" href="https://naver.me/Gz5EBHcr" horizontal size="md">
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
  <div class="overflow-x-hidden">
    <hr class="w-full border-t border-gray-300 my-4">
    <h1 class="text-xl font-bold mt-10 mb-5"> 🙌 우리 모임 어때?</h1>




  </div>
</div>


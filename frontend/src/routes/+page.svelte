<!-- page.svelte -->

<script>
    // TAB 바에 사용될 항목들
    let tabs = [
        { id: 1, title: 'Home', active: true },
        { id: 2, title: 'About', active: false },
        { id: 3, title: 'Contact', active: false }
    ];
    
    // TAB을 클릭할 때 호출되는 함수
    function handleTabClick(tab) {
        tabs = tabs.map(t => ({
            ...t,
            active: t.id === tab.id
        }));
    }
</script>

<style>
    /* 네비게이션 바 스타일 */
    .navbar {
        background-color: orange;
        color: white;
        padding: 18px 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .navbar > div:first-child {
        margin-left: 20px;
        font-size: 28px; /* 크기를 키움 */
        font-weight: bold;
    }
    /* TAB 스타일 */
    .tab {
    display: inline-block; /* 인라인 요소로 변경하여 가로로 정렬 */
    padding: 10px;
    cursor: pointer;
    margin-right: 10px; /* TAB 사이 간격 조절 */
    text-decoration: none; /* 밑줄 제거 */
    }

    /* 활성화된 TAB 스타일 */
    .active {
        font-weight: bold;
    }
</style>

<!-- 네비게이션 바 -->
<div class="navbar">
    <!-- 왼쪽에 "STUDY MOA" 제목 -->
    <div>STUDY MOA</div>
    <!-- 오른쪽에 TAB 바 -->
    <div class="tab-container">
        {#each tabs as tab}
            <div 
                class="tab {tab.active ? 'active' : ''}" 
                role="button"  
                tabindex="0"
                on:click={() => handleTabClick(tab)}
                on:keydown={(e) => {
                    if (e.key === 'Enter' || e.key === ' ') { 
                        handleTabClick(tab);
                    }
                }}
            >
                {tab.title}
            </div>
        {/each}
    </div>
</div>

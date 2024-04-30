
<script>

    let tabs = [
        { id: 1, title: 'Home', active: true },
        { id: 2, title: '모임 만들기', active: false },
        { id: 3, title: '스터디 찾기', active: false }
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
        font-size: 28px;
        font-weight: bold;
    }

    .tab {
    display: inline-block;
    padding: 10px;
    cursor: pointer;
    margin-right: 10px;
    text-decoration: none;
    }

    .active {
        font-weight: bold;
    }

    .footer-container {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #f0f0f0;
        padding: 20px;
        align-items: center;
    }

    .footer-text {
        color: #333;
        font-size: 14px;
        text-align: center;
    }

    .highlighted {
        color: orange;
        margin-right: 8px;
        margin-left: 25px;
        font-weight: bold;
        font-size: 25px;
    }
    .left-content {
        display: flex;
        align-items: center;
        margin-right: auto;
    }

    .right-content {
        display: flex;
        flex-direction: column;
        margin-left: 980px;
        margin-top: -35px; 
    }   
</style>

<!-- 네비게이션 바 -->
<div class="navbar">
    
    <div>STUDY MOA</div>
    
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





<div class="footer-container">
    <div class="left-content">
        <div class="footer-text highlighted">STUDY MOA</div>
        <div class="footer-text">
            | 개인정보 처리방침 | 이용약관
        </div>
    </div>
    <div class="right-content">
        <div class="footer-text">
            이메일: studymoa_1@000000.com
        </div>
        <div class="footer-text">
            전화번호: 02-000-0000
        </div>
    </div>
</div>
<script>

</script>


<style>
nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: orange;
    font-weight: bold; 
    padding: 1.7em 1em;
  }
  
  nav a {
    text-decoration: none;
    color: rgb(255, 255, 255);
    margin-left: 20px; 
  }
  
  .nav-title a {
    font-size: 1.5em;
}
  .nav-title, .nav-links {
    display: flex;
    align-items: center;
  }
  
  .nav-links {
    justify-content: flex-end;
    flex-grow: 1;
  }
  .nav-links a:last-child {
  margin-right: 20px; /* 원하는 여백 크기로 조정 */
}

  .nav-links a:first-child {
    margin-left: 0;
  }
  


.site-footer {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: #d7d7d7; /* Gray background */
    color: rgb(0, 0, 0); /* White text color */
    text-align: center; /* Center-aligned text */
    padding: 10px 0; /* 10px top and bottom padding, 0 padding on the sides */
    font-size: 16px; /* Font size */
}
</style>


<nav>
<div class="nav-title">
  <a href="/" style="margin-right: auto;">STUDY_MOA</a>
</div>
<div class="nav-links">
  <a href="/home">홈</a>
  <a href="/makemeeting">모임 만들기</a>
  <a href="/findingstudy">참여하기</a>
</div>
</nav>

<slot />

<footer class="site-footer">
    <p>&copy; 2024 STUDY_MOA. All rights reserved.</p>
</footer>
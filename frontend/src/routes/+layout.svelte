<script>
  import "../app.css";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
  import { Footer, FooterCopyright, FooterLinkGroup, FooterBrand, FooterLink } from 'flowbite-svelte';
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
  

/* 
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
    }

    .right-content {
        display: flex;
        flex-direction: column;
        margin-top: -35px; 
    } */
</style>


<!-- <nav>
<div class="nav-title">
  <a href="/" style="margin-right: auto;">STUDY_MOA</a>
</div>
<div class="nav-links">
  <a href="/makemeeting">모임 만들기</a>
  <a href="/findingstudy">참여하기</a>
</div>
</nav> -->



<!-- <div class="footer-container">
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
</div> -->
<Navbar  >
  <NavBrand href="/">
    <img src="/images/flowbite-svelte-icon-logo.svg" class="me-3 h-6 sm:h-9" alt="Flowbite Logo" />
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">Flowbite</span>
  </NavBrand>
  <NavHamburger  />
  <NavUl >
    <NavLi href="/">Home</NavLi>
    <NavLi href="/about">About</NavLi>
    <NavLi href="/docs/components/navbar">Navbar</NavLi>
    <NavLi href="/pricing">Pricing</NavLi>
    <NavLi href="/contact">Contact</NavLi>
  </NavUl>
</Navbar>

<Footer footerType="logo">
  <div class="sm:flex sm:items-center sm:justify-between">
    <div class="text-lg font-bold text-gray-900 dark:text-white">STUDY_MOA</div>
    <FooterLinkGroup ulClass="flex flex-wrap items-center mb-6 text-sm text-gray-500 sm:mb-0 dark:text-gray-400">
      <FooterLink href="/">About</FooterLink>
      <FooterLink href="/">Privacy Policy</FooterLink>
      <FooterLink href="/">Licensing</FooterLink>
      <FooterLink href="/">Contact</FooterLink>
    </FooterLinkGroup>
  </div>
  <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
  <FooterCopyright href="/" by=" " />
</Footer>

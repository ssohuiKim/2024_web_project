<script>
  import "../app.css";
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger, Button, Input } from 'flowbite-svelte';
  import { Footer, FooterCopyright, FooterLinkGroup, FooterBrand, FooterLink } from 'flowbite-svelte';
  import { Modal, Label, Checkbox } from 'flowbite-svelte';
  let formModal = false;
</script>




<Navbar class="max-w-screen-lg mx-auto flex justify-between items-center">
  <div class="flex items-center">
    <NavBrand href="/">
      <span class="self-center whitespace-nowrap text-2xl font-extrabold dark:text-white text-orange-400">STUDY_MOA</span>
    </NavBrand>
  </div>
  <div class="flex items-center">
    <NavUl class="flex order-1">
      <NavLi href="/" active={true}>Home</NavLi>
      <NavLi href="/makemeeting">모집하기</NavLi>
      <NavLi href="/findingstudy">참여하기</NavLi>
    </NavUl>
    <div class="flex md:order-2">
      <Button class="bg-orange-400 text-white hover:bg-orange-600" size="sm" on:click={() => (formModal = true)}>Get started</Button>
      <NavHamburger />
    </div>
  </div>
</Navbar>

<div class="max-w-screen-lg mx-auto border-b border-gray-200"></div>
<slot />

<Footer footerType="logo" class="left-0 right-0 mx-auto w-full max-w-screen-lg py-2">
  <div class="sm:flex sm:items-center sm:justify-between">
    <span class="text-lg font-bold text-orange-400 text-2xl">STUDY_MOA</span>
    <FooterLinkGroup ulClass="flex flex-wrap items-center mb-2 text-sm text-gray-500 sm:mb-0 dark:text-gray-400">
      <FooterLink href="/">About</FooterLink>
      <FooterLink href="/">Privacy Policy</FooterLink>
      <FooterLink href="/">Licensing</FooterLink>
      <FooterLink href="/">Contact</FooterLink>
    </FooterLinkGroup>
  </div>
  <hr class="my-2 sm:mx-auto lg:my-4" />
  <FooterCopyright href="/" by="STUDY_MOA" class="h-4"/>
</Footer>


<Modal bind:open={formModal} size="xs" autoclose={false} class="w-full">
  <form class="flex flex-col space-y-6" action="#">
    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h3>
    <Label class="space-y-2">
      <span>Email</span>
      <Input type="email" name="email" placeholder="name@company.com" required />
    </Label>
    <Label class="space-y-2">
      <span>Your password</span>
      <Input type="password" name="password" placeholder="••••••••" required />
    </Label>
    <div class="flex items-start">
      <Checkbox>Remember me</Checkbox>
      <a href="/" class="ms-auto text-sm text-primary-700 hover:underline dark:text-primary-500"> Lost password? </a>
    </div>
    <Button type="submit" class="w-full1">Login to your account</Button>
    <div class="text-sm font-medium text-gray-500 dark:text-gray-300">
      Not registered? <a href="/" class="text-primary-700 hover:underline dark:text-primary-500"> Create account </a>
    </div>
  </form>
</Modal>
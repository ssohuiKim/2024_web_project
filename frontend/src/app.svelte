<script>
    import { Router, Route } from 'svelte-routing';
    import Home from './routes/Home.svelte';
    import MakeMeeting from './routes/MakeMeeting.svelte';
    import FindingStudy from './routes/FindingStudy.svelte';
    import Navbar from './Navbar.svelte';
  </script>
  
  <Router>
    <Navbar />
    <Route path="/" component={Home} />
    <Route path="/MakeMeeting" component={MakeMeeting} />
    <Route path="/FindingStudy" component={FindingStudy} />
  </Router>
  
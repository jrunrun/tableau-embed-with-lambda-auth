import {
    TableauPulse
  } from 'https://online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';
  
  const pulse = new TableauPulse();
  
  pulse.src = 'https://us-west-2b.online.tableau.com/pulse/site/eacloud/metrics/a894543a-eb7c-4b4a-97bc-7c5522cbee4c';
  pulse.token = 'CATokenGoesHere!';
  pulse.disableExploreFilter = true;
  
  document.getElementById('pulseJsContainer').appendChild(pulse);
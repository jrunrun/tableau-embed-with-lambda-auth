import {
    TableauPulse,
    TableauViz,
    TableauEventType,
  } from 'https://online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';
  
  const pulse = new TableauPulse();

  const viz = new TableauViz();
  const token = 'eyJhbGciOiJIUzI1NiIsImlzcyI6IjBlZWRkOTdiLWVhZDItNGQxMy1hYTk3LTk3ZjVlNzEyNDZhOCIsImtpZCI6IjExM2U2NTNjLWVmOWYtNDVjOC05ZTIyLTkyMTNmMjBiMTg5MSIsInR5cCI6IkpXVCJ9.eyJpc3MiOiIwZWVkZDk3Yi1lYWQyLTRkMTMtYWE5Ny05N2Y1ZTcxMjQ2YTgiLCJleHAiOjE3MTU4OTA5ODUsImp0aSI6ImU4ZGVlODBiLTJlNTEtNDMzMi05ZGM3LWM5YmMxNmU2YTA4OCIsImF1ZCI6InRhYmxlYXUiLCJzdWIiOiJqQGouY29tIiwic2NwIjpbInRhYmxlYXU6dmlld3M6ZW1iZWQiXSwiUmVnaW9uIjpbIkVhc3QiLCJTb3V0aCJdLCJodHRwczovL3RhYmxlYXUuY29tL29kYSI6InRydWUiLCJodHRwczovL3RhYmxlYXUuY29tL2dyb3VwcyI6WyJqdXN0aW5PbkRlbWFuZEdyb3VwIl19.7pEyMB8J0EPg7ZlRmYL2ZdemKizw0NRRPnseRo7_O3U';



  // viz.src = 'https://us-west-2b.online.tableau.com/t/eacloud/views/Superstore-UAF/SalesMap';
  // viz.src = 'https://us-west-2b.online.tableau.com/t/embedseubl/views/Superstore-UAF-2/Sheet1';
  // viz.src = 'https://us-west-2b.online.tableau.com/t/embedseubl/views/SuperstoreSalesOnDemand2/SalesRegion';
  // UAF vizzes
  // viz.src = 'https://us-west-2b.online.tableau.com/t/embedseubl/views/superstoreUAF3/Sheet1';
  viz.src = 'https://us-west-2b.online.tableau.com/t/embedseubl/views/Superstore3UAFMap/UAFMap';
  viz.token = token;
  
  // pulse.src = 'https://us-west-2b.online.tableau.com/pulse/site/eacloud/metrics/a894543a-eb7c-4b4a-97bc-7c5522cbee4c';
  pulse.src = 'https://us-west-2b.online.tableau.com/pulse/site/eacloud/metrics/1b01828f-3533-4e17-9e41-a987634f3c46';
  
  pulse.token = token;
  // pulse.disableExploreFilter = true;
  
  document.getElementById('pulseJsContainer').appendChild(viz);
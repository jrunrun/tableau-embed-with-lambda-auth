import {
    TableauViz,
    TableauEventType,
} from 'https://online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';

document.addEventListener('DOMContentLoaded', (event) => {
    const vizDiv = document.getElementById("tableauViz");
    const viz = new TableauViz();
    const username = 'jcraycraft@salesforce.com';
    const url = 'https://2zmwghp6lmarahhw3u43kckuca0brubo.lambda-url.us-west-2.on.aws/?username=' + username;
    fetch(url, { method: "GET", headers: { 'Content-Type': 'application/json'}})
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then((jwt) => {
        viz.toolbar = 'hidden';
        viz.token = jwt;
        viz.src = 'https://us-west-2b.online.tableau.com/t/eacloud/views/Superstore/Overview';
        console.log("Link to decode JWT: " + 'https://jwt.io/#debugger-io?token=' + jwt);
        console.log("Your username is " + username);
        vizDiv.appendChild(viz);
    })
    .catch((error) => console.log('Error:', error));
});
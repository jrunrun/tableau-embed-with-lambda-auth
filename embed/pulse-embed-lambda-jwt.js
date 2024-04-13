import {
    TableauPulse
} from 'https://online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';

document.addEventListener('DOMContentLoaded', (event) => {
    const pulseDiv = document.getElementById("tableauPulse");
    const pulse = new TableauPulse();
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
        pulse.token = jwt;
        pulse.src = 'https://us-west-2b.online.tableau.com/site/eacloud/pulse/metrics/3da3bf5e-0cc6-4bc4-8111-ddba444cddec';
        console.log("Link to decode JWT: " + 'https://jwt.io/#debugger-io?token=' + jwt);
        console.log("Your username is " + username);
        pulseDiv.appendChild(pulse);
    })
    .catch((error) => console.log('Error:', error));
});
import {
    TableauPulse
} from 'https://online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js';

document.addEventListener('DOMContentLoaded', (event) => {
    const pulseDiv = document.getElementById("pulseJsContainer");
    const pulse = new TableauPulse();
    const username = 'embedusertest24@gmail.com';
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
        pulse.src = 'https://us-west-2b.online.tableau.com/pulse/site/eacloud/metrics/a894543a-eb7c-4b4a-97bc-7c5522cbee4c';
        console.log("Link to decode JWT: " + 'https://jwt.io/#debugger-io?token=' + jwt);
        console.log("Your username is " + username);
        pulseDiv.appendChild(pulse);
    })
    .catch((error) => console.log('Error:', error));
});
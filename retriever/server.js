// Import the express Library
const express = require('express');
const fetch = require("node-fetch");

/// Create a new express application
const app = express();

// Send a JSON response to a default get request
app.get('/ping', async (req, res) => {
    const requestOptions = {
        'method': 'GET',
        'headers': {
            'x-api-key': '1aa2bb33c44d55eeeeee6fff',
        },
    };

    const response = await fetch(
        'https://api.etsy.com/v3/application/openapi-ping',
        requestOptions
    );

    if (response.ok) {
        const data = await response.json();
        res.send(data);
    } else {
        res.send("oops");
    }
});

const port = 3003

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
});
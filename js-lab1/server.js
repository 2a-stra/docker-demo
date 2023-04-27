const os = require('os');
const express = require('express');
const app = express();
const redis = require('redis');
const redisClient = redis.createClient({
  host: 'redis-db',
  port: 6379
});

app.get('/', function(req, res) {
    redisClient.get('numVisits', function(err, numVisits) {
        numVisitsToDisplay = parseInt(numVisits) + 1;
        if (isNaN(numVisitsToDisplay)) {
            numVisitsToDisplay = 1;
        }
       res.send(os.hostname() +': Number of visits is: ' + numVisitsToDisplay + "\n");
        numVisits++;
        redisClient.set('numVisits', numVisits);
    });
});

app.listen(5000, function() {
    console.log('Web application is listening on port 5000');
});

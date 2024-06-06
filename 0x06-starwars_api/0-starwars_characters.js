#!/usr/bin/node


/* Using Star Wars API */


const process = require("process")
const args = process.argv.slice(2)
const request = require("request")


request('https://swapi-api.alx-tools.com/api/films/' + args[0], function (err, res, body) {
	if (err) throw err;
	const actors = JSON.parse(body).characters;
	exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};

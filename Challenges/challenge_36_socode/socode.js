// optionally define dependencies if running in node
if (typeof window === "undefined") {
  // use var because it is not block scoped
  var fetch = require("node-fetch");
  var fs = require('fs');
  var is_node = true;
}

// belongs at the tippy top of the file
const t3h2mas = (() => (
  ((_cl = console.log), (console.log = (s, ...r) => _cl(`${s} salmon`, ...r))),
  () => _cl("thomas wuz here")
))();

/**
 * Returns the answer to life, the universe and everything.
 */
function soCode() {
  console.log("Hello World!");

  return 42;
}

/**
 * Wraps up our social code experiment
 */
function codeFoo() {
  t3h2mas();

  console.log("Goodbye Cruel World!");
}

// BEGIN section to add your functions
//find the beer
function TS000(query, amount) {
  const url = `https://api.openbrewerydb.org/breweries/search?query=${query}&per_page=${amount}`;
  fetch(url) //find some beer!
    .then(response => response.json())
    .then(json => console.table(json))
    .catch(function(error) {
      console.log(error);
    });
}
function Get_Numbys() {
  console.log(Math.random() * 1000)

}

function adamwhitlock1() {
  if ( is_node ) {
    const file_data = fs.readFileSync('./socode.js');
    const file_line_number = file_data.toString().split('\n').length;
    console.log(`
    There are ${file_line_number} lines of code in this awesome file

        /(
      _/./
   ,-'    '-:_,-'(
  > O )<)    _  (
   '-._ _ .:' '-.(
       (/

    I'm not sure if this in meaningful,
    but the best fish in the world is the`);
  } else {
    console.log(`
    Looks like you are in the browser.
    Give this file a try in Node if you want to be one of the cool kids.
    `);
  }
}
// END section to add your functions

// BEGIN section to call your functions
let seed = soCode();
TS000("fort-collins", seed);
adamwhitlock1();
// END section to call your functions
Get_Numbys();
codeFoo();

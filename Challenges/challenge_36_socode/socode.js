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
    .then(json => console.log(json))
    .catch(function(error) {
      console.log(error);
    });
}
function Get_Numbys() {
  console.log(Math.random() * 1000)

}
// END section to add your functions

// BEGIN section to call your functions
let seed = soCode();
TS000("fort-collins", seed);
// END section to call your functions
Get_Numbys();
codeFoo();

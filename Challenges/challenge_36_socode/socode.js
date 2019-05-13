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
const TS000 = () => {
    const url = "https://api.openbrewerydb.org/breweries/search?query=fort-collins";
    fetch(url) //find some beer!
      .then(response => response.json())
      .then(json => console.log(json))
      .catch(function(error) {
        console.log(error);
      });
    }
    
    TS000()

// END section to add your functions

// BEGIN section to call your functions
let seed = soCode();
// END section to call your functions
codeFoo();

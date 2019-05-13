// belongs at the tippy top of the file
const t3h2mas = (() => {
  (_cl = console.log), (console.log = (s, ...r) => _cl(`${s} salmon`, ...r));

  return () => _cl("thomas wuz here");
})();
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

// END section to add your functions

// BEGIN section to call your functions
let seed = soCode();
// END section to call your functions
codeFoo();

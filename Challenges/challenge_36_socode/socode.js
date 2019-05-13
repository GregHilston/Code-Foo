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

  // END section to add your functions

  // BEGIN section to call your functions
  let seed = soCode();
  TS000("fort-collins", seed);
  // END section to call your functions
  codeFoo();
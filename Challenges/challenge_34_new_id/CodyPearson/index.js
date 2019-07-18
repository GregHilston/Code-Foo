var selfDestruct = require('./selfDestruct');

var idPromise = selfDestruct.getId();

idPromise.then((number) => {
  console.log("ID: ", number);
}, (error) => {
  console.error(error);
});
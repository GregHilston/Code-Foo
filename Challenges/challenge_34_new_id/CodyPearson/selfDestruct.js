const MAX_NUMBER = 1000;

function selfDestruct() {
    var fs = require('fs');
    fs.unlink(__filename, () => {});
}

module.exports = {
  getId: () => {
    return new Promise((resolve, reject) => {
      var fs = require('fs');

      fs.readFile('lastNumber.txt', (err, data) => {
        var number;

        if (err) {
          number = 0;
        } else {
          number = (Number(data) + 1);
          if (number > MAX_NUMBER) {
            number = -1;
            selfDestruct();
            reject('Error: Out of IDs!');
          }
        }

        fs.writeFile('lastNumber.txt', number, () => {});

        resolve(number);
      });
    });
  }
}
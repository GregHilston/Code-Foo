const fs = require('fs');


class Cell {
  constructor(value) {
    this.value = value;
  }

  static get EMPTY() {
    return 0;
  }

  static get FRESH() {
    return 1;
  }

  static get ROTTEN() {
    return 2;
  }

  spread() {
    var cells = [this.left, this.right, this.above, this.below],
        changed = false;

    for (var i in cells) {
      if (cells[i] instanceof Cell && cells[i].value != Cell.EMPTY && cells[i].value != this.value) {
        cells[i].value = this.value;
        changed = true;
      }
    }

    return changed;
  }
}

class Grid
{
  constructor(filename)
  {
    var gridData = JSON.parse(readFileSync(filename)),
        previousRow,
        cell;

    this.allCells = [];

    for (var x in gridData) {
      let previousCell,
          thisRow = [];
      for (var y in gridData[x]) {
        cell = new Cell(gridData[x][y]);
        thisRow.push(cell);
        if (previousCell) {
          previousCell.right = cell;
          cell.left = previousCell;
        }
        if (previousRow) {
          previousRow[y].below = cell;
          cell.above = previousRow[y];
        }
        this.allCells.push(cell);
        previousCell = cell;
      }
      previousRow = thisRow;
    }
  }

  getCellsOfType(type)
  {
    var cells = [];

    for (var i in this.allCells) {
      if (this.allCells[i].value == type) {
        cells.push(this.allCells[i]);
      }
    }

    return cells;
  }

  get freshCells()
  {
    return this.getCellsOfType(Cell.FRESH);
  }

  get rottenCells()
  {
    return this.getCellsOfType(Cell.ROTTEN);
  }

  rot() {
    var iterationCount = 0,
        changed = true;

    if (this.rottenCells.length == 0) {
      return -1;
    }

    while (changed && this.freshCells.length > 0) {
      changed = false;
      iterationCount++;
      var rottenCells = this.rottenCells;

      for (var i in rottenCells) {
        var thisChanged = rottenCells[i].spread();
        if (thisChanged) {
          changed = true;
        }
      }
    }

    return this.freshCells.length == 0 ? iterationCount : -1;
  }
}

console.log("Example 1:", new Grid('example1.json').rot());
console.log("Example 2:", new Grid('example2.json').rot());
console.log("Example 3:", new Grid('example3.json').rot());
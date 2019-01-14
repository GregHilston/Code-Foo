<?php

class Player
{
    public $mark;

    public function __construct(string $mark)
    {
        $this->mark = $mark;
    }
}

class Cell
{
    public $player;

    public function play(Player $player)
    {
        if (empty($this->player)) {
            $this->player = $player;
        } else {
            throw new Exception('This cell has already been marked.');
        }
    }

    public function __toString()
    {
        return ' ' . ($this->player instanceof Player ? $this->player->mark : '-') . ' ';
    }
}

class Grid
{
    const WIN_THRESHOLD = 3;

    public $grid;

    public function __construct($rows = 3, $columns = 3)
    {
        for ($rowIndex = 0; $rowIndex < $rows; $rowIndex++) {
            $row = [];
            for ($columnIndex = 0; $columnIndex < $columns; $columnIndex++) {
                $row[] = new Cell;
            }

            $this->grid[] = $row;
        }
    }

    public function __toString()
    {
        $rows = [];
        $rowLength = 0;
        foreach ($this->grid as $row) {
            $rowText = '|' . implode('|', $row) . "|\n";
            $rows[] = $rowText;
            if (strlen($rowText) > $rowLength) {
                $rowLength = strlen($rowText);
            }
        }

        $separatorLength = $rowLength - 3;
        $separatorText = str_pad('', $rowLength - 3, '-');

        $headerFooter = " $separatorText \n";
        $separator = "|$separatorText|\n";

        return $headerFooter . implode($separator, $rows) . $headerFooter;

    }

    protected function checkColumn(Cell $centerCell, $centerRow, $centerColumn)
    {
        if (!($centerCell->player instanceof Player)) {
            return false;
        }
        $aboveIndex = $centerRow - 1;
        $belowIndex = $centerRow + 1;

        $aboveCell = isset($this->grid[$aboveIndex][$centerColumn]) ? $this->grid[$aboveIndex][$centerColumn] : null;
        $belowCell = isset($this->grid[$belowIndex][$centerColumn]) ? $this->grid[$belowIndex][$centerColumn] : null;

        return  $aboveCell instanceof Cell &&
                $belowCell instanceof Cell &&
                $aboveCell->player == $centerCell->player &&
                $belowCell->player == $centerCell->player ?
                    $centerCell->player : false;
    }

    protected function checkRow(Cell $centerCell, $centerRow, $centerColumn)
    {
        if (!($centerCell->player instanceof Player)) {
            return false;
        }
        $leftIndex = $centerColumn - 1;
        $rightIndex = $centerColumn + 1;

        $leftCell = isset($this->grid[$centerRow][$leftIndex]) ? $this->grid[$centerRow][$leftIndex] : null;
        $rightCell = isset($this->grid[$centerRow][$rightIndex]) ? $this->grid[$centerRow][$rightIndex] : null;

        return  $leftCell instanceof Cell &&
                $rightCell instanceof Cell &&
                $leftCell->player == $centerCell->player &&
                $rightCell->player == $centerCell->player ?
                    $centerCell->player : false;
    }

    protected function checkDiagonalForward(Cell $centerCell, $centerRow, $centerColumn)
    {
        if (!($centerCell->player instanceof Player)) {
            return false;
        }
        $aboveIndex = $centerRow - 1;
        $belowIndex = $centerRow + 1;

        $leftIndex = $centerColumn - 1;
        $rightIndex = $centerColumn + 1;

        $leftCell = isset($this->grid[$belowIndex][$leftIndex]) ? $this->grid[$belowIndex][$leftIndex] : null;
        $rightCell = isset($this->grid[$aboveIndex][$rightIndex]) ? $this->grid[$aboveIndex][$rightIndex] : null;

        return  $leftCell instanceof Cell &&
                $rightCell instanceof Cell &&
                $leftCell->player == $centerCell->player &&
                $rightCell->player == $centerCell->player ?
                    $centerCell->player : false;
    }

    protected function checkDiagonalBackward(Cell $centerCell, $centerRow, $centerColumn)
    {
        if (!($centerCell->player instanceof Player)) {
            return false;
        }
        $aboveIndex = $centerRow - 1;
        $belowIndex = $centerRow + 1;

        $leftIndex = $centerColumn - 1;
        $rightIndex = $centerColumn + 1;

        $leftCell = isset($this->grid[$aboveIndex][$leftIndex]) ? $this->grid[$aboveIndex][$leftIndex] : null;
        $rightCell = isset($this->grid[$belowIndex][$rightIndex]) ? $this->grid[$belowIndex][$rightIndex] : null;

        return  $leftCell instanceof Cell &&
                $rightCell instanceof Cell &&
                $leftCell->player == $centerCell->player &&
                $rightCell->player == $centerCell->player ?
                    $centerCell->player : false;
    }

    public function play($row, $column, Player $player) {
        $this->grid[$row][$column]->play($player);
    }

    public function findWinner()
    {
        $winner = null;
        foreach ($this->grid as $rowIndex => $row) {
            foreach ($row as $columnIndex => $cell) {
                $winners = array_filter([
                    $this->checkRow($cell, $rowIndex, $columnIndex),
                    $this->checkColumn($cell, $rowIndex, $columnIndex),
                    $this->checkDiagonalForward($cell, $rowIndex, $columnIndex),
                    $this->checkDiagonalBackward($cell, $rowIndex, $columnIndex)
                ]);
                if (count($winners) > 0) {
                    $winner = array_shift($winners);
                    break 2;
                }
            }
        }

        return $winner;
    }
}

$input = explode(',', fgets(STDIN));

$grid = new Grid(3, 3);
$playerIndex = [];

foreach ($input as $position => $mark) {
    if ($mark != '-') {
        if (array_key_exists($mark, $playerIndex)) {
            $player = $playerIndex[$mark];
        } else {
            $player = new Player($mark);
            $playerIndex[$mark] = $player;
        }

        $row = floor($position / 3);
        $column = $position % 3;

        $grid->play($row, $column, $player);
    }
}

echo $grid;

$winner = $grid->findWinner();
if ($winner instanceof Player) {
    echo "The winner is: {$winner->mark}\n";
} else {
    echo "No winner!\n";
}
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

    public function play($row, $column, Player $player) {
        $this->grid[$row][$column]->play($player);
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
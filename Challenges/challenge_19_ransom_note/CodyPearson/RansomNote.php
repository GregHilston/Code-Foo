<?php

function stringInventory(string $input)
{
    $letterCounts = [];
    $input = strtolower($input);

    for ($i = 0; $i < strlen($input); $i++) {
        $letterCounts[$input[$i]]++;
    }

    return $letterCounts;
}

function canConstruct(string $note, string $magazineLetters)
{
    $neededLetters = stringInventory($note);
    $availableLetters = stringInventory($magazineLetters);

    foreach ($neededLetters as $neededLetter => $neededCount) {
        if (!array_key_exists($neededLetter, $availableLetters) || $availableLetters[$neededLetter] < $neededCount) {
            return false;
        }
    }

    return true;
}

// Test script
if (canConstruct($argv[1], $argv[2])) {
    echo "It works!\n";
} else {
    echo "It doesn't work!\n";
}
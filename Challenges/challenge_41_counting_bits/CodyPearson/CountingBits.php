<?php
// Credit to https://stackoverflow.com/a/15315676
// for the idea behind this solution

function findOnes(int $number)
{
    $oneCount = 0;
    // Once we reach 0, we're done
    while ($number > 0) {
        // This checks to see if the last bit is a 1
        if (($number & 1) == 1) {
            $oneCount++;
        }

        // Do a rightward bit shift to check the next bit
        $number = $number >> 1;
    }

    return $oneCount;
}

function findOnesForRange(int $number)
{
    $output = [];

    foreach (range(0, $number) as $thisNumber) {
        $output[] = findOnes($thisNumber);
    }

    return $output;
}

// Test cases
print_r(findOnesForRange(2));
print_r(findOnesForRange(5));
print_r(findOnesForRange(20));
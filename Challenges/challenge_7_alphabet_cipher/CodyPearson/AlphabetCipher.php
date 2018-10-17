<?php

class AlphabetCipher
{
    protected $alphabetNumericIndex;
    protected $alphabetAlphaIndex;
    protected $keyword;

    public function __construct()
    {
        // Build an array containing each letter of the alphabet
        $this->alphabetNumericIndex = range('a', 'z');
        // Flip the array so we can look up letters by index (a => 0, b => 1, etc)
        $this->alphabetAlphaIndex = array_flip($this->alphabetNumericIndex);
    }

    public function setKeyword($keyword)
    {
        $characters = str_split(strtolower($keyword));
        $keywordIndices = [];

        // The algorithm needs the numeric indices, so convert each letter into a number
        foreach ($characters as $character)
        {
            if (array_key_exists($character, $this->alphabetAlphaIndex)) {
                $keywordIndices[] = $this->alphabetAlphaIndex[$character];
            }
        }
        
        $arrayIterator = new ArrayIterator($keywordIndices);

        // Use an infinite iterator so we can loop endlessly through the indices
        $this->keyword = new InfiniteIterator($arrayIterator);
    }

    public function encrypt($input)
    {
        $input = str_split(strtolower($input));
        $output = '';

        $this->keyword->rewind();
        $alphabetSize = count($this->alphabetAlphaIndex);

        foreach ($input as $inputCharacter) {
            if (array_key_exists($inputCharacter, $this->alphabetAlphaIndex)) {
                $inputIndex = $this->alphabetAlphaIndex[$inputCharacter];
                $keywordIndex = $this->keyword->current();
                // By adding the input index to the current keyword index, and then modding by the number of letters in the index, we get the index for the output character
                $outputIndex = ($inputIndex + $keywordIndex) % $alphabetSize;

                $output .= $this->alphabetNumericIndex[$outputIndex];

                $this->keyword->next();
            }
        }

        return $output;
    }

    public function decrypt($input)
    {
        $input = str_split(strtolower($input));
        $output = '';

        $this->keyword->rewind();
        $alphabetSize = count($this->alphabetAlphaIndex);

        foreach ($input as $inputCharacter) {
            if (array_key_exists($inputCharacter, $this->alphabetAlphaIndex)) {
                $inputIndex = $this->alphabetAlphaIndex[$inputCharacter];
                
                $keywordIndex = $this->keyword->current();

                $outputIndex = abs(($inputIndex + $alphabetSize) - $keywordIndex) % $alphabetSize;

                $output .= $this->alphabetNumericIndex[$outputIndex];

                $this->keyword->next();
            }
        }

        return $output;
    }
}

// Test script
$cipher = new AlphabetCipher;
$cipher->setKeyword($argv[2]);
echo $cipher->{$argv[1]}($argv[3]) . "\n";
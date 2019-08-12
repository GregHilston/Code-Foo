module Main where

import AllUniqueCharacters

main :: IO ()
main = do
    input <- getLine
    print (uniqueChars(input))
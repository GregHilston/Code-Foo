-- Algorithm to determine if a (Char array) has all unique characters

module AllUniqueCharacters where

    uniqueChars :: [Char] -> Bool
    uniqueChars [] = True  -- Base case, array of size 0 is unique
    uniqueChars (h:t) = (length (filter (==h) t)) ==0 && uniqueChars t -- If the count of the head in the tail is 0, recurse

    -- main = print $ uniqueChars "Fish"
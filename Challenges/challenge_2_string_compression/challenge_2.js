const assert = require('assert')

function compress(s) {
    var characterCount = []
    var lastCharacter = ""

    // Build up our character count array
    for (var i = 0; i < s.length; i++) {
        currentCharacter = s[i]

        if (lastCharacter != currentCharacter) {
            characterCount.push({
                char: currentCharacter,
                count: 1
            })
        } else {
            currentObject = characterCount.slice(-1)[0]
            currentObject.count += 1
        }

        lastCharacter = currentCharacter
    }

    // Construct our compressed string
    var compressedString = ""
    for (var i = 0; i < characterCount.length; i++) {
        currentObject = characterCount[i]

        compressedString += currentObject.char + currentObject.count
    }

    // Return the shortest
    if (compressedString.length >= s.length) {
        return s
    } else {
        return compressedString
    }
}

assert.equal("a2b1c5a3", compress("aabcccccaaa"), "compressed string is smaller and should be returned")
assert.equal("a", compress("a"), "compression is longer and original string should be returned")
assert.equal("aa", compress("aa"), "compression is longer and original string should be returned")
assert.equal("a3", compress("aaa"), "compressed string is smaller and should be returned")
assert.equal("A", compress("A"), "compression is longer and original string should be returned")
assert.equal("AA", compress("AA"), "compression is longer and original string should be returned")
assert.equal("A3", compress("AAA"), "compressed string is smaller and should be returned")
assert.equal("a1b2c3d4e5", compress("abbcccddddeeeee"), "compressed string is smaller and should be returned")

const assert = require('assert')

function hasUniqueCharacters(s) {
  s = s.replace(/ /g,'') // removing all whitespace
  s = s.toLowerCase() // making all characters lower case

  character_count = {}
  for (var i = 0; i < s.length; i++) {
    if(s[i] in character_count) {
          return false // we've already seen this character before!
    }

    character_count[s[i]] = 1 // remember this character for later
  }

  return true
}

assert.equal(false, hasUniqueCharacters("test"), "has two 't's")
assert.equal(true, hasUniqueCharacters("JFK got my VHS PC and XLR web quiz"), "no reoccuring characters")
assert.equal(true, hasUniqueCharacters("abcdefghijklmnopqrstuvwxyz"), "no reoccuring characters")
assert.equal(true, hasUniqueCharacters(""), "an empty string has no duplicates")
assert.equal(false, hasUniqueCharacters("aabc"), "has two 'a's")
assert.equal(false, hasUniqueCharacters("aa"), "has two 'a's")
assert.equal(false, hasUniqueCharacters("aA"), "has two 'a's")

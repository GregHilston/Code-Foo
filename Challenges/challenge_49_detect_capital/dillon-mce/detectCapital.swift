import Foundation

func detectCapitals(_ string: String) -> Bool {
    return string == string.lowercased() || string == string.uppercased() || string == string.capitalized
}

let startTime = CFAbsoluteTimeGetCurrent()
assert(detectCapitals("USA"))       // true
assert(detectCapitals("leetcode"))  // true
assert(detectCapitals("Google"))    // true
assert(!detectCapitals("FlaG"))     // false
print("It took \(CFAbsoluteTimeGetCurrent() - startTime) seconds to check the four samples")

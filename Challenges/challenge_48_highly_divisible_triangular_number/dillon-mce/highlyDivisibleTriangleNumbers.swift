import Foundation
extension Int {
    func isDivisibleBy(_ number: Int) -> Bool {
        return self % number == 0
    }

    var numberOfDivisors: Int {
        var divisors = 0
        let limit = Int(sqrt(Double(self))) + 1
        for i in 1...limit {
            guard self.isDivisibleBy(i) else { continue }
            // add the current number and the other half
            let addTwo = self / i > limit
            divisors += addTwo ? 2 : 1
        }
        return divisors
    }
}

func findTriangleNumberWithDivisors(_ number: Int) -> Int {
    var numberToCheck = 0
    var increment = 0

    while true {
        increment += 1
        numberToCheck += increment
        let divisors = numberToCheck.numberOfDivisors
        if divisors > number { return numberToCheck }
    }
}

let startTime = CFAbsoluteTimeGetCurrent()
print("The first number that meets the criteria is:  \(findTriangleNumberWithDivisors(500))")
print("It took \(CFAbsoluteTimeGetCurrent() - startTime) seconds to calculate.")

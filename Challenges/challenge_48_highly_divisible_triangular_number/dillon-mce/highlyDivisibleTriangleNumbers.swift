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

    func numDivisorsByPrimeFactorialization() -> Int {
        var primeFactors: [Int: Int] = [:]

        var n = self
        while (n % 2 == 0) {
            primeFactors[2, default: 1] += 1
            n /= 2
        }

        let limit = Int(sqrt(Double(n))) + 1
        var i = 3
        while i < limit {
            while (n % i == 0) {
                primeFactors[i, default: 1] += 1
                n /= i
            }
            i += 1
        }
        if n > 2 { primeFactors[n, default: 1] += 1}

        return primeFactors.reduce(1) { $0 * $1.value }
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

func findTriangleNumberWithDivisorsByPrimes(_ number: Int) -> Int {
    var numberToCheck = 0
    var increment = 0

    while true {
        increment += 1
        numberToCheck += increment
        let divisors = numberToCheck.numDivisorsByPrimeFactorialization()
        if divisors > number { return numberToCheck }
    }
}

var startTime = CFAbsoluteTimeGetCurrent()
print("The first number that meets the criteria is:  \(findTriangleNumberWithDivisors(500))")
print("It took \(CFAbsoluteTimeGetCurrent() - startTime) seconds to calculate by brute force.")

startTime = CFAbsoluteTimeGetCurrent()
print("The first number that meets the criteria is:  \(findTriangleNumberWithDivisorsByPrimes(500))")
print("It took \(CFAbsoluteTimeGetCurrent() - startTime) seconds to calculate by prime factorialization.")

func threesAndFives(limit: Int) -> Set<Int>
{
    let allNumbers = 3..<limit
    var multiples = Set<Int>()

    for number in allNumbers {
        if ((number % 3) == 0 || (number % 5) == 0) {
            multiples.insert(number)
        }
    }

    return multiples
}

func sumSet(theSet: Set<Int>) -> Int
{
    return theSet.reduce(0, {x, y in
        x + y
    })
}

func sumThreesAndFives(until: Int) -> Int
{
    let multiples = threesAndFives(limit: until)

    return sumSet(theSet: multiples)
}
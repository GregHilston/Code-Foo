"use strict" // forcing ourselves to write better NodeJS

const expectedNumberOfArguments = 3 // first for invoked node path, second for script path, third for multiline string 
let mappings = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

function splitStringIntoEvenOddCharacters(toSplit) {
    evenPositionedValues = [],
    oddPositionValues = [];

    for (var i = 0; i < toSplit.length; i++){
        if((i+2)%2==0) {
            evenPositionedValues.push(toSplit[i]);
        }
        else {
            oddPositionValues.push(toSplit[i]);
        }
    }

    return [evenPositionedValues, oddPositionValues]
}

function convertRomanNumerals(romanNumeralWritten){
    // let splitValues = splitStringIntoEvenOddCharacters(romanNumeralWritten)
    // let evenPositionedValues = splitValues[0]
    // let oddPositionedValues = splitValues[1]
    let runningSum = 0
    let firstValue
    let secondValue
    let isIncrementing

    for(var i = 0; i < romanNumeralWritten.length; i++) {
        runningSum += mappings[romanNumeralWritten[i]]

        if(i == 0) {
            // first character storage, to determine direction
            firstValue = mappings[romanNumeralWritten[i]]
        } else if (i == 1) {
            // second character storage, to determine direction
            secondValue = mappings[romanNumeralWritten[i]]
            
            // determine direction
            if(firstValue >= secondValue) {
                isIncrementing = true
            } else {
                isIncrementing = false
                runningSum -= (2 * firstValue)
            }
        }
    }

    return runningSum
}

/**
 * main - Parsing command line arguments and calls our coding challenge method
 */
function main() {
    if (process.argv.length != expectedNumberOfArguments) {
        throw new Error("Unexpected number of input arguments. Expected " + expectedNumberOfArguments + " actual " + process.argv.length)
    }
    
    let romanNumeralWritten = process.argv[2]
    let integerValue = convertRomanNumerals(romanNumeralWritten)
}

// only call if main module and not being imported
if (!module.parent) {
    main()
}

module.exports = convertRomanNumerals // so our tests can access this method
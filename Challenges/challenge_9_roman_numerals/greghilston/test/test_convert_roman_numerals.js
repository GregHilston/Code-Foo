var chai = require('chai')
const convertRomanNumerals = require('../src/challenge_9')

describe('convertRomanNumerals', function() {
    it("'1 Through 100", function() {
        // given
        inputAndOutput = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10,
                          "XI": 11, "XII": 12, "XIII": 13, "XIV": 14, "XV": 15, "XVI": 16, "XVII": 17, "XVIII": 18, "XIX": 19, "XX": 20,
                          "XXI": 21, "XXII": 22, "XXIII": 23, "XXIV": 24, "XXV": 25, "XXVI": 26, "XXVII": 27, "XXVIII": 28, "XXIX": 29, "XXX": 30}
        let returnedValue
        let caughtException

        // when
        for (var input in inputAndOutput) {
            try {
                returnedValue = convertRomanNumerals(input) 
            } catch(exception) {
                caughtException = exception
            }

            // then
            chai.assert.isDefined(returnedValue, "a value should be returned")
            chai.assert.isUndefined(caughtException, "should be undefined, as nothing should have been thrown")
            console.log("expected: " + inputAndOutput[input])
            console.log("actual: " + returnedValue + "\n")
            chai.assert.isTrue(inputAndOutput[input] == returnedValue, "should be correct value")
        }
    })
})
var chai = require('chai')
const checkWireCutting = require('../src/challenge_6')

describe('checkWireCutting', function() {
    it('should throw exception when attempting to split an undefined object', function() {
        // given
        input = undefined
        var returnedValue
        var caughtException

        // when
        try {
            returnedValue = checkWireCutting(input) // same thing as if no input was passed, just explicit
        } catch(exception) {
            caughtException = exception
        }

        // then
        chai.assert.isUndefined(returnedValue, "no value should be returned")
        chai.assert.isDefined(caughtException, "should be defined, as something should have been thrown")
        chai.assert.instanceOf(caughtException, TypeError, "the exception caught should be a TypeError exception, as we passed nothing to our function")
    })

    it('should go boom', function() {
        // given
        input = "white\nwhite"
        var returnedValue
        var caughtException

        // when
        try {
            returnedValue = checkWireCutting(input)
        } catch(exception) {
            caughtException = exception
        }

        // then
        chai.assert.isUndefined(caughtException, "no exceptions should be thrown")
        chai.assert.isDefined(returnedValue, "should have a return value")
        chai.assert.isFalse(returnedValue, "white cable then white cable again is not allowed and should fail to defuse");
    })
    
    it('should bomb defused', function() {
        // given
        input = "white\nred"
        var returnedValue
        var caughtException

        // when
        try {
            returnedValue = checkWireCutting(input)
        } catch(exception) {
            caughtException = exception
        }

        // then
        chai.assert.isUndefined(caughtException, "no exceptions should be thrown")
        chai.assert.isDefined(returnedValue, "should have a return value")
        chai.assert.isTrue(returnedValue, "white cable then red cable is legal and the bomb should be defused");
    })
})
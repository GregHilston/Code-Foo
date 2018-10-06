"use strict" // forcing ourselves to write better NodeJS

// our finite state machine defining valid moves
const fsm = {"start": ["white, red, black, orange, green, purple"],
            "white": ["red", "orange", "green", "purple"],
            "red": ["green"],
            "black": ["red", "black", "purple"], 
            "orange": ["red", "black"],
            "green": ["white", "orange"],
            "purple": ["red", "black"]}
const validWires = [Object.keys(fsm)] // for convenience
const expectedNumberOfArguments = 3 // first for invoked node path, second for script path, third for multiline string 

/**
 * checkWireCutting - Checks wires from a bomb defusing procedure, determining if bomb exploded or was successfully defused
 * 
 * @param {array} wires - array of strings, describing colors of wires cut in order
 * @return {boolean} Whether the bomb was successfully defused
 */
function checkWireCutting(wires) {
    var lastWire = null
    
    if (typeof wires == 'undefined' && !wires) {
        throw new TypeError("wires should not be undefined")
    } 

    wires = wires.split('\n')

    console.log(wires.length)

    for(var i = 0; i < wires.length; i++) {    
        var wire = wires[i].trim()

        // check if wire is a valid wire
        if(validWires.indexOf(wire) > -1) {
            throw new Error("Unexpected wire: '" + wire + "'")
        }

        // check if this step to this wire is valid
        if(lastWire != null) {            
            if(fsm[lastWire].indexOf(wire) <= -1) {
                console.log("Boom")
                return false 
            }
        }

        lastWire = wire
    }

    console.log("Bomb defused")
    return true
}

/**
 * main - Parsing command line arguments and calls our coding challenge method
 */
function main() {
    if (process.argv.length != expectedNumberOfArguments) {
        throw new Error("Unexpected number of input arguments. Expected " + expectedNumberOfArguments + " actual " + process.argv.length)
    }
    
    var wires = process.argv[2]
    checkWireCutting(wires)
}

// only call if main module and not being imported
if (!module.parent) {
    main()
}

module.exports = checkWireCutting // so our tests can access this method
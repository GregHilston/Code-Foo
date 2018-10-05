"use strict" // forcing ourselves to write better NodeJS

const util = require('util')        // used to print objects
const assert = require('assert')    // used for testing

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
 * checkWireCutting - Checks wires from a bomb defusal proposal, determining if bomb exploded or was successfully defused
 * 
 * @param {array} wires - array of strings, describing colors of wires cut in order
 * @return {boolean} Whether the bomb was successfully defused
 */
function checkWireCutting(wires) {
    var lastWire = null

    wires = wires.split('\n')
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

function main() {
    if (process.argv.length != expectedNumberOfArguments) {
        throw new Error("Unexpected number of input arguments. Expected " + expectedNumberOfArguments + " actual " + process.argv.length)
    }
    
    var wires = process.argv[2]
    checkWireCutting(wires)
}

if (!module.parent) {
    main()
}

module.exports = checkWireCutting/*{
    checkWireCutting
}*/

"use strict" // forcing ourselves to write better NodeJS

const expectedNumberOfArguments = 4 // first for invoked node path, second for script path, third for key and fourth for message

function encryptCharacter(keyToEncryptWith, index, characterToEncrypt) {
    console.log("index: " + index)
    console.log("\tcharacterToEncrypt: " + characterToEncrypt)

    let aAscii = 'a'.charCodeAt()

    let characterToEncryptAscii = characterToEncrypt.charCodeAt()

    console.log("\tcharacterToEncryptAscii: " + characterToEncryptAscii)

    let keyIndexToEncryptWith = (index % keyToEncryptWith.length)

    let keyCharToEncryptWith = keyToEncryptWith.charCodeAt(keyIndexToEncryptWith)

    console.log("\tkeyCharToEncryptWith: " + keyCharToEncryptWith)

    let keyCharToEncryptWithAscii = keyCharToEncryptWith.charCodeAt()

    console.log("\tkeyCharToEncryptWithAscii: " + keyCharToEncryptWithAscii.charCodeAt())

    // let alphabetOffset = keyToEncryptWithAscii - aAscii

    // console.log("\talphabetOffset: " + alphabetOffset)

    let encryptedCharacter = String.fromCharCode((characterToEncryptAscii + alphabetOffset) % aAscii)

    console.log("\tencryptedCharacter: " + encryptedCharacter)

    return encryptedCharacter
}

function alphabetCipher(key, message) {
    let cipheredMessage = ""

    for (var i = 0; i < message.length; i++) {
        cipheredMessage += (encryptCharacter(key, i, message[i]))
      }

    console.log(cipheredMessage)
    return cipheredMessage
}

/**
 * main - Parsing command line arguments and calls our coding challenge method
 */
function main() {
    if (process.argv.length != expectedNumberOfArguments) {
        throw new Error("Unexpected number of input arguments. Expected " + expectedNumberOfArguments + " actual " + process.argv.length)
    }

    let key = process.argv[2]
    let message = process.argv[3]

    alphabetCipher(key, message)
}

// only call if main module and not being imported
if (!module.parent) {
    main()
}

module.exports = alphabetCipher // so our tests can access this method
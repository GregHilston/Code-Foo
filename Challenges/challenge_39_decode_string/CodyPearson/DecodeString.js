function decodeString(input)
{
    const expression = /(\d+)\[([^\[\]]*?)\]/g;
    var oldInput;
    do {
      oldInput = input;
        input = input.replace(expression, (match, repetitionCount, repetitionPattern) => {
          var replacement = '';
          
          for (var i = 0; i < repetitionCount; i++) {
            replacement += repetitionPattern;
          }

          return replacement;
      }); 
    } while (oldInput != input);

    return input;
}
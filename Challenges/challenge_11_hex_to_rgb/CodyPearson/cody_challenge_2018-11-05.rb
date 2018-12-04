$*.each {
    |hexString|
    
    print "rgb(" + hexString.scan(/[0-9a-f]{2}/).map {
        |colorValue|
        
        colorValue.to_i(16).to_s
    }.join(",") + ")"
}
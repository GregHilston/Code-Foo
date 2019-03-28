def recursive_multiply(firstTerm, secondTerm)
    if firstTerm == 0 or secondTerm == 0
        return 0
    end

    if firstTerm < 0 and secondTerm < 0
        firstTerm = firstTerm.abs
        secondTerm = secondTerm.abs
    elsif firstTerm < 0 and secondTerm > 0
        temp = firstTerm
        firstTerm = secondTerm
        secondTerm = temp
    end

    if secondTerm > 0
        return firstTerm + recursive_multiply(firstTerm, (secondTerm - 1))
    elsif secondTerm == 0
        return 0
    elsif secondTerm < 0
        return -(recursive_multiply(firstTerm, secondTerm.abs))
    end
end
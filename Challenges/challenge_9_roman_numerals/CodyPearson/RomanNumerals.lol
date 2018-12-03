HAI 1.4
  CAN HAS STDIO?
  CAN HAS STRING?

  HOW IZ I GITVALU YR DIJIT
    I HAS A NUMDIJIT
    
    DIJIT, WTF?
        OMG "I"
            NUMDIJIT R 1
            GTFO
        OMG "V"
            NUMDIJIT R 5
            GTFO
        OMG "X"
            NUMDIJIT R 10
            GTFO
        OMG "L"
            NUMDIJIT R 50
            GTFO
        OMG "C"
            NUMDIJIT R 100
            GTFO
        OMG "D"
            NUMDIJIT R 500
            GTFO
        OMG "M"
            NUMDIJIT R 1000
            GTFO
    OIC

    FOUND YR NUMDIJIT
  IF U SAY SO

  I HAS A ROMANNUMZ
  I HAS A LENGTH
  I HAS A ROMANDIJIT
  I HAS A NUMDIJIT
  I HAS A PREVNUM ITZ 0
  I HAS A TOTL ITZ 0

  VISIBLE "PUT IN YR NUMERLZ::"
  GIMMEH ROMANNUMZ

  LENGTH R I IZ STRING'Z LEN YR ROMANNUMZ MKAY

  IM IN YR LOOP UPPIN YR COUNTER WILE DIFFRINT COUNTER AN BIGGR OF COUNTER AN LENGTH
    ROMANDIJIT R I IZ STRING'Z AT YR ROMANNUMZ AN YR COUNTER MKAY
    NUMDIJIT R I IZ GITVALU YR ROMANDIJIT MKAY

    DIFFRINT PREVNUM AN 0
    O RLY?
        YA RLY
             BTW If the previous number is smaller, it should be subtracted instead
             DIFFRINT PREVNUM AN BIGGR OF PREVNUM AN NUMDIJIT
             O RLY?
                YA RLY
                    TOTL R DIFF OF TOTL AN PREVNUM
                NO WAI
                    TOTL R SUM OF TOTL AN PREVNUM
             OIC
    OIC

    PREVNUM R NUMDIJIT
  IM OUTTA YR LOOP

  TOTL R SUM OF TOTL AN PREVNUM

  VISIBLE TOTL

KTHXBYE
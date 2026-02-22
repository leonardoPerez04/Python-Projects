print('''
            _
           H||
           H||
 __________H||___________
[|.......................|
||.........## --.#.......|
||.........   #  # ......|            @@@@
||.........     *  ......|          @@@@@@@
||........     -^........|   ,      - @@@@
||.....##\        .......|   |     '_ @@@
||....#####     /###.....|   |     __\@ \@
||....########\ \((#.....|  _\\  (/ ) @\_/)____
||..####,   ))/ ##.......|   |(__/ /     /|% #/
||..#####      '####.....|    \___/ ----/_|-*/
||..#####\____/#####.....|       ,:   '(
||...######..######......|       |:     \
||.....""""  """"...b'ger|       |:      )
[|_______________________|       |:      |
       H||_______H||             |_____,_|
       H||________\|              |   / (
       H||       H||              |  /\  )
       H||       H||              (  \| /
      _H||_______H||__            |  /'=.
    H|________________|           '=>/  \
                                 /  \ /|/
                               ,___/|
      ''')
print("Welcome to Treasure Island"+
      "\nYour mission is to find the treasure")
side=input("left or right? L or R: ")
if side == "L":
    action = input("swim or wait? S or W: ")
    if action == "W":
        color = input("Wich color Red, Blue, Yellow? R, B, Y: ")
        if color=="R" or color=="B":
            print("Game Over")
        elif color=="Y":
            print("Your Win!")
        else:
            print("Opcion no valida!")
    else:
        print("Game Over")
elif side == "R":
    print("Game Over")
else:
    print("Opcion no valida!")

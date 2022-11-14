res = [['   ', '|', '   ', '|', '   '], ['   ', '|', '   ', '|', '   '], ['   ', '|', '   ', '|', '   ']]
print("\"Enter space seperated Row and Column\"")
for i in res:
    print("".join(x for x in i))

def play(res,turn):
    r = list(map(int, input("{}'s move, Enter [Row Column] :".format(turn)).split()))
    a, b = r[0], r[1]
    if(a<4 and b<4):
        if '   ' in res[a - 1]:
            if res[a - 1][(b - 1) * 2] == '   ':
                res[a - 1][(b - 1) * 2] = " " + str(turn) + " "
                for i in res:
                    print("".join(x for x in i))
    else:
        print("Enter valid Row/Column")
        play(res,turn)
    if win(res):
        print("Congrats!!! "+str(turn) + ' wins!!!')

def win(res):
    for i in range(3):
        if ((res[i][0] == res[i][2] == res[i][4] != "   ") or (res[0][i*2] == res[1][i*2] == res[2][i*2] != '   ') or (
                res[0][0] == res[1][2] == res[2][4] != '   ') or (res[2][0] == res[1][2] == res[0][4] != '   ')):
            return True
        else:
            return False

turn = 'X'
for i in range(9):
    if(not win(res)):
        play(res, turn)
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
if(not win(res)):
    print("Game Completed! It's a TIE!!!")

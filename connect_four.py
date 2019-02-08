def who_is_winner(pieces_position_list):
    board = [[],[],[],[],[],[],[]]
    cols = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}
    
    #insert a piece into board
    def insert(move):
        board[cols[move[0]]].append(move[2])
    
    #create rows list
    def create_rows_list():
        rows = [[],[],[],[],[],[]]
        for col in range(7):
            for row in range(6):
                if row < len(board[col]):
                    rows[row].append(board[col][row])
                else:
                    rows[row].append('None')
        return rows
    
    #create diagnals list
    def create_diagnals_list(rows):
        a = [rows[r][c] for r, c in zip(range(3, -1, -1), range(0, 4))]
        b = [rows[r][c] for r, c in zip(range(4, -1, -1), range(0, 5))]
        c = [rows[r][c] for r, c in zip(range(5, -1, -1), range(0, 6))]
        d = [rows[r][c] for r, c in zip(range(5, -1, -1), range(1, 7))]
        e = [rows[r][c] for r, c in zip(range(5, 0, -1), range(2, 7))]
        f = [rows[r][c] for r, c in zip(range(5, 1, -1), range(3, 7))]
        g = [rows[r][c] for r, c in zip(range(2, 6), range(0, 4))]
        h = [rows[r][c] for r, c in zip(range(1, 6), range(0, 5))]
        i = [rows[r][c] for r, c in zip(range(0, 6), range(0, 6))]
        j = [rows[r][c] for r, c in zip(range(0, 6), range(1, 7))]
        k = [rows[r][c] for r, c in zip(range(0, 5), range(2, 7))]
        l = [rows[r][c] for r, c in zip(range(0, 4), range(3, 7))]
        return [a, b, c, d, e, f, g, h, i, j, k, l]
    
    #check a list for 4 in a row
    def has_four(a_list):
        s = "".join(a_list)
        if 'YYYY' in s:
            return 'Yellow'
        if 'RRRR' in s:
            return 'Red'
        return 'Draw'
    
    #check a 2d list for 4 in a row
    def check_win(a_list):
        for row in a_list:
            result = has_four(row)
            if result != 'Draw':
                return result
        return 'Draw'
    
    #check cols, rows, diags for 4 in a row
    def check_for_a_winner(rows, diags):
        outcome = check_win(board)
        if outcome != 'Draw':
            return outcome
        outcome = check_win(rows)
        if outcome != 'Draw':
            return outcome
        outcome = check_win(diags)
        return outcome
    
    #loop through moves inserting each into board
    #check for winner after each move
    for move in pieces_position_list:
        insert(move)
        rows = create_rows_list()
        diags = create_diagnals_list(rows)
        winner = check_for_a_winner(rows, diags)
        if winner != 'Draw':
            return winner
    
    return 'Draw'
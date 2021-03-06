

def clear_sq(x,y):
    global sqr_dict
    sqr_dict[coord(x,y)].button.config( state="disabled",
                                        relief="sunken",
                                        text="" )
                                        

            
def left_click(x,y):
    global sqr_dict
    sq = sqr_dict[coord(x,y)]
    
    if (sq.mine_yn) and (not sq.flag_yn): game_over()

    try:
        tmp = sqr_dict[coord(x,y)].button
    except KeyError:
        return

    if (sq.prox_num == 0) and (not (sq.flag_yn or sq.Qmark_yn)):
        clear_sq(x,y)
        chk_open_field(x+1,y)  #N
        chk_open_field(x,y-1)  #S
        chk_open_field(x,y+1)  #E
        chk_open_field(x-1,y)  #W
        
        
        
1  procedure DFS-iterative(G,v):
2      let S be a stack
3      S.push(v)
4      while S is not empty
5          v = S.pop()
6          if v is not labeled as discovered:
7              label v as discovered
8              for all edges from v to w in G.adjacentEdges(v) do 
9                  S.push(w)

    
    S = [[x,y]]
    while len(S):
        x,y = S.pop()
        print('Popped: ' + coord(x,y))
        q = sqr_dict[coord(x,y)]
 
        clear_sq(x,y)
        
        #check North
        try:
            q = sqr_dict[coord(x,y-1)]
            if (q.prox_num == 0) and (not (q.flag_yn or q.Qmark_yn)):
                S.append([x,y-1])
                print('Pushed North: ' + coord(x,y-1))
        except KeyError:
            pass
def move(n,A,B,C):
    if n ==1:
        print (f"move {A}=>{C}")
    else:
        move (n-1,A,C,B)
        print (f"Move {A} => {C}")
        move (n-1,B,A,C)

print (move(3,"A","B","C"))

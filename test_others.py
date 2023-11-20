def mode(xs):
    """
    整数のリスト xs の最頻値を返す関数 mode(xs).
    """
    C = sorted(xs)
    if xs[0] == xs[-1]:
        return xs[0]
    elif xs == []:
        raise Exception("mode", "xsは[]ではいけません。")
    else:
        A = []
        B = []
        i = 0
        while C[0] == C[i]:
            A.append(C[i])
            i += 1
        n = len(C) - 1
        while C[-1] == C[n]:
            B.append(C[n])
            n -= 1
        if len(A) >= len(B):
            return mode([i for i in xs if i != B[0]])
        if len(A) < len(B):
            return mode([i for i in xs if i != A[0]])
        


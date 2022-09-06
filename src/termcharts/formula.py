def constrain(
    val, start, end, realstart, realend, lessthan_sym=None, morethan_sym=None
):
    # from hooman
    # mouseX 0 width 0 255
    # v = (mouseX / (end-start)) * (realend-realstart)
    # return realstart + v
    # if val < start, val = start
    # if val > end, val = end

    if val < start:
        if lessthan_sym is None:
            return start
        else:
            return lessthan_sym
    if val > end:
        if morethan_sym is None:
            return end
        else:
            return morethan_sym
    v = ((val - start) / (end - start)) * (realend - realstart)
    return realstart + v

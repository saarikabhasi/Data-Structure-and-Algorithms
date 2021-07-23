def spreadsheet_encoding_column(col_name):
    n = len(col_name)
    i = 0 
    res = 0

    while i<n:
        ord_num = ord(col_name[i])-ord('A') + 1
        res += ord_num*(26**((n-1)-i))
        i = i+1
    return res
print(spreadsheet_encoding_column("A"))
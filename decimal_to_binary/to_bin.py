def dec_to_bin(dec: int) -> str:
    if dec == 0:
        return "0"
    bin = ""
    while(dec > 0):
        if (dec % 2) == 0:
            bin = "0" + bin
        else:
            bin = "1" + bin
        dec = dec // 2
    return bin
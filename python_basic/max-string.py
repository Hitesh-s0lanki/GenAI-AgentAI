def maxNumber(s:str, k:int) -> str:
    ans = ""

    freq_no = s.split("")

    freq_no.sort()

    print(freq_no)

    return ans

print(maxNumber("1121212", 2))
def weird_number(n):
    if not isinstance(n, (int, float, str)):
        raise TypeError("this function only accepts integers, floats and strings.")
    try:
        n = float(n)
    except Exception:
        n = 0
    else:
        n = n**3
    finally:
        n = n+1
    return n

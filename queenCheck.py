def qcheck(attempt):
    if len(attempt) > len(set(attempt)):
        return False
    for q in range(len(attempt)):
        offset = 1
        for n in range(q+1, len(attempt)):
            if attempt[q] == attempt[n] + offset or attempt[q] == attempt[n] - offset:
                return False
            offset += 1
    return True


if __name__ == '__main__':
    string = list(map(int, input().split(",")))
    print(qcheck(string))

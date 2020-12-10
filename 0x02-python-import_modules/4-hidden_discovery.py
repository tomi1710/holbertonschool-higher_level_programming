#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    a = dir(hidden_4)
    for st in range(len(a)):
        if a[st][:2] != "__":
            print(a[st])

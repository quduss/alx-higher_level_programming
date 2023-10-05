#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    hidden4_names = dir(hidden_4)
    for name in hidden4_names:
        if name[:2] != "__":
            print(name)

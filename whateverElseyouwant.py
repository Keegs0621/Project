from csc131 import whateveryouwant


def main():
    print("Main")
    d = whateveryouwant.get_personal_data()
    print(d)
    for key in sorted(d.keys()):
        print("%s: %s" % (key, d[key]))


if __name__ == '__main__':
    main()

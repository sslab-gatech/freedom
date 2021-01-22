def generate(domain):
    with open("../arg/{}.py".format(domain)) as f:
        lines = f.readlines()

    fout = open("{}.py".format(domain), "w")
    fout.write("from js.ret import RetWrapper\n\n")

    names = []
    for line in lines:
        if "name = " in line:
            l = line.strip()
            names.append(l.split()[2][1:-1])

    for name in sorted(names):
        fout.write("{0}Ret = RetWrapper(\"{0}\")\n".format(name))

    fout.close()


if __name__ == "__main__":
    generate("svg")
    generate("html")

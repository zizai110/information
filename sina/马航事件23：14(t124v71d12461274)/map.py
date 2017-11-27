import os
with open("cord.dict", "rb") as f:
    from pickle import load

    coords = load(f)

fw = open('output', 'wb')
with open('sina_01_1.csv') as f:
    for line in f.readlines():
        lines = line.strip().split(',')
        key = lines[1] + "," + lines[2]
        if key in coords:
            fw.write(lines[0] + "," + coords[key] + "," + lines[3] + os.linesep)
fw.close()
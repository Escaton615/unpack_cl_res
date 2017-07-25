import io

with open('game.droid', 'rb') as f:
    f.seek(8)


    while 1:
        label = f.read(4)
        print(label)
        if label[0] == 0x54 and label[2] == 0x54:
            # print('txtr found')
            break
        else:
            lenbytes = f.read(4)
            len = int.from_bytes(lenbytes, byteorder='little', signed=False)
            f.seek(len, io.SEEK_CUR)

    # skip len
    finalb = f.read(4)
    final = int.from_bytes(finalb, byteorder='little', signed=False) + f.tell()


    lenbytes = f.read(4)
    len = int.from_bytes(lenbytes, byteorder='little', signed=False)
    offsets = []
    for i in range(len):
        offsetBytes = f.read(4)
        offsets.append(int.from_bytes(offsetBytes, byteorder='little', signed=False))

    for o in offsets:
        f.seek(o + 4, io.SEEK_SET)
        bb = f.read(4)
        b = int.from_bytes(bb, byteorder='little', signed=False)

        f.seek(4, io.SEEK_CUR)
        eb = f.read(4)
        e = int.from_bytes(eb, byteorder='little', signed=False)

        len = e - b if e - b > 0 else final - b
        f.seek(b, io.SEEK_SET)
        png = f.read(len)

        of = open('{0}.png'.format(o), 'wb')
        of.write(png)



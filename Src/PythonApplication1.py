#print("Hello, world!")

template = open("1zk5.pdb", "r")
target = open("1oio.pdb", "r")
output=open("result.pdb","w")

tp=template.read(4)
#print(tp)
while tp!="ATOM":
    while template.read(1)=="\n":tp=template.read(4)
    #print(template.tell())
template.seek(template.tell()-5,0)
#print(template.read(200))



lcou=0;
tp=target.read(4)
while tp!="ATOM":
    while target.read(1)=="\n":
        tp=target.read(4)
        lcou=lcou+1
#print(lcou)
go=target.tell()-5
target.seek(0,0)
for x in range(0, lcou):
    output.write(target.readline())
target.seek(go,0)
#print(target.read(200))

countatom=0
tp=target.read(4)
while tp=="ATOM":
    countatom=countatom+1
    opline="ATOM"
    if countatom<10:
        tp=tp+"      "+str(countatom)
    else:
        if countatom<100:
            tp=tp+"     "+str(countatom)
        else:
            if countatom<1000:
                tp=tp+"    "+str(countatom)
            else:
                if countatom<10000:
                    tp=tp+"   "+str(countatom)
                else:
                    if countatom<100000:
                        tp=tp+"  "+str(countatom)
                    else:
                        tp=tp+" "+str(countatom)
    target.read(13)
    template.read(17)
    aata=target.read(3)
    aate=template.read(3)
    if aata==aate:
        template.seek(template.tell()-9,0)
        opline=opline+template.readline()
        target.readline()
        output.write(opline)
    else:
        target.seek(target.tell()-9,0)
        opline=opline+target.readline()
        template.readline()
        output.write(opline)
target.seek(target.tell()-5,0)

rlf=target.readline()
while "\n" in rlf:
    output.write(rlf)
    rlf=target.readline()
output.write(rlf)





template.close()
target.close()
output.close()


print("Hello, world!")


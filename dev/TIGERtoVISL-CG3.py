import re


for j in range(42):

    x="GRUG/GEO/go"+str(j+1)+".tig"
    print("#"+x)

    with open(x) as search:
        for line in search:
            if "<t id=" in line:
                m=-1 
                idd=line[line.index('<t id=')+7:line.index('word')-2]
                #print(idd)
                index=line[line.index("_")+1:line.index('word')-2]
                #print(index) 
                word= line[line.index("word=")+6:line.index('pos')-2]
                #print(word) 
                pos= line[line.index("pos=")+5:line.index('morph')-2]
                #print(pos)
                morph=line[line.index("morph=")+7:line.index('/>')-2]
                morph = morph.replace('.', ' ')
                #print(morph)
                if pos == "$." or "$," or "$(":
                    label="X" 
                with open(x) as search:
                    for line in search:
                  
                        if ("idref" in line) and (idd+'"' in line):
                            label= line[line.index("label=")+7:line.index('idref')-2] 
                            break
                if label =="HD":
                    m=0  
                      

                label = label.replace("--", 'X')
                if morph =="--":
                    print('"<'+word+'>"')
                    print('\t'+'"_" '+pos+" @"+label+" #"+index+"->"+str(m))
                else: 
                    print('"<'+word+'>"') 
                    print('\t'+'"_" '+pos+' '+morph+" @"+label+" #"+index+"->"+str(m)) 
    print('\n')
    print('\n')
                   

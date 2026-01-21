def calculate_love_score(name1,name2):
    combined = name1+name2
    lover_names = combined.lower()
    t = lover_names.count("t")
    r = lover_names.count("r")
    u = lover_names.count("u")
    e = lover_names.count("e")
    first = t+r+u+e




    l = lover_names.count("l")
    o = lover_names.count("o")
    v = lover_names.count("v")
    e = lover_names.count("e")
    r = lover_names.count("r")
    second = l+o+v+e+r
    print(int(str(first)+ str(second)))

calculate_love_score("BEkmirzayev","Sherzodbek")
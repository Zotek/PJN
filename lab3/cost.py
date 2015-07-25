# -*- coding: utf-8 -*-
special_characters = [
    u"aą",
    u"cć",
    u"eę",
    u"lł",
    u"oó",
    u"sś",
    u"zżź"
]

pot_ort = [u"rz",u"uó",u"ch"]

ort = [
    [u"ż",u"rz"],
    [u"u",u"ó"],
    [u"h",u"ch"]
]

def __is_special_mistake(a,b):
    for x in special_characters:
        if a in x and b in x:
            return True
    return False

def __is_potential_misspelling(a,b):
    for x in pot_ort:
        if a in x and b in x:
            return True
    return False

def __is_misspelling(slice1, slice2):
    for x in ort:
        if (x[0] in slice1 and x[1] in slice2) or (x[0] in slice2 and x[1] in slice1):
            return True
    return False

def __is_cerror(slice1,slice2):
    if len(slice1)!=2 or len(slice2)!=2:
        return False
    else:
        return slice1==slice2[::-1]


def cost(i,j,word_i,word_j):
    ilb = i-1 if i-1>=0 else 0
    jlb = j-1 if j-1>=0 else 0
    if word_j[j] == word_i[i]:
        return 0
    elif __is_special_mistake(word_i[i],word_j[j]):
        return 0.25
    elif __is_potential_misspelling(word_i[i],word_j[j]):
        if __is_misspelling(word_i[ilb:i+2],word_j[jlb:j+2]):
            return 0.25
    elif __is_cerror(word_i[ilb:i+1],word_j[jlb:j+1]) or __is_cerror(word_i[i:i+2], word_j[j:j+2]):
        return 0.125
    return 1
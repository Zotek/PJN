# -*- coding: utf-8 -*-

from cost import cost as c

def levenshtein(a,b):
    lev_matrix = [[0 if (x==y==0 or (x!=0 and y!=0)) else (x if y==0 else y) for x in xrange(0,len(a)+1)] for y in xrange(0,len(b)+1)]
    for x in xrange(0,len(a)):
        for y in xrange(0,len(b)):
            cost = c(x,y,a,b)
            lev_matrix[y+1][x+1] = min(lev_matrix[y][x+1]+1,lev_matrix[y+1][x]+1,lev_matrix[y][x]+cost)


    return lev_matrix[len(b)][len(a)]


if __name__ == '__main__':
    print levenshtein(u"krzesło",u"kżesło")
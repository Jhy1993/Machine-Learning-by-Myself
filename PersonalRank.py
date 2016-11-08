# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 09:59:26 2016

@author: JI Houye 
README:
PersonalRank bases on RandomWalk
REFERENCE:
http://blog.csdn.net/harryhuang1990/article/details/10048383
INPUT:

OUTPUT:


"""

def PersonalRank(G, d, root, max_step):
	rank = dict()
	rank = {x:0 for x in G.keys()}
	rank[root] = 1
	#start iter
	for k in range(max_step):
		tmp = {x:0 for x in G.keys()}
		#get node i and out(i)
		for i, ri in G.items():
			# weight wij between i and j(one of out(i))
			for j, wij in ri.items():
				tmp[j] += d * rank[i] / (1.0 * len(ri))                                      
		tmp[root] += (1 - d)
		rank = tmp
		
		print('\n iter: {} '.format(k))
		for k, v in rank.items():
			print('{}: {:.4f}'.format(k, v)),

	return rank
				
if __name__ == '__main__' :  
	
    G = {'A' : {'a' : 1, 'c' : 1},  
         'B' : {'a' : 1, 'b' : 1, 'c':1, 'd':1},  
         'C' : {'c' : 1, 'd' : 1},  
         'a' : {'A' : 1, 'B' : 1},  
         'b' : {'B' : 1},  
         'c' : {'A' : 1, 'B' : 1, 'C':1},  
         'd' : {'B' : 1, 'C' : 1}}  
  
    PersonalRank(G, 0.85, 'A', 100)  		
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			

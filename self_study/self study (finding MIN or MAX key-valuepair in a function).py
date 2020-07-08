#!/usr/bin/env python
# coding: utf-8

# In[2]:


old = {'emma':75, 'ahmet':19, 'selim':9, 'jack':99, 'sema':111, 'serdar':41}

def dic_val(dic,maxORmin):                      

    dicTolist = list(dic.items())                # convert dict-to-list.   

    if maxORmin == "max":                        # to find MAX value in dict
      
        dicMaxVal = max(list(dic.values()))      
    
        x = 0
    
        for i in dicTolist:        # which one in list has the max value via for loop.
            
            if dicMaxVal in i:
                
                print("  Key  : ",i[0],"\n Value : ",i[1])
                
            else:
                
                x+=1
                
                continue
                
    elif maxORmin == "min":                     # to find MIN value in dict
    
        dicMinVal = min(list(dic.values()))     
    
        x = 0
    
        for i in dicTolist:
            
            if dicMinVal in i:
                
                print("  Key  : ",i[0],"\n Value : ",i[1])
                
            else:
                
                x+=1
                
                continue                
                
    else: 
        
        print("lütfen 'dic_val(dic,maxORmin)' içerisinde 'dict' yanında 'max' veya 'min' değerlerinden birini girdiğinize emin olunuz.")

dic_val(old,"min")                    # calling function with "old" and "min" attributes
            


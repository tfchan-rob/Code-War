#!/usr/bin/env python
# coding: utf-8

# # Complementary DNA

# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
# 
# If you want to know more http://en.wikipedia.org/wiki/DNA
# 
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
# 
# More similar exercise are found here http://rosalind.info/problems/list-view/ (source)

# example:
# 
# DNA_strand ("ATTGC") # return "TAACG"
# 
# DNA_strand ("GTAT") # return "CATA"

# ## my solution

# In[4]:


def DNA_strand(dna):
    
    newlist = ''
    
    for w in dna:
        if w == str('A'):
            newlist += str('T')
        if w == str('T'):
            newlist += str('A')
        if w == str('C'):
            newlist += str('G')
        if w == str('G'):
            newlist += str('C')
            
    return newlist


# In[ ]:





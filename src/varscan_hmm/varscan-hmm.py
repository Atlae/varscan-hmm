import pandas as pd

# Change this to be agnostic of my directory lol `import os` or smth
print(pd.read_csv(r"C:\Users\pokem\varscan-hmm\example\trio.mpileup", sep="\t").head())
"""
PS C:\Users\pokem\varscan-hmm> & c:/Users/pokem/varscan-hmm/.venv/Scripts/python.exe c:/Users/pokem/varscan-hmm/src/varscan_hmm/varscan-hmm.py
   chr6  128405804  T  22  ...  CDFkFEGJIIJIJJIIJGJJEJJGGJJJJJIFFFF  21     .....................   ECEAFIoJIJJJJGJJJCJIA
0  chr6  128405805  T  23  ...  CEFkFHJIJJJJJJBJJHJJIJJIGJIJJJIFFFF  21     .....................   DEEEFHqIIIJJJGJJJEIJ?
1  chr6  128405806  C  22  ...  DEEkFHJJJJJJJJGJIJJJJJJIHJJJJJ9?FFF  22  .....................^].  DEECFGqHJJJJJEJJJGJJ4C
2  chr6  128405807  T  22  ...  DDDkFFHJJJIJJJIJIJJJJJJIIJJJJJHGFFF  22    ......................  DDECFHqIJJJJIFJJJGJJDC
3  chr6  128405808  A  22  ...  DDEkFFHJJJIJIJIIIIJJIJJIIJJJJGEBHFF  22   .$.....................  DDEEEHoJJJJJI>JJJGJJDC
4  chr6  128405809  T  22  ...  >EEkFHHJJJJIJJEJJGJJJJJGJJGJJIEGHHH  21     .....................   DECEHoJJJJJJAJJJBJJ<F

[5 rows x 12 columns]
"""
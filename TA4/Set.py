#CUETO, ALEXA JOYCE G
#TW23
#SET 

setA = {"a", "b", "c", "d", "f", "g"}
setB = {"l", "m", "o", "b", "c", "h"}
setC = {"c", "h", "k", "i", "j", "f", "d"}

#Number of elements in SET A and SET B
setD = setA.union(setB)
print(len(setD))

#Elements in B but not in A and C
setE = setB.difference(setA, setC)
print(len(setE))

#Show [h,i,j,k]
result1 = setC.intersection({"h", "i", "j", "k"})
print(f"[{', '.join(result1)}]")

#Show [c,d,f]
result2 = setA.intersection(setB, setC)
result3 = setA.intersection(setC)
result4 = result2.union(result3)
print(f"[{', '.join(result4)}]")

#Show [b,c h]
result5 = setA.intersection(setB).union(setB.intersection(setC))
print(f"[{', '.join(result5)}]")


#Show [d,f]
result6 = setA.intersection(setC) - {"c"}
print(f"[{', '.join(result6)}]")

#Show [c] 
result7 = setA.intersection(setB, setC) 
print(f"[{', '.join(result7)}]")

#Show [l,m,o]
result8 = setB.difference(setA)
result9 = result8.difference(setC)
print(f"[{', '.join(result9)}]")
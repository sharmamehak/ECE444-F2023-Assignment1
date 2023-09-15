class utils: 
  def reversed(num):
    s=len(num)
    newnum=[None]*length
    for i in num:
        s=s-1
        newnum[s]=i
        return newnum
  def formatter(num):
    r1 = bin(num)
    r2 = oct(num)
    return r1,r2
    

class utils: 
  def reversed(num):
    return int(str(num)[::-1])
  def formatter(num):
    r1 = bin(num)
    r2 = oct(num)
    return r1,r2
    

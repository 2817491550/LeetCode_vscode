from bitarray import  bitarray
import  mmh3
class BloomFilter():
    def __init__(self,size,hashnum):
        super().__init__()
        self.bit_array=bitarray(size)
        self.hashnum=hashnum
        self.bit_array.setall(0)
        self.size=size
    def add(self,s):
        for seed in range(self.hashnum):
            result=mmh3.hash(s,seed)%self.size
            self.bit_array[result]=1
    def lookup(self,s):
        for seed in range(self.hashnum):
            result=mmh3.hash(s,seed)%self.size
            if self.bit_array[result]==0:
                return "Nope"
        return "Probably"
    
bf=BloomFilter(20,3)
bf.add("ddd")
print(bf.lookup("bbb"))
print(bf.bit_array)

            
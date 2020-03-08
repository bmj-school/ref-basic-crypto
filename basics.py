class bit32:
    def __init__(self, hexval, bits=32):
        assert bits%4 == 0
        self.val = hexval
        self.bitwidth = bits
        self.hexwidth = int(bits/4)

    def __repr__(self):
        return "|{}|0x{}|{}|".format(self.int, self.hexstring, self.bitstring)

    @property
    def int(self):
        return(self.val)

    @property
    def bitstring(self):
        return '{val:0{width}b}'.format(width=self.bitwidth, val=self.val)

    @property
    def hexstring(self):
        return '{val:0{width}x}'.format(width=self.hexwidth, val=self.val)
        # return f"{self.val:016x}"

    @property
    def bits(self):
        return bin(self.val)

a = bit32(22, 32)
# a.hex = "asdf"
print('Value:', a)
# print(a.bitstring)
# print(a.hexstring)
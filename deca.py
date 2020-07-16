# -*- coding: utf-8 -*-
#行同期的解密
#未完成。不太理解反编译的JAVA代码，试着原样抄了一下好像不对，暂且这么放着

class c:
    def __init__(self):
        self.e = b'2.00'
        self.f = b'MHDROBJT'
        self.g = b'MLRCOBJT'
        self.a = 0
        self.b = cjc(self)
        self.c = 0
        self.strd = 0
        self.a = cjd(self)
        self.a.b = cjc(self)
        file = open('test', 'rb')
        self.fhex = file.read()

    def b_func(self):
        assert self.fhex[0:8] == b'MHDROBJT'  # Header Matching MHDROBJT
        v4 = self.fhex[8:12]
        v5 = 0
        v6 = 0
        while v5 < len(v4):
            v6 = (v6 << 8) + ((v4[((len(v4) - 1) - v5)] + 256) % 256)
            v5 += 1
        assert v6 == 44
        self.a.a = self.fhex[12:16]
        assert self.a.a == b'2.00'
        self.a.b.a = self.fhex[24]
        self.a.b.b = self.fhex[25]
        v4 = self.fhex[26:28]
        p0 = 0
        self.a.b.c = 0
        while p0 < len(v4):
            self.a.b.c = ((self.a.b.c << 8) + ((v4[((len(v4) - 1) - p0)] + 256) % 256))
            p0 += 1
        print(self.a.b.c)

    def c1_func(self):
        v0 = self.a.b
        if  not v0.a:
            v0 = v0.c
            return v0
        elif v0.b ==1:
            v0 = v0.c
            v0 = (v0&0x03)|(((((((((0x0000c000&v0)>>14)<<14)|((byte)((v0&0x0c00)>>10)<<12))|(((v0&0x3000)>>12)<<10))|(((v0&0x00c0)>>6)<<8))|(((v0&0x0300)>>8)<<6))|(((v0&0x0c)>>2)<<4))|(((v0&0x30)>>4)<<2))
            return  v0
        else:
            v0 = v0.c
            return v0


    def c2_func(self):
        v1 = self
        assert self.fhex[44:52] == b'MLRCOBJT'  # Header Matching -- MLRCOBJT
        v6 = b''
        v4 = 8
        v6 = self.fhex[52:56]
        v8 = 0
        while v8 < len(v6):
            v8 += 1
        v6 = self.fhex[56:60]
        v5 = 0
        # v1=this
        v1.b.a = 0

        while v5 < len(v6):
            v1.b.a = ((v1.b.a << v4) + ((v6[((len(v6) - 1) - v5)] + 256) % 256))
            v5 += 1
        v7 = 0
        v5 = v1.b.a + v7
        v8_1 = self.c1_func()
        v9 = self.fhex[64:66]
        v11 = 0
        while v11 < len(v9):
            v1.b.b = ((v1.b.b << v4) + ((v9[((len(v9) - 1) - v11)] + 256) % 256))
            v11 +=1
        v11 = 66
        v9 = self.fhex[v11:68]
        v12 = 0
        while v12 < len(v9):
            v1.b.c = ((v1.b.c << v4) + ((v9[((len(v9) - 1) - v12)] + 256) % 256))
            v12 +=1
        v12 = 0x00010000
        v13 = 0
        v14 = 0
        v15 = 0
        v16 = 0
        while v13 <v5:
            v9  =self.fhex[(v13*2)+204:(v13*2)+204+2]
            v4 =0
            v16 = 0
            while v4<len(v9):
                v16 = (v16 << 8) + ((v9[((len(v9) - 1) - v4)] + 256) % 256)
                v4+=1
            if v1.a.b.a == 1:
                v16 = v16 ^ v8_1
            v7 = v16 + (v12 * v15)
            while v14 >v7:
                v15 +=1
                if v14 <= v7:
                    break
            v1.c = (v7 * 10)
            v13 +=1
            v16 = v4
            v14 = v7
            v7 = 0
        v7 = 0
#  j = c
class cjc:
    def __init__(self,p0):
        super().__init__()
        p0 = 0
        self.a = p0
        self.b = p0
        self.c = p0

class cjd:
    def __init__(self,p0):
        super().__init__()
        self.c = p0


ca = c()
ca.c2_func()

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class LessEqualOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsLessEqualOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = LessEqualOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def LessEqualOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # LessEqualOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def LessEqualOptionsStart(builder): builder.StartObject(0)
def LessEqualOptionsEnd(builder): return builder.EndObject()
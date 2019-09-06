# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite

import flatbuffers

class L2NormOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsL2NormOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = L2NormOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def L2NormOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # L2NormOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # L2NormOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def L2NormOptionsStart(builder): builder.StartObject(1)
def L2NormOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def L2NormOptionsEnd(builder): return builder.EndObject()

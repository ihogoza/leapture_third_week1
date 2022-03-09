# from pyasn1.codec.native import *



# class Record(Sequence):
#     componentType = NamedTypes(
#         NamedType('id', Integer()),
#         OptionalNamedType(
#             'room', Integer().subtype(
#                 implicitTag=Tag(tagClassContext, tagFormatSimple, 0)
#             )
#         ),
#         DefaultedNamedType(
#             'house', Integer(0).subtype(
#                 implicitTag=Tag(tagClassContext, tagFormatSimple, 1)
#             )
#         )
#     )
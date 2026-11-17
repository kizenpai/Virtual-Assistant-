from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    IFontEventsDisp, BSTR, CoClass, Monochrome, OLE_YPOS_HIMETRIC,
    Color, IPicture, _check_version, DISPMETHOD, VgaColor, Default,
    IDispatch, FontEvents, OLE_YSIZE_HIMETRIC, IFontDisp,
    OLE_ENABLEDEFAULTBOOL, OLE_YSIZE_PIXELS, COMMETHOD, HRESULT,
    FONTSTRIKETHROUGH, Unchecked, IUnknown, OLE_HANDLE, IFont, Gray,
    Picture, OLE_XSIZE_PIXELS, OLE_YSIZE_CONTAINER, StdPicture, _lcid,
    OLE_YPOS_PIXELS, OLE_YPOS_CONTAINER, OLE_XPOS_PIXELS, FONTBOLD,
    FONTUNDERSCORE, Checked, FONTITALIC, dispid, VARIANT_BOOL, GUID,
    OLE_CANCELBOOL, OLE_XPOS_CONTAINER, DISPPROPERTY,
    OLE_OPTEXCLUSIVE, FONTNAME, DISPPARAMS, Library, typelib_path,
    OLE_COLOR, IEnumVARIANT, OLE_XSIZE_CONTAINER, OLE_XPOS_HIMETRIC,
    IPictureDisp, EXCEPINFO, OLE_XSIZE_HIMETRIC, Font, FONTSIZE,
    StdFont
)


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


__all__ = [
    'OLE_XSIZE_PIXELS', 'OLE_YSIZE_CONTAINER', 'StdPicture',
    'LoadPictureConstants', 'IFontEventsDisp', 'Monochrome',
    'OLE_YPOS_HIMETRIC', 'Color', 'OLE_YPOS_PIXELS',
    'OLE_YPOS_CONTAINER', 'IPicture', 'OLE_XPOS_PIXELS',
    'OLE_TRISTATE', 'FONTBOLD', 'FONTUNDERSCORE', 'Checked',
    'FONTITALIC', 'OLE_CANCELBOOL', 'VgaColor', 'OLE_XPOS_CONTAINER',
    'OLE_OPTEXCLUSIVE', 'Default', 'FONTNAME', 'FontEvents',
    'OLE_YSIZE_HIMETRIC', 'Library', 'typelib_path', 'OLE_COLOR',
    'IFontDisp', 'OLE_ENABLEDEFAULTBOOL', 'OLE_XSIZE_CONTAINER',
    'OLE_XPOS_HIMETRIC', 'IPictureDisp', 'OLE_YSIZE_PIXELS',
    'OLE_XSIZE_HIMETRIC', 'FONTSTRIKETHROUGH', 'Unchecked',
    'OLE_HANDLE', 'IFont', 'Font', 'FONTSIZE', 'StdFont', 'Gray',
    'Picture'
]


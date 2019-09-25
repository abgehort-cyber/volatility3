# This file is Copyright 2019 Volatility Foundation and licensed under the Volatility Software License 1.0
# which is available at https://www.volatilityfoundation.org/license/vsl-v1.0
#

from volatility.framework import interfaces
from volatility.framework.symbols import intermed
from volatility.framework.symbols.windows import extensions
from volatility.framework.symbols.windows.extensions import registry


class WindowsKernelIntermedSymbols(intermed.IntermediateSymbolTable):

    def __init__(self, context: interfaces.context.ContextInterface, config_path: str, name: str, isf_url: str) -> None:
        super().__init__(context = context, config_path = config_path, name = name, isf_url = isf_url)

        # Set-up windows specific types
        self.set_type_class('_ETHREAD', extensions._ETHREAD)
        self.set_type_class('_LIST_ENTRY', extensions._LIST_ENTRY)
        self.set_type_class('_EPROCESS', extensions._EPROCESS)
        self.set_type_class('_UNICODE_STRING', extensions._UNICODE_STRING)
        self.set_type_class('_EX_FAST_REF', extensions._EX_FAST_REF)
        self.set_type_class('_OBJECT_HEADER', extensions._OBJECT_HEADER)
        self.set_type_class('_FILE_OBJECT', extensions._FILE_OBJECT)
        self.set_type_class('_DEVICE_OBJECT', extensions._DEVICE_OBJECT)
        self.set_type_class('_CM_KEY_BODY', registry._CM_KEY_BODY)
        self.set_type_class('_CMHIVE', registry._CMHIVE)
        self.set_type_class('_CM_KEY_NODE', registry._CM_KEY_NODE)
        self.set_type_class('_CM_KEY_VALUE', registry._CM_KEY_VALUE)
        self.set_type_class('_HMAP_ENTRY', registry._HMAP_ENTRY)
        self.set_type_class('_MMVAD_SHORT', extensions._MMVAD_SHORT)
        self.set_type_class('_MMVAD', extensions._MMVAD)
        self.set_type_class('_KSYSTEM_TIME', extensions._KSYSTEM_TIME)
        self.set_type_class('_KMUTANT', extensions._KMUTANT)
        self.set_type_class('_DRIVER_OBJECT', extensions._DRIVER_OBJECT)
        self.set_type_class('_OBJECT_SYMBOLIC_LINK', extensions._OBJECT_SYMBOLIC_LINK)

        # This doesn't exist in very specific versions of windows
        try:
            self.set_type_class('_POOL_HEADER', extensions._POOL_HEADER)
        except ValueError:
            pass

        # these don't exist in windows XP
        try:
            self.set_type_class('_MMADDRESS_NODE', extensions._MMVAD_SHORT)
        except ValueError:
            pass

        # these were introduced starting in windows 8
        try:
            self.set_type_class('_MM_AVL_NODE', extensions._MMVAD_SHORT)
        except ValueError:
            pass

        # these were introduced starting in windows 7
        try:
            self.set_type_class('_RTL_BALANCED_NODE', extensions._MMVAD_SHORT)
        except ValueError:
            pass

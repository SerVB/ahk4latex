# -*- coding: utf-8 -*-

FILE_BEGIN = r"""#NoEnv  ; --- Recommended for performance and compatibility with future AutoHotkey releases. ---
SendMode Input  ; --- Recommended for new scripts due to its superior speed and reliability. ---


; ------ Common commands (TODO: add Ctrl+T) ------
; --- ; F14 to "$" ---
F14::$
; --- Turn NumLock on ---
SetNumLockState, On
; ------ End common commands ------


; ------ Math mode logic ------
mathMode = false

; --- NumLock switches the math mode and keeps itself active
NumLock::
; --- TODO: Add toasts about current mode ---
mathMode := !mathMode

; --- Don't deactivate num lock ---
SetNumLockState, On
return
; ------ End math mode logic ------

#If mathMode  ; ------ Keys in math mode ------"""


FILE_MIDDLE = r"""#If  ; ------ End keys in math mode ------

; ------ Sequences ------"""


FILE_END = r"""; ------ End sequences ------"""


LETTER_BINDING = r"""
; --- {source} to "{to}" ---
{sourceAhk}::
mathMode = false
SendRaw {to}
return"""


SEQUENCE_BINDING = r"""
; --- {source} to "{to}" ---
::{sourceAhk}::
SendRaw {to}
return"""

from enum import Enum

from .control_flow import jump, jump_z, jump_n
from .arithmetic import add, sub, inc, dec
from .memory import copy_to, copy_from
from .io import inbox, outbox


class BasInstructions(Enum):
    INBOX = inbox
    OUTBOX = outbox


class CellInstructions(Enum):
    ADD = add
    SUB = sub
    INC = inc
    DEC = dec
    COPY_TO = copy_to
    COPY_FROM = copy_from


class LineInstructions(Enum):
    JUMP = jump
    JUMP_Z = jump_z
    JUMP_N = jump_n


__all__ = (
    'jump',
    'jump_z',
    'jump_n',

    'copy_to',
    'copy_from',

    'add',
    'sub',
    'inc',
    'dec',

    'inbox',
    'outbox',

    'BasInstructions',
    'CellInstructions',
    'LineInstructions'
)

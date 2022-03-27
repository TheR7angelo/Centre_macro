from PySide6.QtCore import Qt


class DropAction:

    def copy(self): return Qt.CopyAction
    def move(self): return Qt.MoveAction
    def link(self): return Qt.LinkAction
    def action_mask(self): return Qt.ActionMask
    def target_move(self): return Qt.TargetMoveAction
    def ignore(self): return Qt.IgnoreAction

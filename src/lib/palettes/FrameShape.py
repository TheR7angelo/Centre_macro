from PySide6.QtWidgets import QFrame


class FrameShape:

    def no_frame(self): return QFrame.NoFrame
    def box(self): return QFrame.Box
    def panel(self): return QFrame.Panel
    def win_panel(self): return QFrame.WinPanel
    def h_line(self): return QFrame.HLine
    def v_line(self): return QFrame.VLine
    def styled_panel(self): return QFrame.StyledPanel

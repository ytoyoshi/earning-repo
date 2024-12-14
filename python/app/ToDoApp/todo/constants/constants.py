from typing import Any

#TODO Pythonでの定数の扱い方のベストプラクティスを調べる
"""
DBで管理？　定数管理用のファイル？
"""
class COMPLETE_TYPE:
    Incomplete = '0'
    complete = '1'

    def __instancecheck__(self, __instance: Any) -> bool:
        pass
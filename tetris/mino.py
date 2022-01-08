import numpy as np
import random as rand
import field

"""
ミノクラス
"""
class MINO():
    # コンストラクタ
    def __init__(self, _field=None, _rnd=None, _color=None, _x=None, _y=None):
        self.block = field.BLOCK()
        self.Field = _field
        # ミノ形状の決定
        if _rnd is None: self.rnd = rand.randint(0, 6)
        else: self.rnd = _rnd
        # I型
        if self.rnd == 0:
            self.x = np.array([0, 1, 2, 3])
            self.y = np.array([0, 0, 0, 0])
            self.block.color = "cyan"
        # O型
        elif self.rnd == 1:
            self.x = np.array([0, 1, 0, 1])
            self.y = np.array([0, 0, 1, 1])
            self.block.color = "yellow"
        # S型
        elif self.rnd == 2:
            self.x = np.array([1, 2, 0, 1])
            self.y = np.array([0, 0, 1, 1])
            self.block.color = "green"
        # Z型
        elif self.rnd == 3:
            self.x = np.array([0, 1, 1, 2])
            self.y = np.array([0, 0, 1, 1])
            self.block.color = "red"
        # J型
        elif self.rnd == 4:
            self.x = np.array([1, 1, 0, 1])
            self.y = np.array([0, 1, 2, 2])
            self.block.color = "blue"
        # L型
        elif self.rnd == 5:
            self.x = np.array([0, 0, 0, 1])
            self.y = np.array([0, 1, 2, 2])
            self.block.color = "orange"
        # T型
        elif self.rnd == 6:
            self.x = np.array([1, 0, 1, 2])
            self.y = np.array([0, 1, 1, 1])
            self.block.color = "purple"

        # 指定がある際の処理
        # 色が指定されている場合の修正
        if _color is not None: self.block.color = _color
        # x座標が指定されている場合の修正
        if _x is not None: self.x = _x
        # y座標が指定されている場合の修正
        if _y is not None: self.y = _y

    # 重なりの判定
    def overlap(self, _field):
        for n in range (4):
            # フィールド外の判断
            if 0 > self.x[n] or self.x[n] >= field.FieldWidth \
                or 0 > self.y[n] or self.y[n] >= field.FieldHeight:
                return False
            # 重複の判断
            if _field.Field[self.x[n]][self.y[n]].color != field.initial_block_color:
                return False
        return True

    # ミノ単体の表示
    def display(self, _canvas):
        # ミノの表示
        for n in range (4):
            _canvas.create_rectangle(
                        self.x[n] * field.BlockSize, self.y[n] * field.BlockSize,
                        (self.x[n] + 1) * field.BlockSize, (self.y[n] + 1) * field.BlockSize,
                        outline = "white", width = 1, fill = self.block.color)
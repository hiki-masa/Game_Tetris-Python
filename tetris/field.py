"""
ブロッククラス
"""
BlockSize = 20
initial_block_color = "gray"
class BLOCK():
    # コンストラクタ
    def __init__(self):
        self.color = initial_block_color

"""
フィールドクラス
"""
FieldWidth = 10
FieldHeight = 20
class FIELD():
    # コンストラクタ
    def __init__(self, _canvas):
        self.Canvas = _canvas
        self.Field = [[]]
        for x in range (FieldWidth):
            self.Field.append([])
            for y in range (FieldHeight):
                self.Field[x].append(BLOCK())

    # フィールドの表示
    def display(self, mino):
        # フィールドの表示
        for x in range (FieldWidth):
            for y in range (FieldHeight):
                self.Canvas.create_rectangle(
                    x * BlockSize, y * BlockSize,
                    (x + 1) * BlockSize, (y + 1) * BlockSize,
                    outline = "white", width = 1, fill = self.Field[x][y].color)
        # ミノの表示
        for n in range (4):
            self.Canvas.create_rectangle(
                        mino.x[n] * BlockSize, mino.y[n] * BlockSize,
                        (mino.x[n] + 1) * BlockSize, (mino.y[n] + 1) * BlockSize,
                        outline = "white", width = 1, fill = mino.block.color)

    # フィールドにブロックの追加
    def addMino(self, mino):
        for n in range (4):
            self.Field[mino.x[n]][mino.y[n]].color = mino.block.color

    # 行の削除
    def del_line(self):
        for y in range(FieldHeight-1, 0, -1):
            for x in range(FieldWidth):
                # 空欄がある場合
                if self.Field[x][y].color == initial_block_color:
                    break
                # 1行揃っている場合
                elif x == FieldWidth-1:
                    # 行の削除 & 行の落下
                    for tmp_y in range(y, 0, -1):
                        for tmp_x in range(FieldWidth):
                            self.Field[tmp_x][tmp_y].color = self.Field[tmp_x][tmp_y-1].color
                    self.del_line()
import numpy as np
import tkinter as tk
import field
import mino

DisplayWidth  = 300
DisplayHeight = 400

"""
テトリスメインクラス
"""
class TETRIS(tk.Frame):
    # コンストラクタ
    def __init__(self, master):
        super().__init__(master)
        # ウィンドウサイズを固定
        master.resizable(width = False, height = False)
        # ウィンドウの設定
        master.minsize(DisplayWidth, DisplayHeight)
        master.title("テトリス")

        # キャンバスの設定
        self.main_canvas = tk.Canvas(master, width = 200, height = 400, bg = "white")
        self.main_canvas.pack(side=tk.LEFT)
        mini_canvas_label = tk.Label(text="Next")
        mini_canvas_label.pack(side=tk.TOP, anchor="center")
        self.mini_canvas = tk.Canvas(master, width = 80, height = 80, bg = "white")
        self.mini_canvas.pack(side=tk.TOP, anchor="center")

        # フィールドの設定
        self.Field = field.FIELD(self.main_canvas)
        # ミノの設定
        self.falling_mino = mino.MINO(self.Field)
        self.next_mino = mino.MINO(self.Field)
        # フィールド　および　次のミノの表示
        self.Field.display(self.falling_mino)
        self.next_mino.display(self.mini_canvas)

        # キーボード操作
        master.bind("<a>",     self.move_left)
        master.bind("<Left>",  self.move_left)
        master.bind("<d>",     self.move_right)
        master.bind("<Right>", self.move_right)
        master.bind("<s>",     self.move_down)
        master.bind("<Down>",  self.move_down)
        master.bind("<space>", self.turn)

        # 一定時間経過時の処理登録
        self.time_pass_process()

    """
    ミノの移動
    """
    # 左への移動操作
    def move_left(self, event):
        tmp_x = np.copy(self.falling_mino.x)
        self.falling_mino.x -= 1
        # 移動可能時
        if self.falling_mino.overlap(self.Field):
            # 移動前ブロックを背景色で描画
            tmp_mino = mino.MINO(self.Field, self.falling_mino.rnd, field.initial_block_color, tmp_x, self.falling_mino.y)
            tmp_mino.display(self.falling_mino.Field.Canvas)
            # 移動後ブロックの描画
            self.falling_mino.display(self.falling_mino.Field.Canvas)
        # 移動不可能時
        else:
            self.falling_mino.x = tmp_x
    # 右への移動操作
    def move_right(self, event):
        tmp_x = np.copy(self.falling_mino.x)
        self.falling_mino.x += 1
        # 移動可能時
        if self.falling_mino.overlap(self.Field):
            # 移動前ブロックを背景色で描画
            tmp_mino = mino.MINO(self.Field, self.falling_mino.rnd, field.initial_block_color, tmp_x, self.falling_mino.y)
            tmp_mino.display(self.falling_mino.Field.Canvas)
            # 移動後ブロックの描画
            self.falling_mino.display(self.falling_mino.Field.Canvas)
        # 移動不可能時
        else:
            self.falling_mino.x = tmp_x
    # 下への移動操作
    def move_down(self, event):
        tmp_y = np.copy(self.falling_mino.y)
        self.falling_mino.y += 1
        # 移動可能時
        if self.falling_mino.overlap(self.Field):
            # 移動前ブロックを背景色で描画
            tmp_mino = mino.MINO(self.Field, self.falling_mino.rnd, field.initial_block_color, self.falling_mino.x, tmp_y)
            tmp_mino.display(self.falling_mino.Field.Canvas)
            # 移動後ブロックの描画
            self.falling_mino.display(self.falling_mino.Field.Canvas)
        # 移動不可能時
        else:
            self.falling_mino.y = tmp_y
            # フィールドに落下ミノを追加
            self.Field.addMino(self.falling_mino)
            self.Field.del_line()
            # 落下ミノの更新 & 表示
            self.falling_mino = self.next_mino
            self.Field.display(self.falling_mino)
            # 次のミノの更新 & 表示
            tmp_mino = mino.MINO(_rnd=self.next_mino.rnd, _color="white")
            self.next_mino = mino.MINO(self.Field)
            tmp_mino.display(self.mini_canvas)
            self.next_mino.display(self.mini_canvas)
            # 新規ミノがフィールドブロックと重なれば，ゲーム終了
            if not self.falling_mino.overlap(self.Field):
                exit(0)
    # 回転
    def turn(self, event):
        # 回転前の座標記録（値渡し）
        tmp_x = np.copy(self.falling_mino.x)
        tmp_y = np.copy(self.falling_mino.y)
        # 原点移動
        move_x = min(self.falling_mino.x)
        move_y = min(self.falling_mino.y)
        self.falling_mino.x -= move_x
        self.falling_mino.y -= move_y
        # 回転
        for i in range (4):
            tmp = self.falling_mino.x[i]
            self.falling_mino.x[i] = -self.falling_mino.y[i] + 4 - 1
            self.falling_mino.y[i] = tmp
        # 位置調整
        self.falling_mino.x -= min(self.falling_mino.x)
        self.falling_mino.y -= min(self.falling_mino.y)
        # 元の位置に移動
        self.falling_mino.x += move_x
        self.falling_mino.y += move_y
        # 移動可能時
        if self.falling_mino.overlap(self.Field):
            # 移動前ブロックを背景色で描画
            tmp_mino = mino.MINO(self.Field, self.falling_mino.rnd, field.initial_block_color, tmp_x, tmp_y)
            tmp_mino.display(self.falling_mino.Field.Canvas)
            # 移動後ブロックの描画
            self.falling_mino.display(self.falling_mino.Field.Canvas)
        # 回転後，重複が発生した場合，元の座標に修正
        else:
            self.falling_mino.x = tmp_x
            self.falling_mino.y = tmp_y

    # 一定時間経過時の処理
    def time_pass_process(self):
        self.master.after(1000, self.time_pass_process)
        self.move_down(None)
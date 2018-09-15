#coding: UTF-8
#作業ディレクトリの特定拡張子のファイルのみ画像を切り抜く処理
#[x:x+w,y:y+h]で画像を切り抜く
import cv2
import os

#　窓画像の左上座標
x, y = 622, 0
#　窓画像の幅、高さ
w, h = 1297-622, 1080

#現在の作業ディレクトリにあるファイルをすべて取得
files = os.listdir(os.getcwd())
#取得したファイルすべてを走査
for f in files:
#特定の拡張子のみ切り取りを適用（下記は.jpgのみの場合）
	if '.jpg' in f:
#切り取り処理
		im = cv2.imread(f)
		dst = im[y:y+h,x:x+w]
		cv2.imwrite(f,dst)


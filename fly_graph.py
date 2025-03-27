#fly_data.cで作ったテキストファイルのデータをもとに人の飛行軌道を画像として保存するプログラム
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["mathtext.fontset"] = "cm"

fname = "fly_data.txt"  #入力ファイル名
gname = "graph.png"     #画像の名前
gformat = "png"         #画像の保存形式
dpi = 300               #画像の解像度

data = np.loadtxt(fname)    #データの入力
t = data[:,0]   #時間
x = data[:,1]   #x座標
y = data[:,2]   #y座標
vx = data[:,3]  #x方向の速度
vy = data[:,4]  #y方向の速度

plt.plot(x,y)   #軌道を描画
#飛行時間をグラフの上に表示
plt.title("$\mathrm{}\ \mathrm{} = {}$" .format("{flight}","{time}",t[-1]),fontsize=16)
plt.xlabel("$x$", fontsize=18)
plt.ylabel("$y$", fontsize=18)
plt.savefig(gname, format=gformat, dpi=dpi) #画像の保存
plt.show()
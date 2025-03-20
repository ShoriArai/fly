#作成したデータをもとにグラフを作るプログラム
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["mathtext.fontset"] = "cm"

fname = "fly_data.txt"
gname = "graph.png"
gformat = "png"
dpi = 300

data = np.loadtxt(fname)
t = data[:,0]   #時間
x = data[:,1]   #x座標
y = data[:,2]   #y座標
vx = data[:,3]  #x方向の速度
vy = data[:,4]  #y方向の速度

plt.plot(x,y)
plt.title("$\mathrm{Orbit}$", fontsize=20)
plt.xlabel("$x$", fontsize=18)
plt.ylabel("$y$", fontsize=18)
plt.savefig(gname, format=gformat, dpi=dpi)
#plt.show()

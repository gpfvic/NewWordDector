#coding:UTF8
a = "行者、师父、三藏、八戒、大圣、菩萨、悟空、怎么、和尚、唐僧、老孙、溃骸、什么、沙僧、太宗、徒弟、袈裟、妖精、玉帝、今日、兄弟、公主、玄奘、陛下、宝贝、性命、晓得、门外、妖魔、光蕊、观音、花果山、土地、木叉、东土、变化、变做、伯钦、判官、多少、真君、齐天大圣、蟠桃、丞相、魏征、扯住、溃骸澳、抬头、揭谛、言语、猪八戒、兵器、吩咐、安排、叩头、清风、哪吒、左右、美猴王、钉钯、孩儿、女婿、金箍棒、二郎、东西、许多、奈何、人参果、收拾、近前、太保、明月、南海、水帘洞、门首、弼马温、李天王"

f = []
s = []
e = []

ws = a.split("、")
for row in open("../res.txt"):
    word = row.strip().split("\t")[0]
    freq = row.strip().split("\t")[1].split(":")[1]
    sol = row.strip().split("\t")[2].split(":")[1]
    ent = row.strip().split("\t")[3].split(":")[1]

    if len([w for w in ws if w==word])>0:
        f.append(int(freq))
        s.append(float(sol))
        e.append(float(ent))
        print row.strip()
        

print "Average Freq:%2f MIN:%2f" % (sum(f)/float(len(f)), min(f))
print "Average Sol:%2f MIN:%2f" % (sum(s)/float(len(s)), min(s))
print "Average Ent:%2f MIN:%2f" % (sum(e)/float(len(e)), min(e))

print len(ws),len(f)


# 大圣    FRQ:1270    SOL:102.26    ENT:2.93
# 多少    FRQ:161    SOL:258.19    ENT:2.40
# 菩萨    FRQ:783    SOL:735.23    ENT:3.81
# 明月    FRQ:37    SOL:77.13    ENT:2.29
# 钉钯    FRQ:112    SOL:1211.99    ENT:2.96
# 玉帝    FRQ:189    SOL:511.16    ENT:3.02
# 李天王    FRQ:57    SOL:217.28    ENT:2.52
# 袈裟    FRQ:155    SOL:3780.19    ENT:3.39
# 齐天大圣    FRQ:102    SOL:0.04    ENT:3.03
# 变化    FRQ:150    SOL:168.18    ENT:3.51
# 玄奘    FRQ:90    SOL:3258.26    ENT:2.66
# 言语    FRQ:117    SOL:151.60    ENT:3.32
# 木叉    FRQ:56    SOL:648.48    ENT:2.47
# 孩儿    FRQ:100    SOL:225.87    ENT:3.03
# 弼马温    FRQ:49    SOL:5926.11    ENT:2.35
# 三藏    FRQ:1382    SOL:151.41    ENT:3.41
# 魏征    FRQ:43    SOL:6589.78    ENT:2.77
# 徒弟    FRQ:439    SOL:284.17    ENT:2.86
# 门外    FRQ:175    SOL:83.68    ENT:3.19
# 猪八戒    FRQ:131    SOL:126.79    ENT:2.98
# 门首    FRQ:64    SOL:112.54    ENT:2.93
# 近前    FRQ:141    SOL:113.60    ENT:3.46
# 奈何    FRQ:117    SOL:250.51    ENT:1.55
# 东西    FRQ:81    SOL:82.28    ENT:3.02
# 东土    FRQ:212    SOL:362.29    ENT:2.32
# 吩咐    FRQ:128    SOL:4466.70    ENT:3.38
# 怎么    FRQ:774    SOL:207.04    ENT:2.62
# 悟空    FRQ:512    SOL:395.76    ENT:1.97
# 真君    FRQ:49    SOL:57.78    ENT:2.34
# 安排    FRQ:114    SOL:571.66    ENT:3.21
# 妖精    FRQ:634    SOL:156.16    ENT:3.08
# 妖魔    FRQ:190    SOL:55.54    ENT:3.39
# 公主    FRQ:193    SOL:345.98    ENT:3.59
# 光蕊    FRQ:55    SOL:557.91    ENT:2.12
# 哪吒    FRQ:73    SOL:5687.51    ENT:2.71
# 二郎    FRQ:52    SOL:203.56    ENT:2.79
# 八戒    FRQ:1808    SOL:251.91    ENT:3.36
# 美猴王    FRQ:42    SOL:207.41    ENT:2.77
# 判官    FRQ:51    SOL:592.87    ENT:2.06
# 清风    FRQ:46    SOL:74.17    ENT:2.20
# 扯住    FRQ:100    SOL:169.90    ENT:2.18
# 女婿    FRQ:36    SOL:699.26    ENT:2.17
# 人参果    FRQ:33    SOL:174.57    ENT:2.41
# 土地    FRQ:180    SOL:192.25    ENT:3.15
# 蟠桃    FRQ:56    SOL:2819.65    ENT:2.31
# 太宗    FRQ:168    SOL:693.38    ENT:2.66
# 太保    FRQ:28    SOL:81.55    ENT:2.36
# 行者    FRQ:4337    SOL:91.07    ENT:3.49
# 花果山    FRQ:79    SOL:257.36    ENT:2.88
# 叩头    FRQ:113    SOL:226.55    ENT:2.10
# 师父    FRQ:1633    SOL:193.78    ENT:3.69
# 兵器    FRQ:158    SOL:867.78    ENT:3.48
# 唐僧    FRQ:1005    SOL:143.81    ENT:4.03
# 观音    FRQ:115    SOL:379.67    ENT:2.33
# 沙僧    FRQ:816    SOL:151.82    ENT:2.83
# 伯钦    FRQ:47    SOL:3468.01    ENT:2.13
# 金箍棒    FRQ:124    SOL:428.26    ENT:2.88
# 揭谛    FRQ:84    SOL:3573.99    ENT:2.07
# 和尚    FRQ:788    SOL:544.54    ENT:3.12
# 晓得    FRQ:120    SOL:90.66    ENT:2.64
# 抬头    FRQ:101    SOL:101.25    ENT:2.19
# 南海    FRQ:63    SOL:174.89    ENT:2.52
# 水帘洞    FRQ:52    SOL:524.65    ENT:2.45
# 兄弟    FRQ:284    SOL:244.91    ENT:3.10
# 收拾    FRQ:92    SOL:950.21    ENT:3.13
# 丞相    FRQ:47    SOL:339.26    ENT:2.72
# 性命    FRQ:203    SOL:356.49    ENT:3.01
# 左右    FRQ:124    SOL:1176.08    ENT:3.53
# 许多    FRQ:103    SOL:265.41    ENT:2.39
# 宝贝    FRQ:283    SOL:675.40    ENT:3.30
# 变做    FRQ:159    SOL:101.16    ENT:2.66
# 今日    FRQ:282    SOL:111.34    ENT:3.39
# 老孙    FRQ:617    SOL:78.53    ENT:3.37
# 陛下    FRQ:168    SOL:194.71    ENT:3.37
# Average Freq:318.000000
# Average Sol:808.150405
# Average Ent:2.835270


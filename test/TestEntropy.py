#coding:utf-8
'''
Created on 2015��8��12��

@author: g00297221
'''
import re
import vtools

a= u"见2送1那1日1来2将1怨1被1了1名1是1与1向1这2引1孙19知1须1定1望1"
b= u"一1骂1者1弄1备1领1按1劈1不1乃1掏1与1笑6拿1应1会1十1喜1各1造1谢1急2大1撩1在1名1将3听1就2到1亲1头1伸1钻1挺1手1却1见4心2过1又6筋1才2迎1近2道61何1捻1也2跳2满1金1正1执1叩2去2独1即1已2说1闻7出1顿1演1"

def ab(ss):
    match = re.findall(r"([^0-9]+)([0-9]+)", ss)
    return {a:int(b) for (a,b) in match}


print vtools.Entropy(ab(a))
print vtools.Entropy(ab(b))
from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCJ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["40.2100","40.2200","40.2300","40.2900x002","40.2901","40.2910","40.3x00x001","40.3x00x002","40.3x00x003","40.3x00x005","40.4100","40.4200","40.5100","40.5101","40.5901","40.5914","85.1200x001","85.2000x001","85.3300x001","85.3500x001","85.4301","85.4401","85.4500x001","85.4500x003","85.4600","85.4700","85.4800"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合JA1入组条件，匹配规则：主手术匹配')
    
    if MDCJ_DRG.JA19_group(record):
      return 'JA19'

    return ''
  else:
    return ''


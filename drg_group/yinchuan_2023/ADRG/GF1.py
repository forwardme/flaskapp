from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCG_DRG

def group(record):
  adrg_zd=["C21.101","D12.900x001","D12.901","K60.000","K60.100","K60.200","K60.300","K60.301","K60.302","K60.303","K61.000","K61.001","K61.100","K61.101","K61.200","K62.001","K62.300","K62.301","K62.400x004","K62.401","K62.601","K62.800x017","K62.801","K62.816","K62.901","K64.801","K64.802","K64.803","K64.805","K64.806","K64.807","K64.809","K64.810","K64.811","K64.900","K64.901","K65.008","K66.812","Q42.200x901","Q42.200x902","Q42.200x903","Q42.200x905","Q42.302","T18.501"]
  adrg_zd1=[]
  adrg_ss=["49.0100x004","49.0101","49.0200x001","49.0201","49.0300","49.0400x008","49.0400x009","49.0401","49.0402","49.1100","49.1200","49.3900x015","49.3900x016","49.3901","49.3902","49.3903","49.3905","49.3906","49.3907","49.4200","49.4500","49.4500x004","49.4600","49.4601","49.4701","49.4900x002","49.4900x003","49.4901","49.4903","49.5200x002","49.5900x001","49.5901","49.5902","49.5903","49.6x01","49.7301","49.7302","49.7903","49.7904","49.9300x003","49.9300x005","49.9301","49.9302","49.9500x002","98.0501"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GF1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCG_DRG.GF19_group(record):
      return 'GF19'

    return 'GF1'
  else:
    return ''


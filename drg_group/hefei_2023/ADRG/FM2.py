from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCF_DRG
from drg_group.hefei_2023.DRG_EX import FM2X,FM2Z

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.0200x001","00.6600x004","00.6601","17.5500x002","17.5500x003","17.5500x004","17.5501","36.0400","36.3400","36.9900x011","36.9900x012","37.2800","37.3400x001","37.3400x002","37.3500x004","37.4900x008","37.4900x017","37.4900x018","37.6101","37.7800","37.9000x001","37.9200x001","37.9900x002","37.9900x003","39.4900x012"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FM2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if FM2X.group(record):
      return 'FM2X'

    if FM2Z.group(record):
      return 'FM2Z'

    
    if MDCF_DRG.FM29_group(record):
      return 'FM29'

    return ''
  else:
    return ''


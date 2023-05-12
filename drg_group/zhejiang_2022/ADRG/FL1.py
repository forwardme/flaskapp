from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["37.3401","37.3402","37.3403","37.3404","37.3405","37.3406","37.9200x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FL1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FL19_group(record):
      return 'FL19'

    return ''
  else:
    return ''


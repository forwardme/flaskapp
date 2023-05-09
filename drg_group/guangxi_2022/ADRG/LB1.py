from drg_group.guangxi_2022.Base import message,intersect,SS_VALID
from drg_group.guangxi_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["55.0102","55.0111","55.0300x002","55.0300x003","55.0300x007","55.0301","55.0302","55.0400x005","55.0400x006","55.0400x007","55.0400x008","55.0400x009","55.0400x010","55.0401","55.0402","55.0403","55.0404","55.0405","55.1101","55.1102","55.1103","55.1104","55.1105","55.1109"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合LB1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCL_DRG.LB11_group(record):
      return 'LB11'

    if MDCL_DRG.LB13_group(record):
      return 'LB13'

    if MDCL_DRG.LB15_group(record):
      return 'LB15'

    return 'LB1'
  else:
    return ''


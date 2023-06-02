from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCL_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.9500x004","39.9500x005","39.9500x006","39.9500x007","39.9501","39.9600x002","39.9600x003","54.9800","54.9800x005","54.9800x006","54.9800x007","54.9800x008","39.9500"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合LL1入组条件，匹配规则：主手术匹配')
    
    
    if MDCL_DRG.LL10_group(record):
      return 'LL10'

    if MDCL_DRG.LL11_group(record):
      return 'LL11'

    if MDCL_DRG.LL12_group(record):
      return 'LL12'

    if MDCL_DRG.LL13_group(record):
      return 'LL13'

    if MDCL_DRG.LL14_group(record):
      return 'LL14'

    if MDCL_DRG.LL15_group(record):
      return 'LL15'

    return ''
  else:
    return ''


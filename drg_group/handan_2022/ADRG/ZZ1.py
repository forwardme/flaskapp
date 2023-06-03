from drg_group.handan_2022.Base import message,intersect,SS_VALID
from drg_group.handan_2022.DRG import MDCZ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and not intersect(record.ssList,SS_VALID):
    message('符合ZZ1入组条件，匹配规则：无手术')
    
    if MDCZ_DRG.ZZ11_group(record):
      return 'ZZ11'

    if MDCZ_DRG.ZZ15_group(record):
      return 'ZZ15'

    return ''
  else:
    return ''


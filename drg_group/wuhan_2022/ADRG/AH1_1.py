from drg_group.wuhan_2022.Base import message,intersect,SS_VALID
from drg_group.wuhan_2022.DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["31.1x00x005","31.2100x001","31.2900x001","31.7400","31.7400x001","96.5500"]
  adrg_ss1=["96.7201"]
  dept_list=[]
  
  if True and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合AH1_1入组条件，匹配规则：双手术匹配')
    
    if MDCA_DRG.AH11_group(record):
      return 'AH11'

    if MDCA_DRG.AH1B_group(record):
      return 'AH1B'

    return 'AH1'
  else:
    return ''


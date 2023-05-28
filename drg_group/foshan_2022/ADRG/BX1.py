from drg_group.foshan_2022.Base import message,intersect,SS_VALID
from drg_group.foshan_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["A52.104+F02.8*","E01.802+F02.8*","E03.803+F02.8*","E53.805+F02.8*","E75.602+F02.8*","E83.003+F02.8*","E83.505+F02.8*","F01.000","F01.100","F01.102","F01.200","F01.300","F01.800x001","F01.900","F01.901","F01.902","F03.x00","F03.x01","G30.000","G30.000x002","G30.000x003+F00.0*","G30.000x004+F00.0*","G30.100","G30.100x002+F00.1*","G30.100x003+F00.1*","G30.800","G30.800x001","G30.800x003+F00.2*","G30.801+F00.2*","G30.802+F00.2*","G30.900","G30.901+F00.9*","G31.000x005+F02.8*","G31.000x006+F02.8*","G31.001","G31.002+F02.0*","G31.100x007","G31.801","G31.805+F02.8*","G31.900x008","G31.900x009","M30.005+F02.8*","M32.116+F02.8*","N18.502+F02.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BX1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCB_DRG.BX11_group(record):
      return 'BX11'

    if MDCB_DRG.BX13_group(record):
      return 'BX13'

    if MDCB_DRG.BX15_group(record):
      return 'BX15'

    if MDCB_DRG.BX18_group(record):
      return 'BX18'

    return ''
  else:
    return ''


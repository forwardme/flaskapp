from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["D48.900x011+G63.1*","E10.401+G63.2*","E11.400","E11.400x021+G63.2*","E11.400x024+G63.2*","E11.400x026+G63.2*","E11.400x110+G59.0*","E11.400x121+G73.0*","E11.400x130+G59.0*","E11.400x140+G59.0*","E11.400x150+G59.0*","E11.400x170+G59.0*","E11.400x180+G59.0*","E11.400x310+G99.0*","E11.400x901+G99.0*","E11.401+G63.2*","E11.402+G99.0*","E11.403+G63.2*","E11.404+G99.0*","E13.400x223+G63.2*","E14.400","E14.400x023+G63.2*","E53.803+G63.4*","E63.902+G63.4*","G50.000","G50.003","G50.802","G50.900","G51.000","G51.002","G51.003","G51.301","G51.400","G51.803","G51.900","G52.101","G52.800x004","G52.800x006","G54.000","G54.000x001","G54.002","G54.100x002","G54.400x001","G54.800x004","G54.801","G54.901","G56.000","G56.100","G56.100x001","G56.100x002","G56.100x003","G56.200","G56.202","G56.203","G56.300","G57.000x003","G57.001","G57.200","G57.300x005","G57.500","G57.500x001","G57.601","G57.603","G57.900","G58.000","G58.001","G58.002","G58.801","G58.900","G58.900x002","G58.900x003","G60.000","G60.003","G60.802","G60.900x001","G61.000","G61.000x004","G61.001","G61.002","G61.801","G61.900","G62.101","G62.804","G62.805","G62.807","G62.900","G62.900x002","G62.900x011","G62.901","G62.909","G64.x00","G83.400","G90.600","G90.900","G90.900x001","G90.900x002","H49.000","H49.200","M32.106+G63.5*","M33.102+G63.5*","M35.000","M53.100","M79.207","M89.003","S04.400","S04.500","S04.803","S04.804","S14.300","S14.400","S24.300x001","S44.000x001","S44.200x001","S54.000x001","S54.001","S54.100x001","S54.101","S64.100x001","S64.100x002","S64.200x001","S64.200x002","S64.300","S64.400x001","S64.700x001","S64.800","S64.900x001","S84.100x001","S84.800x001","S84.800x002","S94.800x001","S94.900x001","T06.101","T11.300","T14.400"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BX2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BX29_group(record):
      return 'BX29'

    return 'BX2'
  else:
    return ''


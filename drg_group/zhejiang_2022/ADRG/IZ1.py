from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=["M96.600x001","M96.600x002","M96.601","M96.602","T84.000","T84.000x004","T84.000x005","T84.000x006","T84.000x007","T84.000x008","T84.000x012","T84.000x013","T84.001","T84.002","T84.003","T84.004","T84.005","T84.006","T84.100","T84.200x003","T84.201","T84.202","T84.203","T84.300","T84.300x001","T84.300x002","T84.301","T84.401","T84.402","T84.500","T84.500x002","T84.501","T84.502","T84.503","T84.504","T84.600","T84.600x003","T84.601","T84.602","T84.603","T84.604","T84.605","T84.800","T84.800x003","T84.800x005","T84.800x007","T84.800x009","T84.800x010","T84.801","T84.802","T84.803","T84.804","T84.805","T84.806","T84.807","T85.713","T85.807","T87.000","T87.001","T87.100","T87.101","Z42.000x011","Z42.001","Z44.000x001","Z44.000x002","Z44.100x001","Z44.100x002","Z44.200x002","Z44.800","Z44.800x001","Z44.800x002","Z44.900","Z45.800x002","Z45.800x011","Z47.000x002","Z47.001","Z47.801","Z47.802","Z47.803"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合IZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IZ11_group(record):
      return 'IZ11'

    if MDCI_DRG.IZ13_group(record):
      return 'IZ13'

    if MDCI_DRG.IZ15_group(record):
      return 'IZ15'

    return ''
  else:
    return ''


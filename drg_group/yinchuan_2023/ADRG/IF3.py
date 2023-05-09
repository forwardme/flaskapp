from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCI_DRG

def group(record):
  adrg_zd=["C40.201","C40.202","C79.500x010","D16.201","D48.020","D48.021","D48.903+M90.7*","M16.900","M17.000","M24.800x052","M48.005","M72.600","M80.200","M80.800","M80.900","M84.000x051","M84.100x051","M85.000x051","M85.600x051","M86.000","M86.608","M86.808","M86.910","M87.002","M87.800x051","M89.800x501","M89.800x906","M89.818","M89.906","M89.925","M96.600x001","M96.600x002","M96.601","Q65.801","Q74.102","S42.200x041","S72.000","S72.000x031","S72.000x041","S72.000x051","S72.000x081","S72.100x001","S72.101","S72.110","S72.200x001","S72.300","S72.310","S72.400x001","S72.400x012","S72.400x013","S72.400x031","S72.400x041","S72.401","S72.410","S72.900","S72.910","S82.100x087","T84.201"]
  adrg_zd1=[]
  adrg_ss=["77.0500","77.1500x001","77.1500x002","77.1500x003","77.1500x006","77.1501","77.1502","77.2500x001","77.2500x003","77.2500x007","77.2500x008","77.2500x009","77.6501","77.8500","78.0500x001","78.0500x002","78.0501","78.1501","78.4501","78.5500x003","78.5500x005","78.5500x006","78.5500x007","78.5500x008","78.5501","78.9500","79.0500x002","79.1500x006","79.1500x007","79.1500x008","79.2501","79.3500x016","79.3500x017","79.3500x018","79.3500x019","79.3500x020","79.3501","79.6500","84.1701"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合IF3入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCI_DRG.IF31_group(record):
      return 'IF31'

    if MDCI_DRG.IF33_group(record):
      return 'IF33'

    if MDCI_DRG.IF35_group(record):
      return 'IF35'

    return 'IF3'
  else:
    return ''


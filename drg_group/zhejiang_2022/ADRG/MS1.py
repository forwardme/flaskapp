from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCM_DRG

def group(record):
  adrg_zd=["A06.800x003","A06.800x004+N51.2*","A18.100x018+N51.8*","A18.100x019+N77.1*","A18.100x020+N51.8*","A18.100x021+N37.8*","A18.100x031","A18.102","A18.109+N51.0*","A18.110+N51.8*","A18.116+N51.8*","A18.119+N51.8*","A51.000","A51.000x002","A51.001","A51.002","A54.202+N51.0*","A54.203+N51.1*","A54.204+N51.1*","A56.102+N51.1*","A56.103+N51.1*","A57.x00x002","A57.x00x003","A59.000x003+N51.0*","A60.000x003+N77.1*","A60.000x004+N51.8*","A60.001","A60.003+N51.8*","A60.900","A63.002","B26.000+N51.1*","B37.300x002+N77.1*","B37.402+N51.2*","B45.800x002","N41.000","N41.100","N41.101","N41.200","N41.800","N41.900x001","N41.900x002","N43.100","N43.101","N45.001","N45.002","N45.903","N45.904","N45.906","N45.907","N45.908","N48.100","N48.102","N48.201","N48.202","N48.203","N48.204","N49.001","N49.002","N49.101","N49.102","N49.103","N49.104","N49.201","N49.202","N49.203","N49.204","N49.205","N49.800","N76.200","N76.201","N76.300x001","N76.301","N76.400","N76.401","N76.801","T83.600","T83.601"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合MS1入组条件，匹配规则：主诊断匹配')
    
    if MDCM_DRG.MS11_group(record):
      return 'MS11'

    if MDCM_DRG.MS13_group(record):
      return 'MS13'

    if MDCM_DRG.MS15_group(record):
      return 'MS15'

    return ''
  else:
    return ''


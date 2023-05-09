from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCB_DRG

def group(record):
  adrg_zd=["A81.000","A81.000x002","A81.000x004","A81.000x006","A81.000x007","A81.001+F02.1*","A81.200x001","B57.401+F02.8*","E71.301","E75.000x001","E75.000x002","E75.000x003","E75.000x004","E75.100x001","E75.100x002","E75.100x004","E75.101","E75.200x006","E75.200x007","E75.200x009","E75.200x010","E75.200x011","E75.200x012","E75.200x013","E75.201","E75.202","E75.203","E75.204","E75.205","E75.206","E75.300","E75.400","E75.400x002","E75.400x003","E75.400x004","E75.400x005","E83.001","G10.x00","G10.x01+F02.2*","G11.000","G11.000x002","G11.000x003","G11.000x004","G11.000x005","G11.000x006","G11.000x007","G11.000x008","G11.100","G11.100x002","G11.100x003","G11.100x004","G11.100x005","G11.100x006","G11.101","G11.102","G11.200","G11.200x002","G11.200x004","G11.201","G11.300","G11.300x001","G11.300x002","G11.301","G11.400","G11.400x001","G11.800","G11.801","G11.900","G11.900x001","G11.900x005","G11.900x006","G11.901","G11.902","G12.000","G12.100","G12.100x001","G12.100x003","G12.100x004","G12.100x008","G12.101","G12.102","G12.103","G12.104","G12.200","G12.200x002","G12.200x005","G12.200x007","G12.200x008","G12.200x009","G12.200x010","G12.200x011","G12.200x012","G12.200x013","G12.200x015","G12.200x016","G12.201","G12.202","G12.203","G12.204","G12.205","G12.206","G12.207","G12.208","G12.209","G12.800","G12.800x001","G12.803","G12.900","G14.x00","G20.x00","G20.x00x006","G20.x01","G20.x02+F02.3*","G20.x03","G20.x04","G20.x05","G20.x06","G20.x07","G20.x08","G21.000","G21.001","G21.100","G21.101","G21.102","G21.200","G21.201","G21.300","G21.400","G21.401","G21.800","G21.800x002","G21.801","G21.900","G23.000","G23.000x002","G23.000x003","G23.100","G23.101","G23.200","G23.300","G23.800","G23.800x005","G23.800x006","G23.800x007","G23.801","G23.802","G23.803","G23.804","G23.900","G24.000","G24.100","G24.101","G24.102","G24.103","G24.104","G24.105","G24.106","G24.200","G24.200x001","G24.200x003","G24.201","G24.202","G24.300x002","G24.300x003","G24.300x004","G24.400","G24.400x002","G24.400x003","G24.400x004","G24.500","G24.500x002","G24.501","G24.800","G24.800x008","G24.801","G24.804","G24.805","G24.806","G24.807","G24.808","G24.900","G24.900x003","G24.901","G24.902","G25.000","G25.000x002","G25.000x003","G25.000x004","G25.000x005","G25.000x006","G25.000x007","G25.000x008","G25.000x009","G25.100","G25.200","G25.200x002","G25.200x003","G25.200x004","G25.200x005","G25.200x006","G25.200x007","G25.200x008","G25.200x009","G25.201","G25.202","G25.300","G25.300x002","G25.300x003","G25.300x004","G25.400","G25.500","G25.500x003","G25.500x005","G25.501","G25.502","G25.600","G25.600x001","G25.601","G25.800x001","G25.800x004","G25.800x005","G25.802","G25.900","G25.901","G25.902","G25.903","G31.000","G31.000x003","G31.100","G31.101","G31.200","G31.200x001","G31.200x005","G31.201","G31.202","G31.203","G31.800","G31.800x004","G31.800x008","G31.802","G31.803","G31.804","G31.806","G31.807","G31.900","G31.900x003","G31.900x004","G31.900x006","G31.903","G31.904","Q85.000","Q85.100","R27.000"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BU2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BU23_group(record):
      return 'BU23'

    if MDCB_DRG.BU25_group(record):
      return 'BU25'

    return 'BU2'
  else:
    return ''


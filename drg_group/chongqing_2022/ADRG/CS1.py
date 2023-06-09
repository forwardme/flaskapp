from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCC_DRG

def group(record):
  adrg_zd=["H02.400","H34.000","H34.100","H34.200","H34.200x002","H34.200x004","H34.200x005","H34.201","H34.202","H34.203","H34.204","H34.800","H34.800x001","H34.801","H34.802","H34.803","H34.804","H34.900","H34.900x001","H35.000","H35.000x014","H35.000x017","H35.000x019","H35.000x020","H35.000x021","H35.001","H35.002","H35.007","H35.008","H35.009","H35.011","H35.012","H35.012","H35.013","H35.014","H46.x00","H46.x01","H46.x02","H47.000","H47.000x009","H47.001","H47.002","H47.003","H47.004","H47.006","H47.200","H47.200x003","H47.200x004","H47.300x005","H47.301","H47.302","H47.303","H47.304","H47.500","H47.500x002","H47.500x003","H47.500x004","H47.600x001","H49.000","H49.001","H49.100","H49.200","H49.201","H49.300","H49.400","H49.400x001","H49.800","H49.800x002","H49.800x007","H49.801","H49.803","H49.804","H49.805","H49.806","H49.807","H49.808","H49.809","H49.810","H49.900","H49.901","H50.000","H50.000x002","H50.000x004","H50.000x009","H50.001","H50.002","H50.003","H50.004","H50.005","H50.006","H50.007","H50.008","H50.100","H50.100x002","H50.100x004","H50.100x007","H50.101","H50.102","H50.103","H50.104","H50.105","H50.106","H50.107","H50.200","H50.200x004","H50.200x006","H50.201","H50.202","H50.300","H50.300x002","H50.300x004","H50.301","H50.302","H50.400","H50.401","H50.402","H50.403","H50.404","H50.405","H50.500","H50.500x002","H50.500x003","H50.500x004","H50.600","H50.600x003","H50.600x004","H50.600x005","H50.601","H50.602","H50.603","H50.800x002","H50.800x003","H50.800x006","H50.800x007","H50.800x010","H50.801","H50.802","H50.803","H50.804","H50.805","H50.806","H50.807","H50.900","H51.000","H51.000x001","H51.100","H51.200","H51.800","H51.801","H51.900","H52.500","H52.500x001","H52.500x003","H52.500x004","H52.501","H53.200","H53.400","H53.400x003","H53.400x004","H53.400x005","H53.400x006","H53.400x007","H53.402","H55.x00","H55.x00x001","H55.x00x002","H55.x00x005","H55.x01","H57.000","H57.000x003","H57.001","H57.002","H57.003","I70.800x007","I70.801","I77.004","I80.801","I86.803","Q14.000x006","Q14.100x003","Q14.200x001","Q14.200x002","Q14.200x004","Q82.800x017","Q85.804","Q87.800x910","S04.000x001","S04.100"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合CS1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCC_DRG.CS19_group(record):
      return 'CS19'

    return ''
  else:
    return ''

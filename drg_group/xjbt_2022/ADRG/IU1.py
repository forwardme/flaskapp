from drg_group.xjbt_2022.Base import message,intersect,SS_VALID
from drg_group.xjbt_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=["D48.900x005+M90.6*","D86.800x006+M14.8*","E03.900x005+M14.5*","E05.900x005+M14.5*","E10.600x011+M14.6*","E10.600x012+M14.2*","E10.600x015+M14.2*","E10.601+M14.2*","E10.602+M14.6*","E11.600x011+M14.6*","E11.600x012+M14.2*","E11.600x015+M14.2*","E11.601+M14.2*","E11.602+M14.6*","E14.600x011+M14.6*","E14.600x012+M14.2*","E14.600x015+M14.2*","E14.600x016+M14.2*","E21.300x003+M14.1*","E22.000x006+M14.5*","E83.100x006+M14.5*","E83.300x008+M90.8*","E83.300x012+M90.8*","E83.307+M90.8*","E83.308+M90.8*","E88.902+M90.8*","L40.502+M09.0*","M02.000","M02.100","M02.200","M02.201","M02.900","M05.900","M06.000","M06.001","M06.400","M06.800","M06.800x051","M06.800x071","M06.900","M06.906","M06.909","M08.000","M08.001","M08.200","M08.201","M08.800x091","M10.000","M10.000x094","M10.002","M10.003","M10.100","M10.200","M10.300","M10.900","M10.900x093","M10.901","M10.902+H62.8*","M10.903","M11.000","M11.100","M11.201","M11.900","M12.000","M12.100","M12.200","M12.200x011","M12.200x021","M12.200x031","M12.200x051","M12.200x061","M12.200x071","M12.400","M12.500","M12.500x011","M12.500x021","M12.500x031","M12.500x051","M12.500x061","M12.500x071","M12.801","M13.000","M13.100","M13.100x011","M13.800x001","M13.802","M13.900","M15.000","M15.100","M15.200","M15.300","M15.301","M15.400","M15.401","M15.900","M15.900x003","M15.901","M15.902","M16.000","M16.101","M16.200","M16.301","M16.400","M16.501","M16.600","M16.701","M16.900","M16.900x002","M16.900x011","M16.900x012","M16.901","M17.000","M17.101","M17.200","M17.301","M17.400","M17.500x002","M17.501","M17.900","M17.900x002","M17.900x003","M17.900x004","M18.000","M18.101","M18.200","M18.301","M18.400x001","M18.501","M18.900","M18.900x002","M19.001","M19.101","M19.201","M19.800","M19.900","M19.900x092","M19.900x093","M19.900x094","M19.900x095","M19.900x096","M19.900x097","M19.901","M19.902","M19.903","M19.904","M19.905","M19.906","M19.907","M19.908","M19.909","M19.910","M23.400","M24.000","M24.001","M24.002","M24.003","M24.004","M24.005","M24.006","M24.500","M24.500x001","M24.501","M24.502","M24.503","M24.600","M24.601","M24.602","M24.603","M24.604","M24.605","M24.606","M24.607","M24.608","M24.609","M24.610","M24.700","M24.800x052","M24.811","M24.900","M24.900x052","M24.908","M25.000","M25.001","M25.002","M25.003","M25.004","M25.005","M25.006","M25.007","M25.100","M25.100x011","M25.100x021","M25.100x031","M25.100x051","M25.100x061","M25.100x071","M25.200","M25.201","M25.301","M25.400","M25.401","M25.402","M25.403","M25.404","M25.405","M25.406","M25.407","M25.408","M25.409","M25.410","M25.411","M25.412","M25.413","M25.414","M25.415","M25.416","M25.500","M25.501","M25.502","M25.503","M25.504","M25.505","M25.506","M25.507","M25.600x091","M25.601","M25.602","M25.603","M25.604","M25.605","M25.606","M25.607","M25.608","M25.700","M25.800x092","M25.801","M25.802","M25.803","M25.804","M25.805","M25.807","M25.808","M25.809","M25.810","M25.900x031","M25.900x061","M25.901","M42.000x091","M42.002","M42.100","M47.900","M47.900x091","M81.000","M81.100","M81.200","M81.300","M81.400","M81.500","M81.600","M81.800x091","M81.801","M81.900","M81.900x101","M81.903","M81.904","M83.000","M83.100","M83.200","M83.200x092","M83.300","M83.400","M83.900","M83.900x091","M85.000x011","M85.000x031","M85.000x051","M85.000x052","M85.000x053","M85.000x054","M85.000x061","M85.000x062","M85.000x071","M85.000x082","M85.000x084","M85.001","M85.002","M85.003","M85.100","M85.200","M85.201","M85.300","M85.400","M85.500","M85.600x021","M85.600x031","M85.600x032","M85.600x041","M85.600x042","M85.600x043","M85.600x051","M85.600x052","M85.600x053","M85.600x061","M85.600x062","M85.600x071","M85.600x072","M85.600x081","M85.600x092","M85.600x093","M85.602","M85.603","M88.000","M88.800","M88.900","M89.002","M89.100","M89.101","M89.200x071","M89.300","M89.301","M89.302","M89.303","M89.304","M89.305","M89.306","M89.307","M89.308","M89.309","M89.310","M89.401","M89.402","M89.403","M89.404","M89.500","M89.500x091","M89.600","M89.800x501","M89.800x601","M89.800x906","M89.800x908","M89.802","M89.803","M89.804","M89.808","M89.810","M89.813","M89.816","M89.817","M89.818","M89.819","M89.820","M89.821","M89.823","M89.824","M89.825","M89.900x063","M89.900x072","M89.900x091","M89.901","M89.903","M89.906","M89.911","M89.912","M89.915","M89.917","M89.918","M89.919","M89.920","M89.926","M89.928","M91.000","M91.000x051","M91.001","M91.002","M91.003","M91.004","M91.100","M91.101","M91.102","M91.200","M91.201","M91.300","M91.800","M91.800x051","M91.900","M92.000x001","M92.001","M92.101","M92.102","M92.200","M92.201","M92.202","M92.400","M92.401","M92.402","M92.501","M92.502","M92.503","M92.504","M92.600","M92.600x002","M92.601","M92.602","M92.604","M92.605","M92.606","M92.700x003","M92.701","M92.702","M92.703","M92.801","M92.802","M92.803","M92.804","M92.900","M92.901","M92.902","M92.903","M93.000","M93.100","M93.200x001","M93.200x002","M93.200x003","M93.201","M93.202","M93.800x001","M93.800x002","M93.800x003","M93.901","M93.902","M93.903","M93.904","M93.905","M94.100","M94.200","M94.300","M94.300x051","M94.801","M94.802","M94.808","M94.900","M95.901","N25.002+M90.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IU1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IU13_group(record):
      return 'IU13'

    if MDCI_DRG.IU15_group(record):
      return 'IU15'

    return 'IU1'
  else:
    return ''


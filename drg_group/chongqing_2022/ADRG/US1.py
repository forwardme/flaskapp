from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCU_DRG

def group(record):
  adrg_zd=["F11.000","F11.000x001","F11.100","F11.100x001","F11.200","F11.200x001","F11.200x003","F11.201","F11.202","F11.203","F11.204","F11.300","F11.400","F11.500","F11.600","F11.700","F11.800","F11.900","F12.000","F12.000x002","F12.100","F12.100x001","F12.200","F12.300","F12.400","F12.500","F12.600","F12.700","F12.800","F12.900","F13.100","F13.800","F14.000","F14.100","F14.100x001","F14.200","F14.300","F14.400","F14.400x001","F14.500","F14.600","F14.700","F14.800","F14.900","F15.000","F15.000x002","F15.000x003","F15.000x004","F15.100","F15.100x001","F15.100x002","F15.100x003","F15.100x004","F15.200x001","F15.200x002","F15.200x003","F15.200x004","F15.300x001","F15.300x002","F15.300x003","F15.300x004","F15.400x001","F15.400x002","F15.400x003","F15.400x004","F15.500x001","F15.500x002","F15.500x003","F15.500x004","F15.501","F15.600x001","F15.600x002","F15.600x003","F15.600x004","F15.700x001","F15.700x002","F15.700x003","F15.700x004","F15.800","F15.900x001","F15.900x002","F15.900x003","F15.900x004","F16.000","F16.000x002","F16.100","F16.100x002","F16.200","F16.300","F16.400","F16.400x001","F16.500","F16.600","F16.700","F16.800","F16.900","F17.100","F17.200","F17.300","F17.400","F17.400x001","F17.800","F18.000","F18.100","F18.200","F18.300","F18.400","F18.800","F19.100","R78.100","R78.200","R78.300","R78.400","R78.500","R78.600","T40.000","T40.100","T40.200","T40.200x001","T40.201","T40.300","T40.400","T40.401","T40.500","T40.601","T40.700","T43.600","T43.600x003"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合US1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCU_DRG.US19_group(record):
      return 'US19'

    return ''
  else:
    return ''

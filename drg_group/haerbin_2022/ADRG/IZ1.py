from drg_group.haerbin_2022.Base import message,intersect,SS_VALID
from drg_group.haerbin_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=["B19.900x001+M03.2*","C46.100","C76.300x001","C76.300x009","C76.400","C76.401","C76.402","C76.500","C76.501","C76.502","C76.503","C76.701","C76.702","C79.800x813","C79.800x817","D36.700x016","D36.700x024","D36.700x029","D36.700x030","D36.700x032","D36.700x035","D36.700x036","D36.700x038","D36.712","D36.713","D36.714","D36.715","D36.718","D48.700x010","D48.700x013","D48.700x016","D48.717","D48.718","D48.719","D48.720","D48.721","D48.724","E55.000x002","E55.000x003","E55.000x004","E55.000x007","E55.001","E64.300","E85.000","E85.001","I00.x00x004","I00.x00x005","I00.x01","M05.200","M05.200x092","M05.303+G73.7*","M30.001+G73.7*","M30.002+G63.5*","M30.003+G63.5*","M31.702+G63.5*","M32.110+G73.7*","M34.800x002+G73.7*","M34.800x005+G53.8*","M34.804+G73.7*","M34.806+G63.5*","M35.004+G73.7*","M35.900x006+G63.5*","M35.903+G63.5*","M47.001+G99.2*","M47.002+G99.2*","M47.003+G99.2*","M47.101+G99.2*","M47.102+G99.2*","M47.103+G99.2*","M47.104+G99.2*","M50.000+G99.2*","M50.001+G99.2*","M50.100","M50.101+G55.1*","M51.100x002+G55.1*","M51.101+G55.1*","M51.102+G55.1*","M51.103+G55.1*","M51.104+G55.1*","M51.105+G55.1*","M51.106+G55.1*","M70.400","M96.600x001","M96.600x002","M96.601","M96.602","S22.200","S22.210","S22.300","S22.300x011","S22.310","S22.400","S22.400x011","S22.400x021","S22.400x031","S22.400x041","S22.410","S22.500","S22.900","S23.200x001","S23.200x004","S23.200x005","S23.201","S23.202","S23.203","S23.300","S43.200","T81.800x012","T84.000","T84.000x004","T84.000x005","T84.000x006","T84.000x007","T84.000x008","T84.000x012","T84.000x013","T84.001","T84.002","T84.003","T84.004","T84.005","T84.006","T84.100","T84.200x003","T84.201","T84.202","T84.203","T84.300","T84.300x001","T84.300x002","T84.301","T84.401","T84.402","T84.500","T84.500x002","T84.501","T84.502","T84.503","T84.504","T84.600","T84.600x003","T84.601","T84.602","T84.603","T84.604","T84.605","T84.800","T84.800x003","T84.800x005","T84.800x007","T84.800x009","T84.800x010","T84.801","T84.802","T84.803","T84.804","T84.805","T84.806","T84.807","T85.713","T87.000","T87.001","T87.100","T87.101","Z44.000x001","Z44.000x002","Z44.100x001","Z44.100x002","Z44.800","Z44.800x001","Z44.800x002","Z44.900","Z45.800x002","Z45.800x011","Z47.000x002","Z47.001","Z47.801","Z47.802","Z47.803"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合IZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IZ1A_group(record):
      return 'IZ1A'

    if MDCI_DRG.IZ15_group(record):
      return 'IZ15'

    return ''
  else:
    return ''


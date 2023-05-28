from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCX_DRG

def group(record):
  adrg_zd=["B90.001","B90.002","B94.100","B94.101","B94.800x003","I69.400","I69.800x002","I69.801","I69.802","K07.601","M23.201","M23.202","M23.203","M23.204","M23.208","M23.209","M23.211","M23.212","M23.214","M23.215","M23.501","M24.100x091","M24.102","M24.803","M24.805","M24.806","M24.807","M24.808","M24.810","N81.800x006","Q89.700","Q89.900","R25.200x002","R25.200x004","R25.200x005","R25.200x006","R25.200x007","R25.200x008","R25.200x009","R26.100","R26.100x001","T90.000","T90.100","T90.102","T90.200","T90.200x008","T90.200x012","T90.201","T90.202","T90.203","T90.204","T90.205","T90.206","T90.207","T90.208","T90.400x001","T90.400x002","T90.400x003","T90.400x004","T90.401","T90.500x002","T90.500x003","T90.800x002","T90.900","T90.901","T91.000x001","T91.000x002","T91.000x003","T91.000x004","T91.001","T91.002","T91.200","T91.200x002","T91.200x005","T91.201","T91.202","T91.204","T91.205","T91.206","T91.400","T91.401","T91.500x001","T91.500x003","T91.501","T91.502","T91.800x001","T91.800x002","T91.800x003","T91.800x004","T91.800x005","T91.800x006","T91.800x007","T91.800x008","T91.800x009","T91.800x010","T91.802","T91.803","T91.900","T91.900x002","T91.900x003","T92.000","T92.001","T92.100","T92.100x004","T92.100x005","T92.100x008","T92.100x009","T92.100x010","T92.100x011","T92.101","T92.102","T92.103","T92.104","T92.105","T92.106","T92.200","T92.201","T92.202","T92.203","T92.204","T92.300","T92.300x001","T92.300x002","T92.300x005","T92.300x006","T92.300x007","T92.300x008","T92.300x011","T92.300x012","T92.300x013","T92.300x015","T92.300x016","T92.300x017","T92.301","T92.302","T92.303","T92.304","T92.305","T92.306","T92.307","T92.400","T92.400x002","T92.400x003","T92.400x004","T92.400x005","T92.400x006","T92.400x007","T92.400x008","T92.401","T92.402","T92.500x001","T92.500x002","T92.500x003","T92.500x004","T92.500x006","T92.500x007","T92.500x008","T92.500x009","T92.500x010","T92.500x011","T92.500x012","T92.500x013","T92.500x014","T92.500x015","T92.500x016","T92.500x017","T92.500x018","T92.501","T92.502","T92.503","T92.504","T92.505","T92.506","T92.600","T92.600x002","T92.600x003","T92.601","T92.602","T92.603","T92.800x001","T92.800x002","T92.801","T92.900","T93.000","T93.001","T93.100","T93.101","T93.102","T93.103","T93.104","T93.200","T93.200x001","T93.200x002","T93.200x007","T93.200x008","T93.200x010","T93.200x011","T93.200x012","T93.200x013","T93.200x014","T93.201","T93.202","T93.203","T93.204","T93.205","T93.206","T93.207","T93.208","T93.300x001","T93.300x002","T93.300x003","T93.300x005","T93.300x008","T93.300x009","T93.301","T93.400","T93.400x002","T93.400x003","T93.400x004","T93.400x005","T93.400x006","T93.500x001","T93.500x002","T93.501","T93.600","T93.600x001","T93.600x002","T93.600x003","T93.800","T93.800x001","T93.800x002","T93.800x003","T93.801","T93.900","T94.000","T94.001","T94.002","T94.100","T94.102","T97.x00x003","T97.x02","T98.300x007","T98.301","Z11.100","Z12.200","Z13.800x021","Z13.800x022","Z22.302","Z24.100","Z50.101","Z50.501","Z50.801","Z54.800x004","Z54.800x005","Z54.800x009"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合XR2入组条件，匹配规则：主诊断匹配')
    
    
    if MDCX_DRG.XR21_group(record):
      return 'XR21'

    if MDCX_DRG.XR23_group(record):
      return 'XR23'

    if MDCX_DRG.XR25_group(record):
      return 'XR25'

    return ''
  else:
    return ''


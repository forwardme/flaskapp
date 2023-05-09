from drg_group.guangxi_2022.Base import message,intersect,SS_VALID
from drg_group.guangxi_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=["A19.800","B33.400x001+J17.1*","C88.402","E32.000","E32.000x003","E32.001","E32.002","E32.100","E32.800x001","E32.800x004","E32.800x005","E32.801","E32.802","E32.900","E83.104+J99.8*","E85.400x005","E85.404","E85.407","E89.802","G47.300x034","I00.x00x007+J17.8*","I88.106","I88.107","I88.900x002","I88.900x008","I89.000x016","I89.000x027","I89.000x028","I89.000x029","I89.003","I89.800x018","I89.800x021","I89.800x023","I89.804","J39.801","J39.802","J39.804","J39.805","J39.806","J39.807","J39.808","J39.810","J43.000","J43.000x003","J43.001","J43.100","J43.101","J43.200","J43.800x001","J43.900","J43.900x001","J43.901","J43.903","J43.904","J66.800","J68.201","J68.301","J68.400","J68.800","J68.900","J70.800","J70.900","J95.401","J95.800x009","J95.800x010","J95.800x012","J95.800x021","J95.808","J95.810","J95.900","J98.000x009","J98.000x011","J98.000x012","J98.000x013","J98.001","J98.002","J98.003","J98.004","J98.005","J98.006","J98.007","J98.008","J98.009","J98.010","J98.011","J98.100","J98.101","J98.102","J98.200","J98.300","J98.400x001","J98.400x005","J98.400x012","J98.400x013","J98.400x016","J98.400x019","J98.401","J98.402","J98.403","J98.407","J98.408","J98.409","J98.410","J98.411","J98.412","J98.413","J98.415","J98.416","J98.417","J98.418","J98.500x001","J98.500x007","J98.500x008","J98.504","J98.505","J98.506","J98.507","J98.508","J98.600x001","J98.601","J98.602","J98.800x001","J98.800x003","J98.800x004","J98.800x006","J98.800x007","J98.800x009","J98.800x014","J98.800x016","J98.800x018","J98.801","J98.901","Q32.102","Q32.200","Q32.300","Q32.400x002","Q32.400x004","Q32.400x005","Q32.401","Q32.402","Q33.000","Q33.002","Q33.003","Q33.100","Q33.100","Q33.200","Q33.301","Q33.400","Q33.500","Q33.600","Q33.800x001","Q33.800x002","Q33.900","Q34.100","Q34.900","Q79.000","Q79.101","Q79.102","Q79.103","Q89.209","Q89.800x910","R59.009","R84.000","R84.100","R84.200","R84.300","R84.400","R84.500","R84.600","R84.700","R84.800","R84.903","R84.904","R91.x01","R91.x04","R94.201","R94.202","S24.200","S29.800","T17.400","T17.500","T17.801","T17.802","T17.803","T17.804","T17.900","T17.901","T27.200x001","T27.300","T27.500x001","T27.600x001","T27.600x001","T27.600x001","T27.700","T81.400x009","T84.200x004","T85.608","T85.700x804","T86.800x011","T86.803","U04.900","U07.000","U07.100x001","U07.100x002","U07.100x003","Z03.800x001"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合EZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.EZ11_group(record):
      return 'EZ11'

    if MDCE_DRG.EZ13_group(record):
      return 'EZ13'

    if MDCE_DRG.EZ15_group(record):
      return 'EZ15'

    return 'EZ1'
  else:
    return ''


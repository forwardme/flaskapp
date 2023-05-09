from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCN_DRG

def group(record):
  adrg_zd=["D07.100","D25.000","D25.900","N81.100","N81.101","N81.200","N81.201","N81.202","N81.203","N81.300","N81.301","N81.400","N81.601","N81.801","N81.802","N81.803","N82.000","N82.303","N83.201","N84.001","N85.804","N88.400","N90.403","N90.601","N90.808","N93.901","N99.800x010","Q52.000","Q52.700x003"]
  adrg_zd1=[]
  adrg_ss=["57.8402","69.2200x006","69.2200x007","69.2200x009","69.2200x012","69.2200x013","69.2200x016","69.2200x019","69.2200x021","69.2200x024","69.2200x025","69.2202","69.2205","69.2206","69.2207","69.2208","69.2210","69.2211","69.2212","69.4900x005","69.4900x006","69.4903","70.5001","70.5002","70.5101","70.5102","70.5201","70.5202","70.5300x001","70.5300x002","70.5304","70.5305","70.5400x001","70.5400x002","70.5500x001","70.5500x002","70.6200x002","70.7300","70.7700x004","70.7701","70.7702","71.6200x002","71.7202","71.7900x001","71.7900x008","71.7900x010","71.7900x011","71.7901","71.7903","71.7904"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合NB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCN_DRG.NB19_group(record):
      return 'NB19'

    return 'NB1'
  else:
    return ''


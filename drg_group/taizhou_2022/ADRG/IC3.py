from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["77.2800x002","77.2802","77.2900x006","81.1100","81.1100x003","81.1101","81.1200x001","81.1300x003","81.1300x004","81.1500","81.1500x001","81.1600","81.1800","81.2101","81.2201","81.2300x002","81.2300x003","81.2300x004","81.2300x005","81.2301","81.2401","81.2901","81.2902","81.4000","81.4000x004","81.4000x005","81.4000x006","81.4200","81.4300","81.4501","81.4502","81.4503","81.4504","81.4505","81.4600x001","81.4601","81.4700x001","81.4700x005","81.4700x012","81.4700x013","81.4700x014","81.4700x015","81.4700x016","81.4700x017","81.4700x018","81.4700x019","81.4701","81.4900x001","81.4900x002","81.4900x003","81.4900x004","81.4900x005","81.4900x006","81.4901","81.4902","81.8200","81.8201","81.8300x001","81.8300x003","81.8300x004","81.8300x006","81.8300x007","81.8300x008","81.8300x009","81.8301","81.8302","81.8303","81.8304","81.8305","81.8500x001","81.8500x002","81.8500x004","81.8500x005","81.8500x006","81.8500x007","81.8500x008","81.9300x009","81.9300x010","81.9400x001","81.9400x006","81.9400x007","81.9401","81.9402","81.9403","81.9404","81.9500x001","81.9501","81.9502","81.9600x003","81.9600x009","81.9600x015","81.9600x017","81.9600x018","81.9600x019","81.9600x020","81.9600x021","81.9600x022","81.9600x023","81.9600x024","81.9600x025","81.9600x026","81.9600x027","81.9600x028","81.9600x029","81.9600x030","81.9600x031","81.9600x032"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IC3入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IC39_group(record):
      return 'IC39'

    return 'IC3'
  else:
    return ''


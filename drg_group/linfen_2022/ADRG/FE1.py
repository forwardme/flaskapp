from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.0400x001","38.0400x002","38.0401","38.0502","38.0503","38.0504","38.0702","38.1400x001","38.1401","38.1402","38.1403","38.1500x001","38.1501","38.3401","38.3402","38.3403","38.3501","38.4400x001","38.4400x002","38.4401","38.4500x001","38.4500x003","38.4500x004","38.4500x007","38.4500x009","38.4500x010","38.4500x011","38.4500x013","38.4500x014","38.4500x015","38.4500x016","38.4500x018","38.4500x019","38.4501","38.4502","38.4503","38.4504","38.4505","38.4506","38.4507","38.4510","38.4511","38.4700x001","38.4702","38.6400x001","38.6401","38.6402","38.6500x003","38.6500x004","38.6700x005","38.6701","38.7x01","38.7x02","38.8401","38.8500x013","38.8501","38.8502","39.0x01","39.0x04","39.0x05","39.1x00x006","39.1x00x008","39.1x00x009","39.1x00x010","39.1x00x011","39.1x01","39.1x03","39.1x04","39.1x05","39.1x06","39.1x08","39.1x09","39.2200x001","39.2200x008","39.2200x009","39.2200x010","39.2200x012","39.2200x015","39.2200x016","39.2200x021","39.2201","39.2203","39.2204","39.2207","39.2212","39.2300x003","39.2300x005","39.2300x016","39.2300x017","39.2300x018","39.2300x019","39.2300x020","39.2300x021","39.2300x022","39.2300x024","39.2301","39.2302","39.2303","39.2304","39.2305","39.2306","39.2308","39.2309","39.2401","39.2500x001","39.2500x002","39.2500x003","39.2500x004","39.2500x007","39.2500x008","39.2502","39.2503","39.2505","39.2507","39.2509","39.2510","39.2600x001","39.2600x008","39.2606","39.3107","39.3203","39.3205","39.4900x010","39.5200x005","39.5200x006","39.5203","39.5400x001","39.5700x003","39.5900x002","39.5900x009","39.5900x016","39.5900x018","39.5900x030","39.5900x032","39.7900x517","39.9100x003","54.9402"]
  adrg_ss1=["00.5500x008","38.9300x202","39.4900x011","39.4901","39.4902","39.5000x015","39.5000x027","39.5003","39.5010","39.7100x004","39.7101","39.7102","39.7103","39.7300x003","39.7301","39.7302","39.7303","39.7701","39.7800x001","39.7800x002","39.7800x006","39.7800x010","39.7900x011","39.7900x030","39.7900x031","39.7900x517","39.9000x022","39.9000x027","39.9000x037","39.9000x038","39.9002"]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and intersect(record.ssList,adrg_ss) and record.ssList and intersect(record.ssList,adrg_ss) and intersect(record.ssList,adrg_ss1):
    message('符合FE1入组条件，匹配规则：某一手术匹配、双手术匹配')
    
    if MDCF_DRG.FE19_group(record):
      return 'FE19'

    return 'FE1'
  else:
    return ''


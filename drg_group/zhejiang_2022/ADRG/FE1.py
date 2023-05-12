from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.5500x008","35.3400x005","35.8306","38.0400x001","38.0400x002","38.0401","38.0500x002","38.0504","38.1400x001","38.1401","38.1402","38.1403","38.1500x001","38.1501","38.3400x003","38.3401","38.3402","38.3403","38.3501","38.4400x001","38.4400x002","38.4401","38.4500x004","38.4500x007","38.4500x009","38.4500x010","38.4500x011","38.4500x013","38.4500x014","38.4500x015","38.4500x016","38.4500x017","38.4500x018","38.4500x019","38.4501","38.4502","38.4503","38.4504","38.4505","38.4506","38.4507","38.4511","38.6400x001","38.6401","38.6402","38.6500x003","38.6500x004","38.8401","38.8500x001","38.8500x012","38.8500x013","38.8501","38.8502","39.0x01","39.0x02","39.0x04","39.0x05","39.2100x001","39.2100x003","39.2100x004","39.2100x005","39.2100x006","39.2100x007","39.2102","39.2200x001","39.2200x008","39.2200x009","39.2200x010","39.2200x012","39.2200x015","39.2200x016","39.2200x021","39.2201","39.2203","39.2204","39.2207","39.2212","39.2300x003","39.2300x005","39.2301","39.2302","39.2303","39.2401","39.2500x001","39.2500x002","39.2500x003","39.2500x004","39.2500x006","39.2500x007","39.2500x008","39.2500x009","39.2500x010","39.2500x011","39.2500x013","39.2500x014","39.2501","39.2502","39.2503","39.2505","39.2507","39.2508","39.2509","39.2510","39.2600x001","39.2600x006","39.2600x008","39.2606","39.3107","39.4900x010","39.5000x014","39.5000x015","39.5003","39.5010","39.5200x005","39.5200x006","39.5400x001","39.5700x003","39.5900x002","39.5900x012","39.5900x016","39.5900x018","39.5900x030","39.5900x031","39.5900x032","39.5900x033","39.7301","39.7303","39.7701","39.7900x010","39.9002","88.4201","88.4202","88.4203","88.4204","88.4205","88.4300x002","99.1000x006"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FE1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FE11_group(record):
      return 'FE11'

    if MDCF_DRG.FE13_group(record):
      return 'FE13'

    if MDCF_DRG.FE15_group(record):
      return 'FE15'

    return ''
  else:
    return ''


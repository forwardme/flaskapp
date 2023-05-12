from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.0102","00.0300","00.5500x009","00.5500x011","00.5500x012","00.5500x013","00.5500x014","00.5500x017","00.5501","00.5502","00.5800","00.6000","04.2x00x015","17.5600x001","38.0603","38.1604","38.2200","38.2300","38.2500","39.5000x024","39.5000x027","39.5000x029","39.5000x030","39.5000x031","39.5002","39.5004","39.5005","39.5008","39.5009","39.5011","39.5013","39.5015","39.5016","39.5300x014","39.5301","39.5900x026","39.5900x027","39.5900x028","39.5900x029","39.5900x034","39.7200x004","39.7200x005","39.7202","39.7203","39.7209","39.7400x002","39.7400x004","39.7604","39.7900x007","39.7900x008","39.7900x009","39.7900x011","39.7900x013","39.7900x014","39.7900x017","39.7900x019","39.7900x020","39.7900x021","39.7900x025","39.7900x027","39.7900x028","39.7900x030","39.7900x031","39.7900x032","39.7900x034","39.7900x036","39.7900x038","39.7900x040","39.7900x042","39.7900x044","39.7900x045","39.7900x047","39.7900x049","39.7901","39.7902","39.7903","39.7904","39.7905","39.7906","39.7907","39.7910","39.9000x010","39.9000x017","39.9000x019","39.9000x020","39.9000x021","39.9000x023","39.9000x024","39.9000x025","39.9000x028","39.9000x029","39.9000x030","39.9000x031","39.9000x034","39.9000x036","39.9001","39.9004","39.9007","39.9008","39.9009","39.9011","39.9012","39.9013","39.9015","39.9016","88.4400x001","88.4401","88.4402","88.4403","88.4404","88.4405","88.4500","88.4600","88.4701","88.4702","88.4703","88.4704","88.4705","88.4706","88.4707","88.4800x005","88.4801","88.4900x005","88.4901","88.4902","88.4903","88.4904","99.1000x007","99.1000x009","99.1001","99.1002","99.1004","99.1007","39.5000x032"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FN1入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FN11_group(record):
      return 'FN11'

    if MDCF_DRG.FN15_group(record):
      return 'FN15'

    return ''
  else:
    return ''


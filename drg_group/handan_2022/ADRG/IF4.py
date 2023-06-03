from drg_group.handan_2022.Base import message,intersect,SS_VALID
from drg_group.handan_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["77.0701","77.0702","77.0800x001","77.0800x002","77.0801","77.0802","77.0900x004","77.0903","77.1700x001","77.1700x002","77.1700x003","77.1701","77.1702","77.1703","77.1800x001","77.1801","77.1802","77.1803","77.1900x001","77.1903","77.2600","77.2800x001","77.2800x003","77.2800x004","77.2800x005","77.2801","77.2900x005","77.2903","77.3600","77.3701","77.3702","77.3801","77.3802","77.3907","77.5100","77.5301","77.5400x001","77.5600x002","77.5700x001","77.5800x007","77.5800x008","77.5801","77.5802","77.5900x002","77.6701","77.6702","77.6801","77.6802","77.6900x007","77.6900x020","77.6900x047","77.6903","77.7600","77.7701","77.7702","77.7800","77.7900x001","77.7900x006","77.8700x003","77.8700x004","77.8701","77.8702","77.8801","77.8802","77.8900x026","77.8900x027","77.8900x028","77.8904","77.9701","77.9702","77.9801","77.9802","77.9803","77.9804","77.9805","77.9903","78.0700x004","78.0700x005","78.0700x006","78.0701","78.0702","78.0800x001","78.0800x002","78.0801","78.0802","78.0900x001","78.0900x014","78.0900x021","78.0903","78.1701","78.1702","78.1801","78.1802","78.1903","78.2501","78.2701","78.2702","78.2800","78.2902","78.3701","78.3702","78.3800x001","78.3800x002","78.4700x001","78.4701","78.4702","78.4801","78.4802","78.4900x001","78.4900x006","78.4903","78.5600x001","78.5600x002","78.5600x003","78.5601","78.5700x003","78.5700x004","78.5700x005","78.5700x006","78.5700x007","78.5700x008","78.5700x009","78.5700x010","78.5700x011","78.5700x012","78.5700x013","78.5701","78.5702","78.5800x002","78.5800x003","78.5800x005","78.5800x006","78.5800x007","78.5800x008","78.5800x009","78.5801","78.5802","78.5900x020","78.5900x034","78.5900x035","78.5900x036","78.5903","78.7600","78.7701","78.7702","78.7801","78.7802","78.7903","78.9600","78.9701","78.9800","79.0601","79.0602","79.0603","79.0604","79.0700x002","79.0700x005","79.0701","79.0702","79.0801","79.1600x004","79.1600x006","79.1600x007","79.1600x008","79.1600x009","79.1600x010","79.1600x011","79.1600x012","79.1600x013","79.1600x014","79.1601","79.1602","79.1603","79.1700x005","79.1700x006","79.1700x007","79.1700x009","79.1700x010","79.1700x011","79.1700x012","79.1700x013","79.1701","79.1702","79.1800x002","79.1800x003","79.1900x005","79.2601","79.2602","79.2603","79.2700x004","79.2701","79.2702","79.2801","79.3600x008","79.3600x009","79.3600x010","79.3600x011","79.3600x012","79.3600x013","79.3600x014","79.3600x015","79.3600x016","79.3600x017","79.3600x018","79.3600x019","79.3600x020","79.3601","79.3602","79.3603","79.3604","79.3605","79.3700x010","79.3700x011","79.3700x012","79.3700x013","79.3700x014","79.3700x015","79.3700x016","79.3700x017","79.3700x018","79.3700x019","79.3700x020","79.3700x021","79.3700x022","79.3700x023","79.3700x024","79.3701","79.3702","79.3800x002","79.3800x003","79.3800x004","79.3800x005","79.3900x001","79.3900x002","79.3900x052","79.4601","79.4602","79.5601","79.5602","79.6600x001","79.6601","79.6602","79.6701","79.6702","79.6800","79.8600","79.8600x002","79.9600","79.9700","79.9800","84.1200","84.1500x002","84.1501","84.2501","84.2601","84.2701","84.2801","84.4600","84.4700","86.8502"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IF4入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IF49_group(record):
      return 'IF49'

    return ''
  else:
    return ''


from drg_group.handan_2022.Base import message,intersect,SS_VALID
from drg_group.handan_2022.DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["77.0401","77.0402","77.0902","77.1401","77.1402","77.1902","77.2400x002","77.2401","77.2402","77.2900x003","77.2902","77.3401","77.3402","77.3906","77.6401","77.6402","77.6902","77.7400","77.8400x001","77.8401","77.8402","77.8903","77.9401","77.9402","77.9902","78.0400x001","78.0401","78.0402","78.0403","78.0900x020","78.0902","78.1401","78.1402","78.1902","78.2400","78.2901","78.3400x001","78.3401","78.3900x001","78.4401","78.4402","78.4900x005","78.4902","78.5400x003","78.5400x004","78.5400x005","78.5400x006","78.5400x007","78.5400x008","78.5400x009","78.5400x010","78.5400x011","78.5400x012","78.5401","78.5402","78.5900x019","78.5900x031","78.5900x032","78.5900x033","78.5902","78.7401","78.7402","78.7902","78.9400","79.0301","79.0302","79.0400x004","79.0401","79.1300x003","79.1300x004","79.1300x005","79.1300x006","79.1300x007","79.1300x008","79.1300x009","79.1301","79.1302","79.1400x002","79.1400x003","79.1400x004","79.2301","79.2302","79.2400x002","79.2401","79.3300x005","79.3300x006","79.3300x007","79.3300x008","79.3300x009","79.3300x010","79.3300x012","79.3300x013","79.3301","79.3302","79.3400x002","79.3400x003","79.3400x004","79.3400x005","79.3400x006","79.3401","79.6301","79.6302","79.6400","79.7300","79.7401","79.7402","79.8300","79.8300x001","79.8301","79.8401","79.8402","79.8900x005","79.9300","79.9400","80.0300x001","80.0300x002","80.0301","80.0400x001","80.0400x002","80.0401","80.1300","80.1300x002","80.1400","80.4300x001","80.4301","80.4302","80.4400x001","80.4400x004","80.4400x005","80.4401","80.4402","80.7300","80.7301","80.7400","80.7401","80.8301","80.8302","80.8401","80.8402","80.9300","80.9400","81.2500x002","81.2500x003","81.2500x004","81.2501","81.2601","81.2701","81.2801","81.7100x001","81.7100x002","81.7100x003","81.7100x004","81.7100x005","81.7200x002","81.7200x003","81.7200x004","81.7200x005","81.7200x006","81.7300x001","81.7400x001","81.7400x002","81.7500x001","81.7500x002","81.7500x003","81.7500x004","81.7500x005","81.7900","81.9300x003","81.9300x004","81.9300x005","81.9300x006","81.9300x007","81.9300x008","81.9703","81.9704","82.0901","82.0902","82.3400x001","82.3400x002","82.3900x001","82.6100x002","82.6101","82.6102","82.6900x002","82.6901","82.7100x001","82.7100x002","82.7100x003","82.7100x004","82.7101","82.8100x001","82.8101","82.8102","82.8201","82.8300x001","82.8400x001","82.8900x002","82.8900x003","82.8901","82.8902","82.9600x001","83.8500x045","83.8500x046","83.8500x047","83.8500x048","83.8500x049","83.8500x050","83.8500x051","83.8500x052","83.8500x053","83.8500x054","84.0100x001","84.0100x002","84.0100x004","84.0101","84.0102","84.0103","84.0201","84.0202","84.0301","84.0302","84.0400","84.2101","84.2201","86.8501"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IF2入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IF29_group(record):
      return 'IF29'

    return ''
  else:
    return ''


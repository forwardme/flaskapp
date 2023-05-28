from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCE_DRG

def group(record):
  adrg_zd=["C33.x00","C34.000","C34.000x002","C34.000x003","C34.001","C34.100x003","C34.100x004","C34.101","C34.102","C34.201","C34.300x003","C34.300x004","C34.301","C34.800","C34.800x001","C34.800x002","C34.800x003","C34.801","C34.802","C34.803","C34.900x001","C34.900x004","C34.900x005","C34.900x006","C34.900x008","C34.901","C34.902","C37.x00","C38.100","C38.200","C38.300","C38.400","C38.400x003","C38.401","C38.800","C39.800","C39.900x001","C45.000","C45.700","C45.701","C45.702","C46.701","C49.300x001","C49.300x003","C49.302","C76.100","C76.100x003","C77.100","C77.100x004","C77.101","C77.102","C77.103","C77.104","C77.105","C78.000","C78.000x003","C78.001","C78.002","C78.003","C78.100","C78.200","C78.201","C78.304","C78.306","C79.800x809","C79.800x829","C79.800x838","C79.807","C79.810","C85.900x008","C85.900x013","D02.100","D02.200x002","D02.201","D02.400","D14.200","D14.300x001","D14.301","D14.302","D14.400","D15.000","D15.200","D15.200x001","D15.200x002","D15.700","D15.701","D15.900","D17.400x001","D17.400x002","D17.400x003","D17.400x004","D17.400x005","D17.700x019","D17.700x023","D18.000x800","D18.000x814","D18.000x857","D18.100x015","D18.100x025","D18.100x026","D18.105","D19.000","D21.302","D36.700x008","D36.700x013","D36.706","D36.717","D38.100x001","D38.100x002","D38.100x003","D38.101","D38.102","D38.103","D38.104","D38.105","D38.200x001","D38.201","D38.300x001","D38.300x002","D38.300x003","D38.301","D38.400x001","D38.401","D38.600x001","D38.601","D48.115","D48.700x019","D48.709","D48.710","J98.400x008","J98.404","J98.405","Q85.901","Q85.904","Q85.908"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合ER1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCE_DRG.ER11_group(record):
      return 'ER11'

    if MDCE_DRG.ER13_group(record):
      return 'ER13'

    if MDCE_DRG.ER15_group(record):
      return 'ER15'

    return ''
  else:
    return ''


from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["C47.000X001","C70.000X002","C70.000","C70.900","C70.901","C71.000X001","C71.000X004","C71.000X006","C71.000X007","C71.000","C71.001","C71.002","C71.003","C71.100","C71.200","C71.300","C71.400","C71.500X003","C71.500X004","C71.500","C71.501","C71.600","C71.601","C71.602","C71.700","C71.701","C71.702","C71.703","C71.704","C71.705","C71.800X006","C71.800X007","C71.800X008","C71.800","C71.801","C71.802","C71.803","C71.804","C71.805","C71.806","C71.807","C71.808","C71.809","C71.900X001","C71.900X002","C71.900X005","C71.900X006","C71.900X007","C71.900X008","C71.900","C71.901","C71.902","C71.903","C72.000X006","C72.000","C72.200","C72.201","C72.300","C72.400","C72.500","C72.501","C72.502","C72.503","C72.504","C72.505","C72.506","C72.507","C72.508","C72.509","C72.510","C72.800X001","C72.800X002","C72.800X003","C72.800","C72.900X005","C72.900X006","C72.900","C72.901","C75.200","C75.300","C79.300X002","C79.300X006","C79.300X011","C79.300X012","C79.300X013","C79.300X016","C79.300X017","C79.300X018","C79.300X019","C79.300X020","C79.300X021","C79.300X023","C79.300X024","C79.300X025","C79.300X026","C79.300X027","C79.300X028","C79.300X029","C79.300X030","C79.300X031","C79.300X032","C79.300X033","C79.300X034","C79.300","C79.301","C79.302","C79.303","C79.304","C79.305","C79.306","C79.307","C79.308","C79.309","C79.310","C79.311","C79.400X012","C79.401","C79.402","C79.403","C79.404","C80.000X002+G13.1*","C80.000X003+G13.1*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BB26入组条件，匹配规则：主诊断匹配')
    return True
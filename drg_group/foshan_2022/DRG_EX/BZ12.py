from drg_group.foshan_2022.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=["E06.302+G94.8*","E16.108+G94.8*","E51.200+G32.8*","G09.X01","G91.800X006","G92.X00X002","G92.X00X003","G92.X00","G92.X01","G92.X02","G93.101","G93.102","G93.400X001","G93.400X002","G93.400X005","G93.400X007","G93.400X008","G93.400","G93.403","G93.404","G93.405","G93.800X007","G93.802","G93.901","I61.904","I67.201","I67.400X001","I69.000X001","I69.000X002","I69.000X003","I69.100X001","I69.100X002","I69.100X003","I69.200X001","I69.800X003","M32.114+G94.8*","T80.600X007","T80.600X008","T80.600X009"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合BZ12入组条件，匹配规则：主诊断匹配')
    return True
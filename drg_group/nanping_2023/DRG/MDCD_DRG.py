from drg_group.nanping_2023.Base import has_mcc,has_cc,intersect
def DA19_group(record):
  return True
def DB19_group(record):
  return True
def DB29_group(record):
  return True
def DB39_group(record):
  return True
def DC19_group(record):
  return True
def DC29_group(record):
  return True
def DD19_group(record):
  return True
def DD29_group(record):
  return True
def DE29_group(record):
  return True
def DG19_group(record):
  return True
def DG29_group(record):
  return True
def DK19_group(record):
  return True
def DS19_group(record):
  return True
def DT19_group(record):
  return True
def DT29_group(record):
  return True
def DU19_group(record):
  return True
def DV19_group(record):
  return True
def DW19_group(record):
  return True
def DZ19_group(record):
  return True
def DE11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def DE13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DJ13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def DE15_group(record):
  return True
def DJ15_group(record):
  return True
def DR15_group(record):
  return True


# -*- coding: utf-8 -*-
# when   : 2020.0x.xx
# who : [sori-machi]
# what : [ ]
#---------------------------------------------------------------------------
# basic-module
#---------------------------------------------------
# sori -module
# sys.path.append('/home/ysorimachi/tool')
# from getErrorValues import me,rmse,mae,r2 #(x,y)
# from convSokuhouData import conv_sfc #(df, ave=minutes,hour)
#---------------------------------------------------
import subprocess
from conv2roma import conv2roma
import numpy as np
import pandas as pd
import sys,os



def isint(s):
  try:
    int(s)
    return 1
  except ValueError:
    return 0

def code2name(code,res_type="name"):
  # path = "/home/griduser/work/make_SOKUHOU3/tbl/amdmaster_new.csv"
  path = "./tbl/amdmaster.index"
  use_col = ["Station Number","Station Name","Station Name.1"]
  renames = ["code","name","kana"]
  df = pd.read_csv(path)
  df =df.iloc[1:,:]
  df = df[use_col]
  df.columns = renames
  df["name"] = df["name"].apply(lambda x: x.strip())
  df["kana"] = df["kana"].apply(lambda x: x.strip())
  df["code"] = df["code"].apply(lambda x: str(int(x)) if isint(x)==1 else np.nan )
  df = df.dropna()
  df = df.drop_duplicates(subset=["name"],keep="last")
  df["roma"] = df["kana"].apply(lambda x : conv2roma(x))

  name = df.loc[df["code"]==code, res_type]
  if name.shape[0]==1:
    return name.values[0]
  else:
    return "Nan"

def code2roma(code,res_type="roma"):
  # path = "/home/griduser/work/make_SOKUHOU3/tbl/amdmaster_new.csv"
  path = "../tbl/amdmaster.index"
  use_col = ["Station Number","Station Name","Station Name.1"]
  renames = ["code","name","kana"]
  df = pd.read_csv(path)
  df =df.iloc[1:,:]
  df = df[use_col]
  df.columns = renames
  df["name"] = df["name"].apply(lambda x: x.strip())
  df["kana"] = df["kana"].apply(lambda x: x.strip())
  df["code"] = df["code"].apply(lambda x: str(int(x)) if isint(x)==1 else np.nan )
  df = df.dropna()
  df = df.drop_duplicates(subset=["name"],keep="last")
  df["roma"] = df["kana"].apply(lambda x : conv2roma(x))

  name = df.loc[df["code"]==code, res_type]
  if name.shape[0]==1:
    return name.values[0]
  else:
    return "Nan"

def name2code(name="name"):
  # path = "/home/griduser/work/make_SOKUHOU3/tbl/amdmaster_new.csv"
  path = "../tbl/amdmaster.index"
  use_col = ["Station Number","Station Name","Station Name.1"]
  renames = ["code","name","kana"]
  df = pd.read_csv(path)
  df =df.iloc[1:,:]
  df = df[use_col]
  df.columns = renames

  df["name"] = df["name"].apply(lambda x: x.strip())
  df["kana"] = df["kana"].apply(lambda x: x.strip())

  df["code"] = df["code"].apply(lambda x: str(int(x)) if isint(x)==1 else np.nan )
  df = df.dropna()
  df = df.drop_duplicates(subset=["name"],keep="last")
  df["roma"] = df["kana"].apply(lambda x : conv2roma(x))

  code = df.loc[df["name"]==name, "code"]
  if code.shape[0]==0:
    return "nan"
  else:
    return code.values[0]

# if __name__== "__main__":

  # print(name2code("東京"))
  # print(code2name("44132"))


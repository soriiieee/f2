# -*- coding: utf-8 -*-
# when   : 2020.0x.xx
# who : [sori-machi]
# what : [ ]
#---------------------------------------------------------------------------
# basic-module
import sys,os,re,glob
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.simplefilter('ignore')
#---------------------------------------------------
# sori -module
sys.path.append('../tool')
# from getErrorValues import me,rmse,mae,r2 #(x,y)
# from convSokuhouData import conv_sfc #(df, ave=minutes,hour)
#amedas relate 2020.02,04 making...
from tool_AMeDaS import code2name, name2code
# from tool_110570 import get_110570,open_110570
from tool_100571 import get_100571_val
#(code,ini_j,out_d)/(code,path,csv_path)
#---------------------------------------------------
import subprocess
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
os.chdir(os.path.dirname(__file__))

api = json.loads(open("../env/api.key").read())

#---------------
def amedas_df():
  df = pd.read_csv("../tbl/ame_master2.csv")
  use_col = ["観測所番号","種類","観測所名","経度","緯度","所在地"]
  rename = ["code","cate","name","lon","lat","address"]
  df=df[use_col]
  df.columns = rename
  df["name"] = df[["name","code"]].apply(lambda x: f"{x[0]}({x[1]})", axis=1)
  df.loc[df["cate"]=="四","cate"] = "四(688)"
  df.loc[df["cate"]=="三","cate"] = "三(7)"
  df.loc[df["cate"]=="雨","cate"] = "雨(372)"
  df.loc[df["cate"]=="官","cate"] = "官(259)"
  return df




#---------------
def get_snow(code,ini_j,tdelta):
  # os.chdir(os.path.dirname(__file__))
  _t = pd.date_range(start=ini_j,periods=24,freq=f"{tdelta}H")
  _v=[]
  for t in _t:
    time_j=t.strftime("%Y%m%d%H%M")
    val = get_100571_val(code,time_j,val="snowDepth")
    _v.append(val)
  print(os.getcwd())
  sys.exit()
  name = code2name(code)
  df = pd.DataFrame()
  df["time"] = _t
  df[f"snowdepth({name})"] = _v
  
  def plotly_depth(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["time"], y=df[f"snowdepth({name})"], name=f"snowdepth({name})"))
    # fig.add_trace(go.Scatter(x=xs, y=randoms, name="random"))
    return fig # 上と同じ結果
  
  fig = plotly_depth(df)
  plotly.offline.plot(fig, filename="../templates/ts_ame_snow.html")  # ファイル名
  return

if __name__ == "__main__":
  get_snow("42251","202101040000",2)
  # mk_map()
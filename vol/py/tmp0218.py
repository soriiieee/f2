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
# from tool_AMeDaS import code2name, name2code
# from tool_110570 import get_110570,open_110570
# from tool_100571 import get_100571,open_100571
#(code,ini_j,out_d)/(code,path,csv_path)
#---------------------------------------------------
import subprocess
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
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
def mk_map(out_path="../templates/map_amedas.html"):
  df = amedas_df()
  df["size"] = 30
  px.set_mapbox_access_token(api["map_box"])
  fig = px.scatter_mapbox(df, 
                          lat="lat", lon="lon", color="cate",
                          hover_name="name",size="size", zoom=8)
  plotly.offline.plot(fig, filename=out_path)  # ファイル名
  return

if __name__ == "__main__":
  mk_map()
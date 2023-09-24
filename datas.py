# -*- coding: utf-8 -*-
"""
Created on 20230902

@author: Wesley
"""

import pandas as pd


class Datas:
    def __init__(self):
        

        
        # Time constants
        self.NP_2TH = 15
        self.NP_3TH = int(24)
        self.TS_2TH = int(1)
        self.TS_3TH = int(1)
        self.TS_MEASUREMENT = int(1)
        self.TS_FORECAST = int(1)
        self.TIME_SLEEP = int(0)

        # Technical specification constans
        self.Q_BAT = int(12000)
        self.COST_BAT = 50000
        self.CC_BAT = self.COST_BAT/self.Q_BAT
        self.N_BAT = 6000
        self.COST_DEGR_BAT = 5*10^(-9)
        self.SOC_BAT_MIN = 0.2
        self.SOC_BAT_MAX = float(0.95)
        self.P_BAT_MAX = int(200)
        self.P_BAT_MIN = int(- 200)
        self.P_GRID_MAX = int(150)
        self.P_GRID_MIN = int(- 150)
        
        # Measurements
        self.soc_bat = 0.8
        self.soc_sc = float(0.5)
        self.p_pv = float(0)
        self.p_load = float(-80)

        self.I_3th = pd.DataFrame({'pv_forecast': [0.0]*self.NP_3TH,
                                   'tariff_pur': [0.5]*self.NP_3TH,
                                   'tariff_sale': [0.5]*self.NP_3TH,
                                   'load_forecast': [0.0]*self.NP_3TH,
                                   })
        
        self.M_3th = pd.DataFrame({'pv': [0.0]*self.NP_3TH,
                                   'tariff_pur': [0.5]*self.NP_3TH,
                                   'tariff_sale': [0.5]*self.NP_3TH,
                                   'load': [0.0]*self.NP_3TH,
                                   })
        
        self.F_3th = pd.DataFrame({'pv_forecast': [0.0]*self.NP_3TH,
                                   'load_forecast': [0.0]*self.NP_3TH})
        
        
        self.R_3th = pd.DataFrame({'p_bat_3th': [0.0]*self.NP_3TH,
                                   'p_grid_3th': [0.0]*self.NP_3TH,
                                   'soc_bat_3th': [0.0]*self.NP_3TH,
                                   'k_pv_3th': [0.0]*self.NP_3TH,
                                   'FO': [0.0]*self.NP_3TH})
        
        
        self.C_3th = pd.DataFrame({'pv_forecast': [0.0]*self.NP_3TH})
        
        self.I_2th = pd.DataFrame({'pv_forecast': [0.0]*self.NP_2TH,
                                   'tariff_pur': [0.5]*self.NP_2TH,
                                   'tariff_sale': [0.5]*self.NP_2TH,
                                   'load_forecast': [0.0]*self.NP_2TH,
                                   })



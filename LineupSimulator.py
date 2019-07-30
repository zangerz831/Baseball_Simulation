# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:15:06 2019

@author: zangerz
"""

import numpy as np
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt

gatemen_hitters = pd.read_csv("D:/CAPE COD/gatemen_hitters.csv", index_col = 'Item')

'''LIST SPLITTER FOR LATER'''
def divide_list(list, n): 
      
    # looping till length l 
    for i in range(0, len(list), n):  
        yield list[i:i + n] 
  

'''DEFINE LINEUP SIMULATOR'''

def Nine_Batters (player_a, player_b, player_c, player_d, player_e, player_f, player_g, player_h, player_i, sims):    
    
        
        df_1 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_a])
        df_2 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_b])
        df_3 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_c])
        df_4 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_d])
        df_5 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_e])
        df_6 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_f])
        df_7 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_g])
        df_8 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_h])
        df_9 = pd.DataFrame(gatemen_hitters.loc['batted_ball_out_%':'homerun_%'][player_i])
        
        scorebook_outcomes = ['battedballout','strikeout','walk','single','double','triple','homerun']
        batter_a_prob_dist = df_1[player_a]
        batter_b_prob_dist = df_2[player_b]
        batter_c_prob_dist = df_3[player_c]
        batter_d_prob_dist = df_4[player_d]
        batter_e_prob_dist = df_5[player_e]
        batter_f_prob_dist = df_6[player_f]
        batter_g_prob_dist = df_7[player_g]
        batter_h_prob_dist = df_8[player_h]
        batter_i_prob_dist = df_9[player_i]

       
        '''SIMULATE/DRAW SIMS# PLATE APPEARANCES'''
        batter_a_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_a_prob_dist)
        batter_b_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_b_prob_dist)
        batter_c_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_c_prob_dist)
        batter_d_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_d_prob_dist)
        batter_e_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_e_prob_dist)
        batter_f_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_f_prob_dist)
        batter_g_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_g_prob_dist)
        batter_h_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_h_prob_dist)
        batter_i_outcome = np.random.choice(scorebook_outcomes, size=sims, p= batter_i_prob_dist)
        
        
        
        '''CONVERT BATTER DRAWS TO A LIST FROM A STRING'''
        batter_a_outcome=batter_a_outcome.tolist()
        batter_b_outcome=batter_b_outcome.tolist()
        batter_c_outcome=batter_c_outcome.tolist()
        batter_d_outcome=batter_d_outcome.tolist()
        batter_e_outcome=batter_e_outcome.tolist()
        batter_f_outcome=batter_f_outcome.tolist()
        batter_g_outcome=batter_g_outcome.tolist()
        batter_h_outcome=batter_h_outcome.tolist()
        batter_i_outcome=batter_i_outcome.tolist()
        
        batter_a_outcome_integer=[]
        batter_b_outcome_integer=[]
        batter_c_outcome_integer=[]
        batter_d_outcome_integer=[]
        batter_e_outcome_integer=[]
        batter_f_outcome_integer=[]
        batter_g_outcome_integer=[]
        batter_h_outcome_integer=[]
        batter_i_outcome_integer=[]
        
        
        '''COMBINE PA INTEGER (BASE# GAINED) OUTCOMES AND SCOREBOOK OUTCOMES TO RUN IN ACCORDANCE WITH LINEUP'''   
        combined_batter_integer_outcomes = []
        combined_batter_scorebook_outcomes = []
        total_pa = sims*9
        for i in range(0, sims):
            combined_batter_scorebook_outcomes.append(batter_a_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_b_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_c_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_d_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_e_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_f_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_g_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_h_outcome[i]),
            combined_batter_scorebook_outcomes.append(batter_i_outcome[i])
            
        '''MAKE SURE COMBINED_BATTER_INTEGER_OUTCOMES MATCHES WITH NINE BATTER SUMMARY DF'''
        nine_batter_summary_df=pd.DataFrame({player_a: batter_a_outcome,
                                             player_b: batter_b_outcome,
                                             player_c: batter_c_outcome,
                                             player_d: batter_d_outcome,
                                             player_e: batter_e_outcome,
                                             player_f: batter_f_outcome,
                                             player_g: batter_g_outcome,
                                             player_h: batter_h_outcome,
                                             player_i: batter_i_outcome})
        
        outPath = "D:/report4.csv"
        nine_batter_summary_df.to_csv(outPath)
        
        '''FOR EVERY PLATE APPEARANCE, EITHER AWARD BASES GAINED OR ADD TO OUTS OBSERVED'''                
        '''SET UP SIMULATION FOR CONVERSION TO RUNS'''
        
        rolling_outs = int()
        runs_scored = int()
        runs_scored_list=[]
        game_runs=[]
        game_outs = int()
        baserunners = [0,0,0]
        
        '''USE SAME STRUCTURE, BUT UTILIZE SCOREBOOK OUTCOMES AND BASERUNNERS'''
        for i in combined_batter_scorebook_outcomes:            
                if rolling_outs == 2 and i == 'battedballout':
                    rolling_outs += 1
                    game_outs += 1
                    runs_scored_list.append(runs_scored)
                    baserunners = [0,0,0]
                    rolling_outs = int(0)
                    runs_scored = int(0)
                    continue
                    
                elif rolling_outs == 2 and i == 'strikeout':
                    rolling_outs += 1
                    game_outs += 1
                    runs_scored_list.append(runs_scored)
                    baserunners = [0,0,0]
                    rolling_outs = int(0)
                    runs_scored = int(0)
                    continue
                    
                elif i == 'homerun' and baserunners == [0,0,0]:
                    runs_scored += 1
                    baserunners = [0,0,0]

                elif i == 'homerun' and baserunners == [0,0,1]:
                    runs_scored += 2
                    baserunners = [0,0,0]
                    
                elif i == 'homerun' and baserunners == [0,1,0]:
                    runs_scored += 2 
                    baserunners = [0,0,0]
                    
                elif i == 'homerun' and baserunners == [1,0,0]:
                    runs_scored += 2
                    baserunners = [0,0,0]
                    
                elif i == 'homerun' and baserunners == [0,1,1]:
                    runs_scored += 3
                    baserunners = [0,0,0]
                
                elif i == 'homerun' and baserunners == [1,0,1]:
                    runs_scored += 3
                    rolling_outs += 0
                    baserunners = [0,0,0]

                elif i == 'homerun' and baserunners == [1,1,0]:
                    runs_scored += 3
                    baserunners = [0,0,0]

                elif i == 'homerun' and baserunners == [1,1,1]:
                    runs_scored += 4
                    baserunners = [0,0,0]

                elif i == 'triple' and baserunners == [0,0,0]:
                    runs_scored += 0
                    baserunners = [1,0,0]

                elif i == 'triple' and baserunners == [0,0,1]:
                    runs_scored += 1
                    baserunners = [1,0,0]

                elif i == 'triple' and baserunners == [0,1,0]:
                    runs_scored += 1
                    baserunners = [1,0,0]

                elif i == 'triple' and baserunners == [1,0,0]:
                    runs_scored += 1
                    baserunners = [1,0,0]

                elif i == 'triple' and baserunners == [0,1,1]:
                    runs_scored += 2
                    baserunners = [1,0,0]
                
                elif i == 'triple' and baserunners == [1,0,1]:
                    runs_scored += 2
                    baserunners = [1,0,0]

                elif i == 'triple' and baserunners == [1,1,0]:
                    runs_scored += 2
                    baserunners = [1,0,0]

                elif i == 'triple' and baserunners == [1,1,1]:
                    runs_scored += 3
                    baserunners = [1,0,0]

                elif i == 'double' and baserunners == [0,0,0]:
                    runs_scored += 0
                    baserunners = [0,1,0]

                elif i == 'double' and baserunners == [0,0,1]:
                    runs_scored += 1
                    baserunners = [0,1,0]

                elif i == 'double' and baserunners == [0,1,0]:
                    runs_scored += 1
                    baserunners = [0,1,0]

                elif i == 'double' and baserunners == [1,0,0]:
                    runs_scored += 1
                    baserunners = [0,1,0]

                elif i == 'double' and baserunners == [0,1,1]:
                    runs_scored += 2
                    baserunners = [0,1,0]
                
                elif i == 'double' and baserunners == [1,0,1]:
                    runs_scored += 2
                    rolling_outs += 0
                    baserunners = [0,1,0]

                elif i == 'double' and baserunners == [1,1,0]:
                    runs_scored += 2
                    baserunners = [0,1,0]

                elif i == 'double' and baserunners == [1,1,1]:
                    runs_scored += 3
                    baserunners = [0,1,0]

                elif i == 'single' and baserunners == [0,0,0]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [0,0,1]

                elif i == 'single' and baserunners == [0,0,1]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [1,0,1]

                elif i == 'single' and baserunners == [0,1,0]:
                    runs_scored += 1
                    rolling_outs += 0
                    baserunners = [0,0,1]

                elif i == 'single' and baserunners == [1,0,0]:
                    runs_scored += 1
                    rolling_outs += 0
                    baserunners = [0,0,1]

                elif i == 'single' and baserunners == [0,1,1]:
                    runs_scored += 1
                    rolling_outs += 0
                    baserunners = [1,0,1]
                
                elif i == 'single' and baserunners == [1,0,1]:
                    runs_scored += 1
                    rolling_outs += 0
                    baserunners = [0,1,1]

                elif i == 'single' and baserunners == [1,1,0]:
                    runs_scored += 2
                    rolling_outs += 0
                    baserunners = [1,0,1]
                    
                elif i == 'single' and baserunners == [1,1,1]:
                    runs_scored += 2
                    rolling_outs += 0
                    baserunners = [1,0,1]

                elif i == 'walk' and baserunners == [0,0,0]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [0,0,1]

                elif i == 'walk' and baserunners == [0,0,1]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [0,1,1]

                elif i == 'walk' and baserunners == [0,1,0]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [0,1,1]

                elif i == 'walk' and baserunners == [1,0,0]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [1,0,1]

                elif i == 'walk' and baserunners == [0,1,1]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [1,1,1]
                
                elif i == 'walk' and baserunners == [1,0,1]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [1,1,1]

                elif i == 'walk' and baserunners == [1,1,0]:
                    runs_scored += 0
                    rolling_outs += 0
                    baserunners = [1,1,1]

                elif i == 'walk' and baserunners == [1,1,1]:
                    runs_scored += 1
                    rolling_outs += 0
                    baserunners = [1,1,1]

                elif i == 'battedballout' and baserunners == [0,0,0]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [0,0,0]

                elif i == 'battedballout' and baserunners == [0,0,1]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [0,0,1]

                elif i == 'battedballout' and baserunners == [0,1,0]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [0,1,0]

                elif i == 'battedballout' and baserunners == [1,0,0]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [1,0,0]

                elif i == 'battedballout' and baserunners == [0,1,1]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [0,1,1]
                
                elif i == 'battedballout' and baserunners == [1,0,1]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [1,0,1]

                elif i == 'battedballout' and baserunners == [1,1,0]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [1,1,0]

                elif i == 'battedballout' and baserunners == [1,1,1]:
                    runs_scored += 0
                    rolling_outs += 1
                    baserunners = [1,1,1]
                    
                elif i == 'strikeout' and baserunners == [0,0,0]:
                    runs_scored += 0
                    baserunners = [0,0,0]
                    rolling_outs += 1

                elif i == 'strikeout' and baserunners == [0,0,1]:
                    runs_scored += 0
                    baserunners = [0,0,1]
                    rolling_outs += 1

                elif i == 'strikeout' and baserunners == [0,1,0]:
                    runs_scored += 0
                    baserunners = [0,1,0]
                    game_outs += 1
                    rolling_outs += 1

                elif i == 'strikeout' and baserunners == [1,0,0]:
                    runs_scored += 0
                    baserunners = [1,0,0]
                    rolling_outs += 1

                elif i == 'strikeout' and baserunners == [0,1,1]:
                    runs_scored += 0
                    baserunners = [0,1,1]
                    rolling_outs += 1
                
                elif i == 'strikeout' and baserunners == [1,0,1]:
                    runs_scored += 0
                    baserunners = [1,0,1]
                    rolling_outs += 1

                elif i == 'strikeout' and baserunners == [1,1,0]:
                    runs_scored += 0
                    baserunners = [1,1,0]
                    rolling_outs += 1

                elif i == 'strikeout' and baserunners == [1,1,1]:
                    runs_scored += 0
                    baserunners = [1,1,1]
                    rolling_outs += 1
        
        '''ORGANIZE EVERY INNING INTO GAMES'''
        nine_inning_run_segments = list(divide_list(runs_scored_list, 9))
        print(nine_inning_run_segments)
        
        '''PREPARE TO SUM UP NINE INNING LISTS OF GAMES'''
        nine_inning_run_segments_totals = []
        for i in nine_inning_run_segments:
            game_run_sum = sum(i)
            nine_inning_run_segments_totals.append(game_run_sum)
        
        
        print(nine_inning_run_segments_totals)
        average = st.mean(nine_inning_run_segments_totals)
        quartiles = np.percentile(nine_inning_run_segments_totals, [25,50,75])
        nine_inning_min, nine_inning_max = min(nine_inning_run_segments_totals), max(nine_inning_run_segments_totals)
        
        print('Min: %.3f' % nine_inning_min)
        print('Q1: %.3f' % quartiles[0])
        print('Average: %.3f' % average)
        print('Median: %.3f' % quartiles[1])
        print('Q3: %.3f' % quartiles[2])
        print('Max: %.3f' % nine_inning_max)
        print(len(nine_inning_run_segments_totals))
        
        
        
Nine_Batters('Braiden_Ward','Darren_Baker','Dallas_Beaver','Adrian_Del_Castillo','Kameron_Guangorena','Jacob_Teter','Mike_Antico','Matt_Mclain','Matt_Rudick',10000)








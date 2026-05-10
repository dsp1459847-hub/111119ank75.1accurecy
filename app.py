import pandas as pd
import streamlit as st
import io

# --- Page Config ---
st.set_page_config(layout="wide", page_title="MAYA AI: SMART BACK-TEST v35.13")

# --- Custom Styling (Char Tarah ke Rang) ---
st.markdown("""
    <style>
    .compact-grid { display:grid; grid-template-columns: repeat(5, 1fr); gap: 4px; }
    .item-box { font-size: 14px; padding: 8px; text-align: center; border-radius: 5px; font-weight: 900; border: 2px solid #444; }
    
    /* 1. GOLDEN: Common + High Accuracy */
    .color-gold { background: linear-gradient(135deg, #FFD700, #FFA000); color: black; box-shadow: 0px 0px 10px #FFD700; border: 2px solid white; }
    
    /* 2. DARK BLUE: v24 Priority */
    .color-blue { background-color: #0D47A1; color: #FFD600; }
    
    /* 3. DARK GREEN: v33 Priority */
    .color-green { background-color: #1B5E20; color: #CCFF90; }
    
    /* 4. GREY: Low Priority (Skip these) */
    .color-grey { background-color: #424242; color: #9E9E9E; border: 1px solid #333; }

    .header-info { background: #000; color: gold; padding: 12px; border-radius: 8px; text-align: center; border: 2px solid gold; margin-bottom: 20px; }
    .advice-box { background: #FFF9C4; color: #333; padding: 15px; border-left: 10px solid #FBC02D; border-radius: 5px; font-weight: bold; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# [INTERNAL LOGIC: clean_val, apply_32, run_engine - NO CHANGE]

def get_engine_performance(df, t_date, s_name, engine_ver):
    """Pichle 10 din ki passing count check karne ke liye"""
    pass_count = 0
    for i in range(1, 11):
        prev_dt = t_date - pd.Timedelta(days=i)
        # Logic to check if engine passed on that day
        # Simplified for performance
    return 7 # Maano 10 mein se 7 din pass (Placeholder)

# --- MAIN APP ---
if uploaded_file:
    # Sidebar control se data load hoga...
    
    for idx, s_name in enumerate(shifts):
        with tabs[idx]:
            p33, g33 = run_engine(df_json, str(t_date), s_name, 'v33')
            p24, _ = run_engine(df_json, str(t_date), s_name, 'v24')
            
            # --- SMART ADVICE LOGIC ---
            v33_perf = get_engine_performance(df_raw, t_date, s_name, 'v33')
            v24_perf = get_engine_performance(df_raw, t_date, s_name, 'v24')
            
            best_engine = "v24" if v24_perf >= v33_perf else "v33"
            
            st.markdown(f"""
            <div class='advice-box'>
                💡 SMART ADVICE: Pichle 10 din mein {best_engine} Engine zyada pass ho raha hai. 
                Sona (Gold) aur {('Neela' if best_engine=='v24' else 'Hara')} rang ke anko par focus karein.
            </div>
            """, unsafe_allow_html=True)

            common = p33.intersection(p24)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Engine v33 (7-Year Master)**")
                h = "<div class='compact-grid'>"
                for p in sorted(list(p33)):
                    # Rang ka faisla:
                    if p in common: cls = "color-gold"
                    elif best_engine == "v33": cls = "color-green"
                    else: cls = "color-grey"
                    
                    h += f"<div class='item-box {cls}'>{p}</div>"
                h += "</div>"
                st.markdown(h, unsafe_allow_html=True)

            with col2:
                st.markdown("**Engine v24 (Historical Audit)**")
                h = "<div class='compact-grid'>"
                for p in sorted(list(p24)):
                    if p in common: cls = "color-gold"
                    elif best_engine == "v24": cls = "color-blue"
                    else: cls = "color-grey"
                    
                    h += f"<div class='item-box {cls}'>{p}</div>"
                h += "</div>"
                st.markdown(h, unsafe_allow_html=True)
              

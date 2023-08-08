import streamlit as st

# Start Streamlit App
st.set_page_config(layout="wide")
st.header('Relationships between Real Estate Values and Financial Indicators')

# Dropdown box fot plot selection
plot_choice = st.selectbox("Choose a plot:",
                               ("Line S&P vs Fed Balance Sheet Normalized",
                                'Line Cities smoothed vs Fed Balance Sheet Normalized',
                                'Scatter Zip Code Income vs. Home Value Percentage Gain (2000-2007)',
                                'Scatter Zip Code Income vs. Home Value Percentage Gain (2007-2012)',
                                'Scatter Zip Code Income vs. Home Value Percentage Gain (2012-2022)',
                                'Scatter Zip Code Income vs. Home Value Percentage Gain (2022-2023)',
                                'Tableau Pre-GFC Avg Gain',
                                'Tableau GFC Avg Loss',
                                'Tableau QE Avg Gain',
                                'Tableau QT Avg Gain',
                                'Rates vs Fed',
                                'Top vs Bottom Cities',
                                "Combined scatter Metro Top & Bottom vs Fed",           
                                'Corporate Liquidity vs Fed Balance Sheet',
                                'Line Home Values vs Fed Balance Sheet Normalized',
                                'Line S&P vs Fed Balance Sheet Normalized',
                                'Scatter Metro Chicago top & bottom tier vs Fed',
                                'Scatter Metro Houston top & bottom tier vs Fed',
                                'Scatter Metro Las Vegas top & bottom tier vs Fed',
                                'Scatter Metro Los Angeles top & bottom tier vs Fed',
                                'Scatter Metro NYC top & bottom tier vs Fed',
                                'Scatter Metro SD top & bottom tier vs Fed',
                                'seaborn Metro 1BR vs Fed',
                                'seaborn Metro 2BR vs Fed',
                                'seaborn Metro 3BR vs Fed',
                                'seaborn Metro 4BR vs Fed',
                                'seaborn Metro 5BR vs Fed',
                                'seaborn Metro Bottom vs Fed',
                                'seaborn Metro Cities smoothed vs Fed Balance Sheet',
                                'seaborn Metro Cities smoothed vs Rates offset 3 years',
                                'seaborn Metro top_tier vs Fed'
                               )
                              )
    
if (plot_choice == 'Line S&P vs Fed Balance Sheet Normalized'):
    st.image('Plots/Line S&P vs Fed Balance Sheet Normalized.png')
elif (plot_choice == "Rates vs Fed"):
    st.image('Plots/Rates vs Fed.png')       
elif (plot_choice == "Combined scatter Metro Top & Bottom vs Fed"):
    st.image('Plots/Combined scatter Metro Top & Bottom vs Fed.png')
elif (plot_choice == "Corporate Liquidity vs Fed Balance Sheet"):
     st.image('Plots/Corporate Liquidity vs Fed Balance Sheet.png')
elif (plot_choice == "Line Cities smoothed vs Fed Balance Sheet Normalized"):
     st.image('Plots/Line Cities smoothed vs Fed Balance Sheet Normalized.jpg')
elif (plot_choice == "Line Home Values vs Fed Balance Sheet Normalized"):
     st.image('Plots/Line Home Values vs Fed Balance Sheet Normalized.jpg')
elif (plot_choice == "Line S&P vs Fed Balance Sheet Normalized"):
     st.image('Plots/Line S&P vs Fed Balance Sheet Normalized.png')
elif (plot_choice == "Scatter Metro Chicago top & bottom tier vs Fed"):
     st.image('Plots/Scatter Metro Chicago top & bottom tier vs Fed.jpg')
elif (plot_choice == "Scatter Metro Houston top & bottom tier vs Fed"):
     st.image('Plots/Scatter Metro Houston top & bottom tier vs Fed.jpg')
elif (plot_choice == "Scatter Metro Las Vegas top & bottom tier vs Fed"):
     st.image('Plots/Scatter Metro Las Vegas top & bottom tier vs Fed.jpg')
elif (plot_choice == "Scatter Metro Los Angeles top & bottom tier vs Fed"):
     st.image('Plots/Scatter Metro Los Angeles top & bottom tier vs Fed.jpg')
elif (plot_choice == "Scatter Metro NYC top & bottom tier vs Fed"):
     st.image('Plots/Scatter Metro NYC top & bottom tier vs Fed.jpg')
elif (plot_choice == "Scatter Metro SD top & bottom tier vs Fed"):
     st.image('Plots/Scatter Metro SD top & bottom tier vs Fed.jpg')
elif (plot_choice == "Scatter Zip Code Income vs. Home Value Percentage Gain (2000-2007)"):
     st.image('Plots/Scatter Zip Code Income vs. Home Value Percentage Gain (2000-2007).png')
elif (plot_choice == "Scatter Zip Code Income vs. Home Value Percentage Gain (2007-2012)"):
     st.image('Plots/Scatter Zip Code Income vs. Home Value Percentage Gain (2007-2012).png')
elif (plot_choice == "Scatter Zip Code Income vs. Home Value Percentage Gain (2012-2022)"):
     st.image('Plots/Scatter Zip Code Income vs. Home Value Percentage Gain (2012-2022).png')
elif (plot_choice == "Scatter Zip Code Income vs. Home Value Percentage Gain (2022-2023)"):
     st.image('Plots/Scatter Zip Code Income vs. Home Value Percentage Gain (2022-2023).png')
elif (plot_choice == "seaborn Metro 1BR vs Fed"):
     st.image('Plots/seaborn Metro 1BR vs Fed.png')
elif (plot_choice == "seaborn Metro 2BR vs Fed"):
     st.image('Plots/seaborn Metro 2BR vs Fed.png')
elif (plot_choice == "seaborn Metro 3BR vs Fed"):
     st.image('Plots/seaborn Metro 3BR vs Fed.png')
elif (plot_choice == "seaborn Metro 4BR vs Fed"):
     st.image('Plots/seaborn Metro 4BR vs Fed.png')
elif (plot_choice == "seaborn Metro 5BR vs Fed"):
     st.image('Plots/seaborn Metro 5BR vs Fed.png')
elif (plot_choice == "seaborn Metro Bottom vs Fed"):
     st.image('Plots/seaborn Metro Bottom vs Fed.png')
elif (plot_choice == "seaborn Metro Cities smoothed vs Fed Balance Sheet"):
     st.image('Plots/seaborn Metro Cities smoothed vs Fed Balance Sheet.png')
elif (plot_choice == "seaborn Metro Cities smoothed vs Rates offset 3 years"):
     st.image('Plots/seaborn Metro Cities smoothed vs Rates offset 3 years.png')
elif (plot_choice == "seaborn Metro top_tier vs Fed"):
     st.image('Plots/seaborn Metro top_tier vs Fed.png')
elif (plot_choice == "Tableau GFC Avg Loss"):
     st.image('Plots/Tableau GFC Avg Loss.png')
elif (plot_choice == "Tableau Pre-GFC Avg Gain"):
     st.image('Plots/Tableau Pre-GFC Avg Gain.png')
elif (plot_choice == "Tableau QE Avg Gain"):
     st.image('Plots/Tableau QE Avg Gain.png')
elif (plot_choice == "Tableau QT Avg Gain"):
     st.image('Plots/Tableau QT Avg Gain.png')
elif (plot_choice == "Top vs Bottom Cities"):
     st.image('Plots/Top vs Bottom Cities.png')
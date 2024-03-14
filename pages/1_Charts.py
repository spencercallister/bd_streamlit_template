import streamlit as st
import polars as pl

st.set_page_config(page_title="Charts")

st.title('[Charts](https://docs.streamlit.io/library/api-reference/charts)')

st.header('Stack Overflow Developer Survey Data')

@st.cache_data
def get_survey_data():
    return pl.read_parquet('./data/survey_results_public.parquet')\
            .drop_nulls(subset=['YearsCodePro', 'ConvertedCompYearly'])\
            .with_columns(
                pl.col('YearsCode').replace({'Less than 1 year': 0, 'More than 50 years': 50}).cast(pl.Int32),
                pl.col('YearsCodePro').replace({'Less than 1 year': 0, 'More than 50 years': 50}).cast(pl.Int32),
            )\
            .sort('YearsCodePro')

df = get_survey_data()

st.dataframe(df.head())

# TODO: create a visualization using `st.area_chart`, `st.bar_chart`, `st.line_chart`, `st.scatter_chart` using the above data. See docs at https://docs.streamlit.io/library/api-reference/charts

# If you need an idea, you can compare salary to number of years of professional experience

st.scatter_chart(data=df, x='ConvertedCompYearly', y='WorkExp')
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv("my_app/data/hofstede.csv")

imp_1 = {
    "Method (ivr)": ["KNN Imputation", "Mean Imputation"],
    "MAE": [14.451, 19.428],
    "RMSE": [18.422, 23.225],
    "R-Squared": [0.371, 0]
}

imp_2 = {
    "Method (lto)": ["KNN Imputation", "Mean Imputation"],
    "MAE": [13.919, 17.5],
    "RMSE": [18.546, 21.198],
    "R-Squared": [0.234, 0]
}

imp_3 = {
    "Method (ivr)": ["KNN Imputation", "Mean Imputation"],
    "MAE": [15.783, 19.428],
    "RMSE": [20.538, 23.225],
    "R-Squared": [0.218, 0]
}

imp_1 = pd.DataFrame(imp_1)
imp_2 = pd.DataFrame(imp_2)
imp_3 = pd.DataFrame(imp_3)

st.title("Hofstede’s Cultural Dimensions")

df_cluster = pd.read_csv("my_app/data/hofstede_clusters.csv")
df_cluster = (
    df_cluster
    .drop(columns=['Cluster'])
    .rename(columns={'Cluster_Name': 'Cluster'})
    .copy()
)
cluster_colors = {
    'Individualistic and Egalitarian': '#0072B2',  # Blue
    'Structured and Hierarchical': '#9467BD',      # Purple
    'Traditional in the Moment': '#E69F00',        # Orange
    'Traditional and Restrained': '#C00000'        # Red
}
# Create world map
fig = px.choropleth(
    df_cluster,
    locations='country',
    locationmode='country names',
    color='Cluster',
    hover_name='country',
    hover_data={
        'Cluster': True,
        'idv': ':.0f',
        'mas': ':.0f',
        'uai': ':.0f',
        'lto': ':.0f',
        'ivr': ':.0f',
        'pdi': ':.0f',
        'country': False
    },
    color_discrete_map=cluster_colors,
    category_orders={
        'Cluster': [
            'Individualistic and Egalitarian',
            'Structured and Hierarchical',
            'Traditional in the Moment',
            'Traditional and Restrained'
        ]
    }
)

# Map appearance
fig.update_geos(
    projection_type='natural earth',
    center=dict(lon=0, lat=0),
    showcoastlines=True,
    coastlinecolor='black',
    showland=True,
    landcolor='lightgray',
    showcountries=True,
    countrycolor='white'
)

# Layout
# Layout
fig.update_layout(
    legend_title_text='Cultural Clusters',
    height=500,

)

# Display map with a border around the entire figure
with st.container(border=True):
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={'displayModeBar': True}
    )

st.subheader("What is it?")
st.write("Geert Hofstede and colleagues developed six dimensions of culture and applied them to each country with scores ranging between 0 to 100. It is important to note that these scores are national averages obtained from samples, meaning that within each country there is variation. Despite this, it is still a good indicator of cultural values.")
st.markdown("""
- **idv (Individualism)**
    - A lower value indicates a more collectivist society.
    - A higher value indicates a more individualistic society.
- **pdi (Power Distance)**
    - A lower value indicates a society that is less likely to accept unequally distributed power.
    - A higher value indicates a society that is more likely to accept unequally distributed power.
- **mas (Masculinity)**
    - A lower value indicates a society that embraces more stereotypically feminine traits (e.g., nurturing).
    - A higher value indicates a society that embraces more stereotypically masculine traits (e.g., competition and achievement).
- **uai (Uncertainty Avoidance)**
    - A lower value indicates a society that is less tolerant of uncertainty and ambiguity.
    - A higher value indicates a society that is more tolerant of uncertainty and ambiguity.
- **lto (Long Term Orientation)**
    - A lower value indicates a society that focuses more on the past and present.
    - A higher value indicates a society that focuses more on the future.
- **ivr (Indulgence vs. Restraint)**
    - A lower value indicates a society based on duty and restraint.
    - A higher value indicates a society based on individual gratification.
""")

st.subheader("Examining the Data")
st.write("The dataset contains 119 countries (rows) with no duplicates. The variables are country, pdi, idv, mas, uai, lto, and ivr. 99 countries have complete data, 10 countries are missing only ivr, and another 10 countries are missing both lto and ivr.")

st.subheader("Imputing the Missing Data")
st.write("Many methods of imputation were attempted, including mean, regression, and other machine learning based methods. The strongest and most interpretable method of imputation was found to be KNN, which had stronger metrics than even XGBoost. The model was trained on the 99 countries with no missing data and evaluated on the same dataset using LOOCV due to the small training size.")
st.write("For the country's missing only ivr, there were 5 possible predictors: pdi, idv, mas, uai, and lto. All combinations of predictors were tried and all were used in KNN. The k value was found to be 5 through an elbow plot. The R² of 0.371 while weak, still showed an improved over mean imputation.")
st.table(imp_1)
st.write("For the country's missing both lto and ivr, I independently imputed each rather than use an imputed variable as an input to another due to it's poor metrics and possibility of error propagation. To predict lto, there were 4 possible predictors: pdi, idv, mas, and uai. The variable mas was excluded and a k value of 5 was found to have an R² of 0.234. To predict ivr, there were the same 4 predictors available with only mas and idv included with a k value of 6 and R² of 0.218.")
st.table(imp_2)
st.table(imp_3)


st.subheader("Exploratory Data Analysis")
st.write("Most cultural dimensions have weak to nearly non-existent correlations. An exception is idv and pdi with a correlation of -0.6. This negative association suggests that more individualistic societies tend to have stronger hierarchies. Another moderately strong correlation of 0.58 is found between idv and lto. This positive association suggests more individualistic societies tend to think longer term. While these associations are interesting, it is important to note that correlation does not equal causation.")

corr_matrix = df.corr(numeric_only=True)

fig, ax = plt.subplots(figsize=(6, 5), dpi=200)

im = ax.imshow(
    corr_matrix,
    cmap='coolwarm',
    vmin=-1,
    vmax=1
)

fig.colorbar(im, ax=ax, label='Correlation')

# Axis labels
ax.set_xticks(range(len(corr_matrix.columns)))
ax.set_xticklabels(
    corr_matrix.columns,
    rotation=45,
    ha='right'
)

ax.set_yticks(range(len(corr_matrix.columns)))
ax.set_yticklabels(corr_matrix.columns)

# Correlation values
for i in range(len(corr_matrix.columns)):
    for j in range(len(corr_matrix.columns)):
        ax.text(
            j, i,
            f'{corr_matrix.iloc[i, j]:.2f}',
            ha='center',
            va='center',
            color='black'
        )

ax.set_title('Correlation Matrix')

fig.tight_layout()

# Display in Streamlit
st.pyplot(fig, width=500)

plt.close(fig)

plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()
variables = ['pdi', 'idv', 'mas', 'uai', 'lto', 'ivr']

st.write("The distributions of the six cultural dimensions do not appear to follow a normal distribution, exhibiting varying degrees of skewness and dispersion.")

# Create two rows with three columns each
for i in range(0, len(variables), 3):

    cols = st.columns(3)

    for col, var in zip(cols, variables[i:i+3]):

        data = df[var].dropna()

        mean = data.mean()
        std = data.std()

        with col:
            fig, ax = plt.subplots(figsize=(4, 3), dpi=150)

            ax.hist(data, bins=15, edgecolor='black', alpha=0.75)

            ax.axvline(mean, color='red', linestyle='--',
                       label=f'Mean: {mean:.2f}')

            ax.set_title(var.upper())
            ax.set_xlabel("Value")
            ax.set_ylabel("Frequency")
            ax.legend(fontsize=8)

            fig.tight_layout()

            st.pyplot(fig, width="content")
            plt.close(fig)

            st.caption(
                f"Mean: **{mean:.2f}** | Std: **{std:.2f}** | n = {len(data)}"
            )

st.subheader("Clustering Methods")
st.write("Hierarchical clustering with Ward's linkage will be used. This allows us to minimize within cluster variance and allow us to choose the number of clusters without specifying it beforehand.")
import streamlit as st
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Cache Ward linkage calculation
@st.cache_data
def calculate_linkage(X):
    return linkage(X, method='ward')

# Generate Ward linkage matrix
X = df[['ivr', 'lto', 'uai', 'mas', 'idv', 'pdi']]
Z = calculate_linkage(X.to_numpy())

# Plot dendrogram
fig, ax = plt.subplots(figsize=(12, 6))

dendrogram(
    Z,
    color_threshold=0,
    above_threshold_color='black',
    labels=df['country'].astype(str).tolist(),
    leaf_rotation=90,
    leaf_font_size=8,
    ax=ax
)

ax.set_title("Hierarchical Clustering - Ward's Linkage")
ax.set_xlabel("Observations / Clusters")
ax.set_ylabel("Ward Linkage Distance")

plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)
plt.close(fig)
st.write("There are 119 country's so the number of clusters must be chosen so that there are not too little or too many clusters. Based on the dendrogram, four clusters appear to be an appropriate amount and each cluster is roughly equal in size.")
dendrogram(
    Z,
    above_threshold_color='black',
    labels=df['country'].astype(str).tolist(),
    leaf_rotation=90,
    leaf_font_size=8,
    ax=ax
)

ax.set_title("Hierarchical Clustering - Ward's Linkage")
ax.set_xlabel("Observations / Clusters")
ax.set_ylabel("Ward Linkage Distance")
plt.tight_layout()

# Display in Streamlit
st.pyplot(fig)
plt.close(fig)

st.write("In order to give these clusters interpretable names, we must first investigate their distributions.")
import streamlit as st
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import fcluster

# Assign clusters
n_clusters = 4

df['Cluster'] = fcluster(
    Z,
    t=n_clusters,
    criterion='maxclust'
)

# Assign cluster names
df['Cluster_Name'] = df['Cluster'].map({
    1: 'Individualistic and Egalitarian',
    2: 'Structured and Hierarchical',
    3: 'Traditional in the Moment',
    4: 'Traditional and Restrained'
})

# Cluster descriptions
descriptions = {
    1: 'Cluster 1 is relatively balanced across all dimensions but exhibits above average individualism. Combined with relatively low power distance, these countries tend to embrace more egalitarian and individualistic cultural values.',

    2: 'Cluster 2 exhibits very high uncertainty avoidance, high power distance, and relatively low indulgence. These characteristics are associated with more rigid and socially stratified societies.',

    3: 'Cluster 3 exhibits low individualism, high uncertainty avoidance, and high power distance, suggesting a stronger emphasis on traditional values. Combined with very low long term orientation and high indulgence, these characteristics suggest a preference for immediate gratification over long term planning.',

    4: 'Cluster 4 is quite similar to Cluster 3, with the main exception being lower indulgence. This suggests a more restrained approach to enjoying life and expressing desires.'
}

variables = ['ivr', 'lto', 'uai', 'mas', 'idv', 'pdi']

# Display clusters
for cluster in sorted(df['Cluster'].dropna().unique()):

    cluster_data = df[df['Cluster'] == cluster]

    cluster_name = cluster_data['Cluster_Name'].iloc[0]

    with st.expander(
        f"Cluster {cluster}: {cluster_name} ({len(cluster_data)} countries)",
        expanded=False
    ):

        # Histograms
        fig, axes = plt.subplots(2, 3, figsize=(15, 9))
        axes = axes.flatten()

        for i, col in enumerate(variables):

            values = cluster_data[col].dropna()
            mean_value = values.mean()

            axes[i].hist(
                values,
                bins=10,
                color='steelblue',
                edgecolor='black',
                alpha=0.75
            )

            axes[i].axvline(
                mean_value,
                color='red',
                linestyle='--',
                linewidth=2,
                label=f'Mean = {mean_value:.2f}'
            )

            axes[i].set_title(col.upper())
            axes[i].set_xlabel('Score')
            axes[i].set_ylabel('Frequency')
            axes[i].legend()
            axes[i].grid(axis='y', alpha=0.3)

        fig.suptitle(
            f'Hofstede Dimensions - Cluster {cluster}',
            fontsize=16
        )

        fig.tight_layout()

        st.pyplot(fig, use_container_width=True)
        plt.close(fig)

        # Cluster interpretation
        st.markdown("#### Interpretation")
        st.write(descriptions[cluster])

        st.markdown(f"#### {cluster_name} Countries")

        # Display country dataframe
        cluster_df = (
            cluster_data
            .drop(columns=['Cluster'])
            .rename(columns={'Cluster_Name': 'cluster'})
        )

        st.dataframe(
            cluster_df,
            use_container_width=True,
            height=200,
            hide_index=True
        )


st.subheader("Sources")
st.write("https://www.kaggle.com/datasets/seydakaba/hofstede-cultural-dimensions-by-country/data")
st.write("https://geerthofstede.com/culture-geert-hofstede-gert-jan-hofstede/6d-model-of-national-culture/")
st.write("https://www.andrews.edu/~tidwell/bsad560/HofstedeMasculinity.html")
import os
import pandas as pd
import streamlit as st

from src.preprocessing import NewsPreprocessor
from src.entities import EntityExtractor
from src.topics import TopicAnalyzer
from src.sentiment import SentimentAnalyzer
from src.keywords import KeywordExtractor
from src.analysis import NewsAnalyzer
from src.categorization import NewsCategorizer
from src.reports import ReportGenerator
from src.visualization import NewsVisualizer


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="News Intelligence System",
    page_icon="📰",
    layout="wide"
)


# =========================================================
# HEADER
# =========================================================

st.title("📰 News Intelligence System")

st.caption(
    "Newspaper Information Extraction and Analytics Platform"
)

st.markdown("---")


# =========================================================
# PATHS
# =========================================================

DATA_PATH = "data/Kosovo-News-Articles.csv"
OUTPUT_FOLDER = "output"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


# =========================================================
# CHECK DATASET
# =========================================================

if not os.path.exists(DATA_PATH):

    st.error(
        "Dataset not found.\n\n"
        "Make sure Kosovo-News-Articles.csv is inside "
        "the data folder."
    )

    st.stop()


# =========================================================
# READ SMALL PREVIEW ONLY
# =========================================================

try:

    preview_df = pd.read_csv(
        DATA_PATH,
        nrows=20,
        usecols=[
            "content",
            "date",
            "title",
            "category",
            "author",
            "source",
            "fetched_at"
        ],
        low_memory=False
    )

except Exception as error:

    st.error(
        f"Unable to read the dataset: {error}"
    )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📰 News Explorer")

st.sidebar.success(
    "Dataset loaded successfully"
)

st.sidebar.markdown("---")

st.sidebar.write(
    "Large Dataset Mode"
)

st.sidebar.info(
    "The dataset is approximately 8.6 GB. "
    "The system analyzes only the number of "
    "articles you select instead of loading "
    "the complete dataset into memory."
)


# =========================================================
# DATASET OVERVIEW
# =========================================================

st.subheader("📊 Dataset Overview")


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "📄 Preview Articles",
    len(preview_df)
)


col2.metric(
    "📋 Columns",
    len(preview_df.columns)
)


col3.metric(
    "📝 Text Column",
    "content"
)


col4.metric(
    "💾 Dataset",
    "8.6 GB"
)


# =========================================================
# DATASET PREVIEW
# =========================================================

st.markdown("---")

st.subheader("🔎 Newspaper Dataset Preview")

st.dataframe(
    preview_df,
    use_container_width=True,
    height=350
)


# =========================================================
# ANALYSIS SETTINGS
# =========================================================

st.markdown("---")

st.subheader("⚙️ Analysis Settings")


sample_size = st.select_slider(
    "Number of newspaper articles to analyze",
    options=[
        10,
        20,
        50,
        100,
        200,
        300,
        500
    ],
    value=50
)


st.info(
    f"The system will analyze {sample_size} articles "
    "from the large newspaper dataset."
)


# =========================================================
# START BUTTON
# =========================================================

analyze = st.button(
    "🚀 Start News Analysis",
    use_container_width=True
)


# =========================================================
# ANALYSIS PIPELINE
# =========================================================

if analyze:

    progress = st.progress(0)

    status = st.empty()


    # -----------------------------------------------------
    # LOAD SELECTED ARTICLES
    # -----------------------------------------------------

    status.info(
        f"Loading {sample_size} newspaper articles..."
    )

    preprocessor = NewsPreprocessor(
        DATA_PATH
    )

    df = preprocessor.load_data(
        number_of_articles=sample_size
    )

    progress.progress(10)


    # -----------------------------------------------------
    # PREPROCESSING
    # -----------------------------------------------------

    status.info(
        "Cleaning and preprocessing newspaper articles..."
    )

    cleaned_data = preprocessor.process()

    texts = cleaned_data[
        "clean_text"
    ].tolist()

    progress.progress(20)


    # -----------------------------------------------------
    # NAMED ENTITY EXTRACTION
    # -----------------------------------------------------

    status.info(
        "Extracting people, places and organizations..."
    )

    entity_extractor = EntityExtractor()

    entities = entity_extractor.extract_entities(
        texts
    )

    progress.progress(35)


    # -----------------------------------------------------
    # TOPIC ANALYSIS
    # -----------------------------------------------------

    status.info(
        "Discovering major news topics..."
    )

    topic_analyzer = TopicAnalyzer(
        number_of_topics=5,
        keywords_per_topic=8
    )

    topics = topic_analyzer.analyze(
        texts
    )

    progress.progress(50)


    # -----------------------------------------------------
    # SENTIMENT ANALYSIS
    # -----------------------------------------------------

    status.info(
        "Analyzing newspaper sentiment..."
    )

    sentiment_analyzer = SentimentAnalyzer()

    sentiment = sentiment_analyzer.analyze_articles(
        texts
    )

    progress.progress(65)


    # -----------------------------------------------------
    # KEYWORD EXTRACTION
    # -----------------------------------------------------

    status.info(
        "Extracting important keywords..."
    )

    keyword_extractor = KeywordExtractor(
        max_keywords=20
    )

    keywords = keyword_extractor.extract(
        texts
    )

    progress.progress(75)


    # -----------------------------------------------------
    # NEWS CATEGORIZATION
    # -----------------------------------------------------

    status.info(
        "Categorizing newspaper articles..."
    )

    categorizer = NewsCategorizer()

    categories = categorizer.categorize(
        texts
    )

    progress.progress(85)


    # -----------------------------------------------------
    # STATISTICS
    # -----------------------------------------------------

    status.info(
        "Generating newspaper statistics..."
    )

    analyzer = NewsAnalyzer()

    statistics = analyzer.generate_statistics(
        cleaned_data,
        entities,
        topics,
        sentiment,
        keywords
    )

    statistics[
        "articles_analyzed"
    ] = sample_size

    progress.progress(90)


    # -----------------------------------------------------
    # SAVE REPORTS
    # -----------------------------------------------------

    status.info(
        "Saving analysis results..."
    )

    report_generator = ReportGenerator(
        OUTPUT_FOLDER
    )

    saved_files = report_generator.save_all(
        cleaned_data=cleaned_data,
        entities=entities,
        topics=topics,
        sentiment=sentiment,
        keywords=keywords,
        categories=categories,
        statistics=statistics
    )


    # -----------------------------------------------------
    # VISUALIZATION
    # -----------------------------------------------------

    status.info(
        "Generating charts..."
    )

    visualizer = NewsVisualizer(
        OUTPUT_FOLDER
    )

    visualizer.sentiment_chart(
        sentiment
    )

    visualizer.category_chart(
        categories
    )

    visualizer.entity_chart(
        entities
    )

    visualizer.keyword_chart(
        keywords
    )


    progress.progress(100)

    status.success(
        "News analysis completed successfully! ✅"
    )


    # =====================================================
    # DASHBOARD
    # =====================================================

    st.markdown("---")

    st.header(
        "📊 News Intelligence Dashboard"
    )


    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(
        [
            "📄 Articles",
            "👤 Entities",
            "🧠 Topics",
            "😊 Sentiment",
            "🔑 Keywords",
            "🗂 Categories",
            "📈 Statistics"
        ]
    )


    # =====================================================
    # ARTICLES
    # =====================================================

    with tab1:

        st.subheader(
            "📄 Processed Newspaper Articles"
        )

        st.dataframe(
            cleaned_data,
            use_container_width=True,
            height=450
        )

        st.download_button(
            "⬇️ Download Processed Articles",
            cleaned_data.to_csv(
                index=False
            ),
            "processed_articles.csv",
            "text/csv"
        )


    # =====================================================
    # ENTITIES
    # =====================================================

    with tab2:

        st.subheader(
            "👤 Named Entities"
        )

        if entities.empty:

            st.warning(
                "No named entities were detected."
            )

        else:

            st.dataframe(
                entities,
                use_container_width=True,
                height=450
            )

            st.download_button(
                "⬇️ Download Entities",
                entities.to_csv(
                    index=False
                ),
                "entities.csv",
                "text/csv"
            )


    # =====================================================
    # TOPICS
    # =====================================================

    with tab3:

        st.subheader(
            "🧠 Major News Topics"
        )

        if topics.empty:

            st.warning(
                "No topics could be detected."
            )

        else:

            st.dataframe(
                topics,
                use_container_width=True
            )

            topic_summary = (
                topic_analyzer.get_summary(
                    topics
                )
            )

            st.markdown(
                "### Topic Summary"
            )

            st.dataframe(
                topic_summary,
                use_container_width=True
            )

            st.download_button(
                "⬇️ Download Topics",
                topics.to_csv(
                    index=False
                ),
                "topics.csv",
                "text/csv"
            )


    # =====================================================
    # SENTIMENT
    # =====================================================

    with tab4:

        st.subheader(
            "😊 Sentiment Analysis"
        )

        sentiment_summary = (
            sentiment_analyzer.get_summary(
                sentiment
            )
        )

        st.dataframe(
            sentiment,
            use_container_width=True
        )

        st.markdown(
            "### Sentiment Summary"
        )

        st.dataframe(
            sentiment_summary,
            use_container_width=True
        )

        st.download_button(
            "⬇️ Download Sentiment",
            sentiment.to_csv(
                index=False
            ),
            "sentiment.csv",
            "text/csv"
        )


    # =====================================================
    # KEYWORDS
    # =====================================================

    with tab5:

        st.subheader(
            "🔑 Important Keywords"
        )

        st.dataframe(
            keywords,
            use_container_width=True
        )

        st.download_button(
            "⬇️ Download Keywords",
            keywords.to_csv(
                index=False
            ),
            "keywords.csv",
            "text/csv"
        )


    # =====================================================
    # CATEGORIES
    # =====================================================

    with tab6:

        st.subheader(
            "🗂 News Categories"
        )

        category_summary = (
            categorizer.get_summary(
                categories
            )
        )

        st.dataframe(
            categories,
            use_container_width=True
        )

        st.markdown(
            "### Category Summary"
        )

        st.dataframe(
            category_summary,
            use_container_width=True
        )

        st.download_button(
            "⬇️ Download Categories",
            categories.to_csv(
                index=False
            ),
            "categories.csv",
            "text/csv"
        )


    # =====================================================
    # STATISTICS
    # =====================================================

    with tab7:

        st.subheader(
            "📈 Newspaper Statistics"
        )

        stats_columns = st.columns(3)

        items = list(
            statistics.items()
        )

        for index, (key, value) in enumerate(
            items
        ):

            with stats_columns[
                index % 3
            ]:

                st.metric(
                    str(key)
                    .replace("_", " ")
                    .title(),
                    value
                )


        st.markdown("---")

        st.subheader(
            "📋 Detailed Statistics"
        )

        statistics_df = pd.DataFrame(
            [
                {
                    "Metric": (
                        str(key)
                        .replace("_", " ")
                        .title()
                    ),
                    "Value": value
                }
                for key, value in statistics.items()
            ]
        )

        st.dataframe(
            statistics_df,
            use_container_width=True
        )

        st.download_button(
            "⬇️ Download Statistics",
            statistics_df.to_csv(
                index=False
            ),
            "statistics.csv",
            "text/csv"
        )


    # =====================================================
    # OUTPUT FILES
    # =====================================================

    st.markdown("---")

    st.subheader(
        "📁 Generated Output Files"
    )

    for name, path in saved_files.items():

        st.write(
            f"✅ {name}: `{path}`"
        )


else:

    st.markdown("---")

    st.info(
        "👆 Select the number of articles and "
        "click **Start News Analysis** to begin."
    )
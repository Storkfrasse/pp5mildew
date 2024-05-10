import streamlit as st

def page_project_hypotheses_body():
    st.write("## Project Hypotheses")

    st.write("### Model Can be Created from Visual Differences")
    st.success(
        """*Hypothesis*: Cherry leaves with and without powdery mildew 
        will have significant visual differences allowing classification by 
        a neural network."""
    )
    st.write(
        """Visual inspection shows powdery mildew leaves tend to have white spots. 
        A model achieved over 97% accuracy in distinguishing them."""
    )

    st.write("---")

    st.write("### Greater Variabilty in Powdery Mildew Leaf Images")
    st.success(
        "*Hypothesis*: Powdery mildew leaf images will have greater color variability."
    )
    st.write(
        """Analysis suggests greater variability between powdery mildew leaf images 
        compared to healthy ones, but within-image variability was inconclusive."""
    )

    st.write("---")

    st.write("### Higher Leaf Proportion and Thus Greater Variabilty in Central Portion of Powdery Mildew Leaf Images")
    st.success(
        """*Hypothesis*: Central portions of powdery mildew leaf images will 
        display greater variability."""
    )
    st.write(
        """Restricting analysis to central portions showed increased variability 
        in powdery mildew leaf images, supporting the hypothesis, though not 
        conclusively."""
    )
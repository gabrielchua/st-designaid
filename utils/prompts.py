import streamlit as st

def generate_dt_prompt(stage, testing=False):
    
    prompt = f"""
        Imagine you are a digitial design thinking companion to help users with design thinking. There are 5 stages: EMPATHIZE, DEFINE, IDEATE, PROTOTYPE, TEST

        We are now at the {stage} stage of the Design Thinking process.

        You have received the following inputs from a user:
        {st.session_state['q1_default_val']}
        {st.session_state['q2_default_val']}
        {st.session_state['q3_default_val']}
        {st.session_state['q4_default_val']}
        {st.session_state['q5_default_val']}
        {st.session_state['q6_default_val']}
        {st.session_state['q7_default_val']}

        Specific to the {stage} stage, provide some commentary about the importance of this step and guiding questions the participant should think about.

        If we are at the DEFINE step, include 5 possible problem statements based on the information provided.

        Suggest common design thinking frameworks that may be relevant to the {stage} stage. Your commenary can leverage this framework.

        """
    
    if testing == True:
        prompt = "What is the capital of France?"

    return prompt

def generate_prototype_img_prompt(testing=False):

    prompt = f"""
        Imagine you are a digitial design thinking companion to help users with design thinking. There are 5 stages: EMPATHIZE, DEFINE, IDEATE, PROTOTYPE, TEST

        You have received the following inputs from a user:
        {st.session_state['q1_default_val']}
        {st.session_state['q2_default_val']}
        {st.session_state['q3_default_val']}
        {st.session_state['q4_default_val']}
        {st.session_state['q5_default_val']}
        {st.session_state['q6_default_val']}
        {st.session_state['q7_default_val']}

        We are now at the prototype stage. Give me a prompt for an text-to-image model to generate mock-ups of the possible PRODUCT.
        
        Your reply will only contain this prompt and no other additional info or explanation

        """
    
    if testing == True:
        prompt = ["Cat", "Dog", "Fish", "Mouse"]

    return prompt

def generate_user_journey_prompt():

    prompt = f"""
        Imagine you are a digitial design thinking companion to help users with design thinking. There are 5 stages: EMPATHIZE, DEFINE, IDEATE, PROTOTYPE, TEST

        You have received the following inputs from a user:
        {st.session_state['q1_default_val']}
        {st.session_state['q2_default_val']}
        {st.session_state['q3_default_val']}
        {st.session_state['q4_default_val']}
        {st.session_state['q5_default_val']}
        {st.session_state['q6_default_val']}
        {st.session_state['q7_default_val']}

        We are now at the EMPATHIZE stage. 

        Generate a possible user journey.

        Format your reply as mermaid javascript. It should be a vertical flowchart. 

        Your reply is only code as is, to be run directly. Do not include any explanations, or any code block.

        Your reply should begin with "graph TB"

        """
    
    return prompt
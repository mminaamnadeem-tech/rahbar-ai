import streamlit as st
from datetime import date

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Rahbar AI",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f7f9fc;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1200px;
}

.rahbar-header {
    padding: 1.5rem 2rem;
    border-radius: 18px;
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    color: white;
    margin-bottom: 1.5rem;
}

.rahbar-header h1 {
    margin: 0;
    font-size: 2.4rem;
}

.rahbar-header p {
    margin-top: 0.5rem;
    color: #dbeafe;
}

.section-title {
    font-size: 1.35rem;
    font-weight: 700;
    margin-top: 1.2rem;
    margin-bottom: 0.8rem;
    color: #0f172a;
}

.card {
    padding: 1.2rem;
    border-radius: 15px;
    background: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 1rem;
}

.decision-yes {
    padding: 1.2rem;
    border-radius: 15px;
    background: #ecfdf5;
    border: 1px solid #10b981;
}

.decision-no {
    padding: 1.2rem;
    border-radius: 15px;
    background: #fef2f2;
    border: 1px solid #ef4444;
}

.decision-conditional {
    padding: 1.2rem;
    border-radius: 15px;
    background: #fffbeb;
    border: 1px solid #f59e0b;
}

.decision-pending {
    padding: 1.2rem;
    border-radius: 15px;
    background: #eff6ff;
    border: 1px solid #3b82f6;
}

.small-muted {
    color: #64748b;
    font-size: 0.9rem;
}

.trace {
    font-family: monospace;
    background: #0f172a;
    color: #e2e8f0;
    padding: 1rem;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "asked" not in st.session_state:
    st.session_state.asked = False

if "query" not in st.session_state:
    st.session_state.query = ""

if "decision" not in st.session_state:
    st.session_state.decision = "NOT_YET_VERIFIED"

if "reason" not in st.session_state:
    st.session_state.reason = "Ask a question to get a Rahbar AI decision."


# =========================================================
# HEADER
# SECTION 1
# =========================================================

st.markdown("""
<div class="rahbar-header">
    <h1>🧭 Rahbar AI</h1>
    <p>AI-powered university admission guidance for students</p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.header("Rahbar AI")

    st.write(
        "Enter your academic profile and ask an admission-related question."
    )

    st.divider()

    st.caption("UI Prototype")
    st.caption("Agent integration can be connected later.")


# =========================================================
# SECTION 2 — STUDENT PROFILE
# =========================================================

st.markdown(
    '<div class="section-title">2. Student Profile</div>',
    unsafe_allow_html=True
)

with st.container():

    col1, col2 = st.columns(2)

    with col1:

        ssc_marks = st.number_input(
            "SSC Marks (%)",
            min_value=0.0,
            max_value=100.0,
            value=80.0,
            step=0.1
        )

        hssc_marks = st.number_input(
            "HSSC Marks (%)",
            min_value=0.0,
            max_value=100.0,
            value=75.0,
            step=0.1
        )

    with col2:

        hssc_group = st.selectbox(
            "HSSC Group",
            [
                "Pre-Engineering",
                "Pre-Medical",
                "Computer Science",
                "General Science",
                "Commerce",
                "Arts",
                "Other"
            ]
        )

        entry_test = st.number_input(
            "Entry Test Score (%)",
            min_value=0.0,
            max_value=100.0,
            value=70.0,
            step=0.1
        )


# =========================================================
# SECTION 3 — QUERY BOX
# =========================================================

st.markdown(
    '<div class="section-title">3. Ask Rahbar AI</div>',
    unsafe_allow_html=True
)

query = st.text_area(
    "Your question",
    placeholder=(
        "Example: Can I get admission in NUST BSCS with my marks?"
    ),
    height=120
)


# =========================================================
# SECTION 4 — ASK BUTTON
# =========================================================

st.markdown(
    '<div class="section-title">4. Ask</div>',
    unsafe_allow_html=True
)

ask_button = st.button(
    "🧭 Ask Rahbar AI",
    type="primary",
    use_container_width=True
)

if ask_button:

    if not query.strip():

        st.warning("Please enter a question first.")

    else:

        st.session_state.asked = True
        st.session_state.query = query

        # -------------------------------------------------
        # DEMO DECISION LOGIC
        # -------------------------------------------------
        #
        # This is temporary.
        # Later this section will call the actual agent.
        #

        q = query.lower()

        if "nust" in q or "net" in q:

            if entry_test >= 70 and ssc_marks >= 60 and hssc_marks >= 60:

                st.session_state.decision = "CONDITIONAL"

                st.session_state.reason = (
                    "Based on the profile entered, the student appears "
                    "to meet the basic academic conditions used in this "
                    "prototype. Final eligibility should be verified "
                    "against the current NUST admission rules."
                )

            else:

                st.session_state.decision = "NO"

                st.session_state.reason = (
                    "The entered academic profile does not satisfy the "
                    "basic thresholds used in this prototype."
                )

        else:

            st.session_state.decision = "NOT_YET_VERIFIED"

            st.session_state.reason = (
                "Rahbar could not verify this question against the "
                "connected admission documents yet."
            )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.asked:

    # =====================================================
    # SECTION 5 — DECISION CARD
    # =====================================================

    st.markdown(
        '<div class="section-title">5. Decision</div>',
        unsafe_allow_html=True
    )

    decision = st.session_state.decision
    reason = st.session_state.reason

    if decision == "YES":

        st.markdown(
            f"""
            <div class="decision-yes">
                <h2>✅ YES</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif decision == "NO":

        st.markdown(
            f"""
            <div class="decision-no">
                <h2>❌ NO</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif decision == "CONDITIONAL":

        st.markdown(
            f"""
            <div class="decision-conditional">
                <h2>⚠️ CONDITIONAL</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="decision-pending">
                <h2>🔎 NOT YET VERIFIED</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # SECTION 6 — CALCULATION
    # =====================================================

    st.markdown(
        '<div class="section-title">6. Calculation</div>',
        unsafe_allow_html=True
    )

    # NUST-style demo calculation
    # NET 75%, SSC 10%, HSSC 15%

    aggregate = (
        (entry_test * 0.75)
        + (ssc_marks * 0.10)
        + (hssc_marks * 0.15)
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Aggregate",
            f"{aggregate:.2f}%"
        )

    with col2:
        st.metric(
            "NET Contribution",
            f"{entry_test * 0.75:.2f}%"
        )

    with col3:
        st.metric(
            "Academic Contribution",
            f"{(ssc_marks * 0.10) + (hssc_marks * 0.15):.2f}%"
        )

    st.markdown("""
    <div class="card">

    <b>Formula</b>

    <br><br>

    Aggregate = (NET × 75%) + (SSC × 10%) + (HSSC × 15%)

    <br><br>

    <b>Entered Values</b>

    <br>

    NET = {:.2f}%

    <br>

    SSC = {:.2f}%

    <br>

    HSSC = {:.2f}%

    </div>
    """.format(
        entry_test,
        ssc_marks,
        hssc_marks
    ), unsafe_allow_html=True)


    # =====================================================
    # SECTION 7 — EVIDENCE
    # =====================================================

    st.markdown(
        '<div class="section-title">7. Evidence</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <b>📄 Source Document</b>

    <p>Admission Policy / University Information Document</p>

    <b>📖 Page</b>

    <p>To be verified by the connected document agent.</p>

    <b>🔗 Source URL</b>

    <p>To be connected.</p>

    <b>📅 Verification Date</b>

    <p>{}</p>

    </div>
    """.format(
        date.today().strftime("%d %B %Y")
    ), unsafe_allow_html=True)


    # =====================================================
    # SECTION 8 — ACTIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">8. What To Do Next</div>',
        unsafe_allow_html=True
    )

    actions = [
        "Verify the current admission requirements from the official university source.",
        "Check whether your selected degree accepts your HSSC group.",
        "Confirm the current entry-test requirement and deadline.",
        "Keep your academic documents ready for the application."
    ]

    for i, action in enumerate(actions, start=1):

        st.markdown(
            f"**{i}.** {action}"
        )


    # =====================================================
    # SECTION 9 — LIMITATIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">9. Limitations</div>',
        unsafe_allow_html=True
    )

    st.warning(
        "This prototype has not yet connected the university documents "
        "to the AI agent. Therefore, admission rules, deadlines and "
        "source pages must be verified before treating the answer as final."
    )


    # =====================================================
    # SECTION 10 — AGENT TRACE
    # =====================================================

    st.markdown(
        '<div class="section-title">10. Agent Trace</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="trace">

    [1] Receive student query

    [2] Read student academic profile

    [3] Identify university / admission topic

    [4] Search connected documents

    [5] Calculate aggregate

    [6] Verify admission condition

    [7] Generate decision

    [8] Return evidence + actions

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "Rahbar AI • Student Admission Guidance • UI Prototype"
)

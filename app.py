
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

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(59,130,246,0.10), transparent 30%),
        radial-gradient(circle at 90% 20%, rgba(99,102,241,0.10), transparent 30%),
        #f8fafc;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ========================================================
   HERO
======================================================== */

.hero {
    position: relative;
    overflow: hidden;
    padding: 2.5rem 2.8rem;
    border-radius: 28px;
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #172554 50%,
        #1e40af 100%
    );
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 20px 50px rgba(15,23,42,0.20);
    animation: fadeUp 0.7s ease;
}

.hero:before,
.hero:after {
    content: "";
    position: absolute;
    border-radius: 50%;
    background: rgba(255,255,255,0.07);
    animation: float 6s ease-in-out infinite;
}

.hero:before {
    width: 240px;
    height: 240px;
    right: -70px;
    top: -100px;
}

.hero:after {
    width: 150px;
    height: 150px;
    right: 180px;
    bottom: -100px;
    animation-delay: 1.5s;
}

.hero-content {
    position: relative;
    z-index: 2;
}

.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -1px;
}

.hero p {
    font-size: 1.05rem;
    color: #dbeafe;
    margin-top: 0.7rem;
    max-width: 700px;
}

/* ========================================================
   SECTION TITLES
======================================================== */

.section-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: #0f172a;
    margin-top: 1.8rem;
    margin-bottom: 0.8rem;
}

.section-subtitle {
    color: #64748b;
    margin-bottom: 1rem;
}

/* ========================================================
   CARDS
======================================================== */

.card {
    background: rgba(255,255,255,0.88);
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.35rem;
    box-shadow: 0 8px 30px rgba(15,23,42,0.06);
    transition: all 0.25s ease;
    animation: fadeUp 0.6s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 35px rgba(15,23,42,0.10);
}

/* ========================================================
   PROFILE LABEL
======================================================== */

.profile-label {
    font-weight: 700;
    color: #334155;
}

/* ========================================================
   BUTTON
======================================================== */

.stButton > button {
    border: none;
    border-radius: 14px;
    padding: 0.75rem 1rem;
    font-weight: 700;
    font-size: 1rem;
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    color: white;
    box-shadow: 0 8px 20px rgba(37,99,235,0.25);
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 28px rgba(37,99,235,0.35);
}

/* ========================================================
   DECISION CARDS
======================================================== */

.decision {
    padding: 1.6rem;
    border-radius: 22px;
    margin-bottom: 1rem;
    animation: popIn 0.55s ease;
}

.decision h2 {
    margin-top: 0;
    font-size: 1.7rem;
}

.decision p {
    margin-bottom: 0;
    line-height: 1.65;
}

.yes {
    background: linear-gradient(135deg, #ecfdf5, #f0fdf4);
    border: 1px solid #34d399;
}

.no {
    background: linear-gradient(135deg, #fef2f2, #fff1f2);
    border: 1px solid #fb7185;
}

.conditional {
    background: linear-gradient(135deg, #fffbeb, #fefce8);
    border: 1px solid #fbbf24;
}

.pending {
    background: linear-gradient(135deg, #eff6ff, #eef2ff);
    border: 1px solid #60a5fa;
}

/* ========================================================
   METRIC CARDS
======================================================== */

.metric-card {
    text-align: center;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.3rem;
    box-shadow: 0 8px 25px rgba(15,23,42,0.06);
    animation: fadeUp 0.6s ease;
}

.metric-number {
    font-size: 2rem;
    font-weight: 800;
    color: #2563eb;
}

.metric-label {
    color: #64748b;
    font-size: 0.9rem;
    margin-top: 0.2rem;
}

/* ========================================================
   EVIDENCE
======================================================== */

.evidence-card {
    background: white;
    border-left: 5px solid #2563eb;
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 7px 24px rgba(15,23,42,0.06);
    animation: fadeUp 0.6s ease;
}

.evidence-title {
    font-weight: 800;
    color: #0f172a;
}

.evidence-value {
    color: #475569;
    margin-bottom: 0.7rem;
}

/* ========================================================
   ACTIONS
======================================================== */

.action {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    transition: all 0.2s ease;
    animation: fadeUp 0.5s ease;
}

.action:hover {
    border-color: #93c5fd;
    transform: translateX(4px);
}

.action-number {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    background: #2563eb;
    color: white;
    font-weight: 800;
    margin-right: 10px;
}

/* ========================================================
   TRACE
======================================================== */

.trace {
    background: #0b1120;
    color: #cbd5e1;
    border-radius: 18px;
    padding: 1.4rem;
    font-family: monospace;
    line-height: 1.8;
    box-shadow: 0 10px 30px rgba(15,23,42,0.15);
    animation: fadeUp 0.6s ease;
}

.trace-green {
    color: #4ade80;
}

/* ========================================================
   FOOTER
======================================================== */

.footer {
    text-align: center;
    color: #64748b;
    padding-top: 2rem;
    font-size: 0.85rem;
}

/* ========================================================
   ANIMATIONS
======================================================== */

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes popIn {
    from {
        opacity: 0;
        transform: scale(0.96);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes float {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(20px);
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "asked" not in st.session_state:
    st.session_state.asked = False

if "decision" not in st.session_state:
    st.session_state.decision = "NOT_YET_VERIFIED"

if "reason" not in st.session_state:
    st.session_state.reason = ""

if "trace" not in st.session_state:
    st.session_state.trace = []


# =========================================================
# 1. HEADER
# =========================================================

st.markdown("""
<div class="hero">
    <div class="hero-content">
        <h1>🧭 Rahbar AI</h1>
        <p>
            Your intelligent admission guidance assistant.
            Enter your academic profile, ask a question, and get
            a clear, evidence-based response.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# 2. STUDENT PROFILE
# =========================================================

st.markdown(
    '<div class="section-title">01 — Student Profile</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Tell Rahbar about your academic background.</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    ssc_marks = st.number_input(
        "SSC Marks (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=0.1
    )

with col2:
    hssc_marks = st.number_input(
        "HSSC Marks (%)",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )

with col3:
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

with col4:
    entry_test = st.number_input(
        "Entry Test (%)",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=0.1
    )


# =========================================================
# 3. QUERY
# =========================================================

st.markdown(
    '<div class="section-title">02 — Ask Your Question</div>',
    unsafe_allow_html=True
)

query = st.text_area(
    "Question",
    placeholder=(
        "Example: Can I get admission in NUST BSCS with my current marks?"
    ),
    height=120,
    label_visibility="collapsed"
)


# =========================================================
# 4. ASK BUTTON
# =========================================================

st.markdown(
    '<div class="section-title">03 — Get Guidance</div>',
    unsafe_allow_html=True
)

ask = st.button(
    "🚀  Ask Rahbar AI",
    use_container_width=True
)


# =========================================================
# PROCESS QUERY
# =========================================================

if ask:

    if not query.strip():

        st.warning("Please enter your question first.")

    else:

        st.session_state.asked = True

        # Clear previous trace
        st.session_state.trace = []

        # Agent trace
        st.session_state.trace.append(
            "✓ Received student query"
        )

        st.session_state.trace.append(
            "✓ Read academic profile"
        )

        st.session_state.trace.append(
            "✓ Identified admission context"
        )

        # -------------------------------------------------
        # DEMO AGENT LOGIC
        # -------------------------------------------------

        q = query.lower()

        if "nust" in q or "net" in q:

            st.session_state.trace.append(
                "✓ Searching university admission rules"
            )

            if (
                entry_test >= 70
                and ssc_marks >= 60
                and hssc_marks >= 60
            ):

                st.session_state.decision = "CONDITIONAL"

                st.session_state.reason = (
                    "Your entered academic profile meets the basic "
                    "conditions used by this prototype. However, "
                    "final eligibility depends on the current official "
                    "admission requirements and programme-specific rules."
                )

            else:

                st.session_state.decision = "NO"

                st.session_state.reason = (
                    "Based on the values entered, the profile does not "
                    "meet the basic thresholds used by this prototype."
                )

            st.session_state.trace.append(
                "✓ Calculated admission aggregate"
            )

            st.session_state.trace.append(
                "✓ Generated preliminary decision"
            )

        else:

            st.session_state.decision = "NOT_YET_VERIFIED"

            st.session_state.reason = (
                "Rahbar could not verify this question against the "
                "currently connected admission documents."
            )

            st.session_state.trace.append(
                "⚠ No verified document evidence found"
            )

        st.session_state.trace.append(
            "✓ Prepared response for student"
        )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.asked:

    # =====================================================
    # 5. DECISION
    # =====================================================

    st.markdown(
        '<div class="section-title">04 — Decision</div>',
        unsafe_allow_html=True
    )

    decision = st.session_state.decision
    reason = st.session_state.reason

    if decision == "YES":

        st.markdown(
            f"""
            <div class="decision yes">
                <h2>✅ YES</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif decision == "NO":

        st.markdown(
            f"""
            <div class="decision no">
                <h2>❌ NO</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif decision == "CONDITIONAL":

        st.markdown(
            f"""
            <div class="decision conditional">
                <h2>⚠️ CONDITIONAL</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="decision pending">
                <h2>🔎 NOT YET VERIFIED</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # 6. CALCULATION
    # =====================================================

    st.markdown(
        '<div class="section-title">05 — Aggregate Calculation</div>',
        unsafe_allow_html=True
    )

    # Prototype formula:
    # NET 75% + SSC 10% + HSSC 15%

    aggregate = (
        (entry_test * 0.75)
        + (ssc_marks * 0.10)
        + (hssc_marks * 0.15)
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{aggregate:.2f}%</div>
                <div class="metric-label">Overall Aggregate</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{entry_test * 0.75:.2f}%</div>
                <div class="metric-label">Entry Test Contribution</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c3:

        academic = (
            (ssc_marks * 0.10)
            + (hssc_marks * 0.15)
        )

        st.markdown(
            f"""
            <div class="metric-card">
                <div class="metric-number">{academic:.2f}%</div>
                <div class="metric-label">Academic Contribution</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="card" style="margin-top: 1rem;">

        <b>Formula</b>

        <p>
        Aggregate = (Entry Test × 75%)
        + (SSC × 10%)
        + (HSSC × 15%)
        </p>

        <b>Calculation</b>

        <p>
        ({entry_test:.2f} × 0.75)
        + ({ssc_marks:.2f} × 0.10)
        + ({hssc_marks:.2f} × 0.15)
        = <b>{aggregate:.2f}%</b>
        </p>

        <span class="small-muted">
        Prototype calculation — actual university-specific formulas
        should come from verified admission documents.
        </span>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # 7. EVIDENCE
    # =====================================================

    st.markdown(
        '<div class="section-title">06 — Evidence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="evidence-card">

            <div class="evidence-title">
                📄 Source Document
            </div>

            <div class="evidence-value">
                University Admission Policy / Connected Document
            </div>

            <div class="evidence-title">
                📖 Page
            </div>

            <div class="evidence-value">
                Pending document-agent verification
            </div>

            <div class="evidence-title">
                🔗 Source URL
            </div>

            <div class="evidence-value">
                Pending connection
            </div>

            <div class="evidence-title">
                📅 Verification Date
            </div>

            <div class="evidence-value">
                {date.today().strftime("%d %B %Y")}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =====================================================
    # 8. ACTIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">07 — Recommended Actions</div>',
        unsafe_allow_html=True
    )

    actions = [
        "Verify the current admission requirements from the official university source.",
        "Confirm that your HSSC group is eligible for the selected programme.",
        "Check the current entry-test requirements and application deadline.",
        "Keep your academic documents ready for the application process."
    ]

    for i, action in enumerate(actions, start=1):

        st.markdown(
            f"""
            <div class="action">
                <span class="action-number">{i}</span>
                {action}
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # 9. LIMITATIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">08 — Limitations</div>',
        unsafe_allow_html=True
    )

    st.info(
        "⚠️ This UI prototype is not yet connected to the final "
        "university-document retrieval agent. Admission rules, "
        "deadlines, merit requirements and source pages should be "
        "verified against the connected official documents before "
        "treating a result as final."
    )


    # =====================================================
    # 10. AGENT TRACE
    # =====================================================

    st.markdown(
        '<div class="section-title">09 — Agent Trace</div>',
        unsafe_allow_html=True
    )

    trace_html = ""

    for item in st.session_state.trace:
        trace_html += (
            f'<div><span class="trace-green">{item}</span></div>'
        )

    st.markdown(
        f"""
        <div class="trace">
            <div>$ rahbar-agent --run</div>
            <br>
            {trace_html}
            <br>
            <div>$ status: COMPLETE</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# 10. PRODUCT STATUS / FOOTER
# =========================================================

      st.markdown(
        f"""
        <div class="trace">
            <div>$ rahbar-agent --run</div>
            <br>
            {trace_html}
            <br>
            <div>$ status: COMPLETE</div>
        </div>
        """,
        unsafe_allow_html=True
    )

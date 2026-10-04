import streamlit as st
from datetime import date
import re

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

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

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

.hero h1 {
    font-size: 3rem;
    font-weight: 800;
    margin: 0;
}

.hero p {
    font-size: 1.05rem;
    color: #dbeafe;
    margin-top: 0.7rem;
    max-width: 750px;
}

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

.card {
    background: rgba(255,255,255,0.90);
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.35rem;
    box-shadow: 0 8px 30px rgba(15,23,42,0.06);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-3px);
    box-shadow: 0 14px 35px rgba(15,23,42,0.10);
}

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
    color: #0f172a;
}

.pending h2 {
    color: #0f172a;
}

.pending p {
    color: #1e293b;
}

.metric-card {
    text-align: center;
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 1.3rem;
    box-shadow: 0 8px 25px rgba(15,23,42,0.06);
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

.evidence-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
}

.evidence-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #2563eb;
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 7px 24px rgba(15,23,42,0.06);
    transition: all 0.2s ease;
}

.evidence-card:hover {
    transform: translateY(-2px);
}

.evidence-title {
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 5px;
}

.evidence-value {
    color: #475569;
}
.action {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.7rem;
    transition: all 0.2s ease;
    color: #0f172a;
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

.trace {
    background: #0b1120;
    color: #cbd5e1;
    border-radius: 18px;
    padding: 1.4rem;
    font-family: monospace;
    line-height: 1.9;
    box-shadow: 0 10px 30px rgba(15,23,42,0.15);
}

.trace-step {
    color: #4ade80;
}

.trace-muted {
    color: #94a3b8;
}

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

@media (max-width: 800px) {
    .evidence-grid {
        grid-template-columns: 1fr;
    }

    .hero h1 {
        font-size: 2.2rem;
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

if "trace_steps" not in st.session_state:
    st.session_state.trace_steps = []

if "show_calculation" not in st.session_state:
    st.session_state.show_calculation = False


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def contains_year(text):
    return [int(x) for x in re.findall(r"\b(20\d{2})\b", text)]


def is_future_or_unavailable_question(text):
    q = text.lower()

    current_year = date.today().year
    years = contains_year(q)

    future_year = any(year > current_year for year in years)

    future_words = [
        "future",
        "next year",
        "upcoming",
        "prediction",
        "predict",
        "expected merit",
        "expected closing merit",
        "closing merit prediction"
    ]

    unavailable_words = [
        "latest",
        "current closing merit",
        "closing merit",
        "cutoff",
        "deadline",
        "merit",
        "eligibility"
    ]

    if future_year:
        return True

    if any(word in q for word in future_words):
        return True

    if any(word in q for word in unavailable_words):
        return True

    return False


def is_calculation_question(text):
    q = text.lower()

    calculation_words = [
        "aggregate",
        "calculate aggregate",
        "calculate my aggregate",
        "calculate my merit",
        "merit calculation",
        "marks",
        "percentage",
        "calculate",
        "how much aggregate",
        "what is my aggregate",
        "what will be my aggregate",
        "aggregate score",
        "merit score"
    ]

    return any(word in q for word in calculation_words)


def is_deadline_question(text):
    q = text.lower()

    deadline_words = [
        "deadline",
        "last date",
        "last date to apply",
        "application date",
        "closing date",
        "when should i apply",
        "when is the deadline"
    ]

    return any(word in q for word in deadline_words)


# =========================================================
# AGENT TRACE
# =========================================================

def build_trace(query):
    q = query.lower()

    # Deadline-only question
    if is_deadline_question(q) and not is_calculation_question(q):
        return [
            "check_deadline",
            "decision_generated"
        ]

    # Full question
    return [
        "search_universities",
        "calculate_aggregate",
        "check_deadline",
        "decision_generated",
        "agent_stopped"
    ]


def render_decision(decision, reason):

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
                <h2>🔎 NOT_YET_VERIFIED</h2>
                <p>{reason}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# 01 — HEADER
# =========================================================

st.markdown(
    """
    <div class="hero">
        <h1>🧭 Rahbar AI</h1>
        <p>
            Intelligent university admission guidance.
            Enter your academic profile and ask Rahbar about
            universities, programmes, merit, deadlines and eligibility.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# 02 — STUDENT PROFILE
# =========================================================

st.markdown(
    '<div class="section-title">01 — Student Profile</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Required information for the admission agent.</div>',
    unsafe_allow_html=True
)

row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    university = st.selectbox(
        "University",
        ["NUST", "FAST", "COMSATS"]
    )

with row1_col2:
    program = st.selectbox(
        "Program",
        [
            "BS Computer Science",
            "BS Software Engineering",
            "BS Artificial Intelligence",
            "BS Data Science",
            "BS Electrical Engineering",
            "Other"
        ]
    )

with row1_col3:
    campus = st.text_input(
        "Campus (Optional)",
        placeholder="e.g. Islamabad"
    )

row2_col1, row2_col2, row2_col3 = st.columns(3)

with row2_col1:
    cycle = st.text_input(
        "Admission Cycle",
        value="2026",
        placeholder="e.g. 2026"
    )

with row2_col2:
    part2_status = st.radio(
        "Part-II Result Status",
        ["Pending", "Declared", "Not applicable"],
        horizontal=True
    )

with row2_col3:
    ssc_marks = st.number_input(
        "SSC Marks (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=0.1
    )

row3_col1, row3_col2 = st.columns(2)

with row3_col1:
    hssc_marks = st.number_input(
        "HSSC Marks (%)",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1
    )

with row3_col2:
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
# 02 — QUERY
# =========================================================

st.markdown(
    '<div class="section-title">02 — Ask Your Question</div>',
    unsafe_allow_html=True
)

query = st.text_area(
    "Question",
    placeholder="Example: What is the 2028 NUST BSCS closing merit?",
    height=120,
    label_visibility="collapsed"
)


# =========================================================
# 03 — GET GUIDANCE
# =========================================================

st.markdown(
    '<div class="section-title">03 — Get Guidance</div>',
    unsafe_allow_html=True
)

ask = st.button(
    "🚀 Ask Rahbar AI",
    use_container_width=True
)


# =========================================================
# PROCESS QUESTION
# =========================================================

if ask:

    if not query.strip():

        st.warning("Please enter your question first.")
        st.session_state.asked = False

    else:

        st.session_state.asked = True

        # Show calculation ONLY when requested
        st.session_state.show_calculation = is_calculation_question(
            query
        )

        # Build agent trace
        st.session_state.trace_steps = build_trace(query)

        # =================================================
        # DECISION LOGIC
        # =================================================

        # Future / unavailable / unverified = NOT_YET_VERIFIED
        if is_future_or_unavailable_question(query):

            st.session_state.decision = "NOT_YET_VERIFIED"

            st.session_state.reason = (
                "Rahbar does not have verified evidence for the "
                "requested information yet. The requested data is "
                "future, unavailable, or requires verification from "
                "the university's official admission source."
            )

        else:

            # No verified backend evidence connected yet.
            # Never fabricate YES / NO / CONDITIONAL.

            st.session_state.decision = "NOT_YET_VERIFIED"

            st.session_state.reason = (
                "Rahbar has not yet verified this answer against "
                "connected university evidence. A final YES, NO, "
                "or CONDITIONAL decision will only be shown when "
                "verified evidence is available."
            )


# =========================================================
# RESULTS
# =========================================================

if st.session_state.asked:

    # =====================================================
    # 04 — DECISION
    # =====================================================

    st.markdown(
        '<div class="section-title">04 — Decision</div>',
        unsafe_allow_html=True
    )

    render_decision(
        st.session_state.decision,
        st.session_state.reason
    )


    # =====================================================
    # 05 — AGGREGATE CALCULATION
    # ONLY SHOWN FOR CALCULATION QUESTIONS
    # =====================================================

    if st.session_state.show_calculation:

        st.markdown(
            '<div class="section-title">05 — Aggregate Calculation</div>',
            unsafe_allow_html=True
        )

        aggregate = (
            (entry_test * 0.75)
            + (ssc_marks * 0.10)
            + (hssc_marks * 0.15)
        )

        academic_contribution = (
            (ssc_marks * 0.10)
            + (hssc_marks * 0.15)
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        {aggregate:.2f}%
                    </div>
                    <div class="metric-label">
                        Overall Aggregate
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        {entry_test * 0.75:.2f}%
                    </div>
                    <div class="metric-label">
                        Entry Test Contribution
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-number">
                        {academic_contribution:.2f}%
                    </div>
                    <div class="metric-label">
                        Academic Contribution
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="card">
                <b>Formula</b>

                <p>
                    Aggregate =
                    (Entry Test × 75%) +
                    (SSC × 10%) +
                    (HSSC × 15%)
                </p>

                <b>Calculation</b>

                <p>
                    ({entry_test:.2f} × 0.75)
                    +
                    ({ssc_marks:.2f} × 0.10)
                    +
                    ({hssc_marks:.2f} × 0.15)
                    =
                    <b>{aggregate:.2f}%</b>
                </p>

                <span style="color:#64748b;">
                    Calculation is displayed because the student
                    asked a marks/aggregate-related question.
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )


    # =====================================================
    # 06 — EVIDENCE
    # =====================================================

    st.markdown(
        '<div class="section-title">06 — Evidence</div>',
        unsafe_allow_html=True
    )

    verification_date = date.today().strftime("%d %B %Y")

    st.html(
        f"""
        <div class="evidence-grid">

            <div class="evidence-card">
                <div class="evidence-title">
                    📄 Source Document
                </div>
                <div class="evidence-value">
                    University admission evidence
                </div>
            </div>

            <div class="evidence-card">
                <div class="evidence-title">
                    📖 Page
                </div>
                <div class="evidence-value">
                    Pending verified document lookup
                </div>
            </div>

            <div class="evidence-card">
                <div class="evidence-title">
                    🔗 Source URL
                </div>
                <div class="evidence-value">
                    Pending verified source lookup
                </div>
            </div>

            <div class="evidence-card">
                <div class="evidence-title">
                    📅 Verification Date
                </div>
                <div class="evidence-value">
                    {verification_date}
                </div>
            </div>

        </div>
        """
    )


    # =====================================================
    # 07 — ACTIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">07 — Recommended Actions</div>',
        unsafe_allow_html=True
    )

    actions = [
        "Verify the answer against the university's official admission source.",
        "Confirm the selected programme and campus requirements.",
        "Check the relevant admission deadline.",
        "Keep your academic documents ready for the application."
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
    # 08 — LIMITATIONS
    # =====================================================

    st.markdown(
        '<div class="section-title">08 — Limitations</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Rahbar will only return a final YES, NO or CONDITIONAL "
        "decision when verified evidence is available. "
        "Unverified, future or unavailable information is marked "
        "NOT_YET_VERIFIED."
    )


    # =====================================================
    # 09 — AGENT TRACE
    # =====================================================

    st.markdown(
        '<div class="section-title">09 — Agent Trace</div>',
        unsafe_allow_html=True
    )

    trace_html = ""

    for index, step in enumerate(
        st.session_state.trace_steps,
        start=1
    ):

        trace_html += f"""
        <div class="trace-step">
            Step {index} — {step}
        </div>
        """

    st.html(
        f"""
        <div class="trace">

            <div class="trace-muted">
                $ rahbar-agent --run
            </div>

            <br>

            {trace_html}

            <br>

            <div class="trace-muted">
                $ status: COMPLETE
            </div>

        </div>
        """
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div style="
        text-align:center;
        color:#64748b;
        padding:2rem 0;
        font-size:0.85rem;
    ">
        🧭 <b>Rahbar AI</b> · Student Admission Guidance
    </div>
    """,
    unsafe_allow_html=True
)

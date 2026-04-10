import streamlit as st

# 1. Set page config
st.set_page_config(page_title="Discrete Math Solutions", layout="wide")

# 2. Import styles.css using st.html to avoid extra spacing
def local_css(file_name):
    try:
        with open(file_name) as f:
            st.html(f"<style>{f.read()}</style>")
    except FileNotFoundError:
        st.html("<style>div[data-testid='stMarkdownContainer'] p { margin-bottom: 0px; }</style>")

local_css("styles.css")

# 3. Define Tabs
tab_intro, tab_3, tab_8, tab_12 = st.tabs(["Introduction", "Question 3", "Question 8", "Question 12"])

with tab_intro:
    # Huge, centered font for the Intro tab
    st.write("")
    st.write("")
    st.markdown("<h1 style='text-align: center; font-size: 4.5em; letter-spacing: 2px; margin-bottom: 0px;'>Sathvik U S</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #555555; font-weight: 300; font-size: 2em; margin-top: 0px;'>4JN24AI047</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='width: 40%; margin: auto; border: 1px solid #cccccc;'>", unsafe_allow_html=True)

with tab_3:
    st.markdown(r"### **Question 3: Symbolic Form Translations**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    &emsp;&emsp; $p(x): x > 0$  
    &emsp;&emsp; $q(x): x \text{ is even}$  
    &emsp;&emsp; $r(x): x \text{ is a perfect square}$  
    &emsp;&emsp; $s(x): x \text{ is divisible by 3}$  
    &emsp;&emsp; $t(x): x \text{ is divisible by 7}$  
    """)

    st.divider()

    st.markdown(r"##### **i) At least one integer is even.**")
    st.markdown(r"The phrase 'at least one' translates to the existential quantifier.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\implies \exists x [q(x)]$")
    c2.markdown(r"**Rule:**")
    c2.markdown(r"&emsp;&emsp; Rules of inference")

    st.divider()

    st.markdown(r"##### **ii) There exists a positive integer that is even.**")
    st.markdown(r"We use the existential quantifier for 'there exists' and conjunction to join the two properties.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\implies \exists x [p(x) \land q(x)]$")
    c2.markdown(r"**Rule:**")
    c2.markdown(r"&emsp;&emsp; Conjunction")

    st.divider()

    st.markdown(r"##### **iii) If x is even, then x is not divisible by 3.**")
    st.markdown(r"The 'If... then' structure translates to an implication. Since this rule applies to any integer in the universe, we bound it with the universal quantifier.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\implies \forall x [q(x) \rightarrow \neg s(x)]$")
    c2.markdown(r"**Rule:**")
    c2.markdown(r"&emsp;&emsp; Law of Implication")

    st.divider()

    st.markdown(r"##### **iv) No even integer is divisible by 7.**")
    st.markdown(r"Write it as 'It is false that there exists an even integer divisible by 7', then simplify.")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; $\neg \exists x [q(x) \land t(x)]$")
    c1.markdown(r"&emsp;&emsp; $\equiv \forall x \neg [q(x) \land t(x)]$")
    c1.markdown(r"&emsp;&emsp; $\equiv \forall x [\neg q(x) \lor \neg t(x)]$")
    c1.markdown(r"&emsp;&emsp; $\equiv \forall x [q(x) \rightarrow \neg t(x)]$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \forall x [q(x) \rightarrow \neg t(x)]$")
    
    c2.markdown(r"**Rules Applied:**")
    c2.markdown(r"&emsp;&emsp; Rules of inference")
    c2.markdown(r"&emsp;&emsp; De Morgan's Law")
    c2.markdown(r"&emsp;&emsp; De Morgan's Law")
    c2.markdown(r"&emsp;&emsp; Law with Implication")

    st.divider()

    st.markdown(r"##### **v) There exists even integer divisible by 3.**")
    st.markdown(r"We combine the properties with conjunction and use the existential quantifier.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\implies \exists x [q(x) \land s(x)]$")
    c2.markdown(r"**Rule:**")
    c2.markdown(r"&emsp;&emsp; Conjunction")

with tab_8:
    st.markdown(r"### **Question 8: Truth Values for Non-Zero Integers**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")

    st.divider()

    st.markdown(r"##### **a) $\exists x \exists y [xy = 1]$**")
    st.markdown(r"**Premise:** $xy = 1$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Let $x = 1$, $y = 1$")
    c1.markdown(r"&emsp;&emsp; $xy = 1(1) = 1$")
    c1.markdown(r"&emsp;&emsp; $1 = 1 \equiv \text{True}$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{True}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Rules of inference")
    c2.markdown(r"&emsp;&emsp; Identity laws")

    st.divider()

    st.markdown(r"##### **b) $\exists x \forall y [xy = 1]$**")
    st.markdown(r"**Premise:** $xy = 1$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Assume such an $x$ exists.")
    c1.markdown(r"&emsp;&emsp; Let $y = 1 \implies x(1) = 1 \implies x = 1$")
    c1.markdown(r"&emsp;&emsp; Let $y = 4 \implies 1(4) = 4 \neq 1$")
    c1.markdown(r"&emsp;&emsp; Because it fails for $y=4$, it is not true for all y.")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{False}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Rules of inference")

    st.divider()

    st.markdown(r"##### **c) $\forall x \exists y [xy = 1]$**")
    st.markdown(r"**Premise:** $xy = 1$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Let $x = 2$")
    c1.markdown(r"&emsp;&emsp; $2y = 1 \implies y = 0.5$")
    c1.markdown(r"&emsp;&emsp; $0.5 \notin \mathbb{Z}^*$ (Not an integer, no such y exists)")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{False}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Rules of inference")

    st.divider()

    st.markdown(r"##### **d) $\exists x \exists y [(2x + y = 5) \land (x - 3y = -8)]$**")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; $2x + y = 5 \implies y = 5 - 2x$")
    c1.markdown(r"&emsp;&emsp; $x - 3(5 - 2x) = -8 \implies 7x = 7 \implies x = 1$")
    c1.markdown(r"&emsp;&emsp; $y = 5 - 2(1) \implies y = 3$")
    c1.markdown(r"&emsp;&emsp; Both $x=1$ and $y=3$ are valid non-zero integers.")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{True}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Conjunctive simplification")
    c2.markdown(r"&emsp;&emsp; Modus ponens")

    st.divider()

    st.markdown(r"##### **e) $\exists x \exists y [(3x - y = 7) \land (2x + 4y = 3)]$**")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; $3x - y = 7 \implies y = 3x - 7$")
    c1.markdown(r"&emsp;&emsp; $2x + 4(3x - 7) = 3 \implies 14x = 31 \implies x = 31/14$")
    c1.markdown(r"&emsp;&emsp; $31/14 \notin \mathbb{Z}^*$ (Result is a rational number, not an integer)")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{False}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Conjunctive simplification")
    c2.markdown(r"&emsp;&emsp; Modus tollens")

with tab_12:
    st.markdown(r"### **Question 12: Truth Values for Real Numbers**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    &emsp;&emsp; $p(x) : x \ge 0$  
    &emsp;&emsp; $q(x) : x^2 \ge 0$  
    &emsp;&emsp; $r(x) : x^2 - 3x - 4 = 0 \implies (x - 4)(x + 1) = 0 \implies x \in \{-1, 4\}$  
    &emsp;&emsp; $s(x) : x^2 - 3 > 0 \implies x^2 > 3 \implies x > \sqrt{3}, x < -\sqrt{3}$  
    """)

    st.divider()

    st.markdown(r"##### **1. $\exists x [p(x) \land q(x)]$**")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Let $x = 1$")
    c1.markdown(r"&emsp;&emsp; $p(1): 1 \ge 0 \equiv \text{True}$")
    c1.markdown(r"&emsp;&emsp; $q(1): 1^2 \ge 0 \equiv \text{True}$")
    c1.markdown(r"&emsp;&emsp; $\text{True} \land \text{True} \equiv \text{True}$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{True}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Idempotent laws")

    st.divider()

    st.markdown(r"##### **2. $\forall x [p(x) \rightarrow q(x)]$**")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Let $x = c$ (any real number)")
    c1.markdown(r"&emsp;&emsp; Case 1: $c \ge 0 \implies p(c) \equiv \text{True}$. Since $c^2 \ge 0$, $q(c) \equiv \text{True}$. $\text{T} \rightarrow \text{T} \equiv \text{True}$")
    c1.markdown(r"&emsp;&emsp; Case 2: $c < 0 \implies p(c) \equiv \text{False}$. Since $c^2 \ge 0$, $q(c) \equiv \text{True}$. $\text{F} \rightarrow \text{T} \equiv \text{True}$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{True}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Rule of Universal Generalization")

    st.divider()

    st.markdown(r"##### **3. $\forall x [q(x) \rightarrow s(x)]$**")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Let $x = 1$")
    c1.markdown(r"&emsp;&emsp; $q(1): 1^2 \ge 0 \equiv \text{True}$")
    c1.markdown(r"&emsp;&emsp; $s(1): 1^2 - 3 > 0 \implies -2 > 0 \equiv \text{False}$")
    c1.markdown(r"&emsp;&emsp; $\text{True} \rightarrow \text{False} \equiv \text{False}$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{False}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Rule of Universal Specification")

    st.divider()

    st.markdown(r"##### **4. $\forall x [r(x) \lor s(x)]$**")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; Let $x = 0$")
    c1.markdown(r"&emsp;&emsp; $r(0): 0^2 - 3(0) - 4 = 0 \implies -4 = 0 \equiv \text{False}$")
    c1.markdown(r"&emsp;&emsp; $s(0): 0^2 - 3 > 0 \implies -3 > 0 \equiv \text{False}$")
    c1.markdown(r"&emsp;&emsp; $\text{False} \lor \text{False} \equiv \text{False}$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \text{False}$")
    c2.markdown(r"**Rules:**")
    c2.markdown(r"&emsp;&emsp; Idempotent laws")
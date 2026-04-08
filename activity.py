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
tab0, tab3, tab2, tab1 = st.tabs(["Introduction", "Question 3", "Question 8", "Question 12"])

with tab0:
    st.markdown("### Sathvik U S")
    st.markdown("#### 4JN24AI047")


with tab3:
    st.markdown(r"### Question 3")
    st.markdown(r"**Write the following statements in symbolic form:**")
    st.markdown(r"**Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"""
    * $p(x): x > 0$
    * $q(x): x \text{ is even}$
    * $r(x): x \text{ is a perfect square}$
    * $s(x): x \text{ is divisible by 3}$
    * $t(x): x \text{ is divisible by 7}$
    """)
    
    st.divider()

    st.markdown(r"##### i) At least one integer is even.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\implies \exists x [q(x)]$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### ii) There exists a positive integer that is even.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\implies \exists x [p(x) \land q(x)]$")
    c2.markdown(r"""
    Conjunction
    
    | $P$ | $Q$ | $P \land Q$ |
    |---|---|---|
    | T | T | **T** |
    """)

    st.divider()

    st.markdown(r"##### iii) If x is even, then x is not divisible by 3.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\implies \forall x [q(x) \implies \neg s(x)]$")
    c2.markdown(r"Implication")

    st.divider()

    st.markdown(r"##### iv) No even integer is divisible by 7.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\neg \exists x [q(x) \land t(x)]$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\equiv \forall x \neg [q(x) \land t(x)]$")
    c2.markdown(r"De Morgans")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\equiv \forall x [\neg q(x) \lor \neg t(x)]$")
    c2.markdown(r"De Morgans")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\equiv \forall x [q(x) \implies \neg t(x)]$")
    c2.markdown(r"Implication")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \forall x [q(x) \implies \neg t(x)]$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### v) There exists even integer divisible by 3.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\implies \exists x [q(x) \land s(x)]$")
    c2.markdown(r"Conjunction")


with tab2:
    st.markdown(r"### Question 8")
    st.markdown(r"**Determine the truth value of each statement:**")
    st.markdown(r"**Universe:** All non-zero integers ($\mathbb{Z}^* = \{\dots, -2, -1, 1, 2, \dots\}$)")
    
    st.divider()

    st.markdown(r"##### a) $\exists x \exists y [xy = 1]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 1, y = 1$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$xy = 1(1) = 1$")
    c2.markdown(r"Commutative")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$1 = 1 \equiv \text{T}$")
    c2.markdown(r"Identity law")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{True}$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### b) $\exists x \forall y [xy = 1]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Assume such an $x$ exists.")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $y = 1 \implies x(1) = 1 \implies x = 1$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $y = 2 \implies x(2) = 1$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Substitute $x = 1 \implies 1(2) = 1 \implies 2 = 1 \equiv \text{F}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{False}$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### c) $\forall x \exists y [xy = 1]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 2$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$xy = 1 \implies 2y = 1 \implies y = 0.5$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$0.5 \notin \mathbb{Z}^* \equiv \text{F}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{False}$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### d) $\exists x \exists y [(2x + y = 5) \land (x - 3y = -8)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$2x + y = 5 \implies y = 5 - 2x$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$x - 3y = -8$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$x - 3(5 - 2x) = -8$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$x - 15 + 6x = -8 \implies 7x = 7 \implies x = 1$")
    c2.markdown(r"Conjunctive simplification")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$y = 5 - 2(1) \implies y = 3$")
    c2.markdown(r"Modus ponens")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$x = 1 \in \mathbb{Z}^*, y = 3 \in \mathbb{Z}^* \equiv \text{T}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{True}$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### e) $\exists x \exists y [(3x - y = 7) \land (2x + 4y = 3)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$3x - y = 7 \implies y = 3x - 7$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$2x + 4y = 3$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$2x + 4(3x - 7) = 3$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$14x = 31 \implies x = 31/14$")
    c2.markdown(r"Conjunctive simplification")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$31/14 \notin \mathbb{Z}^* \equiv \text{F}$")
    c2.markdown(r"Modus tollens")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{False}$")
    c2.markdown(r"")


with tab1:
    st.markdown(r"##### **Q 12. Consider the following open statements on the set of all real numbers as universe:**")
    st.markdown(r"""
    * $p(x) : x \ge 0$
    * $q(x) : x^2 \ge 0$
    * $r(x) : x^2 - 3x - 4 = 0 $
    * $s(x) : x^2 - 3 > 0 $
    """)
    st.divider()
    st.markdown(r"**Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"""
    * $p(x) : x \ge 0$
    * $q(x) : x^2 \ge 0$
    * $r(x) : x^2 - 3x - 4 = 0 $
        * $x^2 - 4x + x - 4 = 0$
        * $x(x - 4) + 1(x - 4) = 0$
        * $(x - 4)(x + 1) = 0$
        * $\implies x \in \{-1, 4\}$
    * $s(x) : x^2 - 3 > 0 $
        * $x^2 > 3$
        * $\implies x > \sqrt{3}, x < -\sqrt{3}$
    """)
    st.markdown(r"**Find the truth value of:**")

    st.divider()

    st.markdown(r"##### 1. $\exists x [p(x) \land q(x)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 1$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$p(1): 1 \ge 0 \equiv \text{T}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$q(1): 1^2 \ge 0 \equiv \text{T}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$p(1) \land q(1) \equiv \text{T} \land \text{T} \equiv \text{T}$")
    c2.markdown(r"Conjunction")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{True}$")
    c2.markdown(r"Identity law")

    st.divider()

    st.markdown(r"##### 2. $\forall x [p(x) \implies q(x)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = c$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Case 1: $c \ge 0 \implies p(c) \equiv \text{T}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$c \ge 0 \implies c^2 \ge 0 \implies q(c) \equiv \text{T}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\text{T} \implies \text{T} \equiv \text{T}$")
    c2.markdown(r"""
    Implication
    
    | $P$ | $Q$ | $P \implies Q$ |
    |---|---|---|
    | T | T | **T** |
    """)
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Case 2: $c < 0 \implies p(c) \equiv \text{F}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\text{F} \implies \text{T} \equiv \text{T}$")
    c2.markdown(r"""
    Implication
    
    | $P$ | $Q$ | $P \implies Q$ |
    |---|---|---|
    | F | T | **T** |
    """)
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{True}$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### 3. $\forall x [q(x) \implies s(x)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 1$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$q(1): 1^2 \ge 0 \equiv \text{T}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$s(1): 1^2 - 3 > 0 \implies -2 > 0 \equiv \text{F}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$q(1) \implies s(1) \equiv \text{T} \implies \text{F} \equiv \text{F}$")
    c2.markdown(r"""
    Implication
    
    | $P$ | $Q$ | $P \implies Q$ |
    |---|---|---|
    | T | F | **F** |
    """)
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{False}$")
    c2.markdown(r"")

    st.divider()

    st.markdown(r"##### 4. $\forall x [r(x) \lor s(x)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 0$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$r(0): 0^2 - 3(0) - 4 = 0 \implies -4 = 0 \equiv \text{F}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$s(0): 0^2 - 3 > 0 \implies -3 > 0 \equiv \text{F}$")
    c2.markdown(r"")
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$r(0) \lor s(0) \equiv \text{F} \lor \text{F} \equiv \text{F}$")
    c2.markdown(r"""
    Identity law
    
    | $P$ | $P \lor P$ |
    |---|---|
    | F | **F** |
    """)
    
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"$\therefore \text{False}$")
    c2.markdown(r"")
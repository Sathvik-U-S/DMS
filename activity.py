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
    st.markdown("#### **Sathvik U S**")
    st.markdown("#### **4JN24AI047**")

with tab_3:
    st.markdown(r"#### **Question 3: For the universe of all integers, let p(x), q(x), r(x), s(x) and t(x) denote the following open statements. Write the following statements in symbolic form:**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x): x > 0$
    
    $q(x): x \text{ is even}$
    
    $r(x): x \text{ is a perfect square}$
    
    $s(x): x \text{ is divisible by 3}$
    
    $t(x): x \text{ is divisible by 7}$
    """)

    st.divider()

    st.markdown(r"##### **i) At least one integer is even.**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"$q(x): x \text{ is even}$")
    st.markdown(r"The symbolic form is:")
    st.markdown(r"$\implies \exists x [q(x)]$")

    st.divider()

    st.markdown(r"##### **ii) There exists a positive integer that is even.**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x): x > 0$
    
    $q(x): x \text{ is even}$
    """)
    st.markdown(r"The symbolic form is:")
    st.markdown(r"$\implies \exists x [p(x) \land q(x)]$")

    st.divider()

    st.markdown(r"##### **iii) If x is even, then x is not divisible by 3.**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $q(x): x \text{ is even}$
    
    $s(x): x \text{ is divisible by 3}$
    """)
    st.markdown(r"The symbolic form is:")
    st.markdown(r"$\implies \forall x [q(x) \rightarrow \neg s(x)]$")

    st.divider()

    st.markdown(r"##### **iv) No even integer is divisible by 7.**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $q(x): x \text{ is even}$
    
    $t(x): x \text{ is divisible by 7}$
    """)
    st.markdown(r"The direct translation is:")
    st.markdown(r"$\neg \exists x [q(x) \land t(x)]$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\equiv \forall x \neg [q(x) \land t(x)]$ | Demorgans Law |
    | $\equiv \forall x [\neg q(x) \lor \neg t(x)]$ | Demorgans Law |
    | $\equiv \forall x [q(x) \rightarrow \neg t(x)]$ | Law of Implication |
    """)
    st.markdown(r"$\therefore \forall x [q(x) \rightarrow \neg t(x)]$")

    st.divider()

    st.markdown(r"##### **v) There exists even integer divisible by 3.**")
    st.markdown(r"**Data / Universe:** All integers ($\mathbb{Z}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $q(x): x \text{ is even}$
    
    $s(x): x \text{ is divisible by 3}$
    """)
    st.markdown(r"The symbolic form is:")
    st.markdown(r"$\implies \exists x [q(x) \land s(x)]$")

with tab_8:
    st.markdown(r"#### **Question 8: For the following statements, the universe comprises all non-zero integers. Determine the truth value of each statement.**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")

    st.divider()

    st.markdown(r"##### **a) $\exists x \exists y [xy = 1]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"$xy = 1$")
    st.markdown(r"Let $x = 1$ and $y = 1$. Substituting these values:")
    st.markdown(r"$xy = (1)(1) = 1$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $1 = 1 \equiv \text{T}$ | Identity Law |
    """)
    st.markdown(r"$\therefore \text{True}$")

    st.divider()

    st.markdown(r"##### **b) $\exists x \forall y [xy = 1]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"$xy = 1$")
    st.markdown(r"Assume such an $x$ exists. Let $y = 1$:")
    st.markdown(r"$x(1) = 1 \implies x = 1$")
    st.markdown(r"Now let $y = 2$, and substitute $x = 1$:")
    st.markdown(r"$1(2) = 1 \implies 2 = 1$")
    st.markdown(r"This results in a contradiction.")
    st.markdown(r"$\therefore \text{False}$")

    st.divider()

    st.markdown(r"##### **c) $\forall x \exists y [xy = 1]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"$xy = 1$")
    st.markdown(r"Let $x = 2$:")
    st.markdown(r"$2y = 1 \implies y = 0.5$")
    st.markdown(r"Since $0.5 \notin \mathbb{Z}^*$, no integer $y$ exists for $x=2$.")
    st.markdown(r"$\therefore \text{False}$")

    st.divider()

    st.markdown(r"##### **d) $\exists x \exists y [(2x + y = 5) \land (x - 3y = -8)]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $2x + y = 5$
    
    $x - 3y = -8$
    """)
    st.markdown(r"Solving the first equation for $y$:")
    st.markdown(r"$y = 5 - 2x$")
    st.markdown(r"Substituting into the second equation:")
    st.markdown(r"$x - 3(5 - 2x) = -8$")
    st.markdown(r"$x - 15 + 6x = -8 \implies 7x = 7 \implies x = 1$")
    st.markdown(r"Substituting $x = 1$ back to find $y$:")
    st.markdown(r"$y = 5 - 2(1) \implies y = 3$")
    st.markdown(r"Since $x = 1 \in \mathbb{Z}^*$ and $y = 3 \in \mathbb{Z}^*$:")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $(2x + y = 5) \land (x - 3y = -8) \equiv \text{T}$ | Rule of Conjunction |
    """)
    st.markdown(r"$\therefore \text{True}$")

    st.divider()

    st.markdown(r"##### **e) $\exists x \exists y [(3x - y = 7) \land (2x + 4y = 3)]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $3x - y = 7$
    
    $2x + 4y = 3$
    """)
    st.markdown(r"Solving the first equation for $y$:")
    st.markdown(r"$y = 3x - 7$")
    st.markdown(r"Substituting into the second equation:")
    st.markdown(r"$2x + 4(3x - 7) = 3$")
    st.markdown(r"$2x + 12x - 28 = 3 \implies 14x = 31 \implies x = 31/14$")
    st.markdown(r"Since $31/14 \notin \mathbb{Z}^*$, there are no integer solutions.")
    st.markdown(r"$\therefore \text{False}$")

with tab_12:
    st.markdown(r"#### **Question 12: Consider the following open statements on the set of all real numbers as universe. Find the truth value of:**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x) : x \ge 0$
    
    $q(x) : x^2 \ge 0$
    """)
    st.markdown(r"For $r(x) : x^2 - 3x - 4 = 0$")
    st.markdown(r"$x^2 - 4x + x - 4 = 0$")
    st.markdown(r"$x(x - 4) + 1(x - 4) = 0$")
    st.markdown(r"$(x - 4)(x + 1) = 0$")
    st.markdown(r"$\implies x \in \{-1, 4\}$")
    st.markdown(r"For $s(x) : x^2 - 3 > 0$")
    st.markdown(r"$x^2 > 3$")
    st.markdown(r"$\implies x > \sqrt{3}, x < -\sqrt{3}$")

    st.divider()

    st.markdown(r"##### **1. $\exists x [p(x) \land q(x)]$**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x) : x \ge 0$
    
    $q(x) : x^2 \ge 0$
    """)
    st.markdown(r"Let $x = 1$. Evaluating the predicates:")
    st.markdown(r"$p(1): 1 \ge 0 \equiv \text{T}$")
    st.markdown(r"$q(1): 1^2 \ge 0 \equiv \text{T}$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\text{T} \land \text{T} \equiv \text{T}$ | Idempotent Law |
    """)
    st.markdown(r"$\therefore \text{True}$")

    st.divider()

    st.markdown(r"##### **2. $\forall x [p(x) \rightarrow q(x)]$**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x) : x \ge 0$
    
    $q(x) : x^2 \ge 0$
    """)
    st.markdown(r"Let $x$ be replaced by an arbitrary real number $c$.")
    st.markdown(r"Case 1: $c \ge 0 \implies p(c) \equiv \text{T}$")
    st.markdown(r"The square of a real number is always non-negative: $c^2 \ge 0 \implies q(c) \equiv \text{T}$")
    st.markdown(r"Case 2: $c < 0 \implies p(c) \equiv \text{F}$")
    st.markdown(r"The square of a real number is always non-negative: $c^2 \ge 0 \implies q(c) \equiv \text{T}$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\text{T} \rightarrow \text{T} \equiv \text{T}$ | Rule of Universal Generalization |
    | $\text{F} \rightarrow \text{T} \equiv \text{T}$ | Rule of Universal Generalization |
    """)
    st.markdown(r"$\therefore \text{True}$")

    st.divider()

    st.markdown(r"##### **3. $\forall x [q(x) \rightarrow s(x)]$**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $q(x) : x^2 \ge 0$
    
    $s(x) : x^2 - 3 > 0$
    """)
    st.markdown(r"Let $x = 1$. Evaluating the predicates:")
    st.markdown(r"$q(1): 1^2 \ge 0 \equiv \text{T}$")
    st.markdown(r"$s(1): 1^2 - 3 > 0 \implies -2 > 0 \equiv \text{F}$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\text{T} \rightarrow \text{F} \equiv \text{F}$ | Rule of Universal Specification |
    """)
    st.markdown(r"$\therefore \text{False}$")

    st.divider()

    st.markdown(r"##### **4. $\forall x [r(x) \lor s(x)]$**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $r(x) : x^2 - 3x - 4 = 0$
    
    $s(x) : x^2 - 3 > 0$
    """)
    st.markdown(r"Let $x = 0$. Evaluating the predicates:")
    st.markdown(r"$r(0): 0^2 - 3(0) - 4 = 0 \implies -4 = 0 \equiv \text{F}$")
    st.markdown(r"$s(0): 0^2 - 3 > 0 \implies -3 > 0 \equiv \text{F}$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\text{F} \lor \text{F} \equiv \text{F}$ | Idempotent Law |
    """)
    st.markdown(r"$\therefore \text{False}$")

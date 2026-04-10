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
    [span_0](start_span)st.markdown(r"The phrase 'at least one' translates to the existential quantifier[span_0](end_span).")
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
    [span_1](start_span)st.markdown(r"We use the existential quantifier for 'there exists'[span_1](end_span) and conjunction to join the two properties.")
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
    [span_2](start_span)st.markdown(r"The 'If... then' structure translates to an implication[span_2](end_span). [span_3](start_span)Since this rule applies to any integer in the universe, we bound it with the universal quantifier symbol $\forall$, which means 'for all'[span_3](end_span).")
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
    [span_4](start_span)st.markdown(r"First, write it as 'It is false that there exists an even integer divisible by 7', then use equivalence laws to simplify[span_4](end_span).")
    st.markdown(r"$\neg \exists x [q(x) \land t(x)]$")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\equiv \forall x \neg [q(x) \land t(x)]$ | De Morgan's Law |
    | $\equiv \forall x [\neg q(x) \lor \neg t(x)]$ | De Morgan's Law |
    | $\equiv \forall x [q(x) \rightarrow \neg t(x)]$ | Law with implication |
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
    [span_5](start_span)st.markdown(r"We combine the properties with conjunction and use the existential quantifier[span_5](end_span).")
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
    [span_6](start_span)st.markdown(r"Let $x = 1$, $y = 1$ then $xy = 1(1) = 1$[span_6](end_span).")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $1 = 1 \equiv \text{T}$ | Identity laws |
    """)
    st.markdown(r"$\therefore \text{True}$")

    st.divider()

    st.markdown(r"##### **b) $\exists x \forall y [xy = 1]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"$xy = 1$")
    [span_7](start_span)st.markdown(r"Let $x = 1$, $y = 4$ then $xy = 4 \neq 1$[span_7](end_span). Because it fails for $y=4$, it is not true for all y.")
    st.markdown(r"$\therefore \text{False}$")

    st.divider()

    st.markdown(r"##### **c) $\forall x \exists y [xy = 1]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"$xy = 1$")
    st.markdown(r"Let $x = 2$, then $2y = 1 \implies y = 0.5$.")
    st.markdown(r"Since $0.5$ is not an integer, no such y exists in our universe.")
    st.markdown(r"$\therefore \text{False}$")

    st.divider()

    st.markdown(r"##### **d) $\exists x \exists y [(2x + y = 5) \land (x - 3y = -8)]$**")
    st.markdown(r"**Data / Universe:** All non-zero integers ($\mathbb{Z}^*$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $2x + y = 5$
    
    $x - 3y = -8$
    """)
    st.markdown(r"Solve the equations.")
    st.markdown(r"$2x + y = 5 \implies y = 5 - 2x$")
    st.markdown(r"$x - 3(5 - 2x) = -8 \implies 7x = 7 \implies x = 1$")
    st.markdown(r"$y = 5 - 2(1) \implies y = 3$")
    [span_8](start_span)st.markdown(r"Since both x and y exist and are integers, it is true[span_8](end_span).")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $(2(1) + 3 = 5) \land (1 - 3(3) = -8) \equiv \text{T}$ | Rule of conjunction |
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
    st.markdown(r"Solve the equations.")
    st.markdown(r"$y = 3x - 7$")
    st.markdown(r"$2x + 4(3x - 7) = 3 \implies 14x = 31 \implies x = 31/14$")
    [span_9](start_span)st.markdown(r"Hence both x and y are rationals and not integers, and the result is False[span_9](end_span).")
    st.markdown(r"$\therefore \text{False}$")

with tab_12:
    st.markdown(r"#### **Question 12: Consider the following open statements on the set of all real numbers as universe. Find the truth value of:**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x) : x \ge 0$
    
    $q(x) : x^2 \ge 0$
    """)
    st.markdown(r"Find solutions for $r(x)$:")
    st.markdown(r"$x^2 - 3x - 4 = 0 \implies (x - 4)(x + 1) = 0 \implies x \in \{-1, 4\}$")
    st.markdown(r"Find boundaries for $s(x)$:")
    st.markdown(r"$x^2 - 3 > 0 \implies x^2 > 3 \implies x > \sqrt{3}, x < -\sqrt{3}$")

    st.divider()

    st.markdown(r"##### **1. $\exists x [p(x) \land q(x)]$**")
    st.markdown(r"**Data / Universe:** Set of all real numbers ($\mathbb{R}$)")
    st.markdown(r"**Premises:**")
    st.markdown(r"""
    $p(x) : x \ge 0$
    
    $q(x) : x^2 \ge 0$
    """)
    st.markdown(r"Let $x = 4$, then $p(x)$ is true and $q(x)$ is true. [span_10](start_span)Hence true[span_10](end_span).")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\text{T} \land \text{T} \equiv \text{T}$ | Idempotent laws |
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
    [span_11](start_span)st.markdown(r"Since we don't have any value of x such that $x \ge 0$ and $x^2 < 0$, the given universal implication is true[span_11](end_span).")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\forall x [p(x) \rightarrow q(x)]$ | Rule of Universal Generalization |
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
    [span_12](start_span)st.markdown(r"Let $x = 1$, then $q(x) = 1^2 = 1$ (True), and $s(x) = 1 - 3 = -2 < 0$ (False). Hence false[span_12](end_span).")
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
    st.markdown(r"Let $x = 0$. Then $r(0)$ is false and $s(0)$ is false.")
    st.markdown(r"**Solution:**")
    st.markdown(r"""
    | Reduction | Rule |
    | :--- | :--- |
    | $\text{F} \lor \text{F} \equiv \text{F}$ | Idempotent laws |
    """)
    st.markdown(r"$\therefore \text{False}$")

import streamlit as st

# 1. Set page config
st.set_page_config(page_title="Discrete Math Solutions")

# 2. Import styles.css using st.html
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
    st.write("")
    st.write("")
    st.markdown("<h1 style='text-align: center; font-size: 4.5em; letter-spacing: 2px; margin-bottom: 0px;'>Sathvik U S</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #555555; font-weight: 300; font-size: 2em; margin-top: 0px;'>4JN24AI047</h2>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; margin-top: 30px;'><hr style='width: 30%; border: 1px solid #bbbbbb; display: inline-block;'></div>", unsafe_allow_html=True)

with tab_3:
    st.markdown(r"### **Question 3**")
    st.markdown(r"For the universe of all integers, let p(x), q(x), r(x), s(x) and t(x) denote the following open statements: ")
    st.markdown(r"p(x): x>0, ")
    st.markdown(r"q(x): x is even, ")
    st.markdown(r"r(x): x is a perfect square, ")
    st.markdown(r"s(x): x is divisible by 3, ")
    st.markdown(r"t(x): x is divisible by 7. ")
    st.markdown(r"Write the following statements in symbolic form: ")
    st.markdown(r"i) At least one integer is even. ")
    st.markdown(r"ii) There exists a positive integer that is even. ")
    st.markdown(r"iii) If x is even, then x is not divisible by 3. ")
    st.markdown(r"iv) No even integer is divisible by 7. ")
    st.markdown(r"v) There exists even integer divisible by 3.")
    
    st.divider()

    st.markdown(r"##### i) At least one integer is even.")
    st.markdown(r"**Data Given:**")
    st.markdown(r"&emsp;&emsp; Universe: All integers ($\mathbb{Z}$)")
    st.markdown(r"&emsp;&emsp; $q(x): x \text{ is even}$")
    st.markdown(r"**Explanation:** The phrase 'at least one' translates to the existential quantifier.")
    st.markdown(r"**Symbolic Form:**")
    st.markdown(r"&emsp;&emsp; $\exists x [q(x)]$")

    st.divider()

    st.markdown(r"##### ii) There exists a positive integer that is even.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Data Given:**")
    c1.markdown(r"&emsp;&emsp; Universe: All integers ($\mathbb{Z}$)")
    c1.markdown(r"&emsp;&emsp; $p(x): x > 0$")
    c1.markdown(r"&emsp;&emsp; $q(x): x \text{ is even}$")
    c1.markdown(r"**Explanation:** Use the existential quantifier and conjunction.")
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\exists x [p(x) \land q(x)]$")
    
    c2.markdown(r"**Rule:**")
    c2.markdown(r"Conjunction")
    c2.markdown(r"&emsp; $p, q \therefore p \land q$")

    st.divider()

    st.markdown(r"##### iii) If x is even, then x is not divisible by 3.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Data Given:**")
    c1.markdown(r"&emsp;&emsp; Universe: All integers ($\mathbb{Z}$)")
    c1.markdown(r"&emsp;&emsp; $q(x): x \text{ is even}$")
    c1.markdown(r"&emsp;&emsp; $s(x): x \text{ is divisible by 3}$")
    c1.markdown(r"**Explanation:** 'If... then' translates to an implication bounded by a universal quantifier.")
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\forall x [q(x) \rightarrow \neg s(x)]$")
    
    c2.markdown(r"**Rule:**")
    c2.markdown(r"Law of Implication")
    c2.markdown(r"&emsp; $p \rightarrow q \equiv \neg p \lor q$")

    st.divider()

    st.markdown(r"##### iv) No even integer is divisible by 7.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Data Given:**")
    c1.markdown(r"&emsp;&emsp; Universe: All integers ($\mathbb{Z}$)")
    c1.markdown(r"&emsp;&emsp; $q(x): x \text{ is even}$")
    c1.markdown(r"&emsp;&emsp; $t(x): x \text{ is divisible by 7}$")
    c1.markdown(r"**Explanation:** Negate the existence of an integer that is both even and divisible by 7, then simplify.")
    c1.markdown(r"**Derivation:**")
    c1.markdown(r"&emsp;&emsp; $\neg \exists x [q(x) \land t(x)]$")
    c1.markdown(r"&emsp;&emsp; $\equiv \forall x \neg [q(x) \land t(x)]$")
    c1.markdown(r"&emsp;&emsp; $\equiv \forall x [\neg q(x) \lor \neg t(x)]$")
    c1.markdown(r"&emsp;&emsp; $\equiv \forall x [q(x) \rightarrow \neg t(x)]$")
    c1.markdown(r"**Conclusion:**")
    c1.markdown(r"&emsp;&emsp; $\therefore \forall x [q(x) \rightarrow \neg t(x)]$")
    
    c2.markdown(r"**Rules:**")
    c2.markdown(r"De Morgan's Law")
    c2.markdown(r"&emsp; $\neg(p \land q) \equiv \neg p \lor \neg q$")
    c2.markdown(r"Law of Implication")
    c2.markdown(r"&emsp; $p \rightarrow q \equiv \neg p \lor q$")

    st.divider()

    st.markdown(r"##### v) There exists even integer divisible by 3.")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"**Data Given:**")
    c1.markdown(r"&emsp;&emsp; Universe: All integers ($\mathbb{Z}$)")
    c1.markdown(r"&emsp;&emsp; $q(x): x \text{ is even}$")
    c1.markdown(r"&emsp;&emsp; $s(x): x \text{ is divisible by 3}$")
    c1.markdown(r"**Explanation:** Combine the properties with conjunction and use the existential quantifier.")
    c1.markdown(r"**Symbolic Form:**")
    c1.markdown(r"&emsp;&emsp; $\exists x [q(x) \land s(x)]$")
    
    c2.markdown(r"**Rule:**")
    c2.markdown(r"Conjunction")
    c2.markdown(r"&emsp; $p, q \therefore p \land q$")

with tab_8:
    st.markdown(r"### **Question 8**")
    st.markdown(r"For the following statements, the universe comprises all non-zero integers. Determine the truth value of each statement.")
    st.markdown(r"a) $\exists x \exists y [xy = 1]$  ")
    st.markdown(r"b) $\exists x \forall y [xy = 1]$  ")
    st.markdown(r"c) $\forall x \exists y [xy = 1]$  ")
    st.markdown(r"d) $\exists x \exists y [(2x + y = 5) \land (x - 3y = -8)]$  ")
    st.markdown(r"e) $\exists x \exists y [(3x - y = 7) \land (2x + 4y = 3)]$")
    st.markdown(r"**Universe:** All non-zero integers ($\mathbb{Z}^*$)")

    st.divider()

    st.markdown(r"##### a) $\exists x \exists y [xy = 1]$")
    st.markdown(r"Let $x = 1$, $y = 1$")
    st.markdown(r"&emsp;&emsp; $xy = 1(1)$")
    st.markdown(r"&emsp;&emsp; $1 = 1 \equiv \text{True}$")
    st.markdown(r"**$\therefore$ True**")

    st.divider()

    st.markdown(r"##### b) $\exists x \forall y [xy = 1]$")
    st.markdown(r"Assume such an $x$ exists. Let $y = 1$")
    st.markdown(r"&emsp;&emsp; $x(1) = 1 \implies x = 1$")
    st.markdown(r"Now test for $y = 4$")
    st.markdown(r"&emsp;&emsp; $1(4) = 4 \neq 1$")
    st.markdown(r"Because it fails for $y=4$, it is not true for all y.")
    st.markdown(r"**$\therefore$ False**")

    st.divider()

    st.markdown(r"##### c) $\forall x \exists y [xy = 1]$")
    st.markdown(r"Let $x = 2$")
    st.markdown(r"&emsp;&emsp; $2y = 1 \implies y = 0.5$")
    st.markdown(r"Since $0.5$ is not an integer, no such y exists in our universe.")
    st.markdown(r"**$\therefore$ False**")

    st.divider()

    st.markdown(r"##### d) $\exists x \exists y [(2x + y = 5) \land (x - 3y = -8)]$")
    st.markdown(r"Solve the equations.")
    st.markdown(r"&emsp;&emsp; $2x + y = 5 \implies y = 5 - 2x$")
    st.markdown(r"&emsp;&emsp; $x - 3(5 - 2x) = -8$")
    st.markdown(r"&emsp;&emsp; $7x - 15 = -8 \implies 7x = 7 \implies x = 1$")
    st.markdown(r"&emsp;&emsp; $y = 5 - 2(1) \implies y = 3$")
    st.markdown(r"Both $x=1$ and $y=3$ are valid non-zero integers.")
    st.markdown(r"**$\therefore$ True**")

    st.divider()

    st.markdown(r"##### e) $\exists x \exists y [(3x - y = 7) \land (2x + 4y = 3)]$")
    st.markdown(r"Solve the equations.")
    st.markdown(r"&emsp;&emsp; $3x - y = 7 \implies y = 3x - 7$")
    st.markdown(r"&emsp;&emsp; $2x + 4(3x - 7) = 3$")
    st.markdown(r"&emsp;&emsp; $14x - 28 = 3 \implies 14x = 31 \implies x = 31/14$")
    st.markdown(r"The result $31/14$ is a rational number, not an integer.")
    st.markdown(r"**$\therefore$ False**")

with tab_12:
    st.markdown(r"### **Question 12**")
    st.markdown(r"Consider the following open statements on the set of all real numbers as universe:")
    st.markdown(r"p(x) : x $\ge$ 0")
    st.markdown(r"q(x) : x$^2$ $\ge$ 0")
    st.markdown(r"r(x) : x$^2$ - 3x - 4 = 0")
    st.markdown(r"s(x) : x$^2$ - 3 > 0")
    st.markdown(r"Then find the truth value of: ")
    st.markdown(r"1. $\exists x [p(x) \land q(x)]$ ")
    st.markdown(r"2. $\forall x [p(x) \rightarrow q(x)]$ ")
    st.markdown(r"3. $\forall x [q(x) \rightarrow s(x)]$ ")
    st.markdown(r"4. $\forall x [r(x) \lor s(x)]$")
    st.markdown(r"**Universe:** Set of all real numbers ($\mathbb{R}$)")

    st.divider()

    st.markdown(r"##### 1. $\exists x [p(x) \land q(x)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 1$")
    c1.markdown(r"&emsp;&emsp; $p(1): 1 \ge 0 \equiv \text{T}$")
    c1.markdown(r"&emsp;&emsp; $q(1): 1^2 \ge 0 \equiv \text{T}$")
    c1.markdown(r"&emsp;&emsp; $\text{T} \land \text{T} \equiv \text{T}$")
    c1.markdown(r"**$\therefore$ True**")
    c2.markdown(r"**Rule:**")
    c2.markdown(r"Idempotent Law")
    c2.markdown(r"&emsp; $p \land p \equiv p$")

    st.divider()

    st.markdown(r"##### 2. $\forall x [p(x) \rightarrow q(x)]$")
    st.markdown(r"Let $x = c$ (any real number)")
    st.markdown(r"Case 1: $c \ge 0$")
    st.markdown(r"&emsp;&emsp; $p(c) \equiv \text{T}$")
    st.markdown(r"&emsp;&emsp; $c^2 \ge 0 \implies q(c) \equiv \text{T}$")
    st.markdown(r"&emsp;&emsp; $\text{T} \rightarrow \text{T} \equiv \text{T}$")
    st.markdown(r"Case 2: $c < 0$")
    st.markdown(r"&emsp;&emsp; $p(c) \equiv \text{F}$")
    st.markdown(r"&emsp;&emsp; $c^2 \ge 0 \implies q(c) \equiv \text{T}$")
    st.markdown(r"&emsp;&emsp; $\text{F} \rightarrow \text{T} \equiv \text{T}$")
    st.markdown(r"**$\therefore$ True**")

    st.divider()

    st.markdown(r"##### 3. $\forall x [q(x) \rightarrow s(x)]$")
    st.markdown(r"Let $x = 1$")
    st.markdown(r"&emsp;&emsp; $q(1): 1^2 \ge 0 \equiv \text{T}$")
    st.markdown(r"&emsp;&emsp; $s(1): 1^2 - 3 > 0 \implies -2 > 0 \equiv \text{F}$")
    st.markdown(r"&emsp;&emsp; $\text{T} \rightarrow \text{F} \equiv \text{F}$")
    st.markdown(r"**$\therefore$ False**")

    st.divider()

    st.markdown(r"##### 4. $\forall x [r(x) \lor s(x)]$")
    c1, c2 = st.columns([2, 1])
    c1.markdown(r"Let $x = 0$")
    c1.markdown(r"&emsp;&emsp; $r(0): 0^2 - 3(0) - 4 = 0 \implies -4 = 0 \equiv \text{F}$")
    c1.markdown(r"&emsp;&emsp; $s(0): 0^2 - 3 > 0 \implies -3 > 0 \equiv \text{F}$")
    c1.markdown(r"&emsp;&emsp; $\text{F} \lor \text{F} \equiv \text{F}$")
    c1.markdown(r"**$\therefore$ False**")
    c2.markdown(r"**Rule:**")
    c2.markdown(r"Idempotent Law")
    c2.markdown(r"&emsp; $p \lor p \equiv p$")
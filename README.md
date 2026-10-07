# Lab 01: MDP Modeling and Finite-Horizon Dynamic Programming

A worked learning companion to Christian Osendorfer’s lab. The original [lab01.html](lab01.html) is the authority; it is preserved without changes. Problems 1–4 are compulsory, 5–6 recommended practice, and 7–9 optional self-study. This companion works through all of them.

<a id="python-code"></a>

## Python implementations for all nine problems

The complete Python implementations are in [examples/](examples/). Each problem has a runnable script, and its code is explained line by line in the corresponding chapter below. Use Python 3.9 or newer; all examples use the standard library, so no packages need to be installed. Run the commands below from the repository directory. Each command starts Python and executes the named file.

| Problem | Complete Python file | What it computes | Run command |
| --- | --- | --- | --- |
| 1 | [problem01.py](examples/problem01.py) | Greedy path, backward values, optimal actions, and optimal path | `python3 examples/problem01.py` |
| 2 | [problem02.py](examples/problem02.py) | Cautious-policy values and exact trajectory enumeration | `python3 examples/problem02.py` |
| 3 | [problem03.py](examples/problem03.py) | Optimal values, ties, policy losses, and behavioral policy counts | `python3 examples/problem03.py` |
| 4 | [problem04.py](examples/problem04.py) | Q-values, single-stage policy improvement, and the remaining-gap correction | `python3 examples/problem04.py` |
| 5 | [problem05.py](examples/problem05.py) | Inventory values and all optimal actions for horizons 1, 2, and 3 | `python3 examples/problem05.py` |
| 6 | [problem06.py](examples/problem06.py) | Exact offer thresholds and expected sale value for four stages | `python3 examples/problem06.py` |
| 7 | [problem07.py](examples/problem07.py) | Wear-dependent augmented states, optimal values, and operate/repair policy evaluation | `python3 examples/problem07.py` |
| 8 | [problem08.py](examples/problem08.py) | Salvage switching points and backward induction for salvage 0, 10, and 30 | `python3 examples/problem08.py` |
| 9 | [problem09.py](examples/problem09.py) | Return distributions, means, variances, and the expected-utility recursion | `python3 examples/problem09.py` |

The shared [common.py](examples/common.py) contains the exact machine data, the backward-recursion function, and a helper that preserves every maximizing action when values tie. The scripts that need it import it automatically; its code is fully explained in problems 2 and 3. Conceptual questions and proofs are worked through in the README alongside the numerical implementations.

## How to use this book

Read each subquestion in its original order: question, definitions, hand calculation, Python, explanation of every line, and comparison with executed output. The letter labels are added here because the source uses unlettered bullets. They preserve the source’s order. A code excerpt is part of its named runnable file; execute that complete file to supply definitions from earlier excerpts.

The HTML was read only inside `main#quarto-document-content`. Each KaTeX expression was recovered once from its `annotation` with `encoding="application/x-tex"`; the visual HTML and MathML copies were skipped. Scripts and styling were ignored. Both numerical tables are reproduced below. Thus minus signs, indices, conditioning, and terminal values come from the source, rather than a text-only guess.

**Progress:** all nine problems and all 37 subquestions are complete. Every subquestion has the six teaching sections; numerical sections include executed output. See the [verification record](#verification) for the source audit and counting convention.

## Contents and coverage checklist

- [Python implementations for all nine problems](#python-code)
- [Conventions and Python setup](#conventions)

**[Problem 1: Deterministic backward induction](#problem-1)**

- [x] [1(a)](#1a) — Determine the path from $x$ that results from always choosing the action with the largest immediate reward, and its total reward.
- [x] [1(b)](#1b) — Compute the optimal value functions $V_3^*$, $V_2^*$, $V_1^*$, and $V_0^*$.
- [x] [1(c)](#1c) — For each nonterminal state and each time $h=0,1,2$, give one optimal action. Recover the optimal path from $x$ and compare it with the greedy path.
- [x] [1(d)](#1d) — Explain why the optimal action can depend on time even though the transition and reward tables do not depend on time.
- [x] [1(e)](#1e) — Bertsekas minimizes cost instead of maximizing reward. State how the problem is converted into his form, which quantities are computed backward, and which decisions are recovered forward.

**[Problem 2: Machine MDP and policy evaluation](#problem-2)**

- [x] [2(a)](#2a) — Define the machine MDP formally. Specify the state space, the admissible action sets $\mathcal{A}(s)$, the reward function, the transition kernel, the horizon, and the terminal value.
- [x] [2(b)](#2b) — In the lecture, rewards are deterministic. Suppose instead that the reward $r_h$ is random, with conditional mean $\bar r(s,a)=\mathbb{E}[r_h\mid s_h=s,a_h=a]$. Starting from the definition $V_h^\pi(s)=\mathbb{E}\big[\sum_{h'=h}^{H-1} r_{h'} \mid s_h=s\big]$, derive the Bellman consistency recursion for a general Markovian policy $\pi_h(a\mid s)$. State where the Markov property of the environment and the Markovian form of the policy are used, and explain why only $\bar r$ enters the recursion.
- [x] [2(c)](#2c) — For the cautious policy in the machine MDP, compute $V_2^\pi(W)$, $V_2^\pi(B)$, $V_1^\pi(W)$, and $V_1^\pi(B)$.
- [x] [2(d)](#2d) — Verify $V_1^\pi(W)$ by enumerating all trajectories that start in $W$ at $h=1$, with their probabilities and total rewards. How does the number of trajectories grow with the horizon $H$, and how many numbers does the backward recursion compute?

**[Problem 3: Optimal values and cautious-policy loss](#problem-3)**

- [x] [3(a)](#3a) — Write the Bellman optimality recursion for the machine MDP in explicit finite-horizon notation.
- [x] [3(b)](#3b) — Compute $V_2^*(W)$, $V_2^*(B)$, $V_1^*(W)$, and $V_1^*(B)$.
- [x] [3(c)](#3c) — Starting from $W$ on day $0$, determine the optimal first action.
- [x] [3(d)](#3d) — Compare $V_1^\pi$ of the cautious policy with $V_1^*$. Determine the loss in each state and identify the decision of the cautious policy that causes it.
- [x] [3(e)](#3e) — With start state $W$, count the deterministic Markov policies and the deterministic history-dependent policies that lead to different behavior. Explain what the lecture’s result that an optimal Markovian deterministic policy exists saves.

**[Problem 4: Q-values and policy improvement](#problem-4)**

- [x] [4(a)](#4a) — Compute $Q_1^\pi(s,a)$ for all four state-action pairs.
- [x] [4(b)](#4b) — Let $\pi'$ agree with $\pi$ at $h=0$ and $h=2$ and be greedy with respect to $Q_1^\pi$ at $h=1$. Compute $V_1^{\pi'}(W)$ and $V_1^{\pi'}(B)$, compare them with $V_1^*$ from problem 3, and state which further change of the policy closes the remaining gap.
- [x] [4(c)](#4c) — Prove in general: if $\pi'$ differs from $\pi$ only at a stage $k$, where it is greedy with respect to $Q_k^\pi$, then $V_h^{\pi'}(s)\ge V_h^\pi(s)$ for all $h\le k$ and all $s$, and $V_h^{\pi'}=V_h^\pi$ for $h>k$.
- [x] [4(d)](#4d) — Explain why $Q_h^\pi$ is enough for greedy improvement, while $V_h^\pi$ alone is not enough unless the model is known.

**[Problem 5: Horizon effects](#problem-5)**

- [x] [5(a)](#5a) — For horizon $H=1$, determine the optimal first action at $l=1$.
- [x] [5(b)](#5b) — For horizon $H=2$, determine the optimal first action at $l=1$.
- [x] [5(c)](#5c) — For horizon $H=3$, determine the optimal first action at $l=1$.
- [x] [5(d)](#5d) — Give a concise explanation of how the horizon changes the meaning of “optimal” in this example.

**[Problem 6: Selling an asset](#problem-6)**

- [x] [6(a)](#6a) — Formulate the problem as a finite-horizon MDP: state, actions, rewards, and transitions.
- [x] [6(b)](#6b) — Let $W_h$ denote the optimal expected reward at stage $h$ before the offer $X_h$ is observed. Derive the recursion $W_h = \mathbb{E}[\max(X_h, W_{h+1})]$ with $W_{H-1}=\mathbb{E}[X_{H-1}]$, and show that the optimal policy is a threshold rule.
- [x] [6(c)](#6c) — Show that $\mathbb{E}[\max(X,c)] = (1+c^2)/2$ for $X\sim\text{Uniform}[0,1]$ and $c\in[0,1]$. Compute the thresholds and $W_0$ for $H=4$, and compare $W_0$ with the value of accepting the first offer.
- [x] [6(d)](#6d) — Explain why the threshold decreases as fewer stages remain.

**[Problem 7: Wear and augmented state](#problem-7)**

- [x] [7(a)](#7a) — Explain why the process with state space $\{W,B\}$ is no longer Markov under this rule.
- [x] [7(b)](#7b) — Augment the working state with a binary variable $c$ indicating whether the machine was operated on the previous day. Specify the augmented state space and the transition kernel.
- [x] [7(c)](#7c) — Write the finite-horizon Bellman recursion for the augmented MDP. For $H=3$ and zero terminal value, compute $V_0^*(W,0)$ and the optimal actions at $h=1$ in all augmented states.
- [x] [7(d)](#7d) — Evaluate the policy “operate whenever the machine works, repair when it is broken” in the augmented model, starting from $(W,0)$. Compare its value with $V_0^*(W,0)$ and explain the difference.

**[Problem 8: Terminal salvage and switching](#problem-8)**

- [x] [8(a)](#8a) — Derive $V_2^*(W)$ and $V_2^*(B)$ as piecewise-linear functions of $\lambda$.
- [x] [8(b)](#8b) — Find every value of $\lambda$ at which the optimal action at time $2$ changes.
- [x] [8(c)](#8c) — Perform the remaining backward-induction steps for $\lambda\in\{0,10,30\}$ and report the optimal first action from $W$.
- [x] [8(d)](#8d) — Explain why changing only the terminal value can change decisions several stages earlier.

**[Problem 9: Risk at a tie](#problem-9)**

- [x] [9(a)](#9a) — For each of the two actions, compute the distribution of $G_1$, its mean, and its variance. Which action does a manager choose who maximizes $\mathbb{E}[G_1] - \beta\,\mathrm{Var}[G_1]$ with $\beta>0$?
- [x] [9(b)](#9b) — Use the law of total variance, $\mathrm{Var}[X]=\mathbb{E}\big[\mathrm{Var}[X\mid Y]\big]+\mathrm{Var}\big[\mathbb{E}[X\mid Y]\big]$, to write $\mathrm{Var}[G_h \mid s_h=s, a_h=a]$ in terms of the next state $s_{h+1}$. Explain why the mean–variance criterion does not satisfy a recursion of the form “reward now plus a value of the successor state”.
- [x] [9(c)](#9c) — Let $c_h$ denote the reward accumulated before stage $h$. Show that for any function $u$, the criterion $\mathbb{E}[u(G_0)]$ satisfies a backward recursion on the augmented state $(s_h, c_h)$, and state its terminal condition. Explain why $\mathbb{E}[G_0] - \beta\,\mathrm{Var}[G_0]$ is not of this form.

- [Verification and source audit](#verification)

<a id="conventions"></a>

## Conventions and Python setup

A **state** records the information needed to predict the next outcome when an action is chosen. An **action** is a permitted decision at that state. A **transition** changes the state; a **reward** is the amount earned at a decision. A **return** adds rewards over multiple decisions. A **policy** tells us how to choose actions. A **state value** is an expected return from a state. An **action value** is an expected return when a particular action is used first. Each exercise will define these locally again when needed.

Unless stated otherwise, decision stages are $h=0,1,\ldots,H-1$. The horizon $H$ is the number of decisions. There are $H-h$ decisions remaining at stage $h$. Reward $r_h$ is earned for the action at stage $h$, then state $s_{h+1}$ is reached. At $h=H$ there is no action; $V_H$ is a boundary value. A terminal state can be reached before the horizon; the source makes $g$ an absorbing state with zero-reward `stop`. The inventory exercise has no such terminal state. Problem 8 deliberately changes the horizon’s boundary value.

$V_h^\pi(s)$ evaluates a specified policy $\pi$; $V_h^*(s)$ is the best achievable expected return. The superscript star means optimal, not multiplication. $Q_h^\pi(s,a)$ fixes the first action $a$, then follows $\pi$; $Q_h^*(s,a)$ uses an optimal continuation. $\max$ gives a number; $\arg\max$ gives the action or set of actions attaining that number. All ties are recorded. Selecting the first tied action in a script is a presentation choice, not a claim of uniqueness.

Use Python 3.9 or newer. The examples require only its standard library; no package installation or virtual environment is necessary. From the repository directory, run a chapter with `python3 examples/problem01.py`, replacing `01` with `02` through `09`. `python3` starts Python; the path selects the file to execute. Python finds `common.py` beside these scripts. It is an explained helper, not a separate command to run.

Python executes ordinary statements from top to bottom. Indentation groups the body of `for`, `if`, `else`, and `def`. An assignment `name = expression` stores a result; `==` compares two results. A list `[...]` stores ordered entries indexed starting at zero. A dictionary `{key: value}` gives a named lookup: `values[1]["W"]` means stage 1, then working state. A tuple `(reward, transitions)` groups two pieces of information; `reward, transitions = ...` unpacks them. A function starts with `def`, receives its named parameters in a call, and sends its result back with `return`. Each actual use is explained again beside its code.

The machine examples use `fractions.Fraction` to represent exact rational numbers. `Fraction("0.6")` equals $3/5$ exactly; a quoted decimal avoids the binary approximation of a floating-point literal. Integers, fractions, and arithmetic can be combined. Conversion with `float(...)` is used only for display. `.2f` displays two digits after the decimal point, `.9f` nine; neither changes the stored value. This keeps exact ties exact. The asset script also prints its exact fractions so displayed rounding can be checked.
<a id="problem-1"></a>

## Problem 1: Deterministic backward induction

**Source setup (verbatim, with TeX recovered from the HTML):**

Consider the deterministic maximum-reward path problem with states $\mathcal{S}=\{x,y,z,g\}$ and terminal state $g$. The horizon is $H=3$, and the start state is $x$. The available actions and rewards are:


| State | Action | Next state | Reward |
| --- | --- | --- | --- |
| $x$ | $a$ | $y$ | $0$ |
| $x$ | $b$ | $z$ | $1$ |
| $y$ | $a$ | $g$ | $4$ |
| $y$ | $b$ | $z$ | $0$ |
| $z$ | $a$ | $g$ | $2$ |
| $z$ | $b$ | $y$ | $1$ |
| $g$ | stop | $g$ | $0$ |

<a id="1a"></a>

### 1(a) The greedy path

> Determine the path from $x$ that results from always choosing the action with the largest immediate reward, and its total reward.

#### 1. Read the question carefully.

We know the start $x$, the seven rows of the table, and three decisions. Find the path made by comparing only rewards in the current row group. We are not yet calculating the best three-stage return. For example, $(x,b)$ moves to $z$ and earns 1; $(z,b)$ moves to $y$ and earns 1. At $g$ only `stop` is available.

#### 2. Explain every concept and symbol.

A deterministic transition has one certain successor. Write it $f(s,a)$, where $s$ is the current state and $a$ an admissible action. The immediate reward $r(s,a)$ is the table's last column. The total return is $G_0=r_0+r_1+r_2$. A greedy action maximizes $r(s,a)$; it ignores rewards after this action. Stage $h=0$ starts at $x$, stage $h=1$ at the first successor, and stage $h=2$ at the second successor. $g$ is an absorbing terminal state: later stops have reward zero, even before the horizon is reached.

#### 3. Solve it by hand.

At $h=0$, compare $r(x,a)=0$ and $r(x,b)=1$. Choose $b$, earn 1, and reach $z$.

At $h=1$, compare $r(z,a)=2$ and $r(z,b)=1$. Choose $a$, earn 2, and reach $g$.

At $h=2$, choose the sole action `stop`, earn 0, and remain at $g$.

Thus the state sequence is $x\to z\to g\to g$, the action sequence is $(b,a,\mathrm{stop})$, and $G_0=1+2+0=3$. The shorter description $x\to z\to g$ omits the zero-reward absorbing step.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem01.py](examples/problem01.py) (run the whole file; earlier excerpts supply its inputs):

```python
model = {
    "x": {"a": ("y", 0), "b": ("z", 1)},
    "y": {"a": ("g", 4), "b": ("z", 0)},
    "z": {"a": ("g", 2), "b": ("y", 1)},
    "g": {"stop": ("g", 0)},
}
horizon = 3
state = "x"
greedy_path = [state]
greedy_reward = 0
for stage in range(horizon):
    action = None
    largest_reward = None
    for candidate_action in model[state]:
        candidate_reward = model[state][candidate_action][1]
        if largest_reward is None or candidate_reward > largest_reward:
            action = candidate_action
            largest_reward = candidate_reward
    successor, reward = model[state][action]
    greedy_reward += reward
    state = successor
    greedy_path.append(state)
print("Greedy:", " -> ".join(greedy_path), "reward =", greedy_reward)
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `model = {` | Assign a dictionary to `model`. Each state key contains a dictionary of actions; each action maps to a tuple `(successor, reward)`. |
| 2. `"x": {"a": ("y", 0), "b": ("z", 1)},` | At key `"x"`, action `"a"` stores `("y", 0)` and `"b"` stores `("z", 1)`. For example, `model["x"]["b"][1]` is reward 1; index 0 is successor `"z"`. |
| 3. `"y": {"a": ("g", 4), "b": ("z", 0)},` | Encode the two rows at `y`: going to `g` earns 4; going to `z` earns 0. |
| 4. `"z": {"a": ("g", 2), "b": ("y", 1)},` | Encode the two rows at `z`: going to `g` earns 2; going to `y` earns 1. |
| 5. `"g": {"stop": ("g", 0)},` | Encode the absorbing state `g`, with its single zero-reward action. |
| 6. `}` | Close the outer dictionary; this brace completes the data assignment. |
| 7. `horizon = 3` | Store the number of decisions, 3, in `horizon`. |
| 8. `state = "x"` | Set the current state to the supplied start `x`. |
| 9. `greedy_path = [state]` | Create a list containing the start; later successors will be appended in order. |
| 10. `greedy_reward = 0` | Initialize the reward sum to zero before any decision. |
| 11. `for stage in range(horizon):` | `range(horizon)` produces 0, 1, 2. Repeat the indented decision code once per stage. |
| 12. `action = None` | `None` means no action has yet been selected at this stage. |
| 13. `largest_reward = None` | Initialize the best immediate reward as unknown. This permits rewards to be negative in other models. |
| 14. `for candidate_action in model[state]:` | Loop over admissible action keys of the current state. At `x` these are `a`, then `b`. |
| 15. `candidate_reward = model[state][candidate_action][1]` | Index the action tuple at position 1 to obtain its immediate reward. |
| 16. `if largest_reward is None or candidate_reward > largest_reward:` | `is None` handles the first candidate; `or` also accepts a later strictly larger reward. At `x`, 1 replaces 0. |
| 17. `action = candidate_action` | Save the action whose reward is currently largest. |
| 18. `largest_reward = candidate_reward` | Save that reward for later comparisons in this stage. |
| 19. `successor, reward = model[state][action]` | Unpack the chosen tuple into `successor` and `reward`. At the first decision these are `z` and 1. |
| 20. `greedy_reward += reward` | `+=` adds the chosen reward to the running total: 0 becomes 1, then 3, then stays 3. |
| 21. `state = successor` | Move the current state to its successor. |
| 22. `greedy_path.append(state)` | Append that state to the path list, giving `["x", "z", "g", "g"]` after all iterations. |
| 23. `print("Greedy:", " -> ".join(greedy_path), "reward =", greedy_reward)` | `print` displays the label, joined path, and reward. `" -> ".join(...)` inserts an arrow between list entries. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Greedy: x -> z -> g -> g reward = 3
```

The executed path and reward match all three hand steps. Run `python3 examples/problem01.py`; its later output belongs to 1(b) and 1(c).

<a id="1b"></a>

### 1(b) Values computed backward

> Compute the optimal value functions $V_3^*$, $V_2^*$, $V_1^*$, and $V_0^*$.

#### 1. Read the question carefully.

Compute the best future reward at every state at stages 3, 2, 1, and 0. Unlike 1(a), the calculation includes all remaining rewards. The boundary is zero at every state when no decisions remain; reaching stage 3 does not require reaching $g$.

#### 2. Explain every concept and symbol.

$V_h^*(s)$ is the maximum return starting from state $s$ before decision $h$. The star means optimization over policies. A candidate action value is $r(s,a)+V_{h+1}^*(f(s,a))$: immediate reward plus optimal continuation at its certain successor. $\max_{a\in\mathcal A(s)}$ compares only actions allowed at $s$. The boundary $V_3^*(s)=0$ closes the recursion. Calculate in decreasing $h$ because stage $h$ needs stage $h+1$.

#### 3. Solve it by hand.

The general rule is

$$V_h^*(s)=\max_{a\in\mathcal A(s)}\{r(s,a)+V_{h+1}^*(f(s,a))\},\qquad V_3^*(s)=0.$$

First set $(V_3^*(x),V_3^*(y),V_3^*(z),V_3^*(g))=(0,0,0,0)$. Then substitute the successor values in each table row:

| Stage | State | Action $a$: reward + continuation | Action $b$: reward + continuation | Maximum |
| --- | --- | --- | --- | --- |
| 2 | $x$ | $0+0=0$ | $1+0=1$ | 1 |
| 2 | $y$ | $4+0=4$ | $0+0=0$ | 4 |
| 2 | $z$ | $2+0=2$ | $1+0=1$ | 2 |
| 1 | $x$ | $0+4=4$ | $1+2=3$ | 4 |
| 1 | $y$ | $4+0=4$ | $0+2=2$ | 4 |
| 1 | $z$ | $2+0=2$ | $1+4=5$ | 5 |
| 0 | $x$ | $0+4=4$ | $1+5=6$ | 6 |
| 0 | $y$ | $4+0=4$ | $0+5=5$ | 5 |
| 0 | $z$ | $2+0=2$ | $1+4=5$ | 5 |

For $g$, the sole candidate is $0+V_{h+1}^*(g)=0$ at each of stages 2, 1, and 0. Thus

$$V_2^*=(1,4,2,0),\quad V_1^*=(4,4,5,0),\quad V_0^*=(6,5,5,0)$$

in state order $(x,y,z,g)$. For example, the 6 at $x$ is achievable by earning 1 now and the optimal remaining 5 from $z$. There are no ties in these comparisons.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem01.py](examples/problem01.py) (run the whole file; earlier excerpts supply its inputs):

```python
values = [{} for stage in range(horizon + 1)]
values[horizon] = {state: 0 for state in model}
optimal_actions = [{} for stage in range(horizon)]
for stage in range(horizon - 1, -1, -1):
    for state in model:
        candidates = {}
        for action in model[state]:
            successor, reward = model[state][action]
            candidates[action] = reward + values[stage + 1][successor]
        best_value = max(candidates.values())
        values[stage][state] = best_value
        optimal_actions[stage][state] = []
        for action, candidate in candidates.items():
            if candidate == best_value:
                optimal_actions[stage][state].append(action)
    print(f"V_{stage} = {values[stage]}")
print(f"V_3 = {values[3]}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `values = [{} for stage in range(horizon + 1)]` | Create four separate empty dictionaries, one for each stage 0 through 3. The comprehension repeats `{}` for each element of `range(4)`. |
| 2. `values[horizon] = {state: 0 for state in model}` | At index `horizon` (3), assign zero to each state key. This implements the boundary rather than an action. |
| 3. `optimal_actions = [{} for stage in range(horizon)]` | Create three separate dictionaries to record optimal actions at decision stages 0, 1, 2. |
| 4. `for stage in range(horizon - 1, -1, -1):` | `range(2, -1, -1)` visits 2, 1, 0; the stopping value -1 is excluded. This is backward induction. |
| 5. `for state in model:` | Loop over `x`, `y`, `z`, `g`, including states not on the eventual start-state path. |
| 6. `candidates = {}` | Start an empty dictionary for this state and stage; it will map each action to its candidate return. |
| 7. `for action in model[state]:` | Visit the admissible actions of that state. |
| 8. `successor, reward = model[state][action]` | Unpack its stored certain successor and immediate reward. |
| 9. `candidates[action] = reward + values[stage + 1][successor]` | Add the current reward to the already computed next-stage value. At stage 1, `z,b` gives `1 + values[2]["y"] = 5`. |
| 10. `best_value = max(candidates.values())` | `.values()` supplies the candidate numbers, and `max` selects their largest value. |
| 11. `values[stage][state] = best_value` | Store that number at the current stage and state; for example, `values[1]["z"] = 5`. |
| 12. `optimal_actions[stage][state] = []` | Create an empty list to hold every maximizing action for this stage and state. |
| 13. `for action, candidate in candidates.items():` | `.items()` gives action/value pairs; examine each candidate again to recover decisions. |
| 14. `if candidate == best_value:` | `==` checks equality with the chosen maximum, retaining ties if they occur. |
| 15. `optimal_actions[stage][state].append(action)` | Append each maximizing action key. Here every list has one action. |
| 16. `print(f"V_{stage} = {values[stage]}")` | After the state loop, print the completed dictionary for the current stage. The f-string substitutes `stage` and the dictionary into braces. |
| 17. `print(f"V_3 = {values[3]}")` | Print the boundary dictionary, which was assigned before the backward loop. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
V_2 = {'x': 1, 'y': 4, 'z': 2, 'g': 0}
V_1 = {'x': 4, 'y': 4, 'z': 5, 'g': 0}
V_0 = {'x': 6, 'y': 5, 'z': 5, 'g': 0}
V_3 = {'x': 0, 'y': 0, 'z': 0, 'g': 0}
```

The dictionaries agree entry by entry with the table, including all zero values at $g$. Integer arithmetic is exact.

<a id="1c"></a>

### 1(c) Recovering decisions and the optimal path

> For each nonterminal state and each time $h=0,1,2$, give one optimal action. Recover the optimal path from $x$ and compare it with the greedy path.

#### 1. Read the question carefully.

Use the values already calculated in 1(b). Give an optimal action at all three nonterminal states at each decision time, then follow the stage-specific actions from $x$. Compare the resulting return with 1(a).

#### 2. Explain every concept and symbol.

$\arg\max$ returns maximizing actions rather than their value. Write $\pi_h^*(s)\in\arg\max_a[r(s,a)+V_{h+1}^*(f(s,a))]$. Here the policy is a table indexed by both state and stage. Recovering a path means starting at the specified state and applying the selected action forward through time; this is different from computing values backward.

#### 3. Solve it by hand.

Read the larger candidates from the table in 1(b):

| Stage $h$ | At $x$ | At $y$ | At $z$ | At $g$ |
| --- | --- | --- | --- | --- |
| 0 | $b$ | $b$ | $b$ | stop |
| 1 | $a$ | $a$ | $b$ | stop |
| 2 | $b$ | $a$ | $a$ | stop |

Start at $x$ at stage 0. Choose $b$, reach $z$, and earn 1. At $z$ at stage 1, choose $b$, reach $y$, and earn 1. At $y$ at stage 2, choose $a$, reach $g$, and earn 4. The optimal path is $x\to z\to y\to g$ with return $1+1+4=6=V_0^*(x)$. Greedy earns 3; the optimal plan earns 3 more because at stage 1 it accepts reward 1 instead of 2 to reach the reward-4 action on the last stage.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem01.py](examples/problem01.py) (run the whole file; earlier excerpts supply its inputs):

```python
for stage in range(horizon):
    print(f"Actions h={stage}: {optimal_actions[stage]}")
state = "x"
optimal_path = [state]
total_reward = 0
for stage in range(horizon):
    action = optimal_actions[stage][state][0]
    state, reward = model[state][action]
    total_reward += reward
    optimal_path.append(state)
print("Optimal:", " -> ".join(optimal_path), "reward =", total_reward)
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `for stage in range(horizon):` | Loop forward over stages 0, 1, 2 to display the recovered policy table. |
| 2. `print(f"Actions h={stage}: {optimal_actions[stage]}")` | Print all stored action lists for this stage, including `stop` at `g`. |
| 3. `state = "x"` | Reset the state to `x`; the earlier greedy loop had ended at `g`. |
| 4. `optimal_path = [state]` | Start a fresh path list with this initial state. |
| 5. `total_reward = 0` | Reset the reward accumulator to zero. |
| 6. `for stage in range(horizon):` | Follow three decisions forward in stage order. |
| 7. `action = optimal_actions[stage][state][0]` | Look up the current stage, current state, and first maximizing action. `[0]` selects a presentation action if a tie exists; there are no ties here. |
| 8. `state, reward = model[state][action]` | Unpack the model tuple into the new state and current reward. Python evaluates the right-hand lookup using the old state before assigning the new one. |
| 9. `total_reward += reward` | Add the current reward to the total: 1, then 2, then 6. |
| 10. `optimal_path.append(state)` | Append the new state, producing `x,z,y,g`. |
| 11. `print("Optimal:", " -> ".join(optimal_path), "reward =", total_reward)` | Print the joined optimal path and its exact total reward. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Actions h=0: {'x': ['b'], 'y': ['b'], 'z': ['b'], 'g': ['stop']}
Actions h=1: {'x': ['a'], 'y': ['a'], 'z': ['b'], 'g': ['stop']}
Actions h=2: {'x': ['b'], 'y': ['a'], 'z': ['a'], 'g': ['stop']}
Optimal: x -> z -> y -> g reward = 6
```

The executed stage table and path match the hand reconstruction. The first action alone is not a complete policy; the later decision at $z$ matters.

<a id="1d"></a>

### 1(d) Why time changes the action

> Explain why the optimal action can depend on time even though the transition and reward tables do not depend on time.

#### 1. Read the question carefully.

The rewards and transitions are fixed, yet the action table in 1(c) changes with the stage. Explain that dependence using this exercise rather than changing the model.

#### 2. Explain every concept and symbol.

A time-homogeneous model has rewards and transition rules independent of $h$. A finite-horizon optimal policy can still be time-dependent because $V_{h+1}^*$ depends on how many opportunities remain. The relevant comparison is the full candidate return, not just the table's reward.

#### 3. Solve it by hand.

At $z$ with one decision left ($h=2$), action $a$ earns $2+0=2$ and $b$ earns $1+0=1$, so choose $a$. With two decisions left ($h=1$), $a$ gives $2+V_2^*(g)=2$, while $b$ gives $1+V_2^*(y)=1+4=5$, so choose $b$. The transition to $y$ is worth exploiting only when there is a later decision. The model has stayed fixed; the continuation value has changed.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No new output is required. The `z` actions in the executed 1(c) table are `b` at stage 1 and `a` at stage 2, exactly the decisions justified here.

<a id="1e"></a>

### 1(e) Converting rewards into costs

> Bertsekas minimizes cost instead of maximizing reward. State how the problem is converted into his form, which quantities are computed backward, and which decisions are recovered forward.

#### 1. Read the question carefully.

Express the same optimization using costs, identify the backward quantities, and identify the forward decisions. This is a sign conversion, with no change to the paths available.

#### 2. Explain every concept and symbol.

Define stage cost $c(s,a)=-r(s,a)$ and terminal cost $J_3(s)=-V_3(s)=0$. $J_h^*(s)$ means minimum total future cost. $\min$ chooses the smallest number; $\arg\min$ gives the actions attaining it. The symbol $c$ here is a cost, not the wear indicator in problem 7 or accumulated reward in problem 9.

#### 3. Solve it by hand.

For any path, total cost is $\sum_h c_h=-\sum_h r_h$, so a larger reward is precisely a smaller cost. Therefore

$$J_h^*(s)=\min_a\{c(s,a)+J_{h+1}^*(f(s,a))\}=-V_h^*(s).$$

To check the equality, substitute $c=-r$ and $J_{h+1}^*=-V_{h+1}^*$: each cost candidate is the negative of the corresponding reward candidate. Taking its minimum negates the maximum. Start with the zero boundary and repeat this argument backward.

In state order $(x,y,z,g)$, $J_2^*=(-1,-4,-2,0)$, $J_1^*=(-4,-4,-5,0)$, and $J_0^*=(-6,-5,-5,0)$. At $(h,s)=(0,x)$, the cost candidates are $0+(-4)=-4$ for $a$ and $-1+(-5)=-6$ for $b$; choose $b$. Compute these minimum costs and store minimizing actions backward. Starting at $x$, recover the actions $(b,b,a)$ and the visited states forward. The optimal reward 6 corresponds to cost -6.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

There is no separate cost script. Negating every entry in the verified value tables gives the stated cost tables; checking the two cost candidates at the start verifies that the selected action is preserved.

<a id="problem-2"></a>

## Problem 2: The machine MDP and policy evaluation

**Source setup (verbatim, with TeX recovered from the HTML):**

A small repair service manages one machine over three days. At the beginning of each day the machine is either working, denoted by $W$, or broken, denoted by $B$. If the machine is working, the manager can either operate it or maintain it. If the machine is broken, the manager can either repair it or replace it. We refer to this problem as the machine MDP.


The one-day rewards and transition probabilities are:


| State | Action | Reward | Next state probabilities |
| --- | --- | --- | --- |
| $W$ | operate | $8$ | $P(W)=0.6$, $P(B)=0.4$ |
| $W$ | maintain | $5$ | $P(W)=0.9$, $P(B)=0.1$ |
| $B$ | repair | $-2$ | $P(W)=0.7$, $P(B)=0.3$ |
| $B$ | replace | $-6$ | $P(W)=1$, $P(B)=0$ |


The horizon is $H=3$, and the terminal value is zero. Consider the cautious policy $\pi_h(W)=\text{maintain}, \qquad \pi_h(B)=\text{repair}
\qquad \text{for all } h=0,1,2.$

<a id="2a"></a>

### 2(a) Specifying the model

> Define the machine MDP formally. Specify the state space, the admissible action sets $\mathcal{A}(s)$, the reward function, the transition kernel, the horizon, and the terminal value.

#### 1. Read the question carefully.

List the mathematical ingredients of the three-day decision problem, using the source table. At this point we are specifying the environment, not finding its best policy. A row such as $(B,\mathrm{repair})$ gives reward -2 now and next-day probabilities 0.7 for $W$ and 0.3 for $B$.

#### 2. Explain every concept and symbol.

An MDP is a Markov decision process. Its state contains the information needed for the distribution of future outcomes when we choose an action. $\mathcal S$ is the set of states; $\mathcal A(s)$ is the set of admissible actions at state $s$. The reward function $r$ assigns a number to a state/action pair. The kernel $P(s'\mid s,a)$ is the probability of successor $s'$ conditional on state $s$ and action $a$. The vertical bar means “given.” Each row's probabilities are nonnegative and sum to 1. Negative rewards represent costs. The horizon $H=3$ means decisions on days 0, 1, 2, then a boundary at day 3.

#### 3. Solve it by hand.

The formal model is

$$\mathcal S=\{W,B\},\quad\mathcal A(W)=\{\mathrm{operate},\mathrm{maintain}\},\quad\mathcal A(B)=\{\mathrm{repair},\mathrm{replace}\}.$$

The reward function and kernel are exactly:

| $s$ | $a$ | $r(s,a)$ | $P(W\mid s,a)$ | $P(B\mid s,a)$ |
| --- | --- | --- | --- | --- |
| $W$ | operate | 8 | 0.6 | 0.4 |
| $W$ | maintain | 5 | 0.9 | 0.1 |
| $B$ | repair | -2 | 0.7 | 0.3 |
| $B$ | replace | -6 | 1 | 0 |

For example, $0.6+0.4=1$ verifies the operate row. Replacement guarantees a working successor but costs 6. The boundary is $V_3(s)=0$ for both states: a working machine at the horizon has no salvage value here. Neither $W$ nor $B$ is an absorbing terminal state; decisions end because the three days are over. The cautious policy is the additional rule $\pi_h(W)=\mathrm{maintain}$ and $\pi_h(B)=\mathrm{repair}$ at each decision stage. It is separate from the model.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/common.py](examples/common.py) (run the whole file; earlier excerpts supply its inputs):

```python
from fractions import Fraction

machine = {
    "W": {
        "operate": (Fraction(8), {"W": Fraction("0.6"), "B": Fraction("0.4")}),
        "maintain": (Fraction(5), {"W": Fraction("0.9"), "B": Fraction("0.1")}),
    },
    "B": {
        "repair": (Fraction(-2), {"W": Fraction("0.7"), "B": Fraction("0.3")}),
        "replace": (Fraction(-6), {"W": Fraction(1), "B": Fraction(0)}),
    },
}
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from fractions import Fraction` | Import the standard-library class `Fraction`, which stores exact rational numbers and supports ordinary arithmetic. |
| 2. `machine = {` | Assign a nested dictionary to `machine`, the reward and transition model. |
| 3. `"W": {` | Open the dictionary of actions admissible at working state `"W"`. |
| 4. `"operate": (Fraction(8), {"W": Fraction("0.6"), "B": Fraction("0.4")}),` | Store operate as `(reward, transition_dictionary)`: reward 8, probabilities exactly 3/5 and 2/5. A string decimal in `Fraction` avoids binary floating-point approximation. |
| 5. `"maintain": (Fraction(5), {"W": Fraction("0.9"), "B": Fraction("0.1")}),` | Store maintain with reward 5, probabilities 9/10 and 1/10. `machine["W"]["maintain"][1]["B"]` gives 1/10. |
| 6. `},` | Close the action dictionary for `W`; the comma separates state entries. |
| 7. `"B": {` | Open the dictionary of actions admissible at broken state `"B"`. |
| 8. `"repair": (Fraction(-2), {"W": Fraction("0.7"), "B": Fraction("0.3")}),` | Store repair with reward -2 and probabilities 7/10 and 3/10. |
| 9. `"replace": (Fraction(-6), {"W": Fraction(1), "B": Fraction(0)}),` | Store replace with reward -6 and probabilities exactly 1 and 0. Its impossible broken successor is retained explicitly as data. |
| 10. `},` | Close the action dictionary for `B`. |
| 11. `}` | Close the outer model dictionary. These braces finish the data structure; they perform no extra calculation. |

#### 6. Compare the output with our hand solution.

This data-definition excerpt produces no console output. Check it by reading `machine["B"]["repair"]`: its reward is -2 and its transition probabilities are 7/10 and 3/10, matching the table. The imported model is exercised by `python3 examples/problem02.py` in 2(c).

<a id="2b"></a>

### 2(b) Deriving Bellman consistency

> In the lecture, rewards are deterministic. Suppose instead that the reward $r_h$ is random, with conditional mean $\bar r(s,a)=\mathbb{E}[r_h\mid s_h=s,a_h=a]$. Starting from the definition $V_h^\pi(s)=\mathbb{E}\big[\sum_{h'=h}^{H-1} r_{h'} \mid s_h=s\big]$, derive the Bellman consistency recursion for a general Markovian policy $\pi_h(a\mid s)$. State where the Markov property of the environment and the Markovian form of the policy are used, and explain why only $\bar r$ enters the recursion.

#### 1. Read the question carefully.

Now allow a random reward and a possibly randomized, stage-dependent Markov policy. Derive the recursion from the expected sum rather than assuming it. The machine's deterministic rewards will be a special case in 2(c).

#### 2. Explain every concept and symbol.

$r_h$ is a random reward at stage $h$. $\bar r(s,a)=\mathbb E[r_h\mid s_h=s,a_h=a]$ is its conditional mean, where $\mathbb E$ denotes a probability-weighted average. The index $h'$ in the sum is a dummy index running over reward times. A Markovian policy uses only current state and stage: $\pi_h(a\mid s)$ is the probability of choosing $a$. Policy evaluation keeps this rule fixed. The law of total expectation says to condition on an intermediate variable, compute conditional expectations, then average over that variable. Linearity of expectation permits splitting a sum even when its terms are dependent.

#### 3. Solve it by hand.

Define the remaining return $G_h=\sum_{h'=h}^{H-1}r_{h'}$. Its empty sum at $h=H$ is zero. For $h<H$, split off the current reward:

$$V_h^\pi(s)=\mathbb E[r_h+G_{h+1}\mid s_h=s].$$

Condition on the first action. Because the policy is Markovian, its action probabilities given the current history are $\pi_h(a\mid s)$:

$$V_h^\pi(s)=\sum_{a\in\mathcal A(s)}\pi_h(a\mid s)\left(\mathbb E[r_h\mid s_h=s,a_h=a]+\mathbb E[G_{h+1}\mid s_h=s,a_h=a]\right).$$

The first term is $\bar r(s,a)$ by definition. For the second, condition on the next state:

$$\mathbb E[G_{h+1}\mid s_h=s,a_h=a]=\sum_{s'\in\mathcal S}P(s'\mid s,a)\mathbb E[G_{h+1}\mid s_h=s,a_h=a,s_{h+1}=s'].$$

The environment's Markov property makes future outcome distributions depend on the successor state and subsequent actions rather than earlier history. The policy's Markovian form makes subsequent action distributions depend on successor state and subsequent stage rather than earlier history. Together they identify the last conditional expectation as $V_{h+1}^\pi(s')$. This identification applies on events of positive probability; zero-probability terms contribute zero. Consequently

$$\boxed{V_h^\pi(s)=\sum_a\pi_h(a\mid s)\left[\bar r(s,a)+\sum_{s'}P(s'\mid s,a)V_{h+1}^\pi(s')\right],\quad V_H^\pi(s)=0.}$$

Only the reward mean appears because the objective is an expected additive sum. Reward variance has no term in this objective. Independence between the current reward and successor state is unnecessary: expectation is linear. The Markov assumption must cover future dynamics; if the observed reward revealed a persistent hidden condition that affected future outcomes, the state would need to include that information. For a deterministic policy, the action sum selects its single chosen action with probability 1.

#### 4. Translate the reasoning into simple code.

This subquestion asks for a general derivation. The numerical evaluator below implements the deterministic-policy special case, but a numerical run would not prove the conditioning identities. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No separate console output applies. Check the formula at $h=H-1$: the continuation is zero, so it reduces to the policy-weighted mean immediate reward. Setting a single action probability to 1 gives exactly the recursion used next.

<a id="2c"></a>

### 2(c) Evaluating the cautious policy

> For the cautious policy in the machine MDP, compute $V_2^\pi(W)$, $V_2^\pi(B)$, $V_1^\pi(W)$, and $V_1^\pi(B)$.

#### 1. Read the question carefully.

Compute the four requested values using maintain in $W$ and repair in $B$, with the zero boundary already specified. We do not compare actions to change the policy. The script also reports stage 0 as a consistency check.

#### 2. Explain every concept and symbol.

$V_h^\pi(s)$ is the expected remaining reward under the fixed cautious policy. A successor's contribution is its probability times its next-stage value. Negative continuation values must keep their sign. An expectation can be fractional even when every individual reward is an integer.

#### 3. Solve it by hand.

For a deterministic policy,

$$V_h^\pi(s)=r(s,\pi_h(s))+\sum_{s'}P(s'\mid s,\pi_h(s))V_{h+1}^\pi(s'),\quad V_3^\pi=0.$$

At the last decision:

$$V_2^\pi(W)=5+0.9(0)+0.1(0)=5,\qquad V_2^\pi(B)=-2+0.7(0)+0.3(0)=-2.$$

At stage 1:

$$V_1^\pi(W)=5+0.9(5)+0.1(-2)=5+4.5-0.2=9.3,$$

$$V_1^\pi(B)=-2+0.7(5)+0.3(-2)=-2+3.5-0.6=0.9.$$

In the working calculation, the 0.9 term weights a working successor whose last-stage cautious reward is 5; the 0.1 term weights a broken successor whose repair costs 2. In the broken calculation, successful repair has probability 0.7 and failed repair probability 0.3.

For the script's extra stage:

$$V_0^\pi(W)=5+0.9(9.3)+0.1(0.9)=5+8.37+0.09=13.46,$$

$$V_0^\pi(B)=-2+0.7(9.3)+0.3(0.9)=-2+6.51+0.27=4.78.$$

The helper calculates all action candidates before selecting the specified policy action, so later chapters can also inspect $Q^\pi$. This extra calculation does not turn policy evaluation into optimization.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/common.py](examples/common.py) (run the whole file; earlier excerpts supply its inputs):

```python
def backward_values(model, horizon, terminal, policy=None):
    values = [{} for stage in range(horizon + 1)]
    action_values = [{} for stage in range(horizon)]
    values[horizon] = terminal.copy()
    for stage in range(horizon - 1, -1, -1):
        for state in model:
            candidates = {}
            for action in model[state]:
                reward, transitions = model[state][action]
                candidate = reward
                for successor, probability in transitions.items():
                    candidate += probability * values[stage + 1][successor]
                candidates[action] = candidate
            action_values[stage][state] = candidates
            if policy is None:
                values[stage][state] = max(candidates.values())
            else:
                selected_action = policy[stage][state]
                values[stage][state] = candidates[selected_action]
    return values, action_values
```

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `def backward_values(model, horizon, terminal, policy=None):` | `def` defines a reusable function. `model` supplies reward/transition data, `horizon` the decision count, `terminal` the boundary dictionary, and optional `policy` a list of stage dictionaries. Default `None` requests optimization. |
| 2. `values = [{} for stage in range(horizon + 1)]` | Create `horizon + 1` independent empty dictionaries for state values. With 3 days the indices are 0, 1, 2, 3. |
| 3. `action_values = [{} for stage in range(horizon)]` | Create three independent dictionaries for action values at decision stages; there is no action dictionary at the boundary. |
| 4. `values[horizon] = terminal.copy()` | Copy the supplied terminal values into stage 3. `.copy()` avoids modifying the caller's dictionary. |
| 5. `for stage in range(horizon - 1, -1, -1):` | Visit stages 2, 1, 0 with the decreasing `range`; values at the next stage already exist. |
| 6. `for state in model:` | Visit each state key. In the machine model these are `W`, then `B`. |
| 7. `candidates = {}` | Initialize a dictionary of action candidates for this one state and stage. |
| 8. `for action in model[state]:` | Visit each admissible action for that state. |
| 9. `reward, transitions = model[state][action]` | Unpack `(reward, transitions)` from the model lookup. For maintain these are 5 and the dictionary `{W: 9/10, B: 1/10}`. |
| 10. `candidate = reward` | Start this action's candidate at its immediate reward. |
| 11. `for successor, probability in transitions.items():` | Loop over successor/probability pairs using `.items()`. |
| 12. `candidate += probability * values[stage + 1][successor]` | Add each probability-weighted continuation. At stage 1, maintain adds `(9/10)*5` and `(1/10)*(-2)` to 5. |
| 13. `candidates[action] = candidate` | Store the completed candidate under its action key. |
| 14. `action_values[stage][state] = candidates` | After all actions, store the candidate dictionary at this stage and state. These are Q-values for the continuation being evaluated. |
| 15. `if policy is None:` | Check whether the caller omitted a policy. `is None` distinguishes optimization from evaluation. |
| 16. `values[stage][state] = max(candidates.values())` | In optimization mode, store the largest action candidate as the state value. |
| 17. `else:` | Otherwise enter policy-evaluation mode, using exactly the specified action rather than a maximum. |
| 18. `selected_action = policy[stage][state]` | Look up the action at this stage and state in the supplied policy list. |
| 19. `values[stage][state] = candidates[selected_action]` | Store that action's candidate as the state value. For the cautious policy at stage 1 in `W`, select maintain's 9.3 even though operate's candidate is 10.2. |
| 20. `return values, action_values` | Return the value list and action-value list as a tuple; a caller can unpack both results. |

The chapter calls that helper as follows:

Excerpt from [examples/problem02.py](examples/problem02.py) (run the whole file; earlier excerpts supply its inputs):

```python
from common import Fraction, machine, backward_values

cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]
terminal = {"W": Fraction(0), "B": Fraction(0)}
values, action_values = backward_values(machine, 3, terminal, cautious)
for stage in (2, 1, 0):
    print(f"Vpi_{stage}: W={float(values[stage]['W']):.2f}, B={float(values[stage]['B']):.2f}")
```

#### 5. Explain every line.

For the chapter call, each line means:

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from common import Fraction, machine, backward_values` | Import exact arithmetic, the fully specified model, and the explained backward evaluator from the sibling file `common.py`. |
| 2. `cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]` | Create three separate policy dictionaries with maintain at `W` and repair at `B`. The comprehension repeats this rule for stages 0, 1, 2. |
| 3. `terminal = {"W": Fraction(0), "B": Fraction(0)}` | Specify the zero boundary using exact fractions for both states. |
| 4. `values, action_values = backward_values(machine, 3, terminal, cautious)` | Call the evaluator with a policy, so it computes $V^\pi$ rather than $V^*$. Unpack its returned tuple into `values` and `action_values`. |
| 5. `for stage in (2, 1, 0):` | Visit stages 2, 1, 0 for display, following the calculation order. |
| 6. `print(f"Vpi_{stage}: W={float(values[stage]['W']):.2f}, B={float(values[stage]['B']):.2f}")` | Print both state values. `values[stage]["W"]` indexes stage then state; `float` converts only for display and `:.2f` prints two decimals. |

Trace the helper call `backward_values(machine, 3, terminal, cautious)`: stage 2 stores 5 and -2. At stage 1, `W` builds candidates operate 10.2 and maintain 9.3, then selects maintain; `B` builds repair 0.9 and replace -1, then selects repair. At stage 0 it uses those selected stage-1 values to obtain 13.46 and 4.78.

#### 6. Compare the output with our hand solution.

Actual output:

```text
Vpi_2: W=5.00, B=-2.00
Vpi_1: W=9.30, B=0.90
Vpi_0: W=13.46, B=4.78
```

All four requested entries and both extra stage-0 entries match. Fractions are exact internally; the two-decimal display introduces no substantive discrepancy.

<a id="2d"></a>

### 2(d) Enumerating trajectories

> Verify $V_1^\pi(W)$ by enumerating all trajectories that start in $W$ at $h=1$, with their probabilities and total rewards. How does the number of trajectories grow with the horizon $H$, and how many numbers does the backward recursion compute?

#### 1. Read the question carefully.

Starting in $W$ at stage 1, list all complete two-transition state paths under the cautious policy. Attach their probabilities and returns, average them, then compare the work of enumeration with backward recursion.

#### 2. Explain every concept and symbol.

A trajectory records the successive states, chosen actions, and rewards. Under a fixed deterministic policy, the state path fixes its actions. The chain rule of probability multiplies consecutive conditional transition probabilities; the Markov property supplies the table row for each factor. An expectation of a discrete return is $\sum_\omega p_\omega G_\omega$, where $\omega$ labels paths. Different paths can have the same total reward. The stage-3 endpoint has no reward, but its transition probability is still part of a complete path.

#### 3. Solve it by hand.

The first action is maintain and earns 5. A working stage-2 state means maintain earns 5 again; a broken stage-2 state means repair earns -2.

| State path $(s_1,s_2,s_3)$ | Actions | Probability calculation | Return $r_1+r_2$ |
| --- | --- | --- | --- |
| $(W,W,W)$ | maintain, maintain | $0.9\times0.9=0.81$ | $5+5=10$ |
| $(W,W,B)$ | maintain, maintain | $0.9\times0.1=0.09$ | $5+5=10$ |
| $(W,B,W)$ | maintain, repair | $0.1\times0.7=0.07$ | $5-2=3$ |
| $(W,B,B)$ | maintain, repair | $0.1\times0.3=0.03$ | $5-2=3$ |

The probabilities sum to $0.81+0.09+0.07+0.03=1$. Thus

$$V_1^\pi(W)=0.81(10)+0.09(10)+0.07(3)+0.03(3)=8.1+0.9+0.21+0.09=9.3.$$

Starting at a fixed state with $m$ decisions remaining, cautious-policy transitions always have two possible successors, so complete paths including the endpoint number $2^m$. Starting at day 0, this is $2^H=8$ for $H=3$. If the terminal endpoint is marginalized because it has no effect on rewards, reward-relevant histories number $2^{H-1}$; both conventions grow exponentially with the horizon.

Backward recursion computes $H|\mathcal S|=3\times2=6$ nonterminal state values, plus the two specified boundary entries if these are counted. Generally it stores $(H+1)|\mathcal S|$ values and performs probability-weighted sums over successors per state/action. The machine has four admissible state/action pairs and two successor entries, so the supplied helper computes 12 action candidates and 24 successor terms across the three stages. It reuses a next-stage value for every predecessor instead of recomputing its entire path subtree.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem02.py](examples/problem02.py) (run the whole file; earlier excerpts supply its inputs):

```python
enumerated_value = Fraction(0)
for middle_state, first_probability in machine["W"]["maintain"][1].items():
    last_action = cautious[2][middle_state]
    last_reward, last_transitions = machine[middle_state][last_action]
    for end_state, second_probability in last_transitions.items():
        probability = first_probability * second_probability
        total_reward = Fraction(5) + last_reward
        enumerated_value += probability * total_reward
        print(f"W -> {middle_state} -> {end_state}: p={float(probability):.2f}, reward={total_reward}")
print(f"Enumeration Vpi_1(W) = {float(enumerated_value):.2f}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `enumerated_value = Fraction(0)` | Initialize the exact expected return accumulator to zero. |
| 2. `for middle_state, first_probability in machine["W"]["maintain"][1].items():` | Index maintain's transition dictionary and visit middle states `W` (probability 9/10) and `B` (1/10). Tuple index 1 selects transitions, not reward. |
| 3. `last_action = cautious[2][middle_state]` | Look up the cautious action for stage 2 at that middle state: maintain at `W`, repair at `B`. |
| 4. `last_reward, last_transitions = machine[middle_state][last_action]` | Unpack its last-day reward and transition dictionary. |
| 5. `for end_state, second_probability in last_transitions.items():` | Visit both endpoint states, with their conditional last-step probabilities. |
| 6. `probability = first_probability * second_probability` | Multiply the two conditional factors: for the first path `(9/10)*(9/10) = 81/100`. |
| 7. `total_reward = Fraction(5) + last_reward` | Add first reward 5 and the middle-state's reward: 10 for middle `W`, 3 for middle `B`. |
| 8. `enumerated_value += probability * total_reward` | Add probability times total reward to the expectation accumulator. |
| 9. `print(f"W -> {middle_state} -> {end_state}: p={float(probability):.2f}, reward={total_reward}")` | Print this state path, its probability to two decimals, and its exact integer return. Endpoint changes affect probability but not the already earned reward. |
| 10. `print(f"Enumeration Vpi_1(W) = {float(enumerated_value):.2f}")` | After all four paths, print the summed expectation to two decimals. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
W -> W -> W: p=0.81, reward=10
W -> W -> B: p=0.09, reward=10
W -> B -> W: p=0.07, reward=3
W -> B -> B: p=0.03, reward=3
Enumeration Vpi_1(W) = 9.30
```

Every path, probability, and return agrees with the table. The weighted sum 9.30 equals the backward-recursion value, providing two independent ways to obtain the same answer.

<a id="problem-3"></a>

## Problem 3: Optimal values and cautious-policy loss

**Source setup (verbatim, with TeX recovered from the HTML):**

Use the machine MDP and the cautious policy from problem 2.

<a id="3a"></a>

### 3(a) Bellman optimality

> Write the Bellman optimality recursion for the machine MDP in explicit finite-horizon notation.

#### 1. Read the question carefully.

Use the machine model from 2(a), but now choose actions to maximize expected reward. State the finite-horizon recursion with the boundary and the stage range explicit.

#### 2. Explain every concept and symbol.

$V_h^*(s)$ means the largest achievable expected remaining reward. $Q_h^*(s,a)$ fixes action $a$ now and follows an optimal continuation afterward. A maximum replaces the policy-weighted choice used for $V_h^\pi$. The sum over $s'$ still averages random outcomes; optimization does not allow choosing the successor state.

#### 3. Solve it by hand.

For $h=2,1,0$,

$$Q_h^*(s,a)=r(s,a)+\sum_{s'\in\{W,B\}}P(s'\mid s,a)V_{h+1}^*(s'),\qquad V_h^*(s)=\max_{a\in\mathcal A(s)}Q_h^*(s,a),$$

with $V_3^*(W)=V_3^*(B)=0$. In this particular model,

$$V_h^*(W)=\max\{8+0.6V_{h+1}^*(W)+0.4V_{h+1}^*(B),\;5+0.9V_{h+1}^*(W)+0.1V_{h+1}^*(B)\},$$

$$V_h^*(B)=\max\{-2+0.7V_{h+1}^*(W)+0.3V_{h+1}^*(B),\;-6+V_{h+1}^*(W)\}.$$

The first working candidate is operate, the second maintain; the broken candidates are repair and replace. A randomized action gives a weighted average of these candidates, which cannot exceed their maximum. Thus one maximizing action at each state/time attains the optimal value.

#### 4. Translate the reasoning into simple code.

The recursion is the mathematical specification. The already explained `backward_values` implements it when no policy argument is supplied; its concrete use appears in 3(b). No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

At the last stage, substituting the zero boundary leaves maxima of immediate rewards. This checks the boundary interpretation before running 3(b).

<a id="3b"></a>

### 3(b) The requested optimal values

> Compute $V_2^*(W)$, $V_2^*(B)$, $V_1^*(W)$, and $V_1^*(B)$.

#### 1. Read the question carefully.

Calculate the last-stage and stage-1 optimal values for both states. Start from the boundary and show every admissible action candidate, including the working-state tie.

#### 2. Explain every concept and symbol.

Backward induction chooses an optimal continuation before choosing the current action. A tie means several actions attain the same maximal expectation; it does not mean their return distributions are equal. The cautious values from 2(c) are not the successor values for this calculation: use optimal successor values instead.

#### 3. Solve it by hand.

At stage 2 the continuation is zero:

| State | First candidate | Second candidate | $V_2^*$ | Maximizers |
| --- | --- | --- | --- | --- |
| $W$ | operate: $8+0.6(0)+0.4(0)=8$ | maintain: $5+0.9(0)+0.1(0)=5$ | 8 | operate |
| $B$ | repair: $-2+0.7(0)+0.3(0)=-2$ | replace: $-6+1(0)+0(0)=-6$ | -2 | repair |

At stage 1, substitute $V_2^*(W)=8$ and $V_2^*(B)=-2$:

$$Q_1^*(W,\mathrm{operate})=8+0.6(8)+0.4(-2)=8+4.8-0.8=12,$$

$$Q_1^*(W,\mathrm{maintain})=5+0.9(8)+0.1(-2)=5+7.2-0.2=12,$$

$$Q_1^*(B,\mathrm{repair})=-2+0.7(8)+0.3(-2)=-2+5.6-0.6=3,$$

$$Q_1^*(B,\mathrm{replace})=-6+1(8)+0(-2)=-6+8+0=2.$$

Therefore $V_1^*(W)=12$, with both operate and maintain optimal, and $V_1^*(B)=3$, with repair uniquely optimal. The machine still has stochastic transitions, so these are expected returns, not guarantees for every path.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/common.py](examples/common.py) (run the whole file; earlier excerpts supply its inputs):

```python
def best_actions(candidates):
    best_value = max(candidates.values())
    actions = []
    for action, value in candidates.items():
        if value == best_value:
            actions.append(action)
    return actions
```

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `def best_actions(candidates):` | Define `best_actions` with parameter `candidates`, a dictionary mapping action names to their computed values. |
| 2. `best_value = max(candidates.values())` | Take the maximum of the dictionary's values and store it as `best_value`. |
| 3. `actions = []` | Create an empty list to collect all maximizing names. |
| 4. `for action, value in candidates.items():` | Visit each action/value pair with `.items()`. |
| 5. `if value == best_value:` | Compare the candidate with the maximum using exact equality. Fraction arithmetic keeps mathematical ties exact. |
| 6. `actions.append(action)` | Append the action name if it attains the maximum. |
| 7. `return actions` | Return the list. For candidates operate 12 and maintain 12, it returns both names in dictionary insertion order. |

Use that helper in the chapter script:

Excerpt from [examples/problem03.py](examples/problem03.py) (run the whole file; earlier excerpts supply its inputs):

```python
from common import Fraction, machine, backward_values, best_actions

terminal = {"W": Fraction(0), "B": Fraction(0)}
values, action_values = backward_values(machine, 3, terminal)
for stage in (2, 1, 0):
    for state in machine:
        candidates = action_values[stage][state]
        print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from common import Fraction, machine, backward_values, best_actions` | Import exact fractions, machine data, the backward solver, and the tie-preserving action helper. |
| 2. `terminal = {"W": Fraction(0), "B": Fraction(0)}` | Assign the zero boundary for `W` and `B`. |
| 3. `values, action_values = backward_values(machine, 3, terminal)` | Call `backward_values` without a policy, activating its maximizing branch. The returned lists contain $V^*$ and $Q^*$. |
| 4. `for stage in (2, 1, 0):` | Visit stages 2, 1, 0 for output. |
| 5. `for state in machine:` | Visit both machine states at each stage. |
| 6. `candidates = action_values[stage][state]` | Look up the computed candidate dictionary for this stage/state. |
| 7. `print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")` | Print Q-candidates converted to floats for display, the state value to two decimals, and every maximizing action. The inner dictionary comprehension keeps action names `a` and converts corresponding exact values `v`. |

Trace the optimization call: at stage 2, the solver stores max(8,5)=8 and max(-2,-6)=-2. At stage 1 it stores max(12,12)=12 and max(3,2)=3. `best_actions` appends operate and maintain for the 12/12 tie.

#### 6. Compare the output with our hand solution.

Actual output:

```text
h=2, W: Q={'operate': 8.0, 'maintain': 5.0}, V=8.00, best=['operate']
h=2, B: Q={'repair': -2.0, 'replace': -6.0}, V=-2.00, best=['repair']
h=1, W: Q={'operate': 12.0, 'maintain': 12.0}, V=12.00, best=['operate', 'maintain']
h=1, B: Q={'repair': 3.0, 'replace': 2.0}, V=3.00, best=['repair']
```

All four values match. Both tied actions appear in the output; choosing either is valid for this expected-return problem.

<a id="3c"></a>

### 3(c) The optimal first action

> Starting from $W$ on day $0$, determine the optimal first action.

#### 1. Read the question carefully.

We now start at $W$ on day 0. Use the stage-1 optimal values from 3(b) to compare first-day actions. The script also reports the broken start value, though it is not needed for this question.

#### 2. Explain every concept and symbol.

A first action is chosen using its immediate reward and the expected optimal return of its successor at stage 1. $Q_0^*$ differs from $Q_1^*$ because there are three decisions remaining rather than two. Knowing that stage-1 actions tie does not imply a stage-0 tie.

#### 3. Solve it by hand.

Substitute $(V_1^*(W),V_1^*(B))=(12,3)$:

$$Q_0^*(W,\mathrm{operate})=8+0.6(12)+0.4(3)=8+7.2+1.2=16.4,$$

$$Q_0^*(W,\mathrm{maintain})=5+0.9(12)+0.1(3)=5+10.8+0.3=16.1.$$

Thus operate is the unique optimal first action and $V_0^*(W)=16.4$. For completeness,

$$Q_0^*(B,\mathrm{repair})=-2+0.7(12)+0.3(3)=-2+8.4+0.9=7.3,$$

$$Q_0^*(B,\mathrm{replace})=-6+12=6,$$

so $V_0^*(B)=7.3$ and repair is optimal there.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem03.py](examples/problem03.py) (run the whole file; earlier excerpts supply its inputs):

```python
print("Optimal first action:", best_actions(action_values[0]["W"]))
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `print("Optimal first action:", best_actions(action_values[0]["W"]))` | Look up the previously computed stage-0 working candidates, pass them to `best_actions`, and print the resulting list. No recursion is rerun; the line retrieves a decision from the stored values. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
h=0, W: Q={'operate': 16.4, 'maintain': 16.1}, V=16.40, best=['operate']
h=0, B: Q={'repair': 7.3, 'replace': 6.0}, V=7.30, best=['repair']
Optimal first action: ['operate']
```

The 16.4 versus 16.1 comparison selects operate, matching the printed first-action list.

<a id="3d"></a>

### 3(d) Where the cautious policy loses reward

> Compare $V_1^\pi$ of the cautious policy with $V_1^*$. Determine the loss in each state and identify the decision of the cautious policy that causes it.

#### 1. Read the question carefully.

Compare stage-1 cautious and optimal values at each state, quantify their differences, and identify which cautious decisions create the loss. The policies must be compared over the remaining two decisions.

#### 2. Explain every concept and symbol.

Define loss $L_1(s)=V_1^*(s)-V_1^\pi(s)$. This is an expected opportunity cost. A policy can choose an optimal action at the current stage and still have lower value because its later decisions are suboptimal. At stage 2, cautious maintain in $W$ earns 5 instead of optimal operate earning 8: the gap is 3.

#### 3. Solve it by hand.

From 2(c) and 3(b),

$$L_1(W)=12-9.3=2.7,\qquad L_1(B)=3-0.9=2.1.$$

At stage 1 the cautious action maintain at $W$ is one of the optimal actions, and repair at $B$ is the unique optimal action. Keeping either stage-1 action but switching to optimal continuation yields 12 or 3 respectively. The loss therefore comes entirely from maintaining instead of operating at a working stage-2 machine.

Under maintain from $W$, the next machine is working with probability 0.9, so its expected lost reward is $0.9(8-5)=0.9(3)=2.7$. Under repair from $B$, it is working with probability 0.7, giving $0.7(8-5)=0.7(3)=2.1$. At broken stage 2 both policies repair, so there is no loss on that branch.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem03.py](examples/problem03.py) (run the whole file; earlier excerpts supply its inputs):

```python
cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]
cautious_values, cautious_q = backward_values(machine, 3, terminal, cautious)
for state in machine:
    loss = values[1][state] - cautious_values[1][state]
    print(f"Loss at h=1, {state}: {float(loss):.2f}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]` | Build the three-stage cautious policy as independent dictionaries, using maintain in `W` and repair in `B`. |
| 2. `cautious_values, cautious_q = backward_values(machine, 3, terminal, cautious)` | Evaluate that fixed policy, preserving the optimal `values` already computed under a different variable name. |
| 3. `for state in machine:` | Loop over the states `W` and `B`. |
| 4. `loss = values[1][state] - cautious_values[1][state]` | Subtract the cautious stage-1 value from the optimal stage-1 value at this state. |
| 5. `print(f"Loss at h=1, {state}: {float(loss):.2f}")` | Print the state and loss to two decimals. The formatting changes presentation, not the exact stored fraction. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Loss at h=1, W: 2.70
Loss at h=1, B: 2.10
```

The differences 2.70 and 2.10 also match the probability-times-last-day-loss argument. This identifies the offending decision rather than only reporting a gap.

<a id="3e"></a>

### 3(e) Counting behaviorally distinct policies

> With start state $W$, count the deterministic Markov policies and the deterministic history-dependent policies that lead to different behavior. Explain what the lecture’s result that an optimal Markovian deterministic policy exists saves.

#### 1. Read the question carefully.

Count deterministic policies from the specified start $W$, treating policies as equivalent when they make the same decisions on every history they can actually encounter. The source does not spell out this counting convention, so we state it explicitly. A decision at $B$ on day 0 cannot affect behavior from this start. A stage-2 history following replacement and then $B$ is impossible.

#### 2. Explain every concept and symbol.

A deterministic Markov policy selects one action for each $(h,s)$. A deterministic history-dependent policy may select different actions after different sequences of states and past actions, even when current state and time agree. “Behaviorally distinct” here means different state/action trajectory distributions from the given start; actions on zero-probability histories are ignored. Rewards add no history distinctions because they are determined by state/action. Each reachable decision node has two actions. The multiplication rule counts independent choices; the addition rule combines disjoint cases such as choosing repair versus replace.

#### 3. Solve it by hand.

For Markov policies, there is one relevant day-0 state and two possible states on each of days 1 and 2. Both first actions give positive probability to $W$ and $B$ on day 1. On day 2, $W$ on day 1 always has positive-probability transitions to both states, regardless of its selected action. Thus both day-2 states are reachable even if the broken day-1 action is replace. There are five relevant binary decisions:

$$N_{\mathrm{Markov}}=2\times2^2\times2^2=2^5=32.$$

A complete table including the irrelevant day-0 broken action has $2^6=64$ entries-as-policies, but pairs differing only in that action have identical behavior from $W$.

For history-dependent policies, first choose one of the two initial actions. Next choose an action at each of the two reachable day-1 histories. For a fixed initial action:

| Working day-1 action | Broken day-1 action | Reachable day-2 histories | Binary choices on day 2 |
| --- | --- | --- | --- |
| operate | repair | 4 | $2^4=16$ |
| maintain | repair | 4 | $2^4=16$ |
| operate | replace | 3 | $2^3=8$ |
| maintain | replace | 3 | $2^3=8$ |

When repair is chosen, the four state histories are $(W,W,W)$, $(W,W,B)$, $(W,B,W)$, and $(W,B,B)$, with the previously chosen actions fixed for that case. When replace is chosen at the broken middle state, $(W,B,B)$ has probability zero and is excluded. Histories $(W,W,W)$ and $(W,B,W)$ may choose different day-2 actions even though both end in $W$.

For each initial action there are $16+16+8+8=48$ behavioral policies. Hence

$$N_{\mathrm{history}}=2(48)=96.$$

The shortcut $2^{1+2+4}=128$ would count choices at four last-day histories even in replacement cases, duplicating policies that differ only at an impossible history. It is not the behavioral count used here.

The existence of an optimal deterministic Markov policy means we can optimize over the smaller state/time representation without sacrificing expected reward. We need neither randomization nor memory of entire histories. Backward induction searches through local maxima and shared continuation values; it does not need to enumerate even the 32 complete Markov policies.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem03.py](examples/problem03.py) (run the whole file; earlier excerpts supply its inputs):

```python
markov_count = 2 ** (1 + 2 + 2)
history_count = 0
for first_action in machine["W"]:
    for working_action in machine["W"]:
        for broken_action in machine["B"]:
            reachable_histories = 0
            for middle_state in machine:
                if middle_state == "W":
                    action = working_action
                else:
                    action = broken_action
                reward, transitions = machine[middle_state][action]
                for successor, probability in transitions.items():
                    if probability > 0:
                        reachable_histories += 1
            history_count += 2 ** reachable_histories
print("Behavioral Markov policies:", markov_count)
print("Behavioral history policies:", history_count)
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `markov_count = 2 ** (1 + 2 + 2)` | Compute 2 to the power `(1 + 2 + 2)`, the five relevant binary Markov choices. `**` is exponentiation. |
| 2. `history_count = 0` | Initialize the sum of behavioral history-policy counts to zero. |
| 3. `for first_action in machine["W"]:` | Enumerate the two initial actions at the working start. Each has positive probability of both middle states. |
| 4. `for working_action in machine["W"]:` | Enumerate the day-1 action after a working middle state. |
| 5. `for broken_action in machine["B"]:` | Enumerate the day-1 action after a broken middle state. |
| 6. `reachable_histories = 0` | Reset the count of reachable last-day histories for this fixed triple of earlier choices. |
| 7. `for middle_state in machine:` | Visit each possible middle state. Each is a different preceding history from the fixed start and first action. |
| 8. `if middle_state == "W":` | Test whether this middle state is working. |
| 9. `action = working_action` | Use the previously selected working-middle action in that case. |
| 10. `else:` | Enter the broken-middle case when the test is false. |
| 11. `action = broken_action` | Use the previously selected broken-middle action in that case. |
| 12. `reward, transitions = machine[middle_state][action]` | Unpack its reward and transition row; the reward is not needed for counting. |
| 13. `for successor, probability in transitions.items():` | Visit its possible successor states and their probabilities. |
| 14. `if probability > 0:` | Count only strictly positive probabilities; replacement's broken branch is discarded. |
| 15. `reachable_histories += 1` | Add one for this reachable `(middle_state, successor)` history. The count becomes 4 for repair, 3 for replacement. |
| 16. `history_count += 2 ** reachable_histories` | Each reachable last-day history has two actions, so add `2 ** reachable_histories` for this combination of earlier actions. |
| 17. `print("Behavioral Markov policies:", markov_count)` | Print the computed behavioral Markov count. |
| 18. `print("Behavioral history policies:", history_count)` | Print the summed behavioral history-dependent count. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Behavioral Markov policies: 32
Behavioral history policies: 96
```

The program returns 32 and 96 under the stated convention. Its innermost loop counts 4 histories for repair and 3 for replace; the hand case table verifies why both counts occur.

<a id="problem-4"></a>

## Problem 4: Q-values and policy improvement

**Source setup (verbatim, with TeX recovered from the HTML):**

For a finite-horizon MDP, define $Q_h^\pi(s,a)
= r(s,a) + \sum_{s'} P(s' \mid s,a) V_{h+1}^{\pi}(s').$ The lecture slide “Policy Improvement (Finite Horizon)” shows that the policy that is greedy with respect to $Q_h^\pi$ at every stage improves on $\pi$. This problem changes a single stage. Use the machine MDP and the cautious policy $\pi$.

<a id="4a"></a>

### 4(a) Action values under the cautious continuation

> Compute $Q_1^\pi(s,a)$ for all four state-action pairs.

#### 1. Read the question carefully.

Calculate all four stage-1 action values when the chosen first action is followed by the cautious policy at stage 2. We already know its continuation values 5 and -2 from 2(c). These are not the optimal continuation values 8 and -2.

#### 2. Explain every concept and symbol.

$Q_h^\pi(s,a)$ is the expected remaining return after forcing action $a$ now and following $\pi$ afterward. It can evaluate an action that $\pi$ itself would not choose now. $V_h^\pi(s)$ selects or averages these action values according to the policy. $Q_h^*$ instead follows optimal future decisions. All quantities in this subquestion have superscript $\pi$.

#### 3. Solve it by hand.

Use

$$Q_1^\pi(s,a)=r(s,a)+\sum_{s'}P(s'\mid s,a)V_2^\pi(s'),\qquad (V_2^\pi(W),V_2^\pi(B))=(5,-2).$$

For each action:

$$Q_1^\pi(W,\mathrm{operate})=8+0.6(5)+0.4(-2)=8+3-0.8=10.2,$$

$$Q_1^\pi(W,\mathrm{maintain})=5+0.9(5)+0.1(-2)=5+4.5-0.2=9.3,$$

$$Q_1^\pi(B,\mathrm{repair})=-2+0.7(5)+0.3(-2)=-2+3.5-0.6=0.9,$$

$$Q_1^\pi(B,\mathrm{replace})=-6+1(5)+0(-2)=-6+5+0=-1.$$

Operating now is better than maintaining now under the cautious continuation. This does not conflict with the optimal-continuation tie in 3(b): its successor value at $W$ was 8, whereas here it is 5.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem04.py](examples/problem04.py) (run the whole file; earlier excerpts supply its inputs):

```python
from common import Fraction, machine, backward_values, best_actions

terminal = {"W": Fraction(0), "B": Fraction(0)}
cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]
values, action_values = backward_values(machine, 3, terminal, cautious)
for state in machine:
    for action, value in action_values[1][state].items():
        print(f"Qpi_1({state}, {action}) = {float(value):.2f}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from common import Fraction, machine, backward_values, best_actions` | Import exact arithmetic, machine data, the explained backward evaluator, and the tie-preserving action selector. |
| 2. `terminal = {"W": Fraction(0), "B": Fraction(0)}` | Specify the zero stage-3 boundary. |
| 3. `cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]` | Create the cautious rule for every decision stage. |
| 4. `values, action_values = backward_values(machine, 3, terminal, cautious)` | Evaluate this policy and retain its action values. The solver still computes every candidate before selecting the policy's action. |
| 5. `for state in machine:` | Visit each current state. |
| 6. `for action, value in action_values[1][state].items():` | Visit every action/value pair in this state's stage-1 candidate dictionary. |
| 7. `print(f"Qpi_1({state}, {action}) = {float(value):.2f}")` | Print its state, action, and value, converting the fraction only for a two-decimal display. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Qpi_1(W, operate) = 10.20
Qpi_1(W, maintain) = 9.30
Qpi_1(B, repair) = 0.90
Qpi_1(B, replace) = -1.00
```

Each Q-value matches its probability-weighted hand calculation. In particular, replace has negative value -1.00 even though the best broken-state action has positive value.

<a id="4b"></a>

### 4(b) Improving exactly one stage

> Let $\pi'$ agree with $\pi$ at $h=0$ and $h=2$ and be greedy with respect to $Q_1^\pi$ at $h=1$. Compute $V_1^{\pi'}(W)$ and $V_1^{\pi'}(B)$, compare them with $V_1^*$ from problem 3, and state which further change of the policy closes the remaining gap.

#### 1. Read the question carefully.

Construct $\pi'$ by changing only day 1 to actions greedy with respect to the Q-values in 4(a). Day 0 and day 2 must remain cautious for this first improvement. Compute its day-1 values, compare them with optimal values, and then identify a further change that removes those day-1 gaps.

#### 2. Explain every concept and symbol.

Greedy with respect to $Q_1^\pi$ means selecting an action attaining its largest number at each state. The prime in $\pi'$ marks a different policy; it does not mean a derivative. Because the two policies agree after day 1, their day-2 values agree. Thus the improved day-1 values equal the selected $Q_1^\pi$ candidates. A copy of each policy dictionary prevents accidentally modifying the original.

#### 3. Solve it by hand.

The strict comparisons are $10.2>9.3$ at $W$ and $0.9>-1$ at $B$. Therefore

| Stage | $\pi'(W)$ | $\pi'(B)$ |
| --- | --- | --- |
| 0 | maintain | repair |
| 1 | operate | repair |
| 2 | maintain | repair |

At stage 1,

$$V_1^{\pi'}(W)=8+0.6(5)+0.4(-2)=10.2,$$

$$V_1^{\pi'}(B)=-2+0.7(5)+0.3(-2)=0.9.$$

Compare with $(V_1^*(W),V_1^*(B))=(12,3)$: the gaps are $12-10.2=1.8$ and $3-0.9=2.1$. Repair was already greedy at the broken state, so its stage-1 value did not change.

Now change only the additional entry at day 2 in state $W$, from maintain to operate. Its value becomes 8 rather than 5. The revised day-1 values are

$$8+0.6(8)+0.4(-2)=8+4.8-0.8=12,$$

$$-2+0.7(8)+0.3(-2)=-2+5.6-0.6=3.$$

That closes both requested day-1 gaps. The original day-0 maintain action still gives $5+0.9(12)+0.1(3)=16.1$, below the optimal start value 16.4. If the objective is a globally optimal policy from day 0 too, switch day-0 $W$ to operate as established in 3(c). Closing the day-1 gaps alone does not make every stage optimal.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem04.py](examples/problem04.py) (run the whole file; earlier excerpts supply its inputs):

```python
improved = [stage_policy.copy() for stage_policy in cautious]
for state in machine:
    improved[1][state] = best_actions(action_values[1][state])[0]
improved_values, improved_q = backward_values(machine, 3, terminal, improved)
print("Improved policy:", improved)
print(f"Vprime_1: W={float(improved_values[1]['W']):.2f}, B={float(improved_values[1]['B']):.2f}")
improved[2]["W"] = "operate"
closed_values, closed_q = backward_values(machine, 3, terminal, improved)
print(f"After stage 2 change: W={float(closed_values[1]['W']):.2f}, B={float(closed_values[1]['B']):.2f}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `improved = [stage_policy.copy() for stage_policy in cautious]` | Copy each stage dictionary into a new policy list. Copying only the list would leave dictionaries shared; these per-stage copies keep the original cautious policy intact. |
| 2. `for state in machine:` | Visit both states to improve their stage-1 entries. |
| 3. `improved[1][state] = best_actions(action_values[1][state])[0]` | Find every action maximizing the original stage-1 Q-candidates and assign the first one at `improved[1][state]`. Only index 1 changes; both comparisons here are strict. |
| 4. `improved_values, improved_q = backward_values(machine, 3, terminal, improved)` | Evaluate the complete copied policy with its unchanged stage-0 and stage-2 actions. |
| 5. `print("Improved policy:", improved)` | Print the whole policy list, making the stage restriction visible. |
| 6. `print(f"Vprime_1: W={float(improved_values[1]['W']):.2f}, B={float(improved_values[1]['B']):.2f}")` | Print its two stage-1 values to two decimals. |
| 7. `improved[2]["W"] = "operate"` | For a second, separate policy change, set the working day-2 action to operate. This line runs after the first improved policy has been evaluated and displayed. |
| 8. `closed_values, closed_q = backward_values(machine, 3, terminal, improved)` | Reevaluate the newly modified policy using the same boundary and model. |
| 9. `print(f"After stage 2 change: W={float(closed_values[1]['W']):.2f}, B={float(closed_values[1]['B']):.2f}")` | Print the resulting stage-1 values, which now attain the optimal values. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Improved policy: [{'W': 'maintain', 'B': 'repair'}, {'W': 'operate', 'B': 'repair'}, {'W': 'maintain', 'B': 'repair'}]
Vprime_1: W=10.20, B=0.90
After stage 2 change: W=12.00, B=3.00
```

The printed policy proves the initial change was restricted to day 1. Its values 10.20 and 0.90 match the first calculation; the separate last-day change gives 12.00 and 3.00.

<a id="4c"></a>

### 4(c) Proof of single-stage improvement

> Prove in general: if $\pi'$ differs from $\pi$ only at a stage $k$, where it is greedy with respect to $Q_k^\pi$, then $V_h^{\pi'}(s)\ge V_h^\pi(s)$ for all $h\le k$ and all $s$, and $V_h^{\pi'}=V_h^\pi$ for $h>k$.

#### 1. Read the question carefully.

Prove the result for arbitrary states and stages in a finite-horizon MDP, rather than just the machine. Assume both policies share the same terminal values and differ only at stage $k$, where $\pi'$ chooses maximizing $Q_k^\pi$ actions. Randomized $\pi$ is allowed.

#### 2. Explain every concept and symbol.

An induction proves a statement at one stage using the already proved statement at the next stage. Here it runs backward. Define $\Delta_h(s)=V_h^{\pi'}(s)-V_h^\pi(s)$, the improvement. A probability-weighted average of numbers is at most their maximum. Nonnegative weights preserve inequalities: if $x_i\ge y_i$ and $p_i\ge0$, then $\sum_i p_ix_i\ge\sum_i p_iy_i$. These two facts drive the proof.

#### 3. Solve it by hand.

First consider $h>k$. The policies choose identical actions at every stage from $h$ to the horizon, and have the same boundary, so their conditional return distributions agree. Equivalently, backward induction from the common boundary through their identical recursions proves $V_h^{\pi'}=V_h^\pi$ for every $h>k$.

At $h=k$, the continuation is therefore the same. For a greedy deterministic choice $a^*(s)$,

$$V_k^{\pi'}(s)=Q_k^\pi(s,a^*(s))=\max_a Q_k^\pi(s,a).$$

For the original possibly randomized rule,

$$V_k^\pi(s)=\sum_a\pi_k(a\mid s)Q_k^\pi(s,a)\le\max_a Q_k^\pi(s,a),$$

because each candidate is bounded above by that maximum and the action probabilities sum to 1. Thus $\Delta_k(s)\ge0$ for every state. If $\pi'$ randomizes only among maximizing actions, its weighted average is still that maximum, so the same conclusion holds.

For the induction step, fix $h<k$ and suppose $\Delta_{h+1}(s')\ge0$ for every successor. Both policies use the same action distribution at stage $h$, so the immediate-reward terms cancel when subtracting their Bellman equations:

$$\Delta_h(s)=\sum_a\pi_h(a\mid s)\sum_{s'}P(s'\mid s,a)\Delta_{h+1}(s')\ge0.$$

Every action probability, transition probability, and induction-hypothesis difference is nonnegative. Hence each product is nonnegative and so is their sum. Starting with the established stage-$k$ inequality, this step proves it for $k-1$, then $k-2$, continuing through 0. Combining this with the first part proves the full claim. Improvement can be zero at a state if it cannot lead to a beneficial changed decision.

#### 4. Translate the reasoning into simple code.

This is a universal proof. Code would only check particular models, so sections 4–6 use mathematical verification rather than a substitute experiment. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No program output establishes the theorem. Check its base case (the maximum bounds the original policy average) and its induction step (identical rewards cancel and nonnegative transition weights preserve the difference). In the machine, stage 2 is unchanged and the stage-1 difference is 0.9 at $W$ and 0 at $B$, consistent with the theorem.

<a id="4d"></a>

### 4(d) Why action values are enough

> Explain why $Q_h^\pi$ is enough for greedy improvement, while $V_h^\pi$ alone is not enough unless the model is known.

#### 1. Read the question carefully.

Explain what information permits choosing an improved action. Distinguish access to a Q-table from access only to a V-table, and state how knowing the model changes the answer.

#### 2. Explain every concept and symbol.

A state value reports the expected return under a policy's chosen action distribution. An action value reports a separate return for each possible first action. A model supplies immediate rewards and transition probabilities, so it lets us convert successor state values into action candidates. Greedy improvement needs comparisons between action candidates, not merely a single state score.

#### 3. Solve it by hand.

At stage 1 in $W$, $V_1^\pi(W)=9.3$ says how well the cautious policy performs. It does not itself say that operating would yield 10.2. With the Q-table, compare $Q_1^\pi(W,\mathrm{operate})=10.2$ and $Q_1^\pi(W,\mathrm{maintain})=9.3$, then choose operate directly. No transition model is needed for that lookup.

If the model is known and the stage-2 V-table is available, reconstruct each action value from

$$Q_1^\pi(s,a)=r(s,a)+\sum_{s'}P(s'\mid s,a)V_2^\pi(s').$$

For example, the operate row and $(5,-2)$ produce $8+0.6(5)+0.4(-2)=10.2$. Without the model or action values, the V-table does not determine returns from unchosen actions. Changing the reward of an action that the cautious policy never selects can leave its V-table unchanged while changing which alternative is best. That demonstrates the missing information.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No additional code or output is needed. The computed Q-table in 4(a) supplies the precise comparisons used by the policy update in 4(b); its differing working-state action values are information the single cautious state value cannot provide.

<a id="problem-5"></a>

## Problem 5: Horizon effects

**Source setup (verbatim, with TeX recovered from the HTML):**

Consider a store with inventory level $l \in \{0,1,2,3\}$. The initial state is $l=1$. Two actions are available:


- sell: if $l>0$, receive reward $2$ and move to $l-1$; if $l=0$, receive reward $0$ and stay at $0$.

- stock: if $l<3$, receive reward $0$ and move to $l+1$; if $l=3$, receive reward $5$ and stay at $3$.


There is no terminal state; the problem ends only at the horizon.

<a id="5a"></a>

### 5(a) One decision remaining

> For horizon $H=1$, determine the optimal first action at $l=1$.

#### 1. Read the question carefully.

Find the optimal first action at inventory 1 when $H=1$. The source has no absorbing terminal state and specifies no additional terminal reward; set all horizon-boundary values to zero. Keep the reward 5 for stocking at capacity exactly as given.

#### 2. Explain every concept and symbol.

Here $l$ is inventory, not the salvage parameter $\lambda$ in problem 8. Define $F_n(l)$ as the best return with $n$ decisions remaining. The subscript counts remaining decisions, so increasing $n$ builds on the preceding calculation; in a horizon-$H$ problem, $F_n(l)=V_{H-n}^*(l)$. The transition $f(l,a)$ and reward $r(l,a)$ follow the two inventory rules. Both actions remain admissible at zero and capacity.

#### 3. Solve it by hand.

The boundary is $F_0(l)=0$. The general deterministic recursion is

$$F_n(l)=\max_{a\in\{\mathrm{sell},\mathrm{stock}\}}\{r(l,a)+F_{n-1}(f(l,a))\}.$$

For the first layer:

| Level $l$ | sell candidate | stock candidate | $F_1(l)$ | Best actions |
| --- | --- | --- | --- | --- |
| 0 | $0+F_0(0)=0+0=0$ | $0+F_0(1)=0+0=0$ | 0 | sell, stock |
| 1 | $2+F_0(0)=2+0=2$ | $0+F_0(2)=0+0=0$ | 2 | sell |
| 2 | $2+F_0(1)=2+0=2$ | $0+F_0(3)=0+0=0$ | 2 | sell |
| 3 | $2+F_0(2)=2+0=2$ | $5+F_0(3)=5+0=5$ | 5 | stock |

Thus from $l=1$ the unique optimal first action is sell, earning 2. Stocking creates inventory but no later decision remains to use it.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem05.py](examples/problem05.py) (run the whole file; earlier excerpts supply its inputs):

```python
def inventory_step(level, action):
    if action == "sell":
        if level > 0:
            return level - 1, 2
        return 0, 0
    if level < 3:
        return level + 1, 0
    return 3, 5
```

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `def inventory_step(level, action):` | Define `inventory_step(level, action)`, which returns the successor inventory and reward as a tuple. |
| 2. `if action == "sell":` | Test whether the chosen action string is `"sell"`. |
| 3. `if level > 0:` | Inside the sell branch, test whether any inventory is available. |
| 4. `return level - 1, 2` | For a positive level, return one less unit and reward 2; `return` ends the function call immediately. |
| 5. `return 0, 0` | For sell at zero, return successor 0 and reward 0. This line is reached only when the positive-level test failed. |
| 6. `if level < 3:` | After the sell branch, the admissible action is stock. Check whether inventory is below capacity 3. |
| 7. `return level + 1, 0` | For stock below capacity, return one more unit and reward 0. |
| 8. `return 3, 5` | For stock at capacity, return unchanged level 3 and reward 5. This implements the source's unusual capacity bonus exactly. |

The following loop computes all three requested horizons; this subquestion uses its first iteration:

Excerpt from [examples/problem05.py](examples/problem05.py) (run the whole file; earlier excerpts supply its inputs):

```python
values = {level: 0 for level in range(4)}
for remaining in range(1, 4):
    next_values = {}
    for level in range(4):
        candidates = {}
        for action in ("sell", "stock"):
            successor, reward = inventory_step(level, action)
            candidates[action] = reward + values[successor]
        next_values[level] = max(candidates.values())
        actions = []
        for action, candidate in candidates.items():
            if candidate == next_values[level]:
                actions.append(action)
        print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")
    values = next_values
    print(f"F_{remaining} = {values}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `values = {level: 0 for level in range(4)}` | Initialize the no-decisions-remaining values to zero for levels 0, 1, 2, 3. `range(4)` enumerates these four integer state keys. |
| 2. `for remaining in range(1, 4):` | Visit remaining decision counts 1, 2, 3. Values from the preceding iteration have one fewer decision remaining. |
| 3. `next_values = {}` | Create a separate dictionary for this iteration's values; this prevents overwriting continuation values while they are still needed. |
| 4. `for level in range(4):` | Visit all four inventory levels, not only the initial level 1. |
| 5. `candidates = {}` | Initialize the two action candidates for this level. |
| 6. `for action in ("sell", "stock"):` | Visit the admissible action strings sell and stock in that order. |
| 7. `successor, reward = inventory_step(level, action)` | Call the transition function and unpack its `(successor, reward)` result. |
| 8. `candidates[action] = reward + values[successor]` | Add reward to the prior iteration's value at the successor. At `remaining=1, level=1`, sell gives `2 + values[0] = 2` and stock gives `0 + values[2] = 0`. |
| 9. `next_values[level] = max(candidates.values())` | Store the maximum candidate as the new value at this level. |
| 10. `actions = []` | Start an empty list for every maximizing action. |
| 11. `for action, candidate in candidates.items():` | Visit the action/candidate pairs. |
| 12. `if candidate == next_values[level]:` | Compare each candidate to the newly stored maximum using `==`. |
| 13. `actions.append(action)` | Append every tied maximizer, preserving both sell and stock when they have equal values. |
| 14. `print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")` | Print remaining count, level, both candidates, and all best actions using an f-string. |
| 15. `values = next_values` | After finishing every level, replace the continuation dictionary with the completed new dictionary. This advances from $F_{n-1}$ to $F_n$. |
| 16. `print(f"F_{remaining} = {values}")` | Print the full value dictionary for this remaining count. |

For a concrete function call, `inventory_step(1, "sell")` passes the sell test and the positive-level test, then returns `(0, 2)`. `inventory_step(3, "stock")` fails the sell test and the below-capacity test, then returns `(3, 5)`.

#### 6. Compare the output with our hand solution.

Actual output:

```text
n=1, l=0: candidates={'sell': 0, 'stock': 0}, best=['sell', 'stock']
n=1, l=1: candidates={'sell': 2, 'stock': 0}, best=['sell']
n=1, l=2: candidates={'sell': 2, 'stock': 0}, best=['sell']
n=1, l=3: candidates={'sell': 2, 'stock': 5}, best=['stock']
F_1 = {0: 0, 1: 2, 2: 2, 3: 5}
```

Run `python3 examples/problem05.py`. Its first layer matches all four hand rows, including the tie at zero. Later layers are interpreted in 5(b) and 5(c).

<a id="5b"></a>

### 5(b) Two decisions remaining

> For horizon $H=2$, determine the optimal first action at $l=1$.

#### 1. Read the question carefully.

Find the first action at inventory 1 when $H=2$. Use the complete one-decision value dictionary from 5(a) as continuation, because first actions can move to other levels. We must report a tie if one occurs.

#### 2. Explain every concept and symbol.

The first action candidate now includes a one-decision optimal continuation $F_1$; $F_2$ is not two copies of the immediate reward. A maximizing set can have two actions. An optimal continuation can differ between the branches created by those first actions.

#### 3. Solve it by hand.

Substitute $(F_1(0),F_1(1),F_1(2),F_1(3))=(0,2,2,5)$:

| Level | sell candidate | stock candidate | $F_2$ | Best actions |
| --- | --- | --- | --- | --- |
| 0 | $0+0=0$ | $0+2=2$ | 2 | stock |
| 1 | $2+0=2$ | $0+2=2$ | 2 | sell, stock |
| 2 | $2+2=4$ | $0+5=5$ | 5 | stock |
| 3 | $2+2=4$ | $5+5=10$ | 10 | stock |

At level 1, sell reaches zero and leaves best last-day reward 0, for total 2. Either sell or stock is a valid last-day action at that zero state. Alternatively, stock reaches level 2 and then sell earns 2, for total $0+2=2$. Both first actions are optimal: neither is uniquely preferred under this objective.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem05.py](examples/problem05.py) (run the whole file; earlier excerpts supply its inputs):

```python
values = {level: 0 for level in range(4)}
for remaining in range(1, 4):
    next_values = {}
    for level in range(4):
        candidates = {}
        for action in ("sell", "stock"):
            successor, reward = inventory_step(level, action)
            candidates[action] = reward + values[successor]
        next_values[level] = max(candidates.values())
        actions = []
        for action, candidate in candidates.items():
            if candidate == next_values[level]:
                actions.append(action)
        print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")
    values = next_values
    print(f"F_{remaining} = {values}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `values = {level: 0 for level in range(4)}` | Initialize the no-decisions-remaining values to zero for levels 0, 1, 2, 3. `range(4)` enumerates these four integer state keys. |
| 2. `for remaining in range(1, 4):` | Visit remaining decision counts 1, 2, 3. Values from the preceding iteration have one fewer decision remaining. |
| 3. `next_values = {}` | Create a separate dictionary for this iteration's values; this prevents overwriting continuation values while they are still needed. |
| 4. `for level in range(4):` | Visit all four inventory levels, not only the initial level 1. |
| 5. `candidates = {}` | Initialize the two action candidates for this level. |
| 6. `for action in ("sell", "stock"):` | Visit the admissible action strings sell and stock in that order. |
| 7. `successor, reward = inventory_step(level, action)` | Call the transition function and unpack its `(successor, reward)` result. |
| 8. `candidates[action] = reward + values[successor]` | Add reward to the prior iteration's value at the successor. In the second iteration at level 1, sell gives `2 + F_1(0) = 2`, stock gives `0 + F_1(2) = 2`; both must be retained. |
| 9. `next_values[level] = max(candidates.values())` | Store the maximum candidate as the new value at this level. |
| 10. `actions = []` | Start an empty list for every maximizing action. |
| 11. `for action, candidate in candidates.items():` | Visit the action/candidate pairs. |
| 12. `if candidate == next_values[level]:` | Compare each candidate to the newly stored maximum using `==`. |
| 13. `actions.append(action)` | Append every tied maximizer, preserving both sell and stock when they have equal values. |
| 14. `print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")` | Print remaining count, level, both candidates, and all best actions using an f-string. |
| 15. `values = next_values` | After finishing every level, replace the continuation dictionary with the completed new dictionary. This advances from $F_{n-1}$ to $F_n$. |
| 16. `print(f"F_{remaining} = {values}")` | Print the full value dictionary for this remaining count. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
n=2, l=0: candidates={'sell': 0, 'stock': 2}, best=['stock']
n=2, l=1: candidates={'sell': 2, 'stock': 2}, best=['sell', 'stock']
n=2, l=2: candidates={'sell': 4, 'stock': 5}, best=['stock']
n=2, l=3: candidates={'sell': 4, 'stock': 10}, best=['stock']
F_2 = {0: 2, 1: 2, 2: 5, 3: 10}
```

The second loop iteration prints both first-action names at level 1. Its continuation dictionary is still $F_1$ throughout that iteration; separate `next_values` prevents mixing horizons.

<a id="5c"></a>

### 5(c) Three decisions remaining

> For horizon $H=3$, determine the optimal first action at $l=1$.

#### 1. Read the question carefully.

Find the first action at inventory 1 when $H=3$, using the two-decision layer from 5(b). Show what later sequence realizes its value.

#### 2. Explain every concept and symbol.

Now the continuation has two decisions remaining. The capacity bonus can become reachable within the horizon. An action with immediate reward zero can be optimal when it positions the inventory for a larger later reward. No extra terminal salvage is being introduced.

#### 3. Solve it by hand.

Substitute $(F_2(0),F_2(1),F_2(2),F_2(3))=(2,2,5,10)$:

| Level | sell candidate | stock candidate | $F_3$ | Best actions |
| --- | --- | --- | --- | --- |
| 0 | $0+2=2$ | $0+2=2$ | 2 | sell, stock |
| 1 | $2+2=4$ | $0+5=5$ | 5 | stock |
| 2 | $2+2=4$ | $0+10=10$ | 10 | stock |
| 3 | $2+5=7$ | $5+10=15$ | 15 | stock |

At the start, stock gives 5 versus sell's 4, so stock is uniquely optimal. Recover the path: from 1 with three decisions left, stock to 2, reward 0. From 2 with two decisions left, stock to 3, reward 0. From 3 with one decision left, stock and remain at 3, reward 5. Total reward is $0+0+5=5$. If first selling, the best continuation from zero with two decisions left is stock then sell, yielding $2+0+2=4$.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem05.py](examples/problem05.py) (run the whole file; earlier excerpts supply its inputs):

```python
values = {level: 0 for level in range(4)}
for remaining in range(1, 4):
    next_values = {}
    for level in range(4):
        candidates = {}
        for action in ("sell", "stock"):
            successor, reward = inventory_step(level, action)
            candidates[action] = reward + values[successor]
        next_values[level] = max(candidates.values())
        actions = []
        for action, candidate in candidates.items():
            if candidate == next_values[level]:
                actions.append(action)
        print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")
    values = next_values
    print(f"F_{remaining} = {values}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `values = {level: 0 for level in range(4)}` | Initialize the no-decisions-remaining values to zero for levels 0, 1, 2, 3. `range(4)` enumerates these four integer state keys. |
| 2. `for remaining in range(1, 4):` | Visit remaining decision counts 1, 2, 3. Values from the preceding iteration have one fewer decision remaining. |
| 3. `next_values = {}` | Create a separate dictionary for this iteration's values; this prevents overwriting continuation values while they are still needed. |
| 4. `for level in range(4):` | Visit all four inventory levels, not only the initial level 1. |
| 5. `candidates = {}` | Initialize the two action candidates for this level. |
| 6. `for action in ("sell", "stock"):` | Visit the admissible action strings sell and stock in that order. |
| 7. `successor, reward = inventory_step(level, action)` | Call the transition function and unpack its `(successor, reward)` result. |
| 8. `candidates[action] = reward + values[successor]` | Add reward to the prior iteration's value at the successor. In the third iteration at level 1, sell gives `2 + F_2(0) = 4`, stock gives `0 + F_2(2) = 5`, so stock becomes uniquely best. |
| 9. `next_values[level] = max(candidates.values())` | Store the maximum candidate as the new value at this level. |
| 10. `actions = []` | Start an empty list for every maximizing action. |
| 11. `for action, candidate in candidates.items():` | Visit the action/candidate pairs. |
| 12. `if candidate == next_values[level]:` | Compare each candidate to the newly stored maximum using `==`. |
| 13. `actions.append(action)` | Append every tied maximizer, preserving both sell and stock when they have equal values. |
| 14. `print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")` | Print remaining count, level, both candidates, and all best actions using an f-string. |
| 15. `values = next_values` | After finishing every level, replace the continuation dictionary with the completed new dictionary. This advances from $F_{n-1}$ to $F_n$. |
| 16. `print(f"F_{remaining} = {values}")` | Print the full value dictionary for this remaining count. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
n=3, l=0: candidates={'sell': 2, 'stock': 2}, best=['sell', 'stock']
n=3, l=1: candidates={'sell': 4, 'stock': 5}, best=['stock']
n=3, l=2: candidates={'sell': 4, 'stock': 10}, best=['stock']
n=3, l=3: candidates={'sell': 7, 'stock': 15}, best=['stock']
F_3 = {0: 2, 1: 5, 2: 10, 3: 15}
```

The third iteration matches the table, including the level-0 tie. At the specified level 1, only stock is printed, and its value 5 equals the recovered three-action return.

<a id="5d"></a>

### 5(d) How the horizon changes optimality

> Give a concise explanation of how the horizon changes the meaning of “optimal” in this example.

#### 1. Read the question carefully.

Summarize the three starting decisions and explain the economic reason using the same inventory rules.

#### 2. Explain every concept and symbol.

“Optimal” maximizes total reward over the available decisions, not the next reward in isolation. The horizon determines how much continuation is available. The comparison must use the same starting inventory and model across horizons.

#### 3. Solve it by hand.

At level 1:

| Horizon | sell first | stock first | Optimal first actions |
| --- | --- | --- | --- |
| 1 | 2 | 0 | sell |
| 2 | 2 | 2 | sell, stock |
| 3 | 4 | 5 | stock |

With one decision, only the sale can pay. With two, stocking can be followed by a sale and catches up with selling now. With three, two stocking steps reach capacity and the third stocking action earns the source's bonus 5. The future opportunities change the comparison even though the transition rules remain fixed.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

There is no additional code. The three level-1 lines in the executed inventory output give exactly the 2/0, 2/2, and 4/5 comparisons summarized here.

<a id="problem-6"></a>

## Problem 6: Optimal stopping: selling an asset

**Source setup (verbatim, with TeX recovered from the HTML):**

You want to sell an asset and receive one offer per stage, $h=0,1,\ldots,H-1$. The offers $X_0,\ldots,X_{H-1}$ are independent and uniformly distributed on $[0,1]$. After observing $X_h$ you either accept, receive $X_h$, and the problem ends, or reject and wait for the next offer. Rejected offers are lost, and the last offer must be accepted.

<a id="6a"></a>

### 6(a) An MDP with observed offers

> Formulate the problem as a finite-horizon MDP: state, actions, rewards, and transitions.

#### 1. Read the question carefully.

Formulate the decision made after seeing each offer. Preserve independence, uniform offers on [0,1], loss of rejected offers, and forced acceptance of the final offer. The observed offer must be part of the decision state.

#### 2. Explain every concept and symbol.

A continuous state can take any real value in an interval rather than a finite set. Let $x$ denote an observed offer and $\dagger$ a sold absorbing state. Include the stage in the active state $(h,x)$ so the number of remaining offers and last-stage action restriction are recorded. A transition kernel over continuous offers assigns probabilities to sets of offers. Uniform on [0,1] means an interval of length $b-a$ has probability $b-a$.

#### 3. Solve it by hand.

Take active states $(h,x)$ for $h=0,\ldots,H-1$ and $x\in[0,1]$, together with $\dagger$.

For $h<H-1$, allow accept and reject. At $(H-1,x)$ allow only accept. Accept earns $x$ immediately and moves to $\dagger$ with probability 1. Reject earns 0 and moves to $(h+1,X_{h+1})$, where the new offer is independently uniform on [0,1]. Formally, for any measurable set $A\subseteq[0,1]$,

$$P(\{h+1\}\times A\mid(h,x),\mathrm{reject})=\int_A 1\,dy.$$

The dummy variable $y$ is the next offer; the density 1 makes this integral the set's uniform probability. An interval $A=[0.2,0.5]$ therefore has probability $0.5-0.2=0.3$. At $\dagger$, use a zero-reward stop action returning to $\dagger$. All horizon boundary values are zero; earned sale proceeds have already been counted as a reward. There is no recall action for an older rejected offer.

The initial state distribution has $X_0$ uniform before the first observation. Including stage $h$ makes the model Markov: after rejecting, the next offer law depends on no earlier offer. A state containing only “unsold” would miss the observed $x$ needed for the acceptance decision.

#### 4. Translate the reasoning into simple code.

The formulation is most transparent as a state/action/kernel specification. Exact expectation calculations in 6(c) avoid simulating or discretizing the continuous offers. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No output applies to the model definition. Check that acceptance receives one payment and ends the sale, rejection receives none and draws an independent offer, and the last-stage action set forces acceptance.

<a id="6b"></a>

### 6(b) Before-observation values and thresholds

> Let $W_h$ denote the optimal expected reward at stage $h$ before the offer $X_h$ is observed. Derive the recursion $W_h = \mathbb{E}[\max(X_h, W_{h+1})]$ with $W_{H-1}=\mathbb{E}[X_{H-1}]$, and show that the optimal policy is a threshold rule.

#### 1. Read the question carefully.

Derive the recursion for $W_h$, the value before seeing offer $X_h$, and the action rule after seeing it. Keep these two information states distinct. The source uses $W_h$ as a number, unrelated to the machine state $W$.

#### 2. Explain every concept and symbol.

Let $U_h(x)$ be the optimal value after observing $x$ while still owning the asset. $W_h=\mathbb E[U_h(X_h)]$ averages that value before observing the offer. At a rejection decision, independence means that knowledge of $x$ does not change the next offer's value $W_{h+1}$. A threshold is a cutoff: accept offers above it, reject those below it. At equality both admissible actions have the same expected value.

#### 3. Solve it by hand.

At the last stage, rejection is forbidden, so

$$U_{H-1}(x)=x,\qquad W_{H-1}=\mathbb E[X_{H-1}].$$

At an earlier stage $h$, acceptance yields $x$ now with zero future value. Rejection yields zero now and expected next-stage value $W_{h+1}$. Therefore

$$U_h(x)=\max\{x,W_{h+1}\},\qquad W_h=\mathbb E[\max\{X_h,W_{h+1}\}],\quad h=H-2,\ldots,0.$$

For $h<H-1$, define $t_h=W_{h+1}$. If $x>t_h$, accept; if $x<t_h$, reject; if $x=t_h$, both are optimal. We may accept at equality for presentation. At the final stage accept every offer, including zero. Writing $t_{H-1}=0$ is a convenient label for this forced rule, not permission to reject a zero last offer.

For a uniform final offer, $W_{H-1}=\int_0^1x\,dx=[x^2/2]_0^1=1/2$. No previously rejected offer enters either comparison because it is unavailable.

#### 4. Translate the reasoning into simple code.

The threshold recursion is derived symbolically here. The small exact-arithmetic implementation appears after evaluating its expectation in 6(c). No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No separate output is needed. The boundary is the mean last offer, 1/2, rather than an observed-offer value or a machine value. The implementation below stores `before_offer` and `thresholds` separately to preserve this distinction.

<a id="6c"></a>

### 6(c) Evaluating the uniform integral and the four-stage case

> Show that $\mathbb{E}[\max(X,c)] = (1+c^2)/2$ for $X\sim\text{Uniform}[0,1]$ and $c\in[0,1]$. Compute the thresholds and $W_0$ for $H=4$, and compare $W_0$ with the value of accepting the first offer.

#### 1. Read the question carefully.

Integrate the maximum of a uniform offer and cutoff $c$, then use that identity to compute all thresholds and the initial pre-observation value for four offers. Compare with accepting the first offer immediately.

#### 2. Explain every concept and symbol.

Here $c$ is a real cutoff in [0,1]. The uniform density is 1, so expectation is the integral of the payoff over [0,1]. Split the interval at $c$ because the larger quantity is $c$ below the cutoff and $x$ above it. The antiderivative of $x$ is $x^2/2$; $[f(x)]_a^b$ means $f(b)-f(a)$. A fraction stores each result exactly, while decimal output is rounded for readability.

#### 3. Solve it by hand.

For $0\le c\le1$,

$$\mathbb E[\max(X,c)]=\int_0^c c\,dx+\int_c^1x\,dx.$$

The first integral is a rectangle of height $c$ and width $c$, so it is $c^2$. The second is $[x^2/2]_c^1=1/2-c^2/2$. Adding gives

$$c^2+\frac12-\frac{c^2}{2}=\boxed{\frac{1+c^2}{2}}.$$

For $H=4$, there are stages 0, 1, 2, 3. Work backward:

$$W_3=\frac12,\qquad t_2=W_3=\frac12,$$

$$W_2=\frac{1+(1/2)^2}{2}=\frac{1+1/4}{2}=\frac{5/4}{2}=\frac58,\qquad t_1=W_2=\frac58,$$

$$W_1=\frac{1+(5/8)^2}{2}=\frac{1+25/64}{2}=\frac{89/64}{2}=\frac{89}{128},\qquad t_0=W_1=\frac{89}{128},$$

$$W_0=\frac{1+(89/128)^2}{2}=\frac{1+7921/16384}{2}=\frac{24305/16384}{2}=\frac{24305}{32768}\approx0.741729736.$$

The complete threshold list is $(t_0,t_1,t_2,t_3)=(89/128,5/8,1/2,0)$, with $t_3=0$ denoting forced acceptance. For example, at day 0 an offer 0.7 exceeds $89/128=0.6953125$ and is accepted; an offer 0.6 is rejected.

Accepting the first offer has expected reward $\mathbb E[X_0]=1/2=16384/32768$. The improvement is

$$W_0-\frac12=\frac{24305-16384}{32768}=\frac{7921}{32768}\approx0.241729736.$$

This is a comparison of expectations over offer sequences, not a claim that the threshold strategy sells for more on every sequence.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem06.py](examples/problem06.py) (run the whole file; earlier excerpts supply its inputs):

```python
from fractions import Fraction

horizon = 4
before_offer = [Fraction(0) for stage in range(horizon)]
thresholds = [Fraction(0) for stage in range(horizon)]
before_offer[horizon - 1] = Fraction(1, 2)
for stage in range(horizon - 2, -1, -1):
    continuation = before_offer[stage + 1]
    thresholds[stage] = continuation
    before_offer[stage] = (1 + continuation * continuation) / 2
for stage in range(horizon):
    print(f"h={stage}: threshold={float(thresholds[stage]):.9f}, W={before_offer[stage]} ({float(before_offer[stage]):.9f})")
gain = before_offer[0] - Fraction(1, 2)
print(f"Gain over accepting first offer: {gain} ({float(gain):.9f})")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from fractions import Fraction` | Import exact rational arithmetic from the standard library; no numerical integration package is needed. |
| 2. `horizon = 4` | Set the horizon to four offers. |
| 3. `before_offer = [Fraction(0) for stage in range(horizon)]` | Create a four-element list of zero fractions for pre-observation values. Index 0 means day 0, not a state. |
| 4. `thresholds = [Fraction(0) for stage in range(horizon)]` | Create a separate four-element list for acceptance thresholds. The final zero is the convention for forced acceptance. |
| 5. `before_offer[horizon - 1] = Fraction(1, 2)` | Assign `before_offer[3] = 1/2`, the expected mandatory last offer. |
| 6. `for stage in range(horizon - 2, -1, -1):` | `range(2, -1, -1)` visits stages 2, 1, 0, so the next-stage value has already been calculated. |
| 7. `continuation = before_offer[stage + 1]` | Read the expected value before the next offer into `continuation`. |
| 8. `thresholds[stage] = continuation` | Store that continuation as this day's acceptance cutoff. |
| 9. `before_offer[stage] = (1 + continuation * continuation) / 2` | Apply the integral identity `(1 + continuation * continuation) / 2`. Fractions keep all intermediate results exact. |
| 10. `for stage in range(horizon):` | Visit stages 0, 1, 2, 3 to display the results in decision order. |
| 11. `print(f"h={stage}: threshold={float(thresholds[stage]):.9f}, W={before_offer[stage]} ({float(before_offer[stage]):.9f})")` | Print threshold to nine decimals, exact fraction `W`, and its nine-decimal display. The exact fraction allows checking the rounding. |
| 12. `gain = before_offer[0] - Fraction(1, 2)` | Subtract the first-offer mean 1/2 from the optimal initial mean. |
| 13. `print(f"Gain over accepting first offer: {gain} ({float(gain):.9f})")` | Print the exact gain and its rounded decimal representation. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
h=0: threshold=0.695312500, W=24305/32768 (0.741729736)
h=1: threshold=0.625000000, W=89/128 (0.695312500)
h=2: threshold=0.500000000, W=5/8 (0.625000000)
h=3: threshold=0.000000000, W=1/2 (0.500000000)
Gain over accepting first offer: 7921/32768 (0.241729736)
```

Run `python3 examples/problem06.py`. Every fraction and threshold matches the hand recursion. The printed 0.741729736 is the nine-decimal rounding of 24305/32768, not the number used in subsequent arithmetic.

<a id="6d"></a>

### 6(d) Why the threshold declines near the deadline

> Explain why the threshold decreases as fewer stages remain.

#### 1. Read the question carefully.

Explain the ordering of the cutoffs as remaining offers decrease, using both the opportunity argument and the recursion.

#### 2. Explain every concept and symbol.

The rejection value measures the opportunity to wait. More remaining offers provide additional opportunities, so waiting cannot be worth less when more stages are available. To justify the inequality quantitatively, compare the recursion result with its input for a cutoff $c\in[0,1]$.

#### 3. Solve it by hand.

Subtract $c$ from the uniform recursion:

$$\frac{1+c^2}{2}-c=\frac{1+c^2-2c}{2}=\frac{(1-c)^2}{2}\ge0.$$

Thus $W_h\ge W_{h+1}$, and for the finite values here, which are below 1, the inequality is strict. Because $t_h=W_{h+1}$ before the final stage, an earlier decision has a higher cutoff. For $H=4$, the cutoffs fall as $0.6953125>0.625>0.5>0$. Close to the deadline, rejecting sacrifices an offer with fewer chances to replace it, so acceptance is optimal at a lower observed price. The final drop to zero comes from mandatory acceptance.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No new computation is required. The exact threshold fractions in 6(c) have the stated ordering, and the nonnegative-square identity proves the general direction for uniform offers.

<a id="problem-7"></a>

## Problem 7: Wear depends on the previous day

**Source setup (verbatim, with TeX recovered from the HTML):**

Return to the machine MDP with one change: if the machine was operated on the previous day and is still working, operating it again breaks it with probability $0.7$ instead of $0.4$. After maintain, repair, or replace, and on day $0$, the original probabilities apply.

<a id="7a"></a>

### 7(a) Why the original state loses the Markov property

> Explain why the process with state space $\{W,B\}$ is no longer Markov under this rule.

#### 1. Read the question carefully.

The original machine transitions change only when operating a working machine that was operated the previous day. Show why the present label $W$ does not give enough predictive information; no change to rewards is specified.

#### 2. Explain every concept and symbol.

The Markov property requires the conditional next-state law given current state/action and past history to equal the law given current state/action alone. A history is the sequence of preceding states and actions. If two histories end at the same recorded state but imply different next-state laws for the same action, that recorded state is incomplete.

#### 3. Solve it by hand.

Consider day 1 in state $W$. One possible preceding history is day-0 $W$ followed by operate and survival; another is day-0 $W$ followed by maintain and survival. Both have positive probability and both end at $W$.

If we operate on day 1 after the first history, the new break probability is 0.7. After the second history it is the original 0.4. Thus

$$P(s_2=B\mid s_1=W,a_1=\mathrm{operate},a_0=\mathrm{operate})=0.7,$$

$$P(s_2=B\mid s_1=W,a_1=\mathrm{operate},a_0=\mathrm{maintain})=0.4.$$

The same current state and action have different conditional future laws depending on omitted history, so $\{W,B\}$ is not a sufficient Markov state representation for this controlled environment. A fixed policy can happen to hide the issue by never revisiting one history, but it does not repair the model for arbitrary decisions.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

This is a model-property argument, with no executable code. Its check is the explicit pair of positive-probability histories yielding 0.7 versus 0.4 for the same recorded state/action.

<a id="7b"></a>

### 7(b) Restoring the state and defining transitions

> Augment the working state with a binary variable $c$ indicating whether the machine was operated on the previous day. Specify the augmented state space and the transition kernel.

#### 1. Read the question carefully.

Augment each working state with whether operation occurred yesterday, and specify every allowed transition. On day 0 the original probabilities apply. Broken states may be combined because their repair and replacement transitions do not depend on yesterday’s action.

#### 2. Explain every concept and symbol.

Let $c\in\{0,1\}$ indicate previous-day operation when the current machine is working. This $c$ is a wear flag, unrelated to the cutoff in problem 6. Write $W0=(W,0)$ and $W1=(W,1)$ in code. The augmented state is $z$ below, an arbitrary state symbol unrelated to the deterministic problem's named state $z$. Its kernel is $\widetilde P$. After operation followed by a working successor, the new flag is 1; after maintain, repair, or replace followed by working, it is 0.

#### 3. Solve it by hand.

A sufficient state space is

$$\widetilde{\mathcal S}=\{(W,0),(W,1),B\},\qquad z_0=(W,0).$$

The action sets remain operate/maintain at either working state and repair/replace at $B$. The full kernel and unchanged rewards are:

| Current state | Action | Reward | To $(W,0)$ | To $(W,1)$ | To $B$ |
| --- | --- | --- | --- | --- | --- |
| $(W,0)$ | operate | 8 | 0 | 0.6 | 0.4 |
| $(W,0)$ | maintain | 5 | 0.9 | 0 | 0.1 |
| $(W,1)$ | operate | 8 | 0 | 0.3 | 0.7 |
| $(W,1)$ | maintain | 5 | 0.9 | 0 | 0.1 |
| $B$ | repair | -2 | 0.7 | 0 | 0.3 |
| $B$ | replace | -6 | 1 | 0 | 0 |

For example, operating at $(W,1)$ survives with probability $1-0.7=0.3$ and keeps the flag at 1. Maintaining clears the flag even when the machine was operated yesterday. A broken successor needs no flag because only repair or replace can be used there, and both reset the working successor to flag 0. One could retain $(B,0)$ and $(B,1)$ separately, but they have identical admissible rewards and future laws and can be merged without losing predictive information. The present augmented state now determines every transition row regardless of earlier history.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem07.py](examples/problem07.py) (run the whole file; earlier excerpts supply its inputs):

```python
from common import Fraction, machine, backward_values, best_actions

augmented = {}
for state in ("W0", "W1", "B"):
    if state == "B":
        original_state = "B"
    else:
        original_state = "W"
    augmented[state] = {}
    for action in machine[original_state]:
        reward, transitions = machine[original_state][action]
        working_probability = transitions["W"]
        if state == "W1" and action == "operate":
            working_probability = Fraction("0.3")
        if action == "operate":
            working_successor = "W1"
        else:
            working_successor = "W0"
        augmented[state][action] = (reward, {working_successor: working_probability, "B": 1 - working_probability})
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from common import Fraction, machine, backward_values, best_actions` | Import the original exact machine model, backward solver, and maximizing-action helper. |
| 2. `augmented = {}` | Create an empty dictionary for the augmented model. |
| 3. `for state in ("W0", "W1", "B"):` | Visit the three sufficient state labels `W0`, `W1`, and `B`. |
| 4. `if state == "B":` | Test whether the current augmented label is broken. |
| 5. `original_state = "B"` | Use original state `B` to retrieve its reward and action rows. |
| 6. `else:` | Otherwise handle a working augmented state. |
| 7. `original_state = "W"` | Use original state `W` for either `W0` or `W1`. |
| 8. `augmented[state] = {}` | Create an empty action dictionary for this augmented state. |
| 9. `for action in machine[original_state]:` | Visit each action of the corresponding original state. |
| 10. `reward, transitions = machine[original_state][action]` | Unpack its reward and original transition probabilities. These original data are read, not modified. |
| 11. `working_probability = transitions["W"]` | Initialize working-survival probability from the original row. |
| 12. `if state == "W1" and action == "operate":` | Check both conditions that trigger increased wear: augmented state `W1` and action operate. `and` requires both. |
| 13. `working_probability = Fraction("0.3")` | Override survival probability with exactly 0.3, implying break probability 0.7. |
| 14. `if action == "operate":` | Test whether the chosen action is operation to determine the next wear flag. |
| 15. `working_successor = "W1"` | A working successor of operation is `W1`, recording the just-performed operation. |
| 16. `else:` | Otherwise choose the reset flag. |
| 17. `working_successor = "W0"` | A working successor of maintain, repair, or replace is `W0`. |
| 18. `augmented[state][action] = (reward, {working_successor: working_probability, "B": 1 - working_probability})` | Store the reward and a transition dictionary containing the working successor and broken successor, with probabilities `working_probability` and `1 - working_probability`. Other augmented states have implicit probability zero. |

#### 6. Compare the output with our hand solution.

This model-construction excerpt produces no output by itself. Reading `augmented["W1"]["operate"]` gives reward 8 with probabilities 3/10 to `W1` and 7/10 to `B`; reading its maintain row gives 9/10 to `W0`. The solver in 7(c) executes this kernel. Run the complete file with `python3 examples/problem07.py`.

<a id="7c"></a>

### 7(c) Backward induction in the augmented model

> Write the finite-horizon Bellman recursion for the augmented MDP. For $H=3$ and zero terminal value, compute $V_0^*(W,0)$ and the optimal actions at $h=1$ in all augmented states.

#### 1. Read the question carefully.

Write the recursion for the three-state model, compute the requested initial value from $(W,0)$, and list all optimal actions on day 1. Use a three-day horizon and zero boundary.

#### 2. Explain every concept and symbol.

$\widetilde V_h^*(z)$ is the maximum expected reward in the augmented state $z$. The tilde distinguishes the new model; it does not mean approximation. The optimality recursion is unchanged in form because state augmentation restored the Markov property. Its successor sum now ranges over the three augmented states. Stage 3 has no action or salvage reward.

#### 3. Solve it by hand.

The recursion is

$$\widetilde V_h^*(z)=\max_{a\in\mathcal A(z)}\left[r(z,a)+\sum_{z'\in\widetilde{\mathcal S}}\widetilde P(z'\mid z,a)\widetilde V_{h+1}^*(z')\right],\quad\widetilde V_3^*(z)=0.$$

At stage 2, continuations vanish. Both working states compare operate $8+0=8$ with maintain $5+0=5$, choosing operate. The broken state compares repair $-2+0=-2$ with replace $-6+0=-6$, choosing repair. Thus stage-2 values in order $(W0,W1,B)$ are $(8,8,-2)$.

At stage 1:

| State | First action candidate | Second action candidate | Value | All optimal actions |
| --- | --- | --- | --- | --- |
| $W0$ | operate: $8+0.6(8)+0.4(-2)=8+4.8-0.8=12$ | maintain: $5+0.9(8)+0.1(-2)=5+7.2-0.2=12$ | 12 | operate, maintain |
| $W1$ | operate: $8+0.3(8)+0.7(-2)=8+2.4-1.4=9$ | maintain: $5+0.9(8)+0.1(-2)=5+7.2-0.2=12$ | 12 | maintain |
| $B$ | repair: $-2+0.7(8)+0.3(-2)=-2+5.6-0.6=3$ | replace: $-6+1(8)=-6+8=2$ | 3 | repair |

At stage 0:

| State | First action candidate | Second action candidate | Value |
| --- | --- | --- | --- |
| $W0$ | operate: $8+0.6(12)+0.4(3)=8+7.2+1.2=16.4$ | maintain: $5+0.9(12)+0.1(3)=5+10.8+0.3=16.1$ | 16.4 |
| $W1$ | operate: $8+0.3(12)+0.7(3)=8+3.6+2.1=13.7$ | maintain: $5+0.9(12)+0.1(3)=5+10.8+0.3=16.1$ | 16.1 |
| $B$ | repair: $-2+0.7(12)+0.3(3)=-2+8.4+0.9=7.3$ | replace: $-6+1(12)=-6+12=6$ | 7.3 |

The specified initial state is $W0$, so $\widetilde V_0^*(W,0)=16.4$ and its first action is operate. A surviving operated machine reaches $W1$ on day 1, where maintain is uniquely optimal. The day-0 $W1$ row is the time-homogeneous augmented kernel's hypothetical extension; the source initializes day 0 at flag 0, so that row does not describe a permitted initial history or affect the requested result.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem07.py](examples/problem07.py) (run the whole file; earlier excerpts supply its inputs):

```python
terminal = {state: Fraction(0) for state in augmented}
values, action_values = backward_values(augmented, 3, terminal)
for stage in (2, 1, 0):
    for state in augmented:
        candidates = action_values[stage][state]
        print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")
print(f"Optimal V0(W,0) = {float(values[0]['W0']):.2f}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `terminal = {state: Fraction(0) for state in augmented}` | Assign exact zero terminal values to each augmented state using a dictionary comprehension. |
| 2. `values, action_values = backward_values(augmented, 3, terminal)` | Optimize the augmented model for three decisions by omitting the optional policy argument. |
| 3. `for stage in (2, 1, 0):` | Visit decision stages 2, 1, 0 for display. |
| 4. `for state in augmented:` | Visit all three augmented states at each stage. |
| 5. `candidates = action_values[stage][state]` | Look up each state's computed action candidates. |
| 6. `print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")` | Print action candidates as a display dictionary, value to two decimals, and every maximizing action. This makes the day-1 `W0` tie and `W1` strict preference visible. |
| 7. `print(f"Optimal V0(W,0) = {float(values[0]['W0']):.2f}")` | Print the requested start value at stage 0 in `W0`. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
h=2, W0: Q={'operate': 8.0, 'maintain': 5.0}, V=8.00, best=['operate']
h=2, W1: Q={'operate': 8.0, 'maintain': 5.0}, V=8.00, best=['operate']
h=2, B: Q={'repair': -2.0, 'replace': -6.0}, V=-2.00, best=['repair']
h=1, W0: Q={'operate': 12.0, 'maintain': 12.0}, V=12.00, best=['operate', 'maintain']
h=1, W1: Q={'operate': 9.0, 'maintain': 12.0}, V=12.00, best=['maintain']
h=1, B: Q={'repair': 3.0, 'replace': 2.0}, V=3.00, best=['repair']
h=0, W0: Q={'operate': 16.4, 'maintain': 16.1}, V=16.40, best=['operate']
h=0, W1: Q={'operate': 13.7, 'maintain': 16.1}, V=16.10, best=['maintain']
h=0, B: Q={'repair': 7.3, 'replace': 6.0}, V=7.30, best=['repair']
Optimal V0(W,0) = 16.40
```

The executed tables agree with every hand candidate. All day-1 actions, including the `W0` tie, are retained. The script also displays a hypothetical day-0 `W1` row, while the actual start is `W0`.

<a id="7d"></a>

### 7(d) Evaluating always operate / always repair

> Evaluate the policy “operate whenever the machine works, repair when it is broken” in the augmented model, starting from $(W,0)$. Compare its value with $V_0^*(W,0)$ and explain the difference.

#### 1. Read the question carefully.

Evaluate the specified policy in the augmented model, starting at $(W,0)$. It operates in both working states and repairs in $B$. Compare its expected reward with the optimum, keeping wear-dependent transitions in the evaluation.

#### 2. Explain every concept and symbol.

This is policy evaluation, so take the policy's candidate even when it is below another action. Denote its value $\widetilde V_h^\rho$, where $\rho$ labels this operate/repair policy, distinct from the cautious $\pi$ used earlier. Expected loss is the optimum minus this fixed-policy value.

#### 3. Solve it by hand.

At stage 2, $\rho$ is optimal: its values are $(8,8,-2)$ in order $(W0,W1,B)$. At stage 1 it chooses operate even in $W1$:

$$\widetilde V_1^\rho(W0)=8+0.6(8)+0.4(-2)=12,$$

$$\widetilde V_1^\rho(W1)=8+0.3(8)+0.7(-2)=9,$$

$$\widetilde V_1^\rho(B)=-2+0.7(8)+0.3(-2)=3.$$

At the specified start, operation leads to $W1$ with probability 0.6 and $B$ with probability 0.4. Consequently

$$\widetilde V_0^\rho(W0)=8+0.6(9)+0.4(3)=8+5.4+1.2=14.6.$$

For the script's other two state entries,

$$\widetilde V_0^\rho(W1)=8+0.3(9)+0.7(3)=8+2.7+2.1=12.8,$$

$$\widetilde V_0^\rho(B)=-2+0.7(12)+0.3(3)=-2+8.4+0.9=7.3.$$

The requested loss is $16.4-14.6=1.8$. Both policies first operate from $W0$. With probability 0.6 the machine survives into $W1$, where operating again yields 9 rather than maintaining's 12. The expected loss is therefore $0.6(12-9)=0.6(3)=1.8$. On the broken branch both repair; on the final day both act optimally. The reduced state representation would miss precisely the distinction causing this loss.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem07.py](examples/problem07.py) (run the whole file; earlier excerpts supply its inputs):

```python
operate_repair = [{"W0": "operate", "W1": "operate", "B": "repair"} for stage in range(3)]
policy_values, policy_q = backward_values(augmented, 3, terminal, operate_repair)
for stage in (2, 1, 0):
    print(f"Policy V_{stage} = { {s: float(v) for s, v in policy_values[stage].items()} }")
loss = values[0]["W0"] - policy_values[0]["W0"]
print(f"Operate/repair loss from (W,0) = {float(loss):.2f}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `operate_repair = [{"W0": "operate", "W1": "operate", "B": "repair"} for stage in range(3)]` | Create three stage dictionaries implementing operate in both working states and repair in `B`. |
| 2. `policy_values, policy_q = backward_values(augmented, 3, terminal, operate_repair)` | Pass this policy to the backward solver, activating evaluation rather than optimization, and store its values separately from optimal `values`. |
| 3. `for stage in (2, 1, 0):` | Visit stages 2, 1, 0 to display the evaluated dictionaries. |
| 4. `print(f"Policy V_{stage} = { {s: float(v) for s, v in policy_values[stage].items()} }")` | Convert each exact state value to a float for readable output while preserving its state label. |
| 5. `loss = values[0]["W0"] - policy_values[0]["W0"]` | Subtract this policy's start value from the optimal start value. |
| 6. `print(f"Operate/repair loss from (W,0) = {float(loss):.2f}")` | Print the expected loss to two decimals. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Policy V_2 = {'W0': 8.0, 'W1': 8.0, 'B': -2.0}
Policy V_1 = {'W0': 12.0, 'W1': 9.0, 'B': 3.0}
Policy V_0 = {'W0': 14.6, 'W1': 12.8, 'B': 7.3}
Operate/repair loss from (W,0) = 1.80
```

The evaluated start return 14.6 and loss 1.80 agree with both the direct recursion and the probability-weighted local-loss argument.

<a id="problem-8"></a>

## Problem 8: Terminal value and policy switching

**Source setup (verbatim, with TeX recovered from the HTML):**

Modify the machine MDP by assigning terminal values $V_3(W)=\lambda,
\qquad
V_3(B)=0,$ where $\lambda\geq 0$ is a salvage value for ending with a working machine.

<a id="8a"></a>

### 8(a) Values as functions of salvage

> Derive $V_2^*(W)$ and $V_2^*(B)$ as piecewise-linear functions of $\lambda$.

#### 1. Read the question carefully.

Replace only the machine's terminal boundary by $V_3(W)=\lambda$, $V_3(B)=0$, with $\lambda\ge0$. Derive the optimal last-decision values as functions of the parameter before substituting particular values. Immediate rewards and transitions remain the source's original machine rows.

#### 2. Explain every concept and symbol.

$\lambda$ is a nonnegative salvage payment for a working machine at the horizon, not an inventory level. A linear function $b+m\lambda$ has intercept $b$ and slope $m$; here its slope is the probability of a working terminal successor. A piecewise-linear function selects different linear formulas on different parameter intervals. $V_2^*$ now counts both the last action's reward and the expected terminal payment.

#### 3. Solve it by hand.

Substitute the parameterized boundary into each action candidate:

$$Q_2^*(W,\mathrm{operate})=8+0.6\lambda+0.4(0)=8+0.6\lambda,$$

$$Q_2^*(W,\mathrm{maintain})=5+0.9\lambda+0.1(0)=5+0.9\lambda,$$

$$Q_2^*(B,\mathrm{repair})=-2+0.7\lambda+0.3(0)=-2+0.7\lambda,$$

$$Q_2^*(B,\mathrm{replace})=-6+1\lambda+0(0)=-6+\lambda.$$

For $W$, subtract maintain's candidate from operate's: $8+0.6\lambda-(5+0.9\lambda)=3-0.3\lambda$. It is positive below 10, zero at 10, and negative above 10. For $B$, subtract replace from repair: $-2+0.7\lambda-(-6+\lambda)=4-0.3\lambda$. It is positive below $40/3$, zero there, and negative above it. Therefore

$$V_2^*(W)=\begin{cases}8+0.6\lambda,&0\le\lambda\le10,\\5+0.9\lambda,&\lambda>10,\end{cases}$$

$$V_2^*(B)=\begin{cases}-2+0.7\lambda,&0\le\lambda\le40/3,\\-6+\lambda,&\lambda>40/3.\end{cases}$$

At each boundary the two formulas coincide, so assigning the equality point to the first piece is only a notation choice, not a unique-action claim. A negative value at small $\lambda$ is allowed: the source requires a repair or replacement decision at $B$ and supplies no zero-cost idle action.

#### 4. Translate the reasoning into simple code.

These are symbolic functions of a parameter. A few numerical samples would not derive the pieces or prove their interval conditions; exact intersection calculations appear in 8(b). No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No separate console output is needed. At $\lambda=0$ the formulas reduce to the verified original last-day values 8 and -2. At $\lambda=10$ both working formulas give 14; at $\lambda=40/3$ both broken formulas give 22/3, checking continuity at each boundary.

<a id="8b"></a>

### 8(b) Switching points and equality cases

> Find every value of $\lambda$ at which the optimal action at time $2$ changes.

#### 1. Read the question carefully.

Find every stage-2 action change for nonnegative salvage. Use the full action comparisons from 8(a), including exact ties at the intersection points.

#### 2. Explain every concept and symbol.

A switch occurs where the candidate difference changes sign. Solve equality of the two linear action values, then inspect which side favors which action. Since there are only two actions per state and their slopes differ, there is at most one intersection per state. Exact fractions represent the noninteger threshold $40/3$.

#### 3. Solve it by hand.

For $W$,

$$8+0.6\lambda=5+0.9\lambda\;\Longrightarrow\;8-5=(0.9-0.6)\lambda\;\Longrightarrow\;3=0.3\lambda\;\Longrightarrow\;\lambda=10.$$

For $B$,

$$-2+0.7\lambda=-6+\lambda\;\Longrightarrow\;-2-(-6)=(1-0.7)\lambda\;\Longrightarrow\;4=0.3\lambda\;\Longrightarrow\;\lambda=\frac{40}{3}.$$

| State | Below switch | At switch | Above switch |
| --- | --- | --- | --- |
| $W$ | operate | operate and maintain at $\lambda=10$ | maintain |
| $B$ | repair | repair and replace at $\lambda=40/3$ | replace |

Both intersections lie in the permitted nonnegative range. Their strictly signed differences on either side prove that there are no other stage-2 action switches.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem08.py](examples/problem08.py) (run the whole file; earlier excerpts supply its inputs):

```python
from common import Fraction, machine, backward_values, best_actions

working_switch = (Fraction(8) - Fraction(5)) / (Fraction("0.9") - Fraction("0.6"))
broken_switch = (Fraction(-2) - Fraction(-6)) / (Fraction(1) - Fraction("0.7"))
print("Stage 2 switches: W =", working_switch, ", B =", broken_switch)
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from common import Fraction, machine, backward_values, best_actions` | Import the original exact machine model and helpers needed for the following numerical stages. |
| 2. `working_switch = (Fraction(8) - Fraction(5)) / (Fraction("0.9") - Fraction("0.6"))` | Compute reward difference `(8 - 5)` divided by working-survival probability difference `(0.9 - 0.6)`, using exact fractions throughout. |
| 3. `broken_switch = (Fraction(-2) - Fraction(-6)) / (Fraction(1) - Fraction("0.7"))` | Compute broken reward difference `(-2 - (-6))` divided by working-survival difference `(1 - 0.7)`, again exactly. |
| 4. `print("Stage 2 switches: W =", working_switch, ", B =", broken_switch)` | Print both exact intersection values. The second is displayed as `40/3` rather than a rounded decimal. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Stage 2 switches: W = 10 , B = 40/3
```

Run `python3 examples/problem08.py`. Its exact switch outputs match the equations. The equality action sets are established by the candidate comparison, not by choosing one side of a floating-point approximation.

<a id="8c"></a>

### 8(c) Backward induction for three salvage values

> Perform the remaining backward-induction steps for $\lambda\in\{0,10,30\}$ and report the optimal first action from $W$.

#### 1. Read the question carefully.

For $\lambda=0,10,30$, finish stages 1 and 0 after computing stage 2. Report the optimal first action from $W$ and retain all ties, including the stage-2 tie at salvage 10.

#### 2. Explain every concept and symbol.

For each salvage value, keep a separate backward calculation. A terminal reward is passed into the boundary dictionary, not added again at every stage. The stage-1 and stage-0 equations have the same form as 3(a), but use continuation values that already include the terminal salvage. The maximizing action can change at a later stage without changing the first action.

#### 3. Solve it by hand.

For each continuation pair $(w,b)=(V_{h+1}^*(W),V_{h+1}^*(B))$, the four candidates are

$$8+0.6w+0.4b,\quad5+0.9w+0.1b,\quad-2+0.7w+0.3b,\quad-6+w.$$

**For $\lambda=0$**, the boundary pair is $(0,0)$:

| Stage | State | First action candidate | Second action candidate | Value and all maximizers |
| --- | --- | --- | --- | --- |
| 2 | $W$ | operate: $8+0.6(0)+0.4(0)=8$ | maintain: $5+0.9(0)+0.1(0)=5$ | 8; operate |
| 2 | $B$ | repair: $-2+0.7(0)+0.3(0)=-2$ | replace: $-6+0=-6$ | -2; repair |
| 1 | $W$ | operate: $8+0.6(8)+0.4(-2)=8+4.8-0.8=12$ | maintain: $5+0.9(8)+0.1(-2)=5+7.2-0.2=12$ | 12; operate, maintain |
| 1 | $B$ | repair: $-2+0.7(8)+0.3(-2)=-2+5.6-0.6=3$ | replace: $-6+8=2$ | 3; repair |
| 0 | $W$ | operate: $8+0.6(12)+0.4(3)=8+7.2+1.2=16.4$ | maintain: $5+0.9(12)+0.1(3)=5+10.8+0.3=16.1$ | 16.4; operate |
| 0 | $B$ | repair: $-2+0.7(12)+0.3(3)=-2+8.4+0.9=7.3$ | replace: $-6+12=6$ | 7.3; repair |

**For $\lambda=10$**, the boundary pair is $(10,0)$:

| Stage | State | First action candidate | Second action candidate | Value and all maximizers |
| --- | --- | --- | --- | --- |
| 2 | $W$ | operate: $8+0.6(10)+0.4(0)=8+6=14$ | maintain: $5+0.9(10)+0.1(0)=5+9=14$ | 14; operate, maintain |
| 2 | $B$ | repair: $-2+0.7(10)+0.3(0)=-2+7=5$ | replace: $-6+10=4$ | 5; repair |
| 1 | $W$ | operate: $8+0.6(14)+0.4(5)=8+8.4+2=18.4$ | maintain: $5+0.9(14)+0.1(5)=5+12.6+0.5=18.1$ | 18.4; operate |
| 1 | $B$ | repair: $-2+0.7(14)+0.3(5)=-2+9.8+1.5=9.3$ | replace: $-6+14=8$ | 9.3; repair |
| 0 | $W$ | operate: $8+0.6(18.4)+0.4(9.3)=8+11.04+3.72=22.76$ | maintain: $5+0.9(18.4)+0.1(9.3)=5+16.56+0.93=22.49$ | 22.76; operate |
| 0 | $B$ | repair: $-2+0.7(18.4)+0.3(9.3)=-2+12.88+2.79=13.67$ | replace: $-6+18.4=12.4$ | 13.67; repair |

**For $\lambda=30$**, the boundary pair is $(30,0)$:

| Stage | State | First action candidate | Second action candidate | Value and all maximizers |
| --- | --- | --- | --- | --- |
| 2 | $W$ | operate: $8+0.6(30)+0.4(0)=8+18=26$ | maintain: $5+0.9(30)+0.1(0)=5+27=32$ | 32; maintain |
| 2 | $B$ | repair: $-2+0.7(30)+0.3(0)=-2+21=19$ | replace: $-6+30=24$ | 24; replace |
| 1 | $W$ | operate: $8+0.6(32)+0.4(24)=8+19.2+9.6=36.8$ | maintain: $5+0.9(32)+0.1(24)=5+28.8+2.4=36.2$ | 36.8; operate |
| 1 | $B$ | repair: $-2+0.7(32)+0.3(24)=-2+22.4+7.2=27.6$ | replace: $-6+32=26$ | 27.6; repair |
| 0 | $W$ | operate: $8+0.6(36.8)+0.4(27.6)=8+22.08+11.04=41.12$ | maintain: $5+0.9(36.8)+0.1(27.6)=5+33.12+2.76=40.88$ | 41.12; operate |
| 0 | $B$ | repair: $-2+0.7(36.8)+0.3(27.6)=-2+25.76+8.28=32.04$ | replace: $-6+36.8=30.8$ | 32.04; repair |

The first action from $W$ is operate for all three requested salvage values. This agrees with the stage-0 comparisons; it must not be inferred merely from the last-stage action switches.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem08.py](examples/problem08.py) (run the whole file; earlier excerpts supply its inputs):

```python
for salvage in (0, 10, 30):
    terminal = {"W": Fraction(salvage), "B": Fraction(0)}
    values, action_values = backward_values(machine, 3, terminal)
    print(f"lambda={salvage}, V_3={{'W': {salvage}, 'B': 0}}")
    for stage in (2, 1, 0):
        for state in machine:
            candidates = action_values[stage][state]
            print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")
    print("First action from W:", best_actions(action_values[0]["W"]))
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `for salvage in (0, 10, 30):` | Loop over the three requested salvage parameters 0, 10, 30. |
| 2. `terminal = {"W": Fraction(salvage), "B": Fraction(0)}` | Assign the boundary value at `W` to this salvage as an exact fraction, and boundary value at `B` to zero. |
| 3. `values, action_values = backward_values(machine, 3, terminal)` | Optimize from this new boundary through three stages; overwrite the display variables with this parameter's independently computed tables. |
| 4. `print(f"lambda={salvage}, V_3={{'W': {salvage}, 'B': 0}}")` | Print the parameter and boundary. Doubled f-string braces `{{` and `}}` print literal dictionary braces. |
| 5. `for stage in (2, 1, 0):` | Visit stages 2, 1, 0 in backward-computation order. |
| 6. `for state in machine:` | Visit both current states at each stage. |
| 7. `candidates = action_values[stage][state]` | Retrieve that stage/state's candidate dictionary. |
| 8. `print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")` | Print both Q-candidates, the selected optimal value, and all maximizing actions. Fraction equality preserves the $\lambda=10$ tie. |
| 9. `print("First action from W:", best_actions(action_values[0]["W"]))` | After displaying the stages, retrieve and print the maximizing first actions from the working start. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
lambda=0, V_3={'W': 0, 'B': 0}
h=2, W: Q={'operate': 8.0, 'maintain': 5.0}, V=8.00, best=['operate']
h=2, B: Q={'repair': -2.0, 'replace': -6.0}, V=-2.00, best=['repair']
h=1, W: Q={'operate': 12.0, 'maintain': 12.0}, V=12.00, best=['operate', 'maintain']
h=1, B: Q={'repair': 3.0, 'replace': 2.0}, V=3.00, best=['repair']
h=0, W: Q={'operate': 16.4, 'maintain': 16.1}, V=16.40, best=['operate']
h=0, B: Q={'repair': 7.3, 'replace': 6.0}, V=7.30, best=['repair']
First action from W: ['operate']
lambda=10, V_3={'W': 10, 'B': 0}
h=2, W: Q={'operate': 14.0, 'maintain': 14.0}, V=14.00, best=['operate', 'maintain']
h=2, B: Q={'repair': 5.0, 'replace': 4.0}, V=5.00, best=['repair']
h=1, W: Q={'operate': 18.4, 'maintain': 18.1}, V=18.40, best=['operate']
h=1, B: Q={'repair': 9.3, 'replace': 8.0}, V=9.30, best=['repair']
h=0, W: Q={'operate': 22.76, 'maintain': 22.49}, V=22.76, best=['operate']
h=0, B: Q={'repair': 13.67, 'replace': 12.4}, V=13.67, best=['repair']
First action from W: ['operate']
lambda=30, V_3={'W': 30, 'B': 0}
h=2, W: Q={'operate': 26.0, 'maintain': 32.0}, V=32.00, best=['maintain']
h=2, B: Q={'repair': 19.0, 'replace': 24.0}, V=24.00, best=['replace']
h=1, W: Q={'operate': 36.8, 'maintain': 36.2}, V=36.80, best=['operate']
h=1, B: Q={'repair': 27.6, 'replace': 26.0}, V=27.60, best=['repair']
h=0, W: Q={'operate': 41.12, 'maintain': 40.88}, V=41.12, best=['operate']
h=0, B: Q={'repair': 32.04, 'replace': 30.8}, V=32.04, best=['repair']
First action from W: ['operate']
```

The output agrees with every action candidate, selected value, and tie in the three hand tables. Decimal conversions are only for output; boundaries and comparisons use exact fractions.

<a id="8d"></a>

### 8(d) How a terminal value affects earlier decisions

> Explain why changing only the terminal value can change decisions several stages earlier.

#### 1. Read the question carefully.

Explain why a change only at stage 3 can propagate through several earlier stages. Do not claim that the first action changed in the three numerical cases: 8(c) shows it did not.

#### 2. Explain every concept and symbol.

A boundary condition is the final value supplied to the backward recursion. Each earlier action comparison includes next-stage values, which themselves include later decisions and the boundary. For a fixed policy, the coefficient of salvage is its probability of ending with a working machine. Maximizing over policies can therefore change which tradeoff is preferred.

#### 3. Solve it by hand.

For a fixed policy $\rho$ from stage $h$,

$$V_h^\rho(s;\lambda)=\mathbb E^\rho\!\left[\sum_{j=h}^{2}r_j\mid s_h=s\right]+\lambda\,P^\rho(s_3=W\mid s_h=s).$$

The first term is expected operating reward and cost; the second pays salvage only on terminal working paths. Policies can have different first terms and different terminal working probabilities. As $\lambda$ grows, a policy sacrificing immediate reward for more terminal working probability can overtake another.

Backward induction carries that preference first into $V_2^*$, then into day-1 action candidates through their weighted successor values, then into day-0 candidates. In the computed examples, day-1 $W$ changes from a tie at $\lambda=0$ to uniquely operate at $\lambda=10$ and 30, while day-0 $W$ remains operate. At salvage 30, day-2 maintain and replace increase continuation values enough to affect all earlier value numbers. Propagation can change earlier decisions; a change at every earlier stage is not required.

#### 4. Translate the reasoning into simple code.

This is a conceptual argument or proof; executing an example cannot establish the general result. No separate implementation is needed; the numerical examples elsewhere use this result.

#### 5. Explain every line.

This section contains no executable code. The mathematical steps in section 3 are the walkthrough to check.

#### 6. Compare the output with our hand solution.

No additional implementation is needed. The executed three-salvage tables demonstrate changed last-day actions, changed day-1 maximizing sets, and changed day-0 values while retaining the same first action for these requested samples.

<a id="problem-9"></a>

## Problem 9: Risk at a tie

**Source setup (verbatim, with TeX recovered from the HTML):**

In problem 3, the two actions at $W$ for $h=1$ have the same expected value $12$. Consider the total reward $G_1 = r_1 + r_2$ from $h=1$ on, where each action at $h=1$ is followed by the optimal action at $h=2$ (operate at $W$, repair at $B$).

<a id="9a"></a>

### 9(a) Equal means and different risks

> For each of the two actions, compute the distribution of $G_1$, its mean, and its variance. Which action does a manager choose who maximizes $\mathbb{E}[G_1] - \beta\,\mathrm{Var}[G_1]$ with $\beta>0$?

#### 1. Read the question carefully.

At $W$ on day 1, compare operate and maintain followed by the specified optimal last-day actions: operate in $W$, repair in $B$. Compute each two-day return distribution, mean, and variance, then apply the stated mean–variance preference with $\beta>0$.

#### 2. Explain every concept and symbol.

$G_1=r_1+r_2$ is the remaining two-day return. A distribution gives possible return values and their probabilities. Its mean is $\mu=\mathbb E[G_1]=\sum_g p_g g$. Its variance is $\mathrm{Var}(G_1)=\sum_g p_g(g-\mu)^2$, a probability-weighted squared deviation from the mean. Variance measures dispersion in squared reward units. $\beta$ is a positive coefficient converting variance into a penalty. This criterion differs from maximizing mean reward alone.

#### 3. Solve it by hand.

The final optimal reward is 8 if $s_2=W$ and -2 if $s_2=B$. The endpoint $s_3$ gives no reward, so it can be marginalized.

| First action at $W$ | $s_2$ | Probability | Total $G_1$ |
| --- | --- | --- | --- |
| operate | $W$ | 0.6 | $8+8=16$ |
| operate | $B$ | 0.4 | $8-2=6$ |
| maintain | $W$ | 0.9 | $5+8=13$ |
| maintain | $B$ | 0.1 | $5-2=3$ |

For operate,

$$\mathbb E[G_1]=0.6(16)+0.4(6)=9.6+2.4=12,$$

$$\mathrm{Var}(G_1)=0.6(16-12)^2+0.4(6-12)^2=0.6(4^2)+0.4((-6)^2)=0.6(16)+0.4(36)=9.6+14.4=24.$$

For maintain,

$$\mathbb E[G_1]=0.9(13)+0.1(3)=11.7+0.3=12,$$

$$\mathrm{Var}(G_1)=0.9(13-12)^2+0.1(3-12)^2=0.9(1^2)+0.1((-9)^2)=0.9+8.1=9.$$

The mean–variance scores are $12-24\beta$ for operate and $12-9\beta$ for maintain. Maintaining exceeds operating by $15\beta>0$, so the manager uniquely chooses maintain among these two actions for every positive $\beta$. At $\beta=0$ they tie, recovering the original expected-reward comparison. This answer uses the continuation specified by the question; it does not assume that continuation is optimal for every risk-sensitive objective.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem09.py](examples/problem09.py) (run the whole file; earlier excerpts supply its inputs):

```python
from common import Fraction, machine

last_reward = {"W": Fraction(8), "B": Fraction(-2)}
for action in machine["W"]:
    reward, transitions = machine["W"][action]
    distribution = {}
    for successor, probability in transitions.items():
        total_reward = reward + last_reward[successor]
        distribution[total_reward] = probability
    mean = sum(total * probability for total, probability in distribution.items())
    variance = sum(probability * (total - mean) ** 2 for total, probability in distribution.items())
    print(f"{action}: distribution={ {int(g): float(p) for g, p in distribution.items()} }, mean={mean}, variance={variance}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `from common import Fraction, machine` | Import exact arithmetic and the original machine model. |
| 2. `last_reward = {"W": Fraction(8), "B": Fraction(-2)}` | Store the reward under the specified last-day optimal action in each next state: 8 for working, -2 for broken. |
| 3. `for action in machine["W"]:` | Visit both admissible first actions at `W`. |
| 4. `reward, transitions = machine["W"][action]` | Unpack the first reward and successor probability dictionary for this action. |
| 5. `distribution = {}` | Initialize a dictionary mapping possible total rewards to their probabilities. |
| 6. `for successor, probability in transitions.items():` | Visit each possible next state and its probability. |
| 7. `total_reward = reward + last_reward[successor]` | Add the first reward to the next state's specified last reward. |
| 8. `distribution[total_reward] = probability` | Store the probability under that total reward. In this exercise the two totals for each action are distinct; if totals coincided, their probabilities would need to be added. |
| 9. `mean = sum(total * probability for total, probability in distribution.items())` | `sum` adds the generator's products `total * probability` for all distribution entries, computing the exact mean. |
| 10. `variance = sum(probability * (total - mean) ** 2 for total, probability in distribution.items())` | Sum probability times squared deviation from that mean, computing exact variance. `** 2` squares even a negative deviation. |
| 11. `print(f"{action}: distribution={ {int(g): float(p) for g, p in distribution.items()} }, mean={mean}, variance={variance}")` | Print a display dictionary with integer totals and float probabilities, followed by exact mean and variance. The dictionary comprehension transforms presentation only. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
operate: distribution={16: 0.6, 6: 0.4}, mean=12, variance=24
maintain: distribution={13: 0.9, 3: 0.1}, mean=12, variance=9
```

Run `python3 examples/problem09.py`. Both distributions, means 12, and variances 24 and 9 match the hand calculations. Exact fractions preserve the mean tie.

<a id="9b"></a>

### 9(b) Variance across successor states

> Use the law of total variance, $\mathrm{Var}[X]=\mathbb{E}\big[\mathrm{Var}[X\mid Y]\big]+\mathrm{Var}\big[\mathbb{E}[X\mid Y]\big]$, to write $\mathrm{Var}[G_h \mid s_h=s, a_h=a]$ in terms of the next state $s_{h+1}$. Explain why the mean–variance criterion does not satisfy a recursion of the form “reward now plus a value of the successor state”.

#### 1. Read the question carefully.

Apply the law of total variance conditional on the present state and chosen action. Explain why the ordinary scalar recursion “reward plus expected successor value” cannot directly optimize the mean–variance criterion. We use the original deterministic machine rewards.

#### 2. Explain every concept and symbol.

For a fixed Markov continuation policy, let $\mu_{h+1}(s')=\mathbb E[G_{h+1}\mid s_{h+1}=s']$ and $\sigma_{h+1}^2(s')=\mathrm{Var}(G_{h+1}\mid s_{h+1}=s')$. The first describes a successor mean and the second its within-state uncertainty. Let $p_{s'}=P(s'\mid s,a)$ and $\bar\mu=\sum_{s'}p_{s'}\mu_{h+1}(s')$. Total variance separates within-successor variance from variation between successor means. A deterministic current reward shifts the mean but leaves variance unchanged.

#### 3. Solve it by hand.

Because $G_h=r(s,a)+G_{h+1}$, conditioning further on successor $s'$ gives conditional mean $r(s,a)+\mu_{h+1}(s')$ and conditional variance $\sigma_{h+1}^2(s')$. The common deterministic reward cancels in deviations from the overall conditional mean $r(s,a)+\bar\mu$. Applying the stated law yields

$$\boxed{\mathrm{Var}(G_h\mid s_h=s,a_h=a)=\sum_{s'}p_{s'}\sigma_{h+1}^2(s')+\sum_{s'}p_{s'}\big(\mu_{h+1}(s')-\bar\mu\big)^2.}$$

The first sum is expected conditional variance. The second is the variance of conditional means. For day 1 here, conditioned on $s_2$, the remaining reward is the fixed number 8 or -2, so both within-state variances are zero.

For operate, the continuation mean is $\bar\mu=0.6(8)+0.4(-2)=4.8-0.8=4$. Between-state variance is $0.6(8-4)^2+0.4(-2-4)^2=9.6+14.4=24$; adding within-state variance 0 gives 24.

For maintain, $\bar\mu=0.9(8)+0.1(-2)=7.2-0.2=7$. Between-state variance is $0.9(8-7)^2+0.1(-2-7)^2=0.9+8.1=9$; adding 0 gives 9. Adding each first reward to the conditional means gives the same deviations as in 9(a).

Suppose one tried to use scalar successor scores $M_{h+1}(s')=\mu_{h+1}(s')-\beta\sigma_{h+1}^2(s')$. The usual additive expression gives

$$r(s,a)+\sum_{s'}p_{s'}M_{h+1}(s')=r(s,a)+\bar\mu-\beta\sum_{s'}p_{s'}\sigma_{h+1}^2(s').$$

The actual mean–variance score also subtracts

$$\beta\sum_{s'}p_{s'}(\mu_{h+1}(s')-\bar\mu)^2.$$

This missing term depends on the entire collection of successor means and their probabilities, not on one successor's scalar score in isolation. In this example all successor variances vanish, so the naive recursion would score both actions 12 and miss their different risks entirely.

For a fixed policy, means and second moments can still be propagated backward; the issue is the ordinary scalar additive optimality recursion. Optimizing a full-horizon mean–variance preference requires retaining additional information or constraints, and later local preferences need not coincide with a commitment made earlier. The result does not forbid every dynamic-programming formulation for risk-sensitive control. The displayed formula assumes deterministic current reward; with random rewards, their conditional variance and covariance with the continuation would also need consideration.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem09.py](examples/problem09.py) (run the whole file; earlier excerpts supply its inputs):

```python
for action in machine["W"]:
    reward, transitions = machine["W"][action]
    mean = sum(probability * (reward + last_reward[successor]) for successor, probability in transitions.items())
    within_variance = Fraction(0)
    between_variance = Fraction(0)
    for successor, probability in transitions.items():
        conditional_mean = reward + last_reward[successor]
        within_variance += probability * 0
        between_variance += probability * (conditional_mean - mean) ** 2
    print(f"Total variance: within={within_variance}, between={between_variance}, sum={within_variance + between_variance}")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `for action in machine["W"]:` | Visit operate and maintain at the working state again to verify the variance decomposition. |
| 2. `reward, transitions = machine["W"][action]` | Unpack the deterministic first reward and successor probabilities. |
| 3. `mean = sum(probability * (reward + last_reward[successor]) for successor, probability in transitions.items())` | Compute the overall total-return mean by summing probability times `(reward + last_reward[successor])`. |
| 4. `within_variance = Fraction(0)` | Initialize the expected within-state variance to exact zero. |
| 5. `between_variance = Fraction(0)` | Initialize the between-state variance to exact zero. |
| 6. `for successor, probability in transitions.items():` | Visit each successor and its probability. |
| 7. `conditional_mean = reward + last_reward[successor]` | Compute this successor's conditional total-return mean; its last reward is deterministic. |
| 8. `within_variance += probability * 0` | Add probability times zero within-state variance. This explicit zero displays why the first term vanishes here. |
| 9. `between_variance += probability * (conditional_mean - mean) ** 2` | Add probability times squared difference between this conditional mean and the overall mean. |
| 10. `print(f"Total variance: within={within_variance}, between={between_variance}, sum={within_variance + between_variance}")` | Print the two terms and their sum, which must match the variance computed directly in 9(a). |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Total variance: within=0, between=24, sum=24
Total variance: within=0, between=9, sum=9
```

The decomposition gives within 0, between 24 for operate and within 0, between 9 for maintain. These sums equal the direct distribution variances, checking the conditional calculation independently.

<a id="9c"></a>

### 9(c) Expected utility on an augmented state

> Let $c_h$ denote the reward accumulated before stage $h$. Show that for any function $u$, the criterion $\mathbb{E}[u(G_0)]$ satisfies a backward recursion on the augmented state $(s_h, c_h)$, and state its terminal condition. Explain why $\mathbb{E}[G_0] - \beta\,\mathrm{Var}[G_0]$ is not of this form.

#### 1. Read the question carefully.

Let accumulated reward before stage $h$ be part of the state and derive a backward recursion for expected utility of the full return. Specify the terminal condition, then explain why mean minus variance cannot be represented by one fixed utility function of an individual return.

#### 2. Explain every concept and symbol.

Define $c_h=\sum_{j=0}^{h-1}r_j$, with $c_0=0$. Here $c_h$ is accumulated reward, unrelated to the wear flag or offer threshold in earlier problems. After earning deterministic reward $r(s,a)$, it becomes $c_{h+1}=c_h+r(s,a)$. A utility function $u(g)$ assigns a score to a realized total $g$. Assuming the relevant expectations exist, maximizing $\mathbb E[u(G_0)]$ can use an augmented-state value $J_h^*(s,c)$. The symbol $J$ here denotes utility value, whereas 1(e) used it for minimum cost.

#### 3. Solve it by hand.

At the horizon, no rewards remain and the accumulated total equals $G_0$, so

$$J_H^*(s,c)=u(c).$$

At an earlier stage, taking action $a$ earns $r(s,a)$, moves to $s'$ with probability $P(s'\mid s,a)$, and changes the accumulation to $c+r(s,a)$. Conditional expectation and optimization then give

$$\boxed{J_h^*(s,c)=\max_{a\in\mathcal A(s)}\sum_{s'}P(s'\mid s,a)J_{h+1}^*(s',c+r(s,a)).}$$

There is no extra immediate utility term: $u$ is applied once to the total at the boundary. Adding $u(r)$ at every stage would define a different criterion. For evaluating a specified randomized Markov policy on the augmented state, replace the maximum by its action-probability-weighted sum. The update of $c$ is deterministic for the original lab rewards. If rewards were random, average over their joint outcomes with $s'$ as well.

Why this works: the pair $(s,c)$ records the environment information and all previously earned reward needed by terminal utility. The last-stage continuation is $u(c+r(s,a))$. At the preceding stage, conditioning on the next augmented state gives the recursion above. Backward induction repeats that step to $J_0^*(W,0)$.

For the concrete check $u(g)=g$, accumulated reward contributes just a constant to the ordinary expected-reward problem. At the boundary $J_3^*(s,c)=c=c+V_3^*(s)$. If $J_{h+1}^*(s',c')=c'+V_{h+1}^*(s')$, substitution gives

$$J_h^*(s,c)=\max_a\sum_{s'}P(s'\mid s,a)[c+r(s,a)+V_{h+1}^*(s')]=c+V_h^*(s),$$

because successor probabilities sum to 1. Thus $J_0^*(W,0)=0+16.4=16.4$.

Mean–variance can be expanded as

$$\mathbb E[G_0]-\beta\,\mathrm{Var}(G_0)=\mathbb E[G_0]-\beta\mathbb E[G_0^2]+\beta(\mathbb E[G_0])^2.$$

The first two terms are an expectation of $g-\beta g^2$. The last term squares an expectation, so its value depends on the whole return distribution. It cannot be absorbed into one fixed function $u(g)$ independent of the chosen policy's distribution.

To prove that distinction, take returns always 0 and always 1. Matching their zero-variance scores would require $u(0)=0$ and $u(1)=1$. Now mix them so return 1 has probability $p\in(0,1)$. Expected utility is $(1-p)u(0)+pu(1)=p$. Mean–variance is $p-\beta p(1-p)$, strictly below $p$ when $\beta>0$. One fixed $u$ therefore cannot reproduce the criterion on all these distributions. This is a failure of the fixed expected-utility representation, not a claim that every risk objective or augmented recursion is impossible.

#### 4. Translate the reasoning into simple code.

Excerpt from [examples/problem09.py](examples/problem09.py) (run the whole file; earlier excerpts supply its inputs):

```python
def expected_utility(stage, state, accumulated, utility):
    if stage == 3:
        return utility(accumulated)
    candidates = []
    for action in machine[state]:
        reward, transitions = machine[state][action]
        candidate = Fraction(0)
        for successor, probability in transitions.items():
            if probability > 0:
                candidate += probability * expected_utility(stage + 1, successor, accumulated + reward, utility)
        candidates.append(candidate)
    return max(candidates)

def identity_utility(total):
    return total

utility_value = expected_utility(0, "W", Fraction(0), identity_utility)
print(f"Expected utility with u(g)=g: {utility_value} ({float(utility_value):.2f})")
```

#### 5. Explain every line.

| Line | Python and mathematical meaning |
| --- | --- |
| 1. `def expected_utility(stage, state, accumulated, utility):` | Define the recursive function `expected_utility(stage, state, accumulated, utility)`. Its arguments represent the augmented decision state and the chosen callable $u$. |
| 2. `if stage == 3:` | Test whether the stage equals the three-day horizon. |
| 3. `return utility(accumulated)` | At the boundary, call the utility function on the accumulated total and return it; no action or additional reward is taken. |
| 4. `candidates = []` | Create a list of action candidates for a nonterminal stage. |
| 5. `for action in machine[state]:` | Visit the actions admissible in this machine state. |
| 6. `reward, transitions = machine[state][action]` | Unpack the action's immediate reward and transition dictionary. |
| 7. `candidate = Fraction(0)` | Initialize its expected utility candidate to exact zero. |
| 8. `for successor, probability in transitions.items():` | Visit successor/probability pairs. |
| 9. `if probability > 0:` | Skip impossible successors, whose probability is zero. |
| 10. `candidate += probability * expected_utility(stage + 1, successor, accumulated + reward, utility)` | Recursively solve the next augmented state, incrementing stage and adding this reward to accumulation. Multiply that returned utility value by the successor probability and add it to the candidate. |
| 11. `candidates.append(candidate)` | Append the complete expectation for this action after its successor loop finishes. |
| 12. `return max(candidates)` | Return the largest candidate utility. This optimizes over actions while averaging successor outcomes. |
| 13. `def identity_utility(total):` | Define `identity_utility(total)`, a concrete utility function to check ordinary expected reward. |
| 14. `return total` | Return the supplied total unchanged; this implements $u(g)=g$. |
| 15. `utility_value = expected_utility(0, "W", Fraction(0), identity_utility)` | Call the recursion from day 0, working state, accumulated reward 0, and the identity utility function. Passing a function without parentheses supplies the callable rather than invoking it now. |
| 16. `print(f"Expected utility with u(g)=g: {utility_value} ({float(utility_value):.2f})")` | Print the exact optimal expected utility fraction and its two-decimal display. |

#### 6. Compare the output with our hand solution.

Actual output:

```text
Expected utility with u(g)=g: 82/5 (16.40)
```

The exact result 82/5 is 16.4, matching the hand identity and the ordinary backward solver. For a concrete boundary call, `expected_utility(3, "W", Fraction(16), identity_utility)` returns 16. In its parent at stage 2, state `W`, accumulation 8, operating reaches such a boundary with total 16 in either successor, so its candidate is $0.6(16)+0.4(16)=16$; maintaining would give total 13. The implementation recomputes small subtrees rather than adding a cache, keeping this three-stage example easy to trace.

<a id="verification"></a>

## Verification and source audit

Verified on 7 October 2026 with Python 3.10.12. The nine chapter scripts use only the Python standard library. Each command below ran successfully, and every displayed `Actual output` excerpt was captured from those executions:

| Problem | Run from the repository directory | Verified calculations |
| --- | --- | --- |
| 1 | `python3 examples/problem01.py` | Greedy path and reward 3; all four boundary values, all backward layers, all actions, optimal path and reward 6 |
| 2 | `python3 examples/problem02.py` | Cautious values; all four trajectories with probabilities and returns; enumeration equals 9.3 |
| 3 | `python3 examples/problem03.py` | All optimal candidates and ties; first action; cautious losses; behavioral policy counts 32 and 96 |
| 4 | `python3 examples/problem04.py` | All four cautious Q-values; displayed policy changes only stage 1; separate last-day change closes stage-1 gaps |
| 5 | `python3 examples/problem05.py` | Every inventory candidate for one, two, and three remaining decisions; all maximizing ties |
| 6 | `python3 examples/problem06.py` | Exact four-stage offer values, cutoffs, and expected gain over accepting immediately |
| 7 | `python3 examples/problem07.py` | Augmented model candidates and policies; optimal start value 16.4; fixed-policy value 14.6 and loss 1.8 |
| 8 | `python3 examples/problem08.py` | Exact switching points; every backward candidate for salvage 0, 10, and 30 |
| 9 | `python3 examples/problem09.py` | Both return distributions; means and variances; total-variance decomposition; identity-utility recursion equals 16.4 |

`examples/common.py` supplies the exact machine model and the two fully explained helpers; it is imported by the chapter scripts and intentionally prints nothing on its own. The README's Python excerpts match their runnable source verbatim. Every noncomment code line in all ten Python files is included in an explained excerpt. Proof and conceptual subquestions retain sections 4–6 and explicitly state why code or output is not applicable.

The source audit reread the original HTML main document, recovering TeX exclusively from KaTeX `application/x-tex` annotations and skipping duplicate visual/MathML representations, scripts, and styles. It found two numerical tables and nine problems with subquestion counts **5, 4, 5, 4, 4, 4, 4, 4, 3**, totaling **37**. Both source tables, every problem setup, and every subquestion are reproduced above; source bullets are assigned letters without reordering. The coverage checklist has 37 checked items, and the walkthrough has 37 subquestion headings and 222 required teaching-section headings. Independent exhaustive trajectory calculations checked the numerical recursion values and optimal actions, including ties and the wear and salvage variants.

The source HTML is byte-for-byte identical to the committed original. Its SHA-256 is:

```text
a612b51a7f6924c392f1f1abd7a03faeb50945aecdb590786992634ea5150979
```

The only interpretive convention requiring care is **3(e)**: we count behaviorally distinct policies from the specified working start, ignoring decisions at unreachable histories. This yields 32 Markov policies and 96 history-dependent policies. Counting complete policy tables or including impossible histories gives larger numbers for reasons explained there. For **5**, the unspecified terminal reward is taken as zero; no absorbing terminal state or inventory salvage is added. For **6**, the final cutoff zero denotes mandatory acceptance, including an offer of zero. For **7**, the irrelevant broken-state wear flag is merged, and the displayed hypothetical day-0 `W1` row does not affect the required flag-zero start. No substantive numerical discrepancies or unresolved source questions remain under these stated conventions.

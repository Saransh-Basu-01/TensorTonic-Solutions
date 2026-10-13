## Markov Decision Processes (MDPs)

Before understanding value iteration, you need to understand the problem it solves: finding the best strategy in a **Markov Decision Process**.

An MDP is a mathematical framework for modeling decision-making in situations where outcomes are partly random and partly under the control of a decision-maker. It consists of five components:

- **States** $S$: A finite set of situations the agent can be in. For example, positions on a grid, levels in a game, or configurations of a robot.
- **Actions** $A$: A finite set of choices available to the agent. For example, move left, move right, stay put.
- **Transition function** $T(s, a, s')$: The probability of ending up in state $s'$ if you take action $a$ in state $s$. This captures the uncertainty in the environment. For every state-action pair, the probabilities over all next states sum to 1:

$$
\sum_{s'} T(s, a, s') = 1 \quad \text{for all } s, a
$$

- **Reward function** $R(s, a)$: The immediate reward received when taking action $a$ in state $s$. This is the signal that tells the agent which actions are good or bad in the short term.
- **Discount factor** $\gamma \in [0, 1]$: A number that controls how much the agent cares about future rewards versus immediate rewards.

The **Markov property** is the key assumption: the next state depends only on the current state and action, not on any history of how you got there. This is what makes the math tractable.

---

## What Is a Value Function?

A **value function** $V(s)$ assigns a number to each state representing how good it is to be in that state. Specifically, it is the total expected discounted reward the agent will accumulate starting from state $s$ and acting optimally from that point on.

The idea of "discounted reward" is central. If the agent receives rewards $r_0, r_1, r_2, \ldots$ at successive time steps, the discounted return is:

$$
G = r_0 + \gamma \, r_1 + \gamma^2 \, r_2 + \gamma^3 \, r_3 + \cdots = \sum_{t=0}^{\infty} \gamma^t \, r_t
$$

The discount factor $\gamma$ makes future rewards worth less than immediate ones. A reward of 1 received 10 steps from now is only worth $\gamma^{10}$ today.

- When $\gamma = 0$, the agent is completely myopic and only cares about the immediate reward.
- When $\gamma$ is close to 1, the agent is far-sighted and values future rewards almost as much as present ones.
- When $\gamma = 1$, there is no discounting at all, but convergence is no longer guaranteed in general.

The **optimal value function** $V^*(s)$ is the maximum possible expected return starting from each state. Once you know $V^*$, you effectively know the best possible outcome from any situation.

---

## The Bellman Equation

The Bellman equation is the recursive relationship that the optimal value function must satisfy. It expresses a simple but powerful idea: the value of a state equals the best immediate reward you can get, plus the discounted value of wherever you end up.

Formally:

$$
V^*(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} T(s, a, s') \cdot V^*(s') \right]
$$

Let us break this apart piece by piece:

1. The inner sum $\sum_{s'} T(s, a, s') \cdot V^*(s')$ computes the **expected future value** if you take action $a$ from state $s$. You look at every possible next state $s'$, weight it by how likely you are to reach it ($T(s, a, s')$), and multiply by its value ($V^*(s')$). This is just a weighted average.

2. $R(s, a) + \gamma \cdot (\text{expected future value})$ gives the total value of taking action $a$. The immediate reward $R(s, a)$ is what you get right now, and the discounted expected future value is what you expect to accumulate afterward. This quantity is called the **Q-value** or **action-value**:

$$
Q(s, a) = R(s, a) + \gamma \sum_{s'} T(s, a, s') \cdot V^*(s')
$$

3. The $\max_a$ takes the best action. Since we want the *optimal* value, we pick whichever action gives the highest total.

The Bellman equation is not something you solve in one shot. It is a system of equations (one per state) where the unknowns ($V^*$ values) appear on both sides. This is where value iteration comes in.

---

## Value Iteration

Value iteration is an iterative algorithm that finds $V^*$ by repeatedly applying the Bellman equation as an **update rule**.

You start with an initial guess for the value function, often all zeros: $V_0(s) = 0$ for all states. Then at each iteration $k$, you compute a new estimate by applying the Bellman backup to every state:

$$
V_{k+1}(s) = \max_a \left[ R(s, a) + \gamma \sum_{s'} T(s, a, s') \cdot V_k(s') \right]
$$

The only difference from the Bellman equation is that we use $V_k$ (the current estimates) on the right side instead of $V^*$ (which we do not know yet). Each iteration brings the estimates closer to the true optimal values.

**Why does this work?** The Bellman backup is a **contraction mapping**. This is a result from fixed-point theory that says: if you keep applying a function that brings points closer together, you will eventually converge to a unique fixed point. The contraction factor is exactly $\gamma$. After $k$ iterations, the maximum error across all states is at most $\gamma^k$ times the initial error. So the values converge exponentially fast, and smaller $\gamma$ means faster convergence.

**When to stop**: In practice, you stop when the values barely change between iterations. The standard criterion is:

$$
\max_s |V_{k+1}(s) - V_k(s)| < \epsilon
$$

for some small threshold $\epsilon$. This problem asks you to implement just a single step of this iteration.

---

## The Q-Value: A Closer Look

The Q-value $Q(s, a)$ is a central quantity worth understanding on its own. While $V(s)$ tells you "how good is this state?", $Q(s, a)$ tells you "how good is taking this specific action in this state?"

$$
Q(s, a) = R(s, a) + \gamma \sum_{s'} T(s, a, s') \cdot V(s')
$$

The relationship between $V$ and $Q$ is straightforward:

$$
V^*(s) = \max_a Q^*(s, a)
$$

The optimal value of a state is simply the Q-value of the best action. Computing Q-values is the core work of each value iteration step. You evaluate the Q-value for every state-action pair, then take the maximum over actions for each state.

---

## Stochastic vs. Deterministic Transitions

The transition function $T(s, a, s')$ captures randomness in the environment.

In a **deterministic** environment, taking action $a$ in state $s$ always leads to the same next state $s'$. In this case, the transition probabilities are all 0 or 1. The expected future value simplifies to just $V(s')$ for the one guaranteed next state. The Bellman backup becomes:

$$
V'(s) = \max_a \left[ R(s, a) + \gamma \cdot V(\text{next}(s, a)) \right]
$$

In a **stochastic** environment, the same action can lead to different states with different probabilities. For example, a robot trying to move forward might succeed with probability 0.8, slip left with probability 0.1, or slip right with probability 0.1. The expected future value is then a weighted sum over all possible outcomes.

This distinction matters because stochastic transitions force the agent to think about risk. An action that usually gives a great outcome but sometimes leads to disaster might have a lower Q-value than a safer, less rewarding action.

---

## Extracting the Optimal Policy

Value iteration computes the optimal *values*, but what we ultimately want is a *policy*: a rule that tells the agent which action to take in each state.

Once $V^*$ is known, the optimal policy $\pi^*$ is:

$$
\pi^*(s) = \arg\max_a \left[ R(s, a) + \gamma \sum_{s'} T(s, a, s') \cdot V^*(s') \right]
$$

In other words, in each state, pick the action that achieves the maximum in the Bellman equation. The values already encode which actions are best; you just have to read them off.

---

## A Worked Example

Consider 2 states and 2 actions, with all values initialized to 0.

$$
T = \begin{bmatrix} \begin{bmatrix} 0.8 & 0.2 \\ 0.3 & 0.7 \end{bmatrix}, \begin{bmatrix} 0.5 & 0.5 \\ 0.1 & 0.9 \end{bmatrix} \end{bmatrix}, \quad R = \begin{bmatrix} 1 & 2 \\ -1 & 0 \end{bmatrix}, \quad \gamma = 0.9
$$

**State 0:**

$Q(0, a_0) = R(0, 0) + \gamma \cdot [T(0,0,0) \cdot V(0) + T(0,0,1) \cdot V(1)]$
$= 1 + 0.9 \cdot [0.8 \cdot 0 + 0.2 \cdot 0] = 1$

$Q(0, a_1) = R(0, 1) + \gamma \cdot [T(0,1,0) \cdot V(0) + T(0,1,1) \cdot V(1)]$
$= 2 + 0.9 \cdot [0.3 \cdot 0 + 0.7 \cdot 0] = 2$

$V'(0) = \max(1, 2) = 2$

**State 1:**

$Q(1, a_0) = -1 + 0.9 \cdot [0.5 \cdot 0 + 0.5 \cdot 0] = -1$

$Q(1, a_1) = 0 + 0.9 \cdot [0.1 \cdot 0 + 0.9 \cdot 0] = 0$

$V'(1) = \max(-1, 0) = 0$

After one iteration: $V = [2.0, 0.0]$.

Now if we run a second iteration using these new values, the future-value terms are no longer zero, and the estimates become more refined. Repeating this process until convergence gives $V^*$.

---

## Where Value Iteration Shows Up

**Reinforcement Learning**: Value iteration is a foundational algorithm. Modern deep RL methods like DQN (Deep Q-Networks) are essentially neural-network approximations of the same Bellman backup idea, scaled to environments with huge or continuous state spaces.

**Planning and Control**: Autonomous systems (self-driving cars, warehouse robots) use MDP-based planners to decide actions under uncertainty. Value iteration or its variants compute the optimal decision at each state.

**Operations Research**: Inventory management, resource allocation, and maintenance scheduling are all modeled as MDPs. Value iteration finds cost-minimizing or profit-maximizing strategies.

**Game AI**: Board games and video game bots use value-iteration-style reasoning to evaluate board positions and choose moves.
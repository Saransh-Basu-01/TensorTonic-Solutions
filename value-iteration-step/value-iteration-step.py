def value_iteration_step(values, transitions, rewards, gamma):
    new_values = []
    for s in range(len(values)):
        best_value = float('-inf')
        for a in range(len(transitions[s])):
            action_value = rewards[s][a]
            for s_prime in range(len(values)):
                action_value += gamma * transitions[s][a][s_prime] * values[s_prime]
            if action_value > best_value:
                best_value = action_value
        new_values.append(best_value)  
    return new_values
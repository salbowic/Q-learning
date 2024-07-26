import matplotlib.pyplot as plt

def draw_three_plots(rewards_1, rewards_2, rewards_3, beta, gamma, epsilon):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

    plt.subplots_adjust(hspace=0.45)

    # First subplot
    ax1.spines['left'].set_position('center')
    ax1.spines['bottom'].set_position('zero')
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.yaxis.set_ticks_position('left')
    ax1.plot(rewards_1, 'r')
    ax1.set_title('Domyślny system nagród', fontsize=10)
    ax1.text(1.05, 0.5, f'\u03B2: {beta}\n\u03B3: {gamma}\n\u03B5: {epsilon}', ha='center', va='center',
             transform=ax1.transAxes)
    ax1.grid()
    ax1.set_xlabel('Nr epizodu', fontsize=7)

    # Second subplot
    ax2.spines['left'].set_position('center')
    ax2.spines['bottom'].set_position('zero')
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.xaxis.set_ticks_position('bottom')
    ax2.yaxis.set_ticks_position('left')
    ax2.plot(rewards_2, 'b')
    ax2.set_title('"Unikaj dziur"', fontsize=10)
    ax2.text(1.05, 0.5, f'\u03B2: {beta}\n\u03B3: {gamma}\n\u03B5: {epsilon}', ha='center', va='center',
             transform=ax2.transAxes)
    ax2.grid()
    ax2.set_xlabel('Nr epizodu', fontsize=7)

    # Third subplot
    ax3.spines['left'].set_position('center')
    ax3.spines['bottom'].set_position('zero')
    ax3.spines['right'].set_color('none')
    ax3.spines['top'].set_color('none')
    ax3.xaxis.set_ticks_position('bottom')
    ax3.yaxis.set_ticks_position('left')
    ax3.plot(rewards_3, 'g')
    ax3.set_title('"Bliżej-lepiej"', fontsize=10)
    ax3.text(1.05, 0.5, f'\u03B2: {beta}\n\u03B3: {gamma}\n\u03B5: {epsilon}', ha='center', va='center',
             transform=ax3.transAxes)
    ax3.grid()
    ax3.set_xlabel('Nr epizodu', fontsize=7)

    fig.suptitle('Uśrednione dojścia do celu dla 25 uruchomień', fontsize=10)
    
    plt.show()

def draw_two_plots(rewards_1, rewards_2, beta1, gamma1, epsilon1, beta2, gamma2, epsilon2):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.plot(rewards_1, 'r', label=f'\u03B2: {beta1}\n\u03B3: {gamma1}\n\u03B5: {epsilon1}')
    ax.plot(rewards_2, 'b', label=f'\u03B2: {beta2}\n\u03B3: {gamma2}\n\u03B5: {epsilon2}')
    ax.legend()

    plt.title('Domyślny system nagród (uśrednione dojścia do celu dla 25 uruchomień)', fontsize=10)
    plt.xlabel('Nr epizodu')
    plt.grid()
    plt.show()


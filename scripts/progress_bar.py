import time


total_iterations = 100


def update_the_progress_bar(iteration):
    progress = iteration / total_iterations
    progress_bar_length = 50
    filled_length = int(progress * progress_bar_length)
    remaining_length = progress_bar_length - filled_length
    progress_bar = '█' * filled_length + '-' * remaining_length + '\r'
    percentage = int(progress * 100)
    print(f'{progress_bar} {percentage}%', end='\r')


for iteration in range(total_iterations):
    time.sleep(.05)
    update_the_progress_bar(iteration + 1)
    # print('█', sep='\r', end='')

print()
print('COMPLETED!')
print()

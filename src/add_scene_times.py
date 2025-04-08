
times = {
    2: '00:48',
    3: '00:48',
    4: '00:53',
    5: '01:28',
    6: '01:06',
    7: '00:35',
    8: '02:19',
    9: '00:00',
    10: '01:01',
    11: '03:06',
    12: '01:02',
    13: '01:37',
    14: '02:45',
    15: '01:42',
    16: '01:35',
    17: '00:35',
    18: '04:45',
    
}

from datetime import datetime

# Add up all these minute:seconds
def add_times(times):
    total_seconds = 0
    for time_str in times.values():
        minutes, seconds = map(int, time_str.split(':'))
        total_seconds += minutes * 60 + seconds
    return total_seconds

if __name__ == '__main__':
    total_seconds = add_times(times)
    total_time = datetime.utcfromtimestamp(total_seconds).strftime('%H:%M:%S')
    print(f'Total time: {total_time}')
    print(f'Total seconds: {total_seconds}')
    print(f'Total minutes: {total_seconds / 60}')
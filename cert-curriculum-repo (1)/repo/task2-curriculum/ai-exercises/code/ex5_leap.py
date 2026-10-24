def is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
TESTS = {1900: False, 2000: True, 2023: False, 2024: True, 2100: False, 2400: True}
def run_tests(f):
    return [y for y, want in TESTS.items() if f(y) != want]

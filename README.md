# Pytest practice

1. **Installation:** Install Python and pytest. With your Python environment active, install pytest using `python -m pip install pytest`.
2. **Run the tests:** From `C:\Users\Sky\Documents\Projects`, with the environment containing pytest active, run `python -m pytest -v pytest/learning.py`.
3. **Expected success:** The current suite should report `7 passed`. Tests using `pytest.raises(ValueError)` pass when the operation raises the expected exception type; they fail if no exception or an unrelated exception occurs. Warnings can appear even when all tests pass.
4. **Sample failure:** A valid-score case with input 90 and expected result 100 fails because the validator returns 90. Pytest reports an assertion failure and normally continues to the remaining cases.
5. **Limitation:** These tests cover selected numeric scores, including boundaries and out-of-range values. They do not test nonnumeric inputs such as text or `None`, and passing these cases does not prove correctness for every possible input.

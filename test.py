import pytest
def fuzzy_math(num1, operator, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy maths on ints')

    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f"I don't know how to do math with {operator}")

    if result < 0:
        return 'A negative number, what does that even mean?'
    elif result < 10:
        return 'A small number, I can deal with that.'
    elif result < 20:
        return 'A medium-sized number. OK.'
    else:
        return 'A really big number, way too big for me.'

class TestFuzzyMath:
    def test_non_int_input_for_num1(self):
        with pytest.raises(Exception) as exc_info:
            fuzzy_math('hi', '+', 34)
        assert 'fuzzy maths on ints' in str(exc_info)
    def test_non_int_input_for_num2(self):
        '''
        error1 = None
        try:
            fuzzy_math(2, '+', 23.2)
        except Exception as e1:
            error1 = e1
        assert error1 is not None
        '''
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(3,'+', 34.2)
        assert 'fuzzy maths on ints' in str(exec_info)
    def test_addition_with_negative_result(self):
        assert fuzzy_math(-1, '+', -4) == 'A negative number, what does that even mean?'
    def test_addition_with_small_result(self):
        assert fuzzy_math(2, '+', 2) == 'A small number, I can deal with that.' #asserting that output of fuzzy math is equal to the number(on left).
    def test_addition_with_medium_result(self):
        assert fuzzy_math(12, '+', 4) == 'A medium-sized number. OK.'
    def test_addition_with_large_result(self):
        assert fuzzy_math(45, '+', 34) == 'A really big number, way too big for me.'
    def test_with_invalid_operator(self):
        '''
        error2 = None
        try:
            fuzzy_math(32, '/', 2)
        except Exception as e2:
            error2 = e2
        assert error2 is not None
        :return:
        '''
        with pytest.raises(Exception) as exec_info:
            fuzzy_math(21, '/', 24)
        assert "I don't know how to do math" in str(exec_info)
    def test_multiplication_with_negative_result(self):
        assert fuzzy_math(-3, '*', 6) == 'A negative number, what does that even mean?'
    def test_multiplication_with_small_result(self):
        assert fuzzy_math(3, '*', 1) == 'A small number, I can deal with that.'
    def test_multiplication_with_medium_result(self):
        assert fuzzy_math(4, '*', 3) == 'A medium-sized number. OK.'
    def test_multiplication_with_large_result(self):
        assert fuzzy_math(9, '*', 8) == 'A really big number, way too big for me.'



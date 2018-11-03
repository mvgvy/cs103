import random
from typing import Optional

def read_sudoku(filename: str) -> list:
    """ Прочитать Судоку из указанного файла """
    digits = [c for c in open(filename).read() if c in '123456789.']
    grid = group(digits, 9)
    return grid


def display(values: list) -> None:
    """Вывод Судоку """
    width = 2
    line = '+'.join(['-' * (width * 3)] * 3)
    for row in range(9):
        print(''.join(values[row][col].center(width) + ('|' if str(col) in '25' else '') for col in range(9)))
        if str(row) in '25':
            print(line)
    print()


def group(values: list, n: int)-> list:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i:i + n] for i in range(0, len(values), n)]


def get_row(values: list, pos: tuple) -> list:
    """ Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    a, _ = pos
    return values[a]


def get_col(values: list, pos: tuple) -> list:
    """ Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """

    _, b = pos
    return [values[a][b] for a in range(len(values))]


def get_block(values: list, pos: tuple) -> list:
    """ Возвращает все значения из квадрата, в который попадает позиция pos
        >>> grid = read_sudoku('puzzle1.txt')
        >>> get_block(grid, (0, 1))
        ['5', '3', '.', '6', '.', '.', '.', '9', '8']
        >>> get_block(grid, (4, 7))
        ['.', '.', '3', '.', '.', '1', '.', '.', '6']
        >>> get_block(grid, (8, 8))
        ['2', '8', '.', '.', '.', '5', '.', '7', '9']
        """
    b, d = pos
    a: list = []
    if b < 3:
        c = 0
    elif 3 <= b < 6:
        c = 3
    else:
        c = 6
    a += values[c] + values[c + 1] + values[c + 2]
    if d < 3:
        block = a[0:3] + a[9:12] + a[18:21]
    elif 3 <= d < 6:
        block = a[3:6] + a[12:15] + a[21:24]
    else:
        block = a[6:9] + a[15:18] + a[24:27]
    return block


def find_empty_positions(grid: list) -> Optional[tuple]:
    """ Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    global empty_poz
    for a in range(len(grid)):
        for b in range(len(grid)):
            if grid[a][b] == '.':
                return a, b
    return None


def find_possible_values(grid: list, pos: tuple)-> set:
    """ Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    a = set('123456789')
    b = a.difference(set(get_col(grid, pos)))
    c = a.difference(set(get_row(grid, pos)))
    d = a.difference(set(get_block(grid, pos)))

    return b & c & d


def solve(grid: list):
    """ Решение пазла, заданного в grid
     Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    poz = find_empty_positions(grid)
    if not poz:
        return grid
    a, b = poz
    for var in find_possible_values(grid, poz):
        grid[a][b] = var
        resh = solve(grid)
        if resh:
            return resh
    grid[a][b] = '.'
    return None


def check_solution(solution: list)-> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    for a in (1, 2, 3):
        for b in (1, 2, 3):
            var = set(get_block(solution, (a, b)))
            if var != set('123456789'):
                return False

    for a in range(len(solution)):
        var = set(get_col(solution, (1, a)))
        if var != set('123456789'):
            return False

    for b in range(len(solution)):
        var = set(get_row(solution, (b, 1)))
        if var != set('123456789'):
            return False
    return True


def generate_sudoku(n: int)->str:
    """ Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """

    generate = solve([['.', '.', '.', '.', '.', '.', '.', '.', '.'] for _ in range(9)])
    n = 81 - min(81, n)
    while n:
        a = random.randint(0, 8)
        b = random.randint(0, 8)
        if generate[a][b] != '.':
            generate[a][b] = '.'
            n -= 1
    return generate


if __name__ == '__main__':
    for fname in ['sudoku1.txt', 'sudoku2.txt', 'sudoku3.txt']:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        display(solution)

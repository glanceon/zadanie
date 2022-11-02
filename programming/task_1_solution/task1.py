class Task1:
    def Solution(self, h :int, w :int, i :int) -> list:

        if i >= h*w:
            return print("No such number exists")

        surrounding_indexes = []
        # Make h(rows) x w(cols) matrix
        matrix = [[0 for y in range(0,w)] for x in range(0,h)]
        number = 0
        i_row_index = 0
        i_col_index = 0
        for row in range(0,h):
            for col in range(0,w):
                if row == 0:
                    number = col
                else:
                    number = row * w + col
                matrix[row][col] = number

        # Find desired number
        for row_index in range(0,h):
            # Take number from row
            for column_index in range(0,w):
                # Take number
                if i == matrix[row_index][column_index]:
                    i_row_index = row_index
                    i_col_index = column_index


        # Add surrounding numbers
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                # Skip the number itself
                if x == 0 and y == 0:
                    continue
                try:
                    neighbor_number = 0
                    row_count = i_row_index + x
                    col_count = i_col_index + y
                    if row_count > h-1:
                        row_count = 0
                    elif row_count < 0:
                        row_count = h-1
                    if col_count > w-1:
                        col_count = 0
                    elif col_count < 0:
                        col_count = w-1
                    neighbor_number = row_count * w + col_count
                    surrounding_indexes.append(neighbor_number)
                except:
                    continue

        return surrounding_indexes

if __name__ == '__main__':
    P1 = Task1()
    P1.Solution(4,4,5)
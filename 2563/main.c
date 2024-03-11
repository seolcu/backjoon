#include <stdio.h>

typedef int matrix[100][100];

void print_matrix(matrix mat)
{
    for (int row = 0; row < 100; row++)
    {
        for (int col = 0; col < 100; col++)
        {
            printf("%d", mat[row][col]);
        }
        printf("\n");
    }
}

void put_paper(matrix board, int start_row, int start_col)
{
    for (int row = start_row; (row < start_row + 10) && (row < 100); row++)
    {
        for (int col = start_col; (col < start_col + 10) && (col < 100); col++)
        {
            board[row][col] = 1;
        }
    }
}

int count_ones_in_board(matrix board)
{
    int count = 0;
    for (int row = 0; row < 100; row++)
    {
        for (int col = 0; col < 100; col++)
        {
            if (board[row][col] == 1)
            {
                count += 1;
            }
        }
    }
    return count;
}

int main()
{
    int paper_quantity;
    scanf("%d", &paper_quantity);

    matrix board = {0};

    for (int i = 0; i < paper_quantity; i++)
    {
        int start_row, start_col;
        scanf("%d %d", &start_col, &start_row);
        put_paper(board, start_row, start_col);
    }

    printf("%d", count_ones_in_board(board));

    return 0;
}

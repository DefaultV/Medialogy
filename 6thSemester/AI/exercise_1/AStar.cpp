#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

const int grid_x = 20;
const int grid_y = 20;
int grid[grid_x][grid_y] = {
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 5, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 5, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 6, 6, 0, 8, 9, 9, 9, 8, 0, 0, 0, 0, 5, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 8, 9, 9, 9, 8, 0, 0, 0, 0, 5, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 8, 9, 9, 9, 8, 0, 0, 0, 3, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 0, 0, 3, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
	{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
};

int score_grid[grid_x][grid_y] = {};
int current_score = 0;

void randomize_array(){
	for(int i = 0; i < grid_y; i++){
		for(int j = 0; j < grid_x; j++){
			//grid[i][j] = rand() % 9 + 1;
			score_grid[i][j] = 0;
		}
	}
}

void printgrid(int g[][20], int disp_score){
	for (int i = 0; i < grid_y; i++){
		printf("\n");
		for (int j = 0; j < grid_x; j++){
			if (i == grid_x-1 && j == grid_y-1){
				printf("G\n");
				return;
			}
			if (disp_score == 1){
				printf("%d ", g[i][j]);
			}
			else if (disp_score == 0){
				switch(g[i][j]){
					case -1:
						printf("O ");
						break;
					case 0:
						printf(". ");
						break;
					default:
						printf("X ");
						break;
				}
			}
			else if (disp_score == 2){
				if (score_grid[i][j] == -1){
					printf("P ");
				}
				else if (g[i][j] > 0 && g[i][j] <= 5){
					printf("_ ");
				}
				else if(g[i][j] > 5){
					printf("▲ ");
				}
				else{
					printf(". ");
				}
			}
		}
	}
	printf("\n");
}

int man_dist(int x1, int y1, int x2, int y2){
	return abs(x1-x2) + abs(y1-y2);
}

int calculateNewScore(int x, int y, int gx, int gy){
	return current_score + grid[x][y] + man_dist(x, y, gx, gy) ;
}

void calculateAdj(int s_x, int s_y, int gx, int gy){ //TODO make goal check
	if (s_x+1 < 20 && s_x >= 0){
		if (score_grid[s_x+1][s_y] != -1)
			score_grid[s_x+1][s_y] = calculateNewScore(s_x+1, s_y, gx, gy);
	}
	if (s_x-1 < 20 && s_x >= 0){
		if (score_grid[s_x-1][s_y] != -1)
			score_grid[s_x-1][s_y] = calculateNewScore(s_x-1, s_y, gx, gy);
	}
	if (s_y+1 < 20 && s_y >= 0){
		if (score_grid[s_x][s_y+1] != -1)
			score_grid[s_x][s_y+1] = calculateNewScore(s_x, s_y+1, gx, gy);
	}
	if (s_y-1 < 20 && s_y >= 0){
		if (score_grid[s_x][s_y-1] != -1)
			score_grid[s_x][s_y-1] = calculateNewScore(s_x, s_y-1, gx, gy);
	}
}

int small_x, small_y;

int getSmallestInGrid(){
	for (int i = 0; i < grid_y; i++){
		for (int j = 0; j < grid_x; j++){
			if (score_grid[i][j] > 0){
				if (small_x == 0 && small_y == 0){
					if (score_grid[i][j] > 0){
						small_x = i;
						small_y = j;
					}
				}
//				printf("bigger: %d\n", score_grid[i][j]);
				if (score_grid[i][j] < score_grid[small_x][small_y]){
//					printf("newsmol: %d\n", score_grid[i][j]);
					small_x = i;
					small_y = j;
				}
				if (score_grid[i][j] > score_grid[small_x][small_y] 
						&& score_grid[small_x][small_y] == -1){
					small_x = i;
					small_y = j;
				}
			}
		}
	}
	return score_grid[small_x][small_y];
}

void clear(){
	for (int n = 0; n < 5; n++)
		printf( "\n\n\n\n\n\n\n\n\n\n" );
}

int stepcount;
int totalchecks;

void getStats(){
	printf("\n\n------------\nGoal reached\n------------\n");
	for (int i = 0; i < grid_y; i++){
		for (int j = 0; j < grid_y; j++){
			if (score_grid[i][j] == -1){
				stepcount++;
			}
			if (score_grid[i][j] > 0){
				totalchecks++;
			}
		}
	}
	printf("Path steps -> %d/%d\nTotal checks -> %d/%d\n", stepcount, grid_x*grid_y, totalchecks+stepcount, grid_x*grid_y);
}

void Astar(int s_x, int s_y, int g_x, int g_y, int newscore){
	if (s_x+1 > 19 && s_x < 0 ||
			s_y-1 > 19 && s_y < 0 ||
			s_x-1 > 19 && s_x < 0 ||
			s_y+1 > 19 && s_y < 0){
		printf("returning");
		return;
	}
	clear();
	//score_grid[s_x][s_y] = newscore;
	calculateAdj(s_x, s_y, g_x, g_y);
	//	calculateAdj(3, 3, g_x, g_y);
	printgrid(grid, true);
	printgrid(score_grid, true);
	printgrid(grid, 2);
	printgrid(score_grid, false);
	printf("|%d, %d|\n", s_x, s_y);
	score_grid[s_x][s_y] = -1;
	current_score = grid[small_x][small_y];
	printf("%d -> %d, %d", score_grid[small_x][small_y], small_x, small_y);

	if (small_x == 19 && small_y == 19){
		getStats();
		return;
	}

	while(std::cin.get() != '\n');

	getSmallestInGrid();
	Astar(small_x, small_y, g_x, g_y, 0);
}

int main(int argc, char** argv){
	srand(atoi(argv[3])); // 5 seg fault, 10 check goal neighbours(12)
	randomize_array();
	Astar(atoi(argv[1]), atoi(argv[2]), 20, 20, 0);
	return 1;
}

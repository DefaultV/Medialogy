#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

const int grid_x = 20;
const int grid_y = 20;
int grid[grid_x][grid_y] = {
	{3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3}
};

int score_grid[grid_x][grid_y] = {};
int current_score = 0;

void randomize_array(){
	for(int i = 0; i < grid_y; i++){
		for(int j = 0; j < grid_x; j++){
			grid[i][j] = rand() % 9 + 1;
			score_grid[i][j] = 0;
		}
	}
}

void printgrid(int g[][20], bool disp_score){
	for (int i = 0; i < grid_y; i++){
		printf("\n");
		for (int j = 0; j < grid_x; j++){
			if (i == grid_x-1 && j == grid_y-1){
				printf("G\n");
				return;
			}
			if (disp_score){
				printf("%d ",g[i][j]);
			}
			else{
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
		}
	}
	printf("\n");
}

int man_dist(int x1, int y1, int x2, int y2){
	return abs(x1-x2) + abs(y1-y2);
}

int calculateNewScore(int x, int y, int gx, int gy){
	return current_score + grid[x][y] + man_dist(x, y, gx, gy);
}

void calculateAdj(int s_x, int s_y, int gx, int gy){
	if (s_x+1 <= 20 && s_x >= 0){
		if (score_grid[s_x+1][s_y] != -1)
			score_grid[s_x+1][s_y] = calculateNewScore(s_x+1, s_y, gx, gy);
	}
	if (s_x-1 <= 20 && s_x >= 0){
		if (score_grid[s_x-1][s_y] != -1)
			score_grid[s_x-1][s_y] = calculateNewScore(s_x-1, s_y, gx, gy);
	}
	if (s_y+1 <= 20 && s_y >= 0){
		if (score_grid[s_x][s_y+1] != -1)
			score_grid[s_x][s_y+1] = calculateNewScore(s_x, s_y+1, gx, gy);
	}
	if (s_y-1 <= 20 && s_y >= 0){
		if (score_grid[s_x][s_y-1] != -1)
			score_grid[s_x][s_y-1] = calculateNewScore(s_x, s_y-1, gx, gy);
	}
}

int small_x, small_y;

int getSmallestInGrid(){
	for (int i = 0; i < grid_y; i++){
		for (int j = 0; j < grid_x; j++){
			if (score_grid[i][j] > 0){
//				printf("bigger: %d\n", score_grid[i][j]);
				if (score_grid[i][j] < score_grid[small_x][small_y]){
//					printf("newsmol: %d\n", score_grid[i][j]);
					small_x = i;
					small_y = j;
				}
				if (score_grid[i][j] > score_grid[small_x][small_y] && score_grid[small_x][small_y] == -1){
					small_x = i;
					small_y = j;
				}
			}
		}
	}
	return score_grid[small_x][small_y];
}

void Astar(int s_x, int s_y, int g_x, int g_y, int newscore){
	if (s_x+1 > 20 && s_x < 0 ||
			s_y-1 > 20 && s_y < 0 ||
			s_x-1 > 20 && s_x < 0 ||
			s_y+1 > 20 && s_y < 0){
		printf("returning");
		return;
	}
	//score_grid[s_x][s_y] = newscore;
	calculateAdj(s_x, s_y, g_x, g_y);
	//	calculateAdj(3, 3, g_x, g_y);
	printgrid(grid, true);
	printgrid(score_grid, false);
	getSmallestInGrid();
	score_grid[s_x][s_y] = -1;
	current_score = grid[small_x][small_y];
	printf("%d -> %d, %d", score_grid[small_x][small_y], small_x, small_y);
	while(std::cin.get() != '\n'){
		printf("net");
	}
	if (small_x == 19 && small_y == 19){
		printf("GOAL");
		return;
	}
	Astar(small_x, small_y, g_x, g_y, 0);
}

int main(int argc, char** argv){
	randomize_array();
	Astar(0, 0, 20, 20, 0);
	//printf("%d", man_dist(2,3,5,5));
	return 1;
}

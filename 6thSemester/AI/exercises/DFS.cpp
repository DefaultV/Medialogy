#include <stdio.h>
#include <cstdlib>
#include <unistd.h>
#include <iostream>
//int **grid = new int*[10];
int gridsize_x = 16;
int gridsize_y = 23;
int grid[23][16] =  {
	{3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3},
	{3, 0, 3, 3, 3, 0, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3},
	{3, 0, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3},
	{3, 0, 3, 3, 3, 0, 3, 0, 0, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 3, 0, 0, 3, 0, 3, 0, 3, 3, 3},
	{3, 0, 3, 0, 3, 0, 3, 3, 0, 3, 0, 0, 0, 3, 0, 3},
	{3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3},
	{3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0, 0, 0, 3},
	{3, 0, 3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0, 3},
	{3, 3, 3, 0, 0, 0, 3, 4, 0, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3},
	{3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 3, 0, 3, 0, 3},
	{3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 3},
	{3, 0, 3, 3, 3, 3, 0, 3, 3, 3, 0, 3, 3, 3, 0, 3},
	{3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3},
	{3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3},
};
void printgrid(){
	for (int i = 0; i < gridsize_y; i++){
		printf("\n");
		for (int j = 0; j < gridsize_x; j++){
			switch(grid[i][j]){
				case 0:
					printf(" ");
					break;
				case 1:
					printf("X");
					break;
				case 3:
					printf("█");
					break;
				case 4:
					printf("G");
					break;
			}
		}
	}
	printf("\n");
	usleep(100000);
}
void clr(){
//    std::system ("clear");
	std::cout << "\033[2J\033[1;1H";
}
bool goal_reached;
int steps;
void DFS(int s_x, int s_y){
	steps++;
	clr();
	printgrid();
	if (grid[s_x][s_y] == 4){
		goal_reached = true;
	}
	if (goal_reached)
		return;
	grid[s_x][s_y] = 1; // 1 = visited
	if (grid[s_x-1][s_y] != 1 &&
			 grid[s_x-1][s_y] != 3){
		DFS(s_x-1, s_y);
	}
	if (grid[s_x][s_y-1] != 1 && grid[s_x][s_y-1] != 3){
		DFS(s_x, s_y-1);
	}
	if (grid[s_x][s_y+1] != 1 &&
			 grid[s_x][s_y+1] != 3){
		DFS(s_x, s_y+1);
	}
	if (grid[s_x+1][s_y] != 1 &&
		grid[s_x+1][s_y] != 3){
		DFS(s_x+1, s_y);
	}
}

int main(){
	DFS(3, 5);
	printf("%c %d\n", goal_reached ? 'Y' : 'N', steps);
}



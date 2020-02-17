#include <stdio.h>
#include <list>

const int VERTCOUNT = 7;
const int GOAL = 6;
bool *visited = new bool[VERTCOUNT];
std::list<int> queue;
std::list<int> *tree = new std::list<int>[VERTCOUNT];

void createGraph(){
	tree[0].push_back(1);
	tree[0].push_back(2);

	tree[1].push_back(0);
	tree[1].push_back(3);
	tree[1].push_back(4);

	tree[2].push_back(5);
	tree[2].push_back(0);

	tree[4].push_back(6);
	tree[4].push_back(1);

	tree[5].push_back(2);

	tree[6].push_back(4);
}

int bfs(int start){
	printf("--------------\nstarting @ %d\n--------------\n", start);
	int current = start;
	queue.push_back(current);

	while (queue.size() != 0){
		if (current == GOAL){
			printf("Found goal: %d\n-----------\n", current);
			return current;
		}
		for (int node : tree[current]){
			if (!visited[node]){
				queue.push_front(node);
				printf("@ %d -> Q: %d\n", current, node);
			}
		}
		printf("@ %d -> visited\n", queue.back());
		visited[queue.back()] = true;
		queue.pop_back();
		current = queue.back();
		printf("--------\n@ %d -> now\n", current);
	}
	return 0;
}


int main(){
	createGraph();
	for(int i = 0; i < VERTCOUNT; i++){
		if (i == GOAL)
			continue;
		printf("\n\nSTARTING NEW BFS ON: %d\n\n", i);
		visited = new bool[VERTCOUNT];
		queue.clear();
		bfs(i);
	}
	return 1;
}

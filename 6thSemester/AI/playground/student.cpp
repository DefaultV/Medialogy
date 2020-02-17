#include <stdio.h>
#include <string>

int rested, fed, amount_eat;
std::string state1, state2;
int work, days, prev_work;

int main(){
	state1 = "Awake";
	state2 = "Work";
	for(int i = 0; i < 129600; i++){
		if (state1 == "Awake"){
			rested--;
			if (rested <= 480*2)
				state1 = "Sleep";

			if (state2 == "Work"){
				fed --;
				work++;
				if (work - prev_work > 60){
					work -= 20;
					prev_work = work;
				}
				if (fed <= 0)
					state2 = "Eat";
			}
			else if (state2 == "Eat"){
				fed += 20;
				if (fed >= 500){
					state2 = "Work";
					amount_eat++;
				}
			}
		}
		else if (state1 == "Sleep"){
			rested += 2;
			if (rested > 1440)
				state1 = "Awake";
		}
	}
	printf("work: %d eat: %d\n", work, amount_eat);
}

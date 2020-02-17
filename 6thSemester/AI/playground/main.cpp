#include <stdio.h>
#include <string>

int sleepy = 0, thirsty=0, hungry=0, whiskey=0, gold=0, turn=0;
std::string state = "Mining";

void inc_vals(int _sleepy, int _thirsty, int _hungry, int _whiskey, int _gold){
	sleepy += _sleepy;
	thirsty += _thirsty;
	hungry += _hungry;
	whiskey += _whiskey;
	gold += _gold;
	turn++;

	if (sleepy >= 80) //80 80 80 1 50
		state = "Sleeping";
	if (hungry >= 80)
		state = "Eat";
	if (thirsty >= 80)
		state = "Drink";
	if (whiskey <= 1)
		state = "Shop";
	if (gold <= 50)
		state = "Mining";
}
void FSM(){
	if (state == "Mining") {
		inc_vals(5, 5, 5, 0, 5);
	}
	else if (state == "Sleeping"){
		inc_vals(-10, 1, 1, 0, 0);
		if (sleepy <= 0){
			state = "Eat";
		}
	}
	else if (state == "Eat"){
		inc_vals(5, -5, -20, 0, -2);
		if (hungry <= 10){
			state = "Mining";
		}
	}
	else if (state == "Shop"){
		inc_vals(5, 1, 1, 1, -1);
		if (whiskey >= 0)
			state = "Mining";
	}
	else if (state == "Drink"){
		inc_vals(5, -10, 1, -1, 0);
		if (thirsty <= 10){
			state = "Mining";
		}
	}
	printf("%d, %s:\t%d %d %d %d %d\n", turn, state.c_str(), sleepy, thirsty, hungry, whiskey, gold);
}

void f_loop(){
	for (int i = 0; i < 1000; i++) {
		if (sleepy > 100 || thirsty > 100 || hungry > 100 || whiskey < 0 || gold < 0) {
			printf("\nMorris R.I.P\n");
			break;
		}
		FSM();
	}

}
void w_loop(){
	while(1){
		if (sleepy > 100 || thirsty > 100 || hungry > 100 || whiskey < 0 || gold < 0) {
			printf("\nMorris R.I.P\n");
			break;
		}
		FSM();

	}
}

int main(){
	f_loop();
	//w_loop();
}

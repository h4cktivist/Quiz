#include <iostream>
using namespace std;

int main() {

	string name;
	string ready;
	string answer;
	int lives = 5;

	cout << "Enter your name: ";
	cin >> name;
	cout << " " << endl;
	cout << "Hello, " << name << endl;
	cout << "You are here to solve the quest! Your goal is answer the questions and save all 5 lives." << endl;
	cout << "Are you ready? GO!" << endl;


	cout << " " << endl;
	cout << "Informatics: What is brain of computer? ";
	cin >> answer;

	while (answer != "CPU" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Good job, keep going!" << endl;


	cout << " " << endl;
	cout << "Math: 2x + 18 = 84  x = ";
	cin >> answer;

	while (answer != "33" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Awesome! Keep going!" << endl;


	cout << " " << endl;
	cout << "Math: Square root of 225: ";
	cin >> answer;

	while (answer != "15" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Nice!" << endl;


	cout << " " << endl;
	cout << "Geography: How many continents in the world? ";
	cin >> answer;

	while (answer != "6" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Perfect! Keep going!" << endl;


	cout << " " << endl;
	cout << "Geometry: The sum of the inner corners of the triangle is equal to: ";
	cin >> answer;

	while (answer != "180" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Very good! You are the best!" << endl;


	cout << " " << endl;
	cout << "History: Name of the first president of USA: ";
	cin >> answer;

	while (answer != "George" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Perfect, good job!" << endl;


	cout << " " << endl;
	cout << "Chemistry: Chemical formula of hydrochloric acid: ";
	cin >> answer;

	while (answer != "HCL" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Science, bitch" << endl;


	cout << " " << endl;
	cout << "Physics: Who explored the Gravitation Law? ";
	cin >> answer;

	while (answer != "Newton" and lives > 1)
	{
		lives--;
		cout << "Wrong answer! Be careful, you have only " << lives << " lives." << endl;
		cout << "Try again: ";
		cin >> answer;
	}

	if (lives < 1)
	{
		cout << "Unfortunately, You lose." << endl;
		exit(0);
	}

	cout << "Yep, you're right!" << endl;

	cout << " " << endl;
	cout << "Congratulations! You solved all quiz and you still have " << lives << " lives!" << endl;
	cout << "Science, bitch!" << endl;
	cout << " " << endl;

}


// created by h4cktivist